class Toy:
    def __init__(self, color, size, job):
        self._color = color
        self._size = size
        self._job = job

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job

    def show(self):
        print("I am", self.color, self.job, "of size", self.size)