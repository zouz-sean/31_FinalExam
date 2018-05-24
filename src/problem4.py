"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Zhengxiao Zou.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    pig1 = Pig(100)
    print('the weight of the pig1 is:',pig1.w)
    w1 = pig1.get_weight()
    print('the pig1 weight using get weight function:',w1)
    pig1.eat(100)
    print('New pig weight after eating 100:',pig1.w)
    pig1.eat_for_a_year()
    print('New pig weight after eating for a year(a pound a day):', pig1.w)
    pig2 = Pig(300)
    print('the weight of the pig2 is:', pig1.w)
    the_heacy_pig = pig1.heavier_pig(pig2)
    print('This is the weight of the heavier pig:',the_heacy_pig.get_weight())
    pig3 = pig1.new_pig(pig2)
    print('This is the weight of the new pig:', pig3.get_weight())


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.
        self.w = weight

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.
        return self.w

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.
        self.w = self.w + pounds_of_slop
    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.
        for k in range (365):
            self.eat(1)

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.
        if self.w > other_pig.w:
            return self
        else:
            return other_pig

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.
        if self.w > other_pig.w:
            newpig = self
        else:
            newpig = other_pig
        return newpig



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
