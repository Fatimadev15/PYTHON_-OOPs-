class Line:
    def __init__(self,length,start_point,end_point):
        self.length=length
        self.start_point=start_point
        self.end_point=end_point

    def set(self,length,start_point,end_point):
        self.length=length
        self.start_point=start_point
        self.end_point=end_point

    def get(self):
        return self.length,self.start_point,self.end_point

    def show(self):
        print("length",self.length)
        print("start_points",self.start_point)
        print("end_points",self.end_point)
