from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import QSize
from controllers.abc_controller import AbstractDialogController
from controllers.application_context import ApplicationContext
from views.ui_connect_album_dialog import Ui_ConnectAlbumDialog
from controllers.database import DatabaseController
from models.album import AlbumModel, EMPTY_ALBUM
from models.shelf import GLOBAL_SHELF, ShelfModel


class ConnectAlbumDialog(AbstractDialogController):

    def __init__(self, context: ApplicationContext, shelf: ShelfModel) -> None:
        super().__init__(context, Ui_ConnectAlbumDialog(), {})
        self._shelf = shelf
        self._initUI()

    @property
    def ui(self) -> Ui_ConnectAlbumDialog:
        return self._ui

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {
            "save_btn": ("clicked", self._on_clicked_save_btn),
            "add_album_to_shelf_btn": ("clicked", self._on_clicked_add_album_to_shelf_btn),
            "remove_album_from_shelf_btn": ("clicked", self._on_clicked_remove_album_from_shelf_btn),
            "global_albums_list": ("itemDoubleClicked", self._on_clicked_add_album_to_shelf_btn),
            "shelf_albums_list": ("itemDoubleClicked", self._on_clicked_remove_album_from_shelf_btn),
        }

    def controller_images(self) -> dict[str, str]:
        return {
            "img_lbl_1": ("shelf.png", QSize(48, 48))
        }

    def _initUI(self) -> None:
        self.setWindowTitle("Conection albums")
        self.ui.shelf_albums_list.setIconSize(QSize(48, 48))
        self.ui.global_albums_list.setIconSize(QSize(48, 48))
        self.ui.title_lbl.setText(f"## Conection albums to shelf '{self._shelf.name}'")
        self._reload_albums()

    def _reload_albums(self) -> None:
        self._reload_shelf_albums(self.ui.global_albums_list ,shelf=GLOBAL_SHELF)
        self._reload_shelf_albums(self.ui.shelf_albums_list ,shelf=self._shelf)

    def _reload_shelf_albums(self, _list: QListWidget, shelf: ShelfModel) -> None:
        db: DatabaseController = self.context.database
        albums = list(
            filter(
                lambda album: album.is_archived == self.context.is_archive_mode,
                db.get_shelf_albums(shelf)
            )
        )

        _list.clear()
        for album in albums:
            item = QListWidgetItem(
                self.context.load_icon("album.png"),
                f"{album.name}"
            )
            setattr(item, "__album__", album)

            _list.addItem(item)

    def _on_clicked_save_btn(self) -> None:
        db: DatabaseController = self.context.database

        # connection albums
        for index in range(self.ui.shelf_albums_list.count()):
            item: QListWidgetItem = self.ui.shelf_albums_list.item(index)
            if not hasattr(item, "__album__"):
                continue

            album: AlbumModel = getattr(item, "__album__")
            if album.shelf_name == self._shelf.name:
                continue

            album.shelf_name = self._shelf.name
            db.update_album(album.name, album)

        # disconnection albums
        for index in range(self.ui.global_albums_list.count()):
            item: QListWidgetItem = self.ui.global_albums_list.item(index)
            if not hasattr(item, "__album__"):
                continue

            album: AlbumModel = getattr(item, "__album__")
            if album.shelf_name != self._shelf.name:
                continue

            album.shelf_name = GLOBAL_SHELF.name
            db.update_album(album.name, album)

        self.close()

    def _on_clicked_add_album_to_shelf_btn(self, album_item: QListWidgetItem = None) -> None:
        if album_item is None or not isinstance(album_item, QListWidgetItem):
            album_item: QListWidgetItem = self.ui.global_albums_list.currentItem()

        if album_item is None:
            return

        self.ui.shelf_albums_list.addItem(
            self.ui.global_albums_list.takeItem(
                self.ui.global_albums_list.row(album_item)
            )
        )

    def _on_clicked_remove_album_from_shelf_btn(self, album_item: QListWidgetItem = None) -> None:
        if album_item is None or not isinstance(album_item, QListWidgetItem):
            album_item: QListWidgetItem = self.ui.shelf_albums_list.currentItem()

        if album_item is None:
            return

        self.ui.global_albums_list.addItem(
            self.ui.shelf_albums_list.takeItem(
                self.ui.shelf_albums_list.row(album_item)
            )
        )
