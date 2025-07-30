from point_interface.point_3D.point_3D import Point_3D
from pen import Pen

Dimension_3D = Point_3D(10, 12, 15)

piano = Pen("Silk", "Ball-point", "Blue")
piano.set_coordinates_3D(
    Dimension_3D.get_x(),
    Dimension_3D.get_y(),
    Dimension_3D.get_z()
)

piano.show()