

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Customer:
    def __init__(self,name,balacne,):
        self.name = name
        self.balance = balacne
        self.cart = []

    def add_to_cart(self,product):
        self.cart.append({
            "name":product.name,
            "price":product.price,
            "quantity":product.quantity,
        })
        
    def shop(self,):
        price_list = list(product["price"] for product in self.cart)
        amount_list = list(product["quantity"] for product in self.cart)
        
        price = 0

        for p, a in zip(price_list,amount_list):
            price += p * a 
        
        if self.balance < price:
            return 

        self.balance -= price

        return f"Покупка прошло успешно\n Ваш балан {self.balance}"

acer_swift = Product("Acer Swift 3",20000,1)
note_11 = Product("RedMi Note 11",7000,1)

hikmatulloh = Customer("Hikmatulloh",40000)

hikmatulloh.add_to_cart(acer_swift)
hikmatulloh.add_to_cart(note_11)

print(hikmatulloh.shop())