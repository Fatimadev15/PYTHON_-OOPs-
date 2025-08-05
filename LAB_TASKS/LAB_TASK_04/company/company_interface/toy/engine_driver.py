from company_interface.teddy import Teddy

class EngineDriver(Teddy):
    def __init__(self, size):
        super().__init__("Blue", size, "Engine Driver")

    def inspect_engine(self):
        print("Engine Driver carefully inspects the engine — everything looks perfect!")

    def signal_departure(self):
        print("Engine Driver blows the whistle — time to roll out from the station!")
