import pprint
from PySide6.QtWidgets import QMainWindow
from controllers.application_context import ApplicationContext, LogLevel
from views.ui_main_window import Ui_MainWindow


class WhiteBoardWindow(QMainWindow):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__()
        self._context = context
        self._ui = Ui_MainWindow()
        self._pages = [

        ]
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
        for page in self._pages:
            self.ui.pages_stack_widget.addWidget(page)

        self._ui.pages_stack_widget.setCurrentIndex(0)

    @property
    def ui(self) -> Ui_MainWindow:
        return self._ui

    @property
    def context(self) -> ApplicationContext:
        return self._context
