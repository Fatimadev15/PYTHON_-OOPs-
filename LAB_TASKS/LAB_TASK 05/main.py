from triangle import Triangle

if __name__ == "__main__":

    t1 = Triangle.default()
    print("Default:", t1)
    print("Perimeter:", t1.perimeter())
    print("Right angled?", t1.is_right_angled())
    print()


    t2 = Triangle.equilateral(5)
    print("Equilateral:", t2)
    print("Perimeter:", t2.perimeter())
    print("Right angled?", t2.is_right_angled())
    print()


    t3 = Triangle.isosceles(4, 6)
    print("Isosceles:", t3)
    print("Perimeter:", t3.perimeter())
    print("Right angled?", t3.is_right_angled())
    print()


    t4 = Triangle(3, 4, 5)
    print("Scalene:", t4)
    print("Perimeter:", t4.perimeter())
    print("Right angled?", t4.is_right_angled())
    print()


    t5 = Triangle.from_existing(t4)
    print("Cloned:", t5)
    print("Perimeter:", t5.perimeter())
    print("Right angled?", t5.is_right_angled())
    print()


    print("Total Triangles Created:", Triangle.object_count())