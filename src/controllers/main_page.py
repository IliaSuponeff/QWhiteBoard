import pprint
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QListWidgetItem
from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext, LogLevel
from controllers.album_info_page import AlbumInfoPage
from controllers.shelf_info_page import ShelfInfoPage
from controllers.album_construct_dialog import CreationAlbumDialog, EditAlbumDialog
from controllers.shelf_construct_dialog import CreationShelfDialog, EditShelfDialog
from controllers.database import DatabaseController, AlbumModel
from views.ui_main_page import Ui_MainPage
from models.shelf import EMPTY_SHELF


class MainPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_MainPage(), bindings)
        self._pages = {
            "empty_page": self.ui.empty_page,
            "album_info_page": AlbumInfoPage(
                self.context,
                bindings={
                    "delete_album_btn": ("clicked", self._on_click_delete_item_btn),
                    "edit_album_btn": ("clicked", self._on_click_edit_album_btn),
                    "archive_swap_btn": ("clicked", self._on_click_archive_item_btn)
                }
            ),
            "shelf_info_page": ShelfInfoPage(
                self.context,
                bindings={
                    "delete_shelf_btn": ("clicked", self._on_click_delete_item_btn),
                    "edit_shelf_btn": ("clicked", self._on_click_edit_album_btn),
                    "archive_swap_btn": ("clicked", self._on_click_archive_item_btn)
                }
            )
        }
        self._shelfs_count = 0
        self._current_page_name = "empty_page"
        self._initUI()

    @property
    def shelfs_count(self) -> int:
        return self._shelfs_count

    def reload_ui(self) -> None:
        self.ui.items_list_widget.clear()
        self._load_shelfs()
        self._load_albums()

    def _initUI(self):
        for page_name in self._pages:
            if page_name == "empty_page":
                continue

            page = self._pages[page_name]
            if page is None or not isinstance(page, AbstractPageController):
                continue

            if page in self.ui.items_info_widgets_stack.children():
                continue

            self.ui.items_info_widgets_stack.addWidget(page)

        self.setCurrentPage("empty_page")

        self.ui.items_list_widget.setIconSize(QSize(48, 48))
        self.reload_ui()

    def _load_shelfs(self) -> None:
        shelfs = self.context.database.get_shelfs()
        shelfs = list(filter(lambda shelf: shelf.is_archived == self.context.is_archive_mode, shelfs))
        self.context.log(
            LogLevel.DEBUG,
            f"Loaded shelfs",
            f"Controller: {self.__class__.__name__}",
            f"Mode: {'ARCHIVE' if self.context.is_archive_mode else 'NORMAL'}",
            f"Shelfs count: {len(shelfs)}",
            *shelfs
        )

        self._shelfs_count = len(shelfs)
        for shelf in shelfs:
            item = QListWidgetItem(
                self.context.load_icon("shelf.png"),
                f"{'[ARCHIVE] ' if shelf.is_archived else ''}{shelf.name}"
            )
            self.ui.items_list_widget.addItem(item)

    def _load_albums(self) -> None:
        albums: list[AlbumModel] = self.context.database.get_shelf_albums(EMPTY_SHELF)
        albums = list(filter(lambda album: album.is_archived == self.context.is_archive_mode, albums))
        self.context.log(
            LogLevel.DEBUG,
            f"Loaded albums",
            f"Controller: {self.__class__.__name__}",
            f"Mode: {'ARCHIVE' if self.context.is_archive_mode else 'NORMAL'}",
            f"Albums count: {len(albums)}",
            *albums
        )

        for album in albums:
            item = QListWidgetItem(
                self.context.load_icon("album.png"),
                f"{'[ARCHIVE] ' if album.is_archived else ''}{album.name}"
            )
            self.ui.items_list_widget.addItem(item)

    def setCurrentPage(self, page_name: str, *args, **kwargs) -> None:
        if page_name not in self._pages:
            self.context.log(
                LogLevel.ERROR,
                f"Page not found",
                f"Controller: {self.__class__.__name__}",
                f"Page name: {page_name}",
                f"Pages list: {pprint.pformat(list(self._pages.keys()))}"
            )
            return

        page = self._pages[page_name]
        if page_name != "empty_page" and (page is None or not isinstance(page, AbstractPageController)):
            self.context.log(
                LogLevel.ERROR,
                f"Invalid page found",
                f"Controller: {self.__class__.__name__}",
                f"Page name: {page_name}",
                f"Page: {page}",
                f"Pages list: {pprint.pformat(self._pages.keys())}"
            )
            return

        self.ui.items_info_widgets_stack.setCurrentWidget(page)
        if hasattr(page, "updateData"):
            page.updateData(*args, **kwargs)
        
        self._current_page_name = page_name

    @property
    def ui(self) -> Ui_MainPage:
        return self._ui

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {
            "add_album_btn": ("clicked", self._on_clicked_add_album_btn),
            "add_new_shelf_btn": ("clicked", self._on_clicked_add_new_shelf_btn),
            "items_list_widget": ("currentItemChanged", self._on_click_list_item),
            "archive_swap_btn": ("clicked", self._on_click_archive_mode_swap_btn),
        }

    def controller_images(self) -> dict[str, str]:
        return {}

    def _on_clicked_add_album_btn(self) -> None:
        dialog, exec_code = self.context.call_dialog(
            CreationAlbumDialog(self.context)
        )
        if exec_code != 0:
            return

        self.reload_ui()

    def _on_clicked_add_new_shelf_btn(self) -> None:
        dialog, exec_code = self.context.call_dialog(
            CreationShelfDialog(self.context)
        )
        if exec_code != 0:
            return

        self.reload_ui()

    def _on_click_list_item(self, item: QListWidgetItem, *args) -> None:
        if item is None:
            return

        db: DatabaseController = self.context.database
        index = self.ui.items_list_widget.row(item)

        if 0 <= index < self._shelfs_count:
            shelf = db.get_shelf(item.text().replace("[ARCHIVE]", "").strip())
            self.setCurrentPage("shelf_info_page", shelf=shelf)
        else:
            album = db.get_album(item.text().replace("[ARCHIVE]", "").strip())
            self.setCurrentPage("album_info_page", album=album)

    def _on_click_delete_item_btn(self) -> None:
        if self._current_page_name == "empty_page":
            return

        page = self._pages[self._current_page_name]
        if hasattr(page, "album"):
            item = page.album
        elif hasattr(page, "shelf"):
            item = page.shelf
        else:
            return

        db: DatabaseController = self.context.database
        db.remove_item(item)
        self.reload_ui()
        self.setCurrentPage("empty_page")

    def _on_click_edit_album_btn(self) -> None:
        if self._current_page_name == "empty_page":
            return

        page_name = self._current_page_name
        page = self._pages[page_name]
        if hasattr(page, "album"):
            item = page.album
        elif hasattr(page, "shelf"):
            item = page.shelf
        else:
            return

        dialog, exec_code = self.context.call_dialog(
            EditAlbumDialog(item, self.context)
                if isinstance(item, AlbumModel) else
            EditShelfDialog(item, self.context)
        )
        if exec_code != 0:
            return

        self.reload_ui()
        if hasattr(dialog, "album"):
            self.setCurrentPage(page_name, album=dialog.album)
        elif hasattr(dialog, "shelf"):
            self.setCurrentPage(page_name, shelf=dialog.shelf)

    def _on_click_archive_item_btn(self) -> None:
        if self._current_page_name == "empty_page":
            return

        page = self._pages[self._current_page_name]
        if hasattr(page, "album"):
            item = page.album
        elif hasattr(page, "shelf"):
            item = page.shelf
        else:
            return

        item.is_archived = not item.is_archived
        db: DatabaseController = self.context.database
        db.update_item(item.name, item)
        self.reload_ui()
        self.setCurrentPage("empty_page")

    def _on_click_archive_mode_swap_btn(self) -> None:
        self.context.is_archive_mode = not self.context.is_archive_mode
        self.ui.archive_swap_btn.setText(
            'Close archive' if self.context.is_archive_mode else 'See archive'
        )
        self.ui.add_album_btn.setDisabled(self.context.is_archive_mode)
        self.ui.add_new_shelf_btn.setDisabled(self.context.is_archive_mode)

        self.reload_ui()
        self.setCurrentPage("empty_page")
