# Solution for problem #12 at Project Euler
# (http://projecteuler.net/index.php?section=problems&id=12)
# Author: Baishampayan Ghose <b.ghose@gnu.org>
 
from math import sqrt
import sys
 
# import psyco
# psyco.full()
 
def factors(x):
    ''' return the number of divisors of x
    '''
    num = 2 # itself and 1
    for i in xrange(2, int(sqrt(x)) + 1):
        if ((x % i) == 0):
            if (i != sqrt(x)):
                num += 2
            else:
                num += 1
    return num
 
def triangle():
    ''' generate triangular numbers
    '''
    i = 1
    while True:
        yield int(0.5 * i * (i + 1))
        i += 1
 
 
t = triangle()
 
while True:
    num = t.next()
    if (factors(num) >= 501):
        print num
        sys.exit(0)
