class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def display_bike(self):
        print("Total Bikes", self.stock)
    def Bike_rent(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print('Enter the quantity less then the stock')
        else:
            self.stock=self.stock-q
            print("Total price of bike", q*100)
            print("Total bike left",self.stock)

while True:
    obj=BikeShop(100)
    uc=int(input('''
    1 Display Available Bikes
    2 Bike for Rent
    3 Exit   
'''))
    if uc==1:
            obj.display_bike()
    elif uc==2:
        n=int(input("Enter the quantity:-"))
        obj.Bike_rent(n)
    else:
        break
