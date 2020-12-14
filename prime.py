#!/usr/local/bin/python3

import argparse, math
from collections import Counter

def primes(n):
  # Returns a list of primes of n
  factors = []
  if n < 2:
    print("There are no primes as number is less than 2.")
    return(factors)
  
  # The upper limit of prime factors of n cannot be more then the sqrt rounded down
  limit = int(math.sqrt(n)+0.5)

  # Initialize with first prime
  i = 2
  while i <= limit:
    if n % i: # is n divisible by i?
      i = i + 1 # if not, increment i by 1. 
      # We are wasting cycles by not checking if i is prime, but unless we already have a list of primes, 
      # figuring out if i is prime may take even longer. By doing blind incrementing, non prime i
      # will be skipped as they won't be able to divide the new n.
    else:
      factors.append(i) # otherwise, i is factor of n
      n = n / i 
      limit = int(math.sqrt(n)+0.5)
  factors.append(int(n))
  return(factors)


if __name__ == "__main__":
  # execute only if run as a script
  parser = argparse.ArgumentParser(epilog="If more than 1 argument is provided, the script also calculates GCF and LCM.")
  parser.add_argument("number", nargs="*", type=int, default=[12],
    help="Positive integer to factorize into primes, default 12")

  args = parser.parse_args()
  fDict = {}
  intersect = Counter()
  union = Counter()
  iniFlag = False # On first entry to loop, initialize intersect and union
 
  for n in args.number:
    fDict[n] = primes(n)
    print("The primes for %i are %s" % (n, fDict[n]))
    if len(args.number) > 1:
      if iniFlag:
        intersect = intersect & Counter(fDict[n])
      else:
        intersect = Counter(fDict[n]) 
      if iniFlag:
        union = union | Counter(fDict[n])
      else:
        union = Counter(fDict[n])
      iniFlag = True # Mark that the intersect and union has been initialized

  if len(args.number) > 1:
    try: # Use math.prod if available
      gcf = math.prod(list(intersect.elements()))
      lcm = math.prod(list(union.elements()))
    except AttributeError: # fallback to reduce if math.prod is not available
      from functools import reduce
      lcm = reduce(lambda x,y: x*y, list(union.elements()))
      try: # reduce will throw an error is empty, lcm should never be empty
        gcf = reduce(lambda x,y: x*y, list(intersect.elements()))
      except TypeError:
        gcf = 1
      
    print("GCF primes:", list(intersect.elements()), "=", gcf)
    print("LCM primes:", list(union.elements()), "=", lcm)

