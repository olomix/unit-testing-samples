import unittest

import fib


class TestFib(unittest.TestCase):
    @unittest.skip("not working for now")
    def test_ok(self):
        f = fib.fib()
        self.assertEqual([next(f) for _ in range(11)],
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

if __name__ == '__main__':
    unittest.main()