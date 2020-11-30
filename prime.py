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
  limit = int(math.sqrt(n))

  # Initialize with first prime
  i = 2
  while i <= limit:
    if n % i: # is n divisible by i?
      i = i + 1 # if not, increment i by 1
    else:
      factors.append(i) # otherwise, i is factor of n
      n = n / i 
      limit = int(math.sqrt(n))
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
      if setflag:
        intersect = intersect & Counter(fDict[n])
      else:
        intersect = Counter(fDict[n]) 
      if setflag:
        union = union | Counter(fDict[n])
      else:
        union = Counter(fDict[n])
      iniFlag = True # Mark that the intersect and union has been initialized

  if len(args.number) > 1:
    try: # Use math.prod if available
      gcf = math.prod(list(intersect.elements()))
      lcm = math.prod(list(union.elements()))
    except AttributeError: # fallback to reduce
      from functools import reduce
      lcm = reduce(lambda x,y: x*y, list(union.elements()))
      if list(intersect.elements()):
        gcf = reduce(lambda x,y: x*y, list(intersect.elements()))
      else:
        gcf = 1
      
    print("GCF primes:", list(intersect.elements()), "=", gcf)
    print("LCM primes:", list(union.elements()), "=", lcm)

