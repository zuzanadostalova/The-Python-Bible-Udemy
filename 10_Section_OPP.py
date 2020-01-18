# # 65. lesson - Object Oriented Programming Section overview
# # objects, classes
# # class variables, class methods
# # class constructors and destructors, class variable and class methods

# # Model a coin
# # model a sets of coins
# # build your own bank

# # 66. lesson - classes and objects
# # objects coming from templates, template in programming = class
# # class/template to get and object (copy = instance)
# # if we make an instance of a class => object

# # classes made from variables = states, functions = methods
# # each variable in Python has its own class
# # they act differently based on diff. states and methods

# # states: value = 0.1 (pound), color = "silver", number of edges = 1, 
# # diameter = 24.5 (mm), thickness = 1.85 (mm), heads = True

# # methods: flip() -  change state randomly from heads to tails and conv.

# # real life object - states and behaviour/actions
# # in programming -  we use variables to create states and methods to create actions

# # methods = the same as functions, we call them methods refering to classes

# # 67. lesson - Making a coin
# class Pound: # class has 6 states

#     value = 1.00
#     color = "gold"
#     num_edges = 1
#     diameter  = 22.5 # mm
#     thickness = 3.15 # mm
#     heads = True # heads is true


# coin1 = Pound() # instance of class = object
# print(coin1.value) # type object name coin1. and pick up one of the states - value
# # Output: 1.0
# print(type(coin1))
# # Output: <class '__main__.Pound'>
# print(coin1.color)
# # Output: gold

# # we can change the states in the run
# coin1.color = "greenish"
# print(coin1.color)
# # Output: greenish

# coin2 = Pound()
# print(coin2.color)
# # Output: gold ... difference btw objects and classes - class is a template, new 
# # objects are made from it, the created object then becomes independent of the class
# # and can have different characteristics

# coin1.value = 1.25
# print(coin1.value)
# # Output: 1.25

# print(coin2.value)
# # Output: 1.0 - we can see that even if they originated from the same
# # template coin1 and coin2 are independent of each other

# 68. lesson - Make your own coin II
class Pound: # class has 6 states

    def __init__(self, rare=False): # rare is boolean - more costly

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00 

        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter  = 22.5 
        self.thickness = 3.15 
        self.heads = True 

    def rust(self):
        self.color = "greenish"
    
    def __del__(self): # destructor
        print("Coin spent!")

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        import random
        choice = random.choice(heads_options)
        self.heads = choice

# constructor def __init__(self) to create class methods
# self -  refers to specific instance of the class when we write its code
# self  - coin1 e.g.

# coin1 = Pound(rare=True)

# print(coin1.rare)
# print(coin1.value)
# coin2 = Pound()

# print(coin2.rare)
# print(coin2.value)

# # Output: 
# # True
# # 1.25
# # False
# # 1.0

coin1 = Pound()
coin2 = Pound()
print(coin1.color)
print(coin2.color)
# Output: 
# gold
# gold

coin1.rust() # first we change color then we print it
print(coin1.color)
print(coin2.color)
# Output: 
# greenish
# gold

coin1.clean()
print(coin1.color)
# Output: 
# gold

coin1 = Pound()
print(coin1.heads)
# Output: 
# True
coin1.flip()
print(coin1.heads)
# Output: 
# False eventually

del coin1
print(coin1)
# Output: 
# Coin spent!

# different internal states of coins - one rusty, one normal
# object oriented encapsulation