class Circle:
    def __init__(self,radius,center):
        self.radius=radius
        self.center = center

    def set(self,center):
        self.center=center
        self.radius=radius

    def get(self):
        return self.center
        return self.radius

    def show(self):
        print("radius of circle:",self.radius)
        print("center points",(self.center))

