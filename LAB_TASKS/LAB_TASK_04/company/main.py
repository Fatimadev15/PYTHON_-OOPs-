from company_interface.toy.engine_driver import EngineDriver
from company_interface.toy.gardener import Gardener
from company_interface.toy.clown import Clown
from company_interface.toy.bank_manager import BankManager

if __name__ == "__main__":

    toy1 = EngineDriver("Small")
    toy1.make_noise()
    toy1.show()
    toy1.inspect_engine()
    toy1.signal_departure()
    print()

    toy2 = Gardener("Medium")
    toy2.make_noise()
    toy2.show()
    toy2.water_flowers()
    toy2.talk_to_plants()
    print()

    toy3 = Clown("Large")
    toy3.make_noise()
    toy3.show()
    toy3.blow_balloons()
    toy3.perform_tricks()
    print()

    toy4 = BankManager("Medium")
    toy4.make_noise()
    toy4.show()
    toy4.open_account()
    toy4.review_transactions()
    print()
