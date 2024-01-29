from PySide6.QtSql import QSqlDatabase, QSqlQuery
from controllers.application_context import ApplicationContext, LogLevel

class DatabaseSqlScript(QSqlQuery):

    def __init__(self, script: str, db: QSqlDatabase) -> None:
        super().__init__(db)
        self._script = script
        self._is_valid_executing = False

    @property
    def script(self) -> str:
        return self._script

    @property
    def is_valid_executing(self) -> bool:
        return self._is_valid_executing

    def exec(self) -> bool:
        self._is_valid_executing = super().exec(self.script)
        return self._is_valid_executing


class DatabaseController(QSqlDatabase):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__('QSQLITE')
        self._context = context
        self.setDatabaseName(self.context.database_filename)
        self.open()
        self.context.database = self
        self.execute_script("initialize")

    @property
    def context(self) -> ApplicationContext:
        return self._context

    def execute_script(self, script_name: str, default_script: str = "") -> list[DatabaseSqlScript]:
        script_data = self.context.load_sql_script(script_name, default_script=default_script)
        if not script_data:
            return []

        queries_list = []
        if ';' in script_data:
            scripts_datalist = [str(script).strip() for script in script_data.split(';')]
        else:
            scripts_datalist = [script_data]
        
        for script_data in scripts_datalist:
            if not script_data:
                continue

            query = self._execute_sql_query(script_data)
            queries_list.append(query)
        
        return queries_list

    def _execute_sql_query(self, script_data: str) -> DatabaseSqlScript:
        query = DatabaseSqlScript(script_data, self)
        if not query.exec():
            self.log(
                LogLevel.ERROR,
                "SQL script error",
                f"Script: {script_data}",
                f"Error by driver: {query.lastError().driverText()}"
                f"Error by database: {query.lastError().databaseText()}"
            )
        return query

    def __del__(self) -> None:
        if not self.isOpen():
            return

        self.close()
