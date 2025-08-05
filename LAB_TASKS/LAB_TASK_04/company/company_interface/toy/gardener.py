from company_interface.teddy import Teddy

class Gardener(Teddy):
    def __init__(self, size):
        super().__init__("Red", size, "Gardener")

    def water_flowers(self):
        print("Gardener gently waters the blooming flowers with love.")

    def talk_to_plants(self):
        print("Gardener whispers kind words to help the plants grow strong.")
 