"""
Problem:

    Professor Oak is interested in developing a simulator for pokemon battles,
    to try and see who will win. The function 'battle' is his first attempt.

    'battle' takes 4 arguments, the names of both pokemons and their power
    level. It should print out the name of the winner, unless it is a draw
    in which case it should print "Draw"

    Professor Oak's first attempts at creating some rules for his simulator
    are very simple: the pokemon with the highest power wins UNLESS one of
    the pokemon is Mewtwo. Mewtwo is so awesome, his actual power level
    should be considered 100 more than it actually is.

Tests:

    >>> battle("Pikachu", 80, "Bulbasaur", 110)
    Bulbasaur
    >>> battle("Squirtle", 150, "Weedle", 90)
    Squirtle
    >>> battle("Pidgey", 200, "Rattata", 200)
    Draw
    >>> battle("Mewtwo", 90, "Vileplume", 150)
    Mewtwo
    >>> battle("Golduck", 170, "Mewtwo", 50)
    Golduck
    >>> battle("Abra", 120, "Mewtwo", 20)
    Draw
    >>> battle("Mewtwo", 60, "Mewtwo", 60)
    Draw

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)
        if name1 == "Mewtwo":
        power1 == power1+100

    if name2 == "Mewtwo":
        power2 == power2+100

    if name1 == "Mewtwo" or name2 == "Mewtwo":
        print("Draw")


    elif power1 < power2:
        print(name2)

    elif power2 < power1:
        print(name1)

    else:
        print("Draw")

    


# Edit this code
def battle(name1, power1, name2, power2):

