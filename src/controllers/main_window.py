import pprint
from PySide6.QtWidgets import QMainWindow
from controllers.application_context import ApplicationContext, LogLevel
from controllers.main_page import MainPage, AbstractPageController
from views.ui_main_window import Ui_MainWindow


class WhiteBoardWindow(QMainWindow):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__()
        self._context = context
        self._ui = Ui_MainWindow()
        self._pages = {
            "main_page": MainPage(
                self.context,
                bindings={
                    "MainPage": {
                        ("openAlbum", print),
                        ("openShelf", print),
                    },
                }
            ),
        }
        self._call_history = []
        self._initUI()

    def _initUI(self):
        self.ui.setupUi(self)
        self.ui.app_icon_lbl.setPixmap(self.context.load_pixmap("icon.png"))
        self.ui.settings_btn.setIcon(self.context.load_icon("settings.png"))
        self.ui.app_name_lbl.setText(f"# {self.context.application.applicationDisplayName()}")

        # Clearing pages stack
        childrens = [self.ui.pages_stack_widget.widget(i) for i in range(self.ui.pages_stack_widget.count())]
        for children in childrens:
            self.ui.pages_stack_widget.removeWidget(children)

        # Filling pages stack
        for page_name in self._pages:
            page = self._pages.get(page_name, None)
            if page is None or not isinstance(page, AbstractPageController):
                continue

            self.ui.pages_stack_widget.addWidget(page)

        self.setCurrentPage("main_page")

    @property
    def ui(self) -> Ui_MainWindow:
        return self._ui

    @property
    def context(self) -> ApplicationContext:
        return self._context

    def setCurrentPage(self, page_name: str, save_history: bool = True) -> None:
        if page_name not in self._pages:
            self.context.log(
                LogLevel.ERROR,
                f"Page not found",
                f"Controller: {self.__class__.__name__}",
                f"Page name: {page_name}",
                f"Pages list: {pprint.pformat(list(self._pages.keys()))}"
            )
            return

        if len(self._call_history) > 0 and self._call_history[-1] == page_name:
            self.context.log(
                LogLevel.DEBUG,
                f"Page already opened",
                f"Controller: {self.__class__.__name__}",
                f"Page name: {page_name}"
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

        if save_history:
            self._call_history.append(page_name)

        self.ui.pages_stack_widget.setCurrentWidget(self._pages[page_name])
