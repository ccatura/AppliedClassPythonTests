class car(): 
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 
        print()
          

audi = car("audi a4", "blue") 
ferrari = car("ferrari 488", "green") 
  
audi.show()     # same output as car.show(audi) 
ferrari.show()  # same output as car.show(ferrari) 
  
