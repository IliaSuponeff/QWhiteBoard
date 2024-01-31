class ShelfModel:

    def __init__(self, _id: int, name: str, description: str, is_archived: bool) -> None:
        self._id = _id
        self._name = name
        self._description = description
        self._is_archived = bool(is_archived)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def is_archived(self) -> bool:
        return self._is_archived

    @is_archived.setter
    def is_archived(self, value: bool) -> None:
        self._is_archived = bool(value)

    def __str__(self) -> str:
        return f"ShelfModel(id={self._id}, name={self._name}, is_archived={self._is_archived})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        if __value is None:
            return False

        if not isinstance(__value, ShelfModel):
            return False

        return self._id == __value._id or self._name == __value._name


EMPTY_SHELF = ShelfModel(-1, "", "", False)
