from point_interface.point_2D import Point_2D

class Point_3D(Point_2D):
    def __init__(self,x , y, z):
        super().__init__(x, y)
        self.z = z

    def set_z(self, z):
        self.z = z

    def get_z(self):
        return self.z

    def set_3D(self, x, y, z):
        self.set_x(x)
        self.set_y(y)
        self.z = z