from company_interface.bunny import Bunny

class BankManager(Bunny):
    def __init__(self, size):
        super().__init__("Black", size, "Bank Manager")

    def open_account(self):
        print("Bank Manager is opening a new savings account for a customer.")

    def review_transactions(self):
        print("Bank Manager is reviewing recent transactions.")

