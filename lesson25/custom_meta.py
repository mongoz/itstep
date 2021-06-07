class Metaclass(type):
    def __new__(self, class_name, bases, attrs):
        global class_new
        attr = {}
        for key, value in attrs.items():
            if not key.startswith('__'):
                attr['method_' + key] = value
                class_new = class_name.lower()
            else:
                attr[key] = value
        return type(class_new, bases, attr)


class Ork(metaclass=Metaclass):
    def __init__(self):
        self.method_ork = None
    heads = 2
    name = 'Jubilee'


def print_car(self):
    print(self.year)


if __name__ == '__main__':
    ork = Ork()
    print(ork.method_ork)