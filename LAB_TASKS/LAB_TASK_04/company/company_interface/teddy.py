from toy import Toy

class Teddy(Toy):
    def __init__(self, color, size, job):
        super().__init__(color, size, job)

    def make_noise(self):
        print("Rawrr! I'm your fuzzy bedtime guardian.")

    def tell_story(self):
        print("Once upon a time, in a cozy little forest, there lived a brave little teddy...")

    def dance(self):
        print(" it's teddy dance time!")
      