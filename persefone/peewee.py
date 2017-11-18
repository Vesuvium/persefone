# -*- coding: utf-8 -*-
import ujson


class Siren:

    def __init__(self, data, path, model=None, total_items=0, current_page=1):
        self.data = data
        self.path = path
        self.model = model
        self.total_items = total_items
        self.current_page = current_page

    def paginate(self):
        """
        Generates pagination metadata
        """
        links = [
            {'rel': ['self'], 'href': self.path}
        ]

        if self.total_items > len(self.data):
            href = '{}?page={}'.format(self.path, self.current_page + 1)
            links.append({'rel': ['next'], 'href': href})

        if self.current_page != 1:
            href = '{}?page={}'.format(self.path, self.current_page - 1)
            links.append({'rel': ['previous'], 'href': href})
        return links

    def make_entity(self):
        """
        Produces a Siren document with a single data object.
        """
        href = '{}/{}'.format(self.path, self.data.id)
        return {
            'properties': self.data._data,
            'class': [self.data.__class__.__name__],
            'links': [
                {'href': href, 'rel': 'self'}
            ]
        }

    def make_entities(self):
        entities = []
        for item in self.data:
            entities.append(self.make_entity(item))

        fields = []
        name = 'add-item'
        if self.model:
            fields = self.model.get_columns()
            name = 'add-' + self.model._meta.name

        actions = [
            {'name': name, 'method': 'POST', 'type': 'application/json',
             'fields': fields}
        ]
        links = self.paginate()
        return {'entities': entities, 'actions': actions, 'links': links}

    def encode(self):
        if type(self.data) == list:
            return ujson.dumps(self.make_entities())
        return ujson.dumps(self.make_entity(self.data))
