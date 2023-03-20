class Rectangle:
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2))** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            result = ""
            for i in range(self.height):
                for j in range(self.width):
                    result += "*"
                result += "\n"
            return result

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

class Square(Rectangle):
    def __str__(self):
        return "Square(side={})".format(self.width)

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
