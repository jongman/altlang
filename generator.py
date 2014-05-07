from random import seed, normalvariate, randint
from sys import argv
from time import time

seed(argv[1] if len(argv) > 1 else None)
n = randint(10, 100)
print n
for i in xrange(n):
    print ' '.join(['%.4lf' % normalvariate(0, 1)
                    for j in xrange(n)])

