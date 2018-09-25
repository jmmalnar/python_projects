import unittest

# Find all the prime numbers less than a given integer

def is_prime(num):
    """
    Iterate from 2 up to the (number-1).
    Assume the number is prime, and work through all lower numbers.
    If the number is divisible by ANY of the lower numbers,
    then it's not prime
    """
    prime_status = True

    # 1, by definition, is not a prime number, so lets account for that directly
    if num == 1:
        prime_status = False
        return prime_status

    for i in range(2, num):
        mod = num % i
        if mod == 0:
            prime_status = False
            break
    return prime_status




def find_primes(num):

    primes = []

    for n in range(1, num):
        prime_status = is_prime(n)
        if prime_status:
            primes.append(n)
    return primes


########
# TEST #
########

class IsPrimesTest(unittest.TestCase):
    def test_19_should_be_prime(self):
        """Verify that inputting a prime number into the is_prime method returns true"""
        self.assertEqual(is_prime(19), True)

    def test_20_should_not_be_primer(self):
        """Verify that inputting a non-prime number into the is_prime method returns false"""
        self.assertEqual(is_prime(20), False)

    def test_1_should_not_be_prime(self):
        """Verify that inputting a non-prime number into the is_prime method returns false"""
        self.assertEqual(is_prime(1), False)

class FindPrimesTests(unittest.TestCase):
    def test_primes_to_20(self):
        primes = find_primes(20)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_1_should_not_be_prime(self):
        primes = find_primes(1)
        self.assertEqual(primes, [])

if __name__ == '__main__':
    unittest.main()