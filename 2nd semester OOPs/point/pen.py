class Pen:
    def __init__(self, name, type, color):
        self.cp_x = 0
        self.cp_y = 0
        self.cp_z = 0
        self.name = name
        self.type = type
        self.color = color

    def set_coordinates_3D(self, cp_x, cp_y, cp_z):
        self.cp_x = cp_x
        self.cp_y = cp_y
        self.cp_z = cp_z

    def set_info(self, name, pen_type, color):
        self.name = name
        self.type = pen_type
        self.color = color

    def write(self):
        print("This pen is best for smooth writing!")

    def show(self):
        print(f"{self.name}")
        print(f"{self.type}")
        print(f"{self.color}")
        print(f"({self.cp_x}, {self.cp_y}, {self.cp_z})")