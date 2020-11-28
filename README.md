# prime

Simple script to decompose a positive integer into its primes

<pre>
usage: prime.py [-h] [number ...]

positional arguments:
  number      Positive integer to factorize into primes, default 12

optional arguments:
  -h, --help  show this help message and exit

If more than 1 argument is provided, the script also calculates GCF and LCM.
</pre>

## Sample Output
<pre>
./prime.py 21 14
The primes for 21 are [3, 7]
The primes for 14 are [2, 7]
GCF primes: [7] = 7
LCM primes: [3, 7, 2] = 42
</pre>
