from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import QListWidgetItem
from controllers.abc_controller import AbstractPageController, LogLevel
from controllers.application_context import ApplicationContext
from controllers.album_info_page import AlbumInfoPage
from controllers.album_construct_dialog import CreationAlbumDialog, EditAlbumDialog
from controllers.connect_album_dialog import ConnectAlbumDialog
from controllers.database import DatabaseController
from models.album import AlbumModel
from models.shelf import ShelfModel, GLOBAL_SHELF
from views.ui_shelf_page import Ui_ShelfPage


class ShelfPage(AbstractPageController):

    openAlbum = Signal((AlbumModel,))

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_ShelfPage(), bindings)
        self._pages = {
            "empty_page": self.ui.empty_page,
            "album_info_page": AlbumInfoPage(
                self.context,
                bindings={
                    "delete_album_btn": ("clicked", self._on_click_delete_album_btn),
                    "edit_album_btn": ("clicked", self._on_click_edit_album_btn),
                    "archive_swap_btn": ("clicked", self._on_click_archive_album_btn),
                    "open_album_btn": ("clicked", self._on_click_open_album_btn),
                }
            )
        }
        self._shelf = None
        self._initUI()

    @property
    def ui(self) -> Ui_ShelfPage:
        return self._ui

    @property
    def shelf(self) -> ShelfModel:
        return self._shelf

    def _initUI(self) -> None:
        for page_name in self._pages:
            if page_name == "empty_page":
                continue

            page = self._pages[page_name]
            if page is None or not isinstance(page, AbstractPageController):
                continue

            if page in self.ui.albums_info_stack.children():
                continue

            self.ui.albums_info_stack.addWidget(page)

        self.setCurrentPage("empty_page")
        self.ui.albums_list.setIconSize(QSize(48, 48))
        self._reload_albums()

    def _reload_albums(self) -> None:
        self.ui.albums_list.clear()
        db: DatabaseController = self.context.database
        albums: list[AlbumModel] = db.get_shelf_albums(self.shelf)

        self.context.log(
            LogLevel.DEBUG,
            f"Loaded albums",
            f"Controller: {self.__class__.__name__}",
            f"Albums count: {len(albums)}",
            *albums
        )

        for album in albums:
            item = QListWidgetItem(
                self.context.load_icon("album.png"),
                f"{album.name}"
            )
            self.ui.albums_list.addItem(item)

    def updateData(self, shelf: ShelfModel) -> None:
        self._shelf = shelf
        self.ui.shelf_name_lbl.setText(f"## {shelf.name}")
        self._reload_albums()

    def setCurrentPage(self, page_name: str, **kwargs) -> None:
        if page_name not in self._pages:
            return

        page = self._pages[page_name]

        self.ui.albums_info_stack.setCurrentWidget(page)
        if hasattr(page, "updateData"):
            page.updateData(**kwargs)

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {
            "add_new_album_btn": ("clicked", self._on_click_add_new_album_btn),
            "connect_album_btn": ("clicked", self._on_click_connect_album_btn),
            "disconnect_album_btn": ("clicked", self._on_click_disconnect_album_btn),
            "albums_list": {
                ("currentItemChanged", self._on_click_albums_list_item),
                ("itemDoubleClicked", self._on_click_open_album_btn)
            }
        }

    def controller_images(self) -> dict[str, str|tuple[str, QSize]]:
        return {
            "back_btn": ("back.png", QSize(24, 24)),
            "img_lbl_1": ("shelf.png", QSize(48, 48))
        }

    def _on_click_add_new_album_btn(self):
        dialog, exec_code = self.context.call_dialog(
            CreationAlbumDialog(self.context, self.shelf)
        )

        if exec_code != 0:
            return

        self._reload_albums()

    def _on_click_connect_album_btn(self):
        dialog, exec_code = self.context.call_dialog(
            ConnectAlbumDialog(self.context, self.shelf)
        )

        if exec_code != 0:
            return

        self._reload_albums()

    def _on_click_disconnect_album_btn(self):
        db: DatabaseController = self.context.database
        album_item: QListWidgetItem = self.ui.albums_list.currentItem()
        if album_item is None:
            return

        album = db.get_album(album_item.text())
        album.shelf_name = GLOBAL_SHELF.name
        db.update_album(album.name, album)
        self._reload_albums()

    def _on_click_albums_list_item(self, item: QListWidgetItem, *args) -> None:
        if item is None:
            return

        album = self.context.database.get_album(item.text())
        self.setCurrentPage("album_info_page", album=album)

    def _on_click_delete_album_btn(self):
        album: AlbumModel = self._pages["album_info_page"].album
        if album is None:
            return

        db: DatabaseController = self.context.database
        db.remove_album(album)
        self._reload_albums()

    def _on_click_archive_album_btn(self):
        album: AlbumModel = self._pages["album_info_page"].album
        print(album)
        if album is None:
            return

        album.is_archived = not album.is_archived
        album.shelf_name = GLOBAL_SHELF.name

        db: DatabaseController = self.context.database
        db.update_album(album.name, album)
        self._reload_albums()

    def _on_click_edit_album_btn(self):
        album: AlbumModel = self._pages["album_info_page"].album
        if album is None:
            return

        dialog, exec_code = self.context.call_dialog(
            EditAlbumDialog(album, self.context)
        )

        if exec_code != 0:
            return

        self._reload_albums()
        self.setCurrentPage("album_info_page", album=dialog.album)

    def _on_click_open_album_btn(self):
        album: AlbumModel = self._pages["album_info_page"].album
        if album is None:
            return

        self.openAlbum.emit(album)
