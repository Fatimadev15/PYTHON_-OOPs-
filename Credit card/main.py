from card_interface.creditcard import Credit

card = Credit("fatima","HBL",3572839729,10000)     
print ("customer name:",card.get_customer())
print ("bank:",card.get_bank())
print ("acc no:",card.get_acc())
print ("card limit:",card.get_limit())
print ("charge:",card.charge(5000))
print (card.payment_method(500))