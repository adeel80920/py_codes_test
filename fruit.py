class Fruit:
        def __init__(self, name, price):
            self.fruit_name = name
            self.fruit_price = price
         
        def name_app(self):
            print(f"Name of fruit is {self.fruit_name}")

        def price_app(self):  
            print(f"price is:{self.fruit_price}")

def main():  
     apple = Fruit("Irani Apple",200) 
     apple.name_app()
     apple.price_app()

if __name__ == "__main__":
 main()