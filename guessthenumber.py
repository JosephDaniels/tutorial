#### here's an example of what I mean:
##
##class GameLogic(object):
##    """
##    I am a game of Guess My Number.
##
##    You a) start a game and I pick a number. b) you guess it. d) I tell if you are too high or too low until you win or lose
##
##    (**  This class implements ONLY the logic, if you want to actually interact with people or display results, you need to do more.
##    You'll either have to subclass it(the traditional object oriented solution) and replace any virtual functions, or (the hacky
##    way) directly replace any callbacks with other functions. Either way you need this following information.
##
##    For any object you need to know how to interact with it, this requires you to have some kind of interface across which
##    you perform actions on it(the methods). States of the objects are accessed via its attributes. You should limit them as
##    much as possible to keep the interface clean and clear. So this is the documented interface for this game:    **)
##
##    
##
##    The public interface to this game are these methods and attributes:
##    
##    start() - starts a game
##    guess(a_number) - you guess a number
##
##    win - a boolean that is set when you win a game
##    guesses_left - an int of the number yof guesses you have left
##
##    (note these attributes should be read-only, you shouldn't have to set them, they are
##    provided to let you easily read the state of the game)
##
##
##    - to interface this logic with your view a number of callbacks are used,
##    you override or replace these callbacks to 'wire' the response of the
##    game logic into your view and controller
##
##    do_too_high_callback() - during the do_guess() will call this on too high a guess
##    do_too_low_callback()  - "       "    "         "    "    "    "   "  low " "
##    do_win_callback()      - called on a winning guess
##    do_lose_callback()     - called on a losing guess
##    
##
##    """
##    def __init__(self):
##        self.guesses_left = 0
##        self.win = False
##
##    def start(self):
##        import random
##        self.guess_left = 4
##        self._true_answer = random.randint(1,10) ## note the leading _, this is supposed to be "private" and not part of the interface
##        self.win = False
##
##    def do_guess(self, guess):
##        if self.guesses_left == 0:
##            self.do_error_call_back("no more turns")
##        else:    
##            if guess > self._true_answer:
##                self.num_turns -= 1
##                self.do_too_high_callback()
##            elif guess<self._true_answer:
##                self.do_too_low_callback()
##            else:
##                self.win = True
##                self.do_win_callback()
##                
##    
##    # the following methods you need to override or replace to "wire" into your view/controller
##    
##    def too_high_call_back(self):
##        pass
##    
##    def too_low_call_back(self):
##        pass
##    
##    def win_call_back(self):
##        pass
##
##    def too_high_call_back(self):
##        pass
##    # if I want to do this 'properly' I should be raising a NotImplmented exception instead of  pass
##    # this will guarantee that I don't miss them  by accident and not properly
##    # have  handler in place.
##    # i.e.
##    # raise exception.NotImplemented()
##
#### *******
#### part two - tommorrow I will show how separating the logic as cleanly as possible makes for creating/using different views easier
###
##
