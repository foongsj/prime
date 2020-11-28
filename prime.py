#!/usr/local/bin/python3

import argparse, math

parser = argparse.ArgumentParser()

parser.add_argument("number", nargs="?", type=int, default=12,
  help="Number to factorize into primes, default 12")

args = parser.parse_args()

n = int(args.number)
limit = int(math.sqrt(n))

print(n, limit)
factors = []
i = 2
while i <= limit:
  if n % i:
    i = i + 1
  else:
    factors.append(i)
    n = n / i
    limit = int(math.sqrt(n))

factors.append(int(n))
print(factors)
