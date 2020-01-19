# 69. lesson - Make all of the coins
# polymorphisms
# abstract classes

import random

class Coin: # general class
    def __init__(self, rare=False, clean=True, heads=True, **kwargs): 
# packing arguments inside dict kwargs

# loop over kwargs to define self. is
        for key,value in kwargs.items():
            setattr(self,key,value)
# taking thickness, parameter, flexible...for any dict

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            set.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color # general category - we cannot say greenish

    def clean(self):
        self.color = self.clean_color # cannot say gold

    # def __del__(self): # destructor
    #     print("Coin spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    


class Pound(Coin): # delete pound class; make it inherit to Coin instead
# it is going to get all of the methods
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)
# using parent class to set up everything else
# run innit
# inside init - we get the parent's init = constructer for the data of coins
# call the generic class to set up everything else
# we pass data to the parent's innit and let it deal with it - super function it means parent
# unpacking data from the dict and packing it up above

one_pound_coin = Pound()
print(one_pound_coin.color)
# Output:
# gold

one_pound_coin.rust()
print(one_pound_coin.color)

# Output:
# greenish

# 70. lesson
class One_Pence(Coin):
    def __init__(self):

        data = {
            "original_value": 0.01,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }
        super().__init__(**data)

class Two_Pence(Coin): 
    def __init__(self):

        data = {
            "original_value": 0.02,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }
        super().__init__(**data)

class Five_Pence(Coin): # delete pound class; make it inherit to Coin instead
# it is going to get all of the methods
    def __init__(self):

        data = {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self): # probably not necessary - inherited
            self.color = self.clean_color

class Ten_Pence(Coin): # delete pound class; make it inherit to Coin instead
# it is going to get all of the methods
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
        }
        super().__init__(**data)

class Twenty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
        }
        super().__init__(**data)

class Fifty_Pence(Coin): 
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00
        }
        super().__init__(**data)
        
class One_Pound(Coin): # delete pound class; make it inherit to Coin instead
# it is going to get all of the methods
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

class Two_Pound(Coin): 
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00
        }
        super().__init__(**data)



