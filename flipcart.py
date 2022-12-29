class Cart: 
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price 
        self.deal_price = deal_price
        self.rating = rating
        self.you_saved = price - deal_price
    def display_prodect_details(self):
        print("product : {}".format(self.name))
        print("price : {}".format(self.price))
        print("deal_price : {}".format(self.deal_price))
        print("rating : {}".format(self.rating))
        print("you_saved : {}".format(self.you_saved))

class ElceticIteam(Cart):
    def __init__(self,name,price,deal_price,rating,warrenty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warrenty_in_months = warrenty_in_months
    def display_prodect_details(self):
        super().display_prodect_details()
        print("warrenty_in_months : {}".format(self.warrenty_in_months))
        
class GroceryIteam(Cart):
    def __init__(self,name,price,deal_price,rating,expired_date):
        super().__init__(name,price,deal_price,rating)
        self.expired_date = expired_date
    def display_prodect_details(self):
        super().display_prodect_details()
        print("expired_date : {}".format(self.expired_date))
        
        
class order:
    delivery_charges = {
            "normal" : 0,
            "prime_delivery" : 100
        }
    def __init__(self,delivery_method,delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address
        
    def add_item(self,product,quntatiy):
        item = (product,quntatiy)
        self.items_in_cart.append(item)
        
    def define_display_order_detals(self):
        print("delivery_method {}".format(self.delivery_method))
        print("delivery_address {} ".format(self.delivery_address))
        print("product")
    total_bill = self.total_bill()
    print("total bill {}".format(total_bill))
    def total_bill(self):
        total = 0 
        for product,quntatiy in self.items_in_cart:
            total_bill + total_bill + product.deal_price * quntatiy
        return total_bill
            
tv = ElceticIteam("tv",4000,500,4.5,24)
milk = GroceryIteam("milk",20,3,4.8,"Jan 23")
tv.display_prodect_details()
milk.display_prodect_details()