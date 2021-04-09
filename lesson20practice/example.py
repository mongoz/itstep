snake_case = 'variables'


class Shape:
    color = 'green'
    form = 'rectangle'

    def change_color(self, color):
        self.color = color

    def change_form(self, form):
        self.form = form


rectangle = Shape()
print(rectangle)
print(rectangle.color, rectangle.form)

square = Shape()
print(square)
print(square.color, square.form)
