import abc
from controllers.abc_controller import AbstractDialogController
from controllers.application_context import ApplicationContext, LogLevel
from controllers.database import DatabaseController
from views.ui_shelf_construct_dialog import Ui_ShelfConstructDialog
from models.shelf import ShelfModel, EMPTY_SHELF, QDateTime
from PySide6.QtGui import QRegularExpressionValidator


class ShelfConstructDialog(AbstractDialogController):

    def __init__(self,shelf: ShelfModel , context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_ShelfConstructDialog(), bindings)
        self._shelf = shelf
        self._initUI()

    def _initUI(self) -> None:
        input_validator = QRegularExpressionValidator()
        input_validator.setRegularExpression(r"^[a-zA-Zа-яА-Я0-9 ]*$")

        self.ui.name_le.setValidator(input_validator)
        self.ui.name_le.setText(self.shelf.name)
        self.ui.description_text_edit.setText(self.shelf.description)

    @property
    def shelf(self) -> ShelfModel:
        return self._shelf

    @property
    def ui(self) -> Ui_ShelfConstructDialog:
        return self._ui

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {
            "construct_btn": ("clicked", self._on_clicked_construct_btn)
        }

    def controller_images(self) -> dict[str, str]:
        return {
            "shelf_img_lbl": "shelf.png",
        }

    def _on_clicked_construct_btn(self) -> None:
        if not self._is_valide_shelf_data():
            self.context.log(
                LogLevel.ERROR,
                "Shelf exsists",
                f"Shelf with name: '{self.ui.name_le.text().strip()}'",
                "Already exsist in application",
                f"Change it, and try againg",
                is_window_log=True
            )
            return

        self._shelf = self._compile_shelf()
        self.close()

    @abc.abstractmethod
    def _is_valide_shelf_data(self) -> bool:
        return True

    @abc.abstractmethod
    def _compile_shelf(self) -> ShelfModel:
        pass


class CreationShelfDialog(ShelfConstructDialog):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__(EMPTY_SHELF, context)

    def _compile_shelf(self) -> ShelfModel:
        name: str = self.ui.name_le.text().strip()
        description: str = self.ui.description_text_edit.toPlainText().strip()

        db: DatabaseController = self.context.database
        return db.create_new_shelf(name, description)

    def _is_valide_shelf_data(self) -> bool:
        name: str = self.ui.name_le.text().strip()
        return len(name) > 0 and not self.context.database.is_contain_shelf(shelf_name=name)


class EditShelfDialog(ShelfConstructDialog):

    def __init__(self, shelf: ShelfModel, context: ApplicationContext) -> None:
        super().__init__(shelf, context)

    def _compile_shelf(self) -> ShelfModel:
        name: str = self.ui.name_le.text().strip()
        description: str = self.ui.description_text_edit.toPlainText().strip()

        db: DatabaseController = self.context.database
        return db.update_shelf(
            self.shelf.name,
            ShelfModel(
                _id=0,
                name=name,
                create_on=self.shelf.create_on,
                change_on=QDateTime.currentDateTime(),
                is_archived=self.shelf.is_archived,
                description=description
            )
        )

    def _is_valide_shelf_data(self) -> bool:
        name: str = self.ui.name_le.text().strip()
        return len(name) > 0 and not self.context.database.is_contain_shelf(shelf_name=name)
