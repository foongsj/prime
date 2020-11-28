#!/usr/local/bin/python3

import argparse, math

parser = argparse.ArgumentParser()

parser.add_argument("number", nargs="?", type=int, default=12,
  help="Positive integer to factorize into primes, default 12")

args = parser.parse_args()

n = int(args.number)
if n < 2:
  print("There are no primes as number is less than 2.")
  exit(1)
limit = int(math.sqrt(n))

factors = []

# Initialize with first prime
i = 2
while i <= limit:
  if n % i:
    i = i + 1
  else:
    factors.append(i)
    n = n / i
    limit = int(math.sqrt(n))

factors.append(int(n))
print("The primes are:", factors)
