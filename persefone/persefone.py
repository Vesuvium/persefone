# -*- coding: utf-8 -*-


class Persefone():

    def __init__(self, data, path, model=None, total_items=0, current_page=1):
        self.data = data
        self.path = path
        self.model = model
        self.total_items = total_items
        self.current_page = current_page

    def encode(self):
        raise NotImplementedError
