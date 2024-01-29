from PySide6.QtSql import QSqlDatabase, QSqlQuery
from controllers.application_context import ApplicationContext


class DatabaseController(QSqlDatabase):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__('QSQLITE')
        self._context = context
        self.setDatabaseName(self.context.database_filename)
        self.open()
        self.context.database = self


    @property
    def context(self) -> ApplicationContext:
        return self._context

    def __del__(self) -> None:
        if not self.isOpen():
            return

        self.close()
