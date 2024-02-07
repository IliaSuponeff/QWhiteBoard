from PySide6.QtCore import QObject, Signal, QSize, Qt
from PySide6.QtWidgets import QWidget, QDialog
from controllers.application_context import ApplicationContext, LogLevel, QIcon


class AbstractPageController(QWidget):

    def __init__(self, context: ApplicationContext, ui, bindings:dict[str, list[str, object]] = {}) -> None:
        super().__init__()
        self._context = context
        self._ui = ui
        self._ui.setupUi(self)
        self.load_bindings(bindings)
        self.load_bindings(self.controller_bindings())
        self.load_images(**self.controller_images())

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {}

    def controller_images(self) -> dict[str, str|tuple[str, QSize]]:
        return {}

    def load_bindings(self, bindings: dict[str, set[tuple[str, object]]]) -> None:
        for ui_element_name in bindings.keys():
            if ui_element_name == "self" or ui_element_name.lower() == str(self.__class__.__name__).lower():
                self._bind_signal(self, bindings[ui_element_name])
                continue

            if not hasattr(self.ui, ui_element_name):
                continue

            ui_element = getattr(self.ui, ui_element_name)
            self._bind_signal(ui_element, bindings[ui_element_name])

    def _bind_signal(self, ui_element: QObject, binding: tuple[str, object] | set[tuple[str, object]]) -> None:
        if isinstance(binding, (set, frozenset,)):
            for bind_tuple in binding:
                self._bind_signal(ui_element, bind_tuple)

            return

        if not isinstance(binding, (list, tuple,)):
            self.context.log(
                LogLevel.ERROR,
                f"Invalid binding",
                f"Controller: {self.__class__.__name__}"
                f"Invalid type of bind object: {type(binding)}. Bind object {binding}",
                "Bind object must be tuple or list with length 2. "
                "First element is name of ui element and second element is callback function"
            )
            return

        try:
            signal_name = binding[0]
            callback = binding[1]
            if not hasattr(ui_element, signal_name):
                raise AttributeError(f"Not found signal: '{signal_name}'")
            
            signal: Signal = getattr(ui_element, signal_name)
            signal.connect(callback)
        except Exception as ex:
            self.context.log(
                LogLevel.ERROR,
                f"Invalid binding: {binding}",
                f"Controller: {self.__class__.__name__}"
                f"Failed to init binding for {ui_element.objectName()}",
                ex
            )

    def load_images(self, **images) -> None:
        for ui_element_name in images.keys():
            if not hasattr(self.ui, ui_element_name):
                continue

            ui_element = getattr(self.ui, ui_element_name)
            self._load_image(ui_element, images[ui_element_name])

    def _load_image(self, ui_element: QObject, image_info: str | tuple[str, QSize]):
        image_name = image_info[0] if isinstance(image_info, tuple) else image_info
        image = self.context.load_pixmap(image_name)
        if isinstance(image_info, tuple):
            size = image_info[1]
            image = image.scaled(size)
            if hasattr(ui_element, "setIconSize"):
                ui_element.setIconSize(size)

        if hasattr(ui_element, "setPixmap"):
            ui_element.setPixmap(image)
            return
        elif hasattr(ui_element, "setIcon"):
            ui_element.setIcon(QIcon(image))
            return

        self.context.log(
            LogLevel.ERROR,
            f"Failed to load image",
            f"Controller: {self.__class__.__name__}",
            f"Image name: {image_name}",
            f"UI object: {ui_element.objectName()}",
        )

    @property
    def context(self) -> ApplicationContext:
        return self._context
    
    @property
    def ui(self) -> object:
        return self._ui


class AbstractDialogController(QDialog):

    def __init__(self, context: ApplicationContext, ui, bindings:dict[str, list[str, object]] = {}) -> None:
        super().__init__()
        self._context = context
        self._ui = ui
        self._execution_message = ""
        self._ui.setupUi(self)
        self.setModal(True)
        self.load_bindings(bindings)
        self.load_bindings(self.controller_bindings())
        self.load_images(**self.controller_images())

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {}

    def controller_images(self) -> dict[str, str]:
        return {}

    def load_bindings(self, bindings:dict[str, tuple[str, object]]) -> None:
        for ui_element_name in bindings.keys():
            if not hasattr(self.ui, ui_element_name):
                continue

            ui_element = getattr(self.ui, ui_element_name)
            try:
                signal_name = bindings[ui_element_name][0]
                callback = bindings[ui_element_name][1]

                if not hasattr(ui_element, signal_name):
                    continue

                getattr(ui_element, signal_name).connect(callback)
            except Exception as ex:
                self.context.log(
                    LogLevel.ERROR,
                    f"Failed to init binding for {ui_element_name}",
                    ex
                )

    def load_images(self, **images) -> None:
        for ui_element_name in images.keys():
            if not hasattr(self.ui, ui_element_name):
                continue

            ui_element = getattr(self.ui, ui_element_name)
            image_name = images[ui_element_name]
            if hasattr(ui_element, "setPixmap"):
                ui_element.setPixmap(self.context.load_pixmap(image_name))
                continue

            if hasattr(ui_element, "setIcon"):
                ui_element.setIcon(self.context.load_icon(image_name))
                continue

            self.context.log(
                LogLevel.ERROR,
                f"Failed to load image {image_name} for UI object {ui_element_name} on {self.__class__.__name__}"
            )

    @property
    def context(self) -> ApplicationContext:
        return self._context

    @property
    def ui(self) -> object:
        return self._ui

    @property
    def execution_message(self) -> str:
        return self._execution_message

    @execution_message.setter
    def execution_message(self, message: str) -> None:
        if message is None:
            return

        self._execution_message = str(message)
