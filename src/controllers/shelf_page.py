from PySide6.QtCore import QSize
from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext
from controllers.album_info_page import AlbumInfoPage
from models.album import AlbumModel
from models.shelf import ShelfModel
from views.ui_shelf_page import Ui_ShelfPage


class ShelfPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_ShelfPage(), bindings)
        self._pages = {
            "empty_page": self.ui.empty_page,
            "album_info_page": AlbumInfoPage(
                self.context,
                bindings={
                    # "delete_album_btn": ("clicked", self._on_click_delete_item_btn),
                    # "edit_album_btn": ("clicked", self._on_click_edit_album_btn),
                    # "archive_swap_btn": ("clicked", self._on_click_archive_item_btn),
                    # "open_album_btn": ("clicked", self._on_click_open_item_btn),
                }
            )
        }
        self._initUI()

    @property
    def ui(self) -> Ui_ShelfPage:
        return self._ui

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

    def updateData(self, shelf: ShelfModel) -> None:
        print(f"Shelf: {shelf}")

    def setCurrentPage(self, page_name: str, **kwargs) -> None:
        if page_name not in self._pages:
            return

        page = self._pages[page_name]

        self.ui.albums_info_stack.setCurrentWidget(page)
        if hasattr(page, "updateData"):
            page.updateData(**kwargs)

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {}

    def controller_images(self) -> dict[str, str]:
        return {
            "back_btn": "back.png",
        }
