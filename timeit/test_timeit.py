import unittest
from time import sleep

from timeit import timeit


class TestTimeit(unittest.TestCase):
    def test_ok(self):
        self.called = False

        def check_total(total):
            self.called = True
            self.assertAlmostEqual(total, 0.1, 5)

        @timeit(check_total)
        def x():
            sleep(0.1)

        x()

        self.assertTrue(self.called)

    def test_failed(self):
        @timeit(None)
        def x():
            sleep(0.1)

        with self.assertRaises(TypeError):
            x()

if __name__ == '__main__':
    unittest.main()