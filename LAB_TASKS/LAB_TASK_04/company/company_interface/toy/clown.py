from company_interface.bunny import Bunny

class Clown(Bunny):
    def __init__(self, size):
        super().__init__("White", size, "Clown")

    def blow_balloons(self):
        print("Clown is blowing colorful balloons for everyone!")

    def perform_tricks(self):
        print("Clown is performing tricks with a magic hat.")    