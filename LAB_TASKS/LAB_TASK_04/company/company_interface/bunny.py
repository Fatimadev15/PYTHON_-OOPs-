from toy import Toy

class Bunny(Toy):
    def __init__(self, color, size, job):
        super().__init__(color, size, job)

    def make_noise(self):
        print("Squeak-squeak! Your fluffy friend is here!")

    def hide_eggs(self):
        print("I'm hiding colorful eggs for a fun surprise!")

    def sniff_flowers(self):
        print("flowers smell like springtime joy!")
