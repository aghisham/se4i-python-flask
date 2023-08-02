from marshmallow import Schema, fields


class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class ItemStore:
    def __init__(self):
        self.items = []
        self.next_id = 1

    def create_item(self, name, description):
        item = Item(self.next_id, name, description)
        self.items.append(item)
        self.next_id += 1
        return item

    def get_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def update_item(self, id, name, description):
        item = self.get_item(id)
        if item:
            item.name = name
            item.description = description
            return item
        return None

    def delete_item(self, id):
        item = self.get_item(id)
        if item:
            self.items.remove(item)
            return item
        return None


class DefaultFileResponseSchema(Schema):
    """Default File Response Schema"""

    message = fields.Str()
    path = fields.Str()


class DefaultResponseSchema(Schema):
    """Default Response Schema"""

    message = fields.Str()


class ItemSchema(Schema):
    """Item Schema"""

    id = fields.Int()
    name = fields.Str()
    description = fields.Str()