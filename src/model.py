class Item:
    _item_list = []

    @classmethod
    def create(cls, name: str):
        cls._item_list.append(name)
        return name

    @classmethod
    def read(cls):
        return cls._item_list
