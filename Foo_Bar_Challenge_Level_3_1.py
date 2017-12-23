"""
Google Foo Bar challenge Level 3 - Stage 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Find the Access Codes
In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need
access to it. But the only door leading to the LAMBCHOP chamber is secured with
a unique lock system whose number of passcodes changes daily. Commander Lambda
gets a report every day that includes the locks' access codes, but only she
knows how to figure out which of several lists contains the access codes. You
need to find a way to determine which list contains the access codes once
you're ready to go in.
Fortunately, now that you're Commander Lambda's personal assistant, she's
confided to you that she made all the access codes "lucky triples" in order to
help her better find them in the lists. A "lucky triple" is a tuple (x, y, z)
where x divides y and y divides z, such as (1, 2, 4). With that information,
you can figure out which list contains the number of access codes that matches
the number of locks on the door when you're ready to go in (for example, if
there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access
codes).
Write a function answer(l) that takes a list of positive integers l and counts
the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k.
The length of l is between 2 and 2000 inclusive.  The elements of l are between
1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some
of the lists are purposely generated without any access codes to throw off
spies, so if no triples are found, return 0.
For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6],
[1, 3, 6], making the answer 3 total.

"""

from itertools import combinations
from random import randrange


def answer(l):
    """ Returns the number of 'lucky triples' present in a given list (size 2 to 2000) 
        of integers (1 to 999999).
        
        Lucky triple is defined as a list of three numbers (x, y, z) such that x divides y, 
        and y divides z and the indices of x, y & z (i, j, k) are such that i < j < k
    """
    d, m = ([0] * len(l) for _ in range(2))
    for i, x in enumerate(l):
        for j, y in enumerate(l[i+1:], i+1):
            if y % x == 0:
                d[j] += 1
                m[i] += 1
    return sum([d[x] * m[x] for x, _ in enumerate(l)])


def safe_solution(l):
    """ Expected solution computed using the traditional long route.
        Used for validation only.
    """
    sol = 0
    for x, y, z in combinations(l, 3):
        if y % x == 0 and z % y == 0:
            sol += 1
    return sol


def test(test_size):
    """ Test the results of answer function against expected results """
    random_list = [randrange(1, test_size) for _ in range(test_size)]
    my_solution = answer(random_list)
    expected_solution = safe_solution(random_list)
    if my_solution != expected_solution:
        print("Failed on {!r}\n My Solution = {}, Expected Solution = {}".
              format(random_list, my_solution, expected_solution))
        return False
    else:
        return True

if __name__ == '__main__':
    print('Running random test cases')
    if all([test(i) for i in range(2, 100)]):
        print('All tests passed')
    else:
        ('Testing completed with some errors')
