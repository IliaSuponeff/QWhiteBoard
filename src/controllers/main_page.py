import pprint
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QListWidgetItem
from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext, LogLevel
from controllers.album_info_page import AlbumInfoPage
from controllers.album_construct_dialog import CreationAlbumDialog
from controllers.database import DatabaseController
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
                    "delete_album_btn": ("clicked", self._on_click_delete_album_btn),
                }
            ),
        }
        self._initUI()

    def reload_ui(self) -> None:
        self.ui.items_list_widget.clear()
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

    def _load_albums(self) -> None:
        albums = self.context.database.get_shelf_albums(EMPTY_SHELF)
        self.context.log(
            LogLevel.DEBUG,
            f"Loaded albums",
            f"Controller: {self.__class__.__name__}",
            f"Albums count: {len(albums)}",
            *albums
        )

        for album in albums:
            item = QListWidgetItem(self.context.load_icon("album.png"), album.name)
            self.ui.items_list_widget.addItem(item)

    def setCurrentPage(self, page_name: str, **kwargs) -> None:
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
            page.updateData(**kwargs)

    @property
    def ui(self) -> Ui_MainPage:
        return self._ui

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {
            "add_album_btn": ("clicked", self._on_clicked_add_album_btn),
            "items_list_widget": ("itemClicked", self._on_click_list_item)
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

    def _on_click_list_item(self, item: QListWidgetItem) -> None:
        db: DatabaseController = self.context.database
        album = db.get_album(item.text())
        self.setCurrentPage("album_info_page", album=album)

    def _on_click_delete_album_btn(self) -> None:
        db: DatabaseController = self.context.database
        db.remove_album(self._pages["album_info_page"].album)
        self.reload_ui()
        self.setCurrentPage("empty_page")
