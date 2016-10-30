"""
Problem:

    A cinema has different prices depending on the day of the week,
    and the age of the customer.

    On a saturday, it costs £6.50 for everyone.
    
    On other days, it costs:
        - £4.00 for OAPS (65 or over)
        - £3.00 for Juniors (10 or under)
        - £5.00 for everyone else

    The function price, takes two inputs: the day of the week, and the
    age of the customer.  It should print the required price.

    The day of the week will always be provided in title case.

Tests:

    >>> price("Saturday", 25)
    £6.50
    >>> price("Saturday", 72)
    £6.50
    >>> price("Saturday", 4)
    £6.50
    >>> price("Monday", 8)
    £3.00
    >>> price("Tuesday", 45)
    £5.00
    >>> price("Wednesday", 65)
    £4.00
    >>> price("Thursday", 80)
    £4.00
    >>> price("Friday", 10)
    £3.00

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def price(day, age):
    
      if day == "Saturday":
        print("£6.50")

    elif age >= 65:
        print("£4.00")

    elif age <= 10:
        print("£3.00")

    else:
        print("£5.00")



