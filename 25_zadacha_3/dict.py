import copy


class MyDict:

    def __init__(self, *dicts):
        self.some_dict = dict()
        self.some_dict.update(*dicts)

    def __str__(self):
        temp_string = ''
        for items in self.some_dict.items():
            temp_string += str(items)
        return temp_string

    def get(self, key, default=0):
        for keys, value in self.some_dict.items():
            if key == keys:
                return value
        return default
