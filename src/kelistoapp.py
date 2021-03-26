class Cesta(object):
    buy_one_get_one = False
    bulk_discount = False

    items = {'GR1':3.11, 'SR1':5.00, 'CF1':11.23}

    shop_cart = []

    def __init__(self, buy_one_get_one, bulk_discount):
        self.buy_one_get_one = buy_one_get_one
        self.bulk_discount = bulk_discount

    def scan(self, item):
        self.shop_cart.append(item)
    
    def total(self):
        totalPrice = 0
        gr1Count = 0
        sr1Count = 0
        for product in self.shop_cart:
            totalPrice += self.items[product]
            if product == 'GR1': gr1Count += 1
            if product == 'SR1': sr1Count += 1
        if self.buy_one_get_one == True:
            gr1Count = int(gr1Count / 2)
            totalPrice -= gr1Count * 3.11
        if self.bulk_discount == True and sr1Count >= 3:
            totalPrice -= sr1Count * 0.50
        print(totalPrice)