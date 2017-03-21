class Guest:
    def __init__(self,n,h):
        self.name = n
        self.hunger = h
        
    def eat(self):
        self.hunger-1
        print(self.hunger)
        if self.hunger==0:
            print("I am full!")
            
    
    
g = Guest("Niamh",0)

g.eat()

class Restaurant:
    
    def __init__(self,s):
        self.size = s
        self.my_list=[None]*s
        
    def seat(self, guest):
        
        for i in range len(self.my_list)
        
        if self.my_list.count(None) != 0:
            print("No free tables!")
        else:
            self.my_list[None]="Occupied"
            
    def serve(self):