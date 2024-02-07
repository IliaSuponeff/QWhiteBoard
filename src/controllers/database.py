from PySide6.QtCore import QSize, QDateTime
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from controllers.application_context import ApplicationContext, LogLevel
from models.album import AlbumModel, SlideType
from models.shelf import ShelfModel


class DatabaseSqlScript(QSqlQuery):

    def __init__(self, script: str, db: QSqlDatabase, **kwargs) -> None:
        super().__init__(db)
        for key, value in kwargs.items():
            if not isinstance(value, (str, int,)):
                value = str(value).replace('(', '').replace(')', '').replace('\'', '')

            script = script.replace("{{" + key + "}}", str(value))
        self._script = script.strip()

    @property
    def script(self) -> str:
        return self._script

    def exec(self) -> bool:
        return super().exec(self.script)

    def __str__(self) -> str:
        script_view = self.script.replace("\n", ' ')
        return f"DatabaseSqlScript(script={script_view})"

    def __repr__(self) -> str:
        return self.__str__()


class DatabaseController(QSqlDatabase):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__('QSQLITE')
        self._context = context
        self.setDatabaseName(self.context.database_filename)
        self.open()
        self.context.database = self
        self.execute_script("initialize")

    @property
    def context(self) -> ApplicationContext:
        return self._context

    def execute_script(self, script_name: str, default_script: str = "", **kwargs) -> list[DatabaseSqlScript]:
        script_data = self.context.load_sql_script(script_name, default_script=default_script)
        if not script_data:
            return []

        queries_list = []
        if ';' in script_data:
            scripts_datalist = [str(script).strip() for script in script_data.split(';')]
        else:
            scripts_datalist = [script_data.strip()]
        
        for script_data in scripts_datalist:
            if not script_data:
                continue

            query = self._execute_sql_query(script_data, **kwargs)
            queries_list.append(query)
        
        return queries_list

    def _execute_sql_query(self, script_data: str, **kwargs) -> DatabaseSqlScript:
        query = DatabaseSqlScript(script_data, self, **kwargs)
        if not query.exec():
            self.context.log(
                LogLevel.ERROR,
                "SQL script error",
                f"Script: {query.script}",
                f"Error by driver: {query.lastError().driverText()}"
                f"Error by database: {query.lastError().databaseText()}"
            )

        return query

    def is_contain_album(self, album_name: str) -> bool:
        query = self.execute_script("is_contain_item", table="albums", field="name", value=album_name)[0]
        query.next()

        return query.value(0) != 0

    def is_contain_shelf(self, shelf_name: str) -> bool:
        query = self.execute_script("is_contain_item", table="shelfs", field="name", value=shelf_name)[0]
        
        query.next()
        return query.value(0) != 0

    def create_new_album(self, album_name: str, shelf_name: str, slide_type: SlideType, slide_size: QSize, description: str) -> AlbumModel:
        query = self.execute_script(
            "add_album",
            name=album_name,
            shelf_name=shelf_name,
            create_on=QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm"),
            change_on=QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm"),
            slide_type=slide_type.name,
            slide_size=f"{slide_size.width()}x{slide_size.height()}",
            description=description
        )[0]
        return self.get_album(album_name)

    def create_new_shelf(self, shelf_name: str, description: str) -> ShelfModel:
        query = self.execute_script(
            "add_shelf",
            name=shelf_name,
            create_on=QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm"),
            change_on=QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm"),
            description=description
        )[0]
        return self.get_shelf(shelf_name)

    def get_album(self, name: str) -> AlbumModel:
        query = self.execute_script("get_item", table="albums", field="name", value=name)[0]
        query.next()
        return AlbumModel(
            query.value(0),
            query.value(1),
            query.value(2),
            QDateTime.fromString(query.value(3), "yyyy-MM-dd hh:mm"),
            QDateTime.fromString(query.value(4), "yyyy-MM-dd hh:mm"),
            SlideType[query.value(5)],
            QSize(*list(map(int, query.value(6).split('x')))),
            query.value(7),
            bool(query.value(8))
        )

    def get_shelf(self, name: str) -> ShelfModel:
        query = self.execute_script("get_item", table="shelfs", field="name", value=name)[0]
        query.next()
        return ShelfModel(
            query.value(0),
            query.value(1),
            QDateTime.fromString(query.value(2), "yyyy-MM-dd hh:mm"),
            QDateTime.fromString(query.value(3), "yyyy-MM-dd hh:mm"),
            query.value(4),
            bool(query.value(5)),
        )

    def get_shelf_albums(self, shelf: ShelfModel) -> list[AlbumModel]:
        if shelf is None:
            return []

        return self.get_shelf_albums_by_name(shelf_name=shelf.name)

    def get_shelf_albums_by_name(self, shelf_name) -> list[AlbumModel]:
        if shelf_name is None:
            return []

        query = self.execute_script("get_item", table="albums", field="shelf_name", value=str(shelf_name))[0]
        albums = []
        while query.next():
            album = AlbumModel(
                query.value(0),
                query.value(1),
                query.value(2),
                QDateTime.fromString(query.value(3), "yyyy-MM-dd hh:mm"),
                QDateTime.fromString(query.value(4), "yyyy-MM-dd hh:mm"),
                SlideType[query.value(5)],
                QSize(*list(map(int, query.value(6).split('x')))),
                query.value(7),
                bool(query.value(8))
            )
            albums.append(album)

        return albums

    def get_shelfs(self) -> list[ShelfModel]:
        query = self.execute_script("get_all_items", table="shelfs")[0]
        shelfs = []
        while query.next():
            shelf = ShelfModel(
                query.value(0),
                query.value(1),
                QDateTime.fromString(query.value(2), "yyyy-MM-dd hh:mm"),
                QDateTime.fromString(query.value(3), "yyyy-MM-dd hh:mm"),
                query.value(4),
                bool(query.value(5)),
            )
            shelfs.append(shelf)

        return shelfs

    def remove_album(self, album: AlbumModel) -> None:
        self.remove_album_by_name(album_name=album.name)

    def remove_album_by_name(self, album_name: str) -> None:
        self.execute_script("remove_item", table="albums", field="name", value=album_name)

    def remove_shelf(self, shelf: ShelfModel) -> None:
        self.remove_shelf_by_name(shelf_name=shelf.name)

    def remove_shelf_by_name(self, shelf_name: str) -> None:
        self.execute_script("remove_item", table="shelfs", field="name", value=shelf_name)
        shelf_albums = self.get_shelf_albums_by_name(shelf_name=shelf_name)
        for album in shelf_albums:
            self.remove_album(album)

    def remove_item(self, item: object) -> None:
        if isinstance(item, AlbumModel):
            self.remove_album(item)
        elif isinstance(item, ShelfModel):
            self.remove_shelf(item)
        else:
            self.context.log(LogLevel.ERROR, f"Unknown item type: {item} to delete it")

    def update_album(self, last_name: str, album: AlbumModel) -> None:
        self.execute_script(
            "update_item",
            table="albums", key="name", key_value=last_name,
            values=(
                f"shelf_name=\"{album.shelf_name}\"",
                f"name=\"{album.name}\"",
                f"change_on=\"{QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm')}\"",
                f"slide_type=\"{album.slide_type.name}\"",
                f"slide_size=\"{album.slide_size.width()}x{album.slide_size.height()}\"",
                f"description=\"{album.description}\"",
                f"is_archived={1 if album.is_archived else 0}",
            )
        )
        return self.get_album(album.name)

    def update_shelf(self, last_name: str ,shelf: ShelfModel) -> None:
        self.execute_script(
            "update_item",
            table="shelfs", key="name", key_value=last_name,
            values=(
                f"name=\"{shelf.name}\"",
                f"change_on=\"{QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm')}\"",
                f"description=\"{shelf.description}\"",
                f"is_archived={1 if shelf.is_archived else 0}",
            )
        )
        return self.get_shelf(shelf.name)

    def update_item(self, last_name: str, item: object) -> None:
        if isinstance(item, AlbumModel):
            self.update_album(last_name, item)
        elif isinstance(item, ShelfModel):
            self.update_shelf(last_name, item)
        else:
            self.context.log(LogLevel.ERROR, f"Unknown item type: {item} to update it")

    def __del__(self) -> None:
        if not self.isOpen():
            return

        self.commit()
        self.close()
