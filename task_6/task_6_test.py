import unittest
from task_6_program import poly, count_characters, fizzbuzz


class Test(unittest.TestCase):
    def test_count_characters(self):
        example = {'H': 1, 'e': 1, 'l': 3, 'o': 2,
                   ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        self.assertEqual(count_characters('Hello, world'), example)

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), ['1', '2', 'Fizz'])
        self.assertEqual(fizzbuzz(5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(fizzbuzz(15), ['1', '2', 'Fizz', '4', 'Buzz',
                                        'Fizz', '7', '8', 'Fizz', 'Buzz',
                                        '11', 'Fizz', '13', '14', 'FizzBuzz'])
        self.assertEqual(fizzbuzz(0), [])

    def test_poly(self):
        self.assertFalse(poly(8855332))
        self.assertTrue(poly('cakekac'))
        self.assertTrue(poly())


if __name__ == '__main__':
    unittest.main()
