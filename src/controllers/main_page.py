import pprint
from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext, LogLevel
from controllers.album_info_page import AlbumInfoPage
from views.ui_main_page import Ui_MainPage

class MainPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_MainPage(), bindings)
        self._pages = {
            "empty_page": self.ui.empty_page,
            "album_info_page": AlbumInfoPage(self.context),
        }
        self._initUI()

    def _initUI(self):
        for page_name in self._pages:
            page = self._pages[page_name]
            if page is None or not isinstance(page, AbstractPageController):
                continue

            if page in self.ui.items_info_widgets_stack.children():
                continue

            self.ui.items_info_widgets_stack.addWidget(page)

        self.setCurrentPage("empty_page")

    def setCurrentPage(self, page_name: str) -> None:
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
        if page is None or not isinstance(page, AbstractPageController):
            self.context.log(
                LogLevel.ERROR,
                f"Invalid page found",
                f"Controller: {self.__class__.__name__}",
                f"Page name: {page_name}",
                f"Page: {page}",
                f"Pages list: {pprint.pformat(self._pages.keys())}"
            )
            return

        self.ui.items_info_widgets_stack.setCurrentWidget(self._pages[page_name])

    @property
    def ui(self) -> Ui_MainPage:
        return self._ui
