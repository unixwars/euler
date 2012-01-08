"""
Library for common Euler functions
"""
import time
import math
import sys
import random
from fractions import gcd # handy to have here

def fibonacci():
    """Infinite Fibonacci sequence generator
    """
    x,y = 0,1
    while True:
        x,y = y, x+y
        yield x


def sieve():
    """Sieve of Erathostenes. Generate an infinite sequence of prime
    numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # http://refactormycode.com/codes/1130-sieve-of-eratosthenes
    D = {}
    q = 2 # running integer that's checked for primeness

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

prime = sieve


def prime_factors (N):
    """Return prime factors of N
    """
    if N == 1: return [1]
    factors = []
    for p in sieve():
        if p > N:
            break
        
        while N % p == 0:
            factors.append(p)
            N = N / p
    return factors


def triangle(n=1):
    """Generate infintie sequence of triangle numbers (1st=1, 2nd =
    1+2, 3rd = 1+2+3...), optionally beginnig at the nth element
    """
    while True:
        yield (n*(n+1))/2
        n+=1

def binomial_coefficient (n, k):
    """Combinations of k elements from a group of n = n! / (k!(n-k)!)
    """
    num = math.factorial(n)
    den = math.factorial(k)*math.factorial(n-k)
    return num/den


def benchmark(func):
    """Decorator to benchmark execution times
    """
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print 'Processing time: %s (%s)' %(time.clock()-t, func.__name__)
        return res
    return wrapper


def proper_divisors (n):
    """Generate list of proper divisors of N, that is, the ones that
    divide it evenly
    """   
    aux = [1]
    for i in range(2, (n+1)/2+1):
        if n%i==0:
            aux.append(i)
    return aux


def proper_divisors (n):
    """Generate list of proper divisors of N, that is, the ones that
    divide it evenly, excluding itself.
    """
    # Instead of testing up until max = (n+1)/2, we can accelerate the
    # process by just going up to sqrt(n). Then, every n/i will also
    # be a divisor except when n/i==i. This method is orders of
    # magnitude faster.

    divisors = set()
    for i in range(1, int(math.sqrt(n)+1)):
        if(n % i == 0):
            divisors.add(i)
            if (n/i == n): continue
            divisors.add(n/i)
    return sorted(list(divisors))
 

def bellman_ford(g, start):
    """
    The Bellman-Ford algorithm:
    http://en.wikipedia.org/wiki/Bellman-Ford_algorithm

    Find shortest path using Bellman-Ford algorithm. The starting
    point must be any vertex of the graph, and this structure is like:

        graph = {
            'a': {'b': -1, 'c':  4},
            'b': {'c':  3, 'd':  2, 'e':  2},
            'c': {},
            'd': {'b':  1, 'c':  5},
            'e': {'d': -3}
            }

    Graph API:

        iter(graph) gives all nodes
        iter(graph[u]) gives neighbours of u
        graph[u][v] gives weight of edge (u, v)
    """
    paths = {}
    costs = dict([(k, float('inf')) for k in g.keys()])
    costs[start] = 0

    edges = []
    for node, adj in g.items():
        for aux in adj.keys():
            edges.append((node, aux))
            
    # relax edges
    for i in range(1, len(g) - 1):
        for u, v in edges:
            if costs[u] + g[u][v] < costs[v]:
                costs[v] = costs[u] + g[u][v]
                paths[v] = u

    # check negative cycles
    for u, v in edges:
        if costs[u] + g[u][v] < costs[v]:
            raise Exception, 'Negative weight cycle detected'

    return paths, costs


def miller_rabin(n, s = 50):
    """
    Mille-Rabin primality test (probabilistic, but very fast).
    miller_rabin(n, s = 1000) -> bool Checks whether n is prime or not
    http://snippets.dzone.com/posts/show/4200

    This is an extremley fast algorithm designed to test very large
    numbers.  s is the number of tests to perform. The chance that
    Rabin-Miller is mistaken about a number (i.e. thinks it's prime,
    but it's not) is 2^(-s). So, a value of 50 for s is more than
    enough for any imaginable goal (2^(-50) is
    8.8817841970012523e-16).    

    Returns:
    - True, if n is probably prime.
    - False, if n is complex.
    """
    def toBinary(n):
        r = []
        while (n > 0):
            r.append(n % 2)
            n = n / 2
        return r

    def is_complex(a, n):
        """
        is_complex(a, n) -> bool Tests whether n is complex (False if n
        is a probable prime).
        """
        b = toBinary(n - 1)
        d = 1
        for i in xrange(len(b) - 1, -1, -1):
            x = d
            d = (d * d) % n
            if d == 1 and x != 1 and x != n - 1:
                return True # Complex
            if b[i] == 1:
                d = (d * a) % n
        if d != 1:
            return True # Complex
        return False # Prime

    if n < 1:
        return False
    if n == 1:
        return True
    
    for j in xrange(1, s + 1):
        a = random.randint(1, n - 1)
        if (is_complex(a, n)):
            return False # n is complex
    return True # n is prime

is_prime = miller_rabin
