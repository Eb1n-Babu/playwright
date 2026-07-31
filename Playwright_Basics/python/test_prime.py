import unittest
from primeNumber import prime

class TestPrimeNumber(unittest.TestCase):
    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 13, 97]
        for num in primes:
            with self.subTest(i=num):
                self.assertTrue(prime(num))

    def test_non_prime_numbers(self):
        non_primes = [0, 1, 4, 6, 9, 100]
        for num in non_primes:
            with self.subTest(i=num):
                self.assertFalse(prime(num))

    def test_negative_numbers(self):
        negatives = [-1, -5, -23]
        for num in negatives:
            with self.subTest(i=num):
                self.assertFalse(prime(num))

if __name__ == '__main__':
    unittest.main()
