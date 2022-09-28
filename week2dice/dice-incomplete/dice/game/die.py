import random
# : Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
 
"""A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
class Die:

# 2) Create the class constructor. Use the following method comment.

    def __init__(self):
        self.value = 0
        self.points = 0



# 3) Create the roll(self) method. Use the following method comment.
        """Generates a new random value and calculates the points.Args:
            self (Die): An instance of Die.
        """
    def roll(self):
        number = random.randint(1,6)
        self.value = number
        if number == 5:
            random_point = 50
            self.points = random_point
        elif number == 1:
            random_point = 100
            self.points = random_point
        else:
            random_point = 0
            self.points = random_point