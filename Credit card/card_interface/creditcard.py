class Credit:

    def __init__(self,customer,bank,acc,limit):
        self.customer=customer
        self.bank=bank
        self.acc=acc
        self.limit=limit
        self.balance=0

    def get_customer (self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_acc (self):
        return self.acc

    def get_limit (self):
        return self.limit
    def get_balance(self):
        return self.balance

    def charge(self,price):
        if price+ self.balance >self.limit:
          return False                    
        else:
         self.balance += price 
         return True
       

    def payment_method(self,amount):   
        self.balance -= amount
        return self.get_balance()