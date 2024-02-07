from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext
from views.ui_shelf_info_page import Ui_ShelfInfoPage
from models.shelf import GLOBAL_SHELF, ShelfModel


class ShelfInfoPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_ShelfInfoPage(), bindings)
        self._shelf: ShelfModel = GLOBAL_SHELF
        self.updateData(GLOBAL_SHELF)

    @property
    def ui(self) -> Ui_ShelfInfoPage:
        return self._ui
    
    @property
    def shelf(self) -> ShelfModel:
        return self._shelf

    def updateData(self, shelf: ShelfModel) -> None:
        self._shelf = shelf
        self.ui.shelf_name_lbl.setText(f"## {shelf.name}")
        self.ui.create_datetime_edit.setDateTime(shelf.create_on)
        self.ui.chage_datetime_edit.setDateTime(shelf.change_on)
        self.ui.description_te.setPlainText(self.shelf.description.replace('\\r', '\r').replace('\\t', '\t').replace('\\n', '\n'))
        self.ui.archive_swap_btn.setText('Unarchivate' if shelf.is_archived else 'Archivate')
        self.ui.open_shelf_btn.setDisabled(self.context.is_archive_mode)
        self.ui.edit_shelf_btn.setDisabled(self.context.is_archive_mode)

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {}

    def controller_images(self) -> dict[str, str]:
        return {}

