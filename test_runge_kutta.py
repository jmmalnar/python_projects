import unittest
from math import sqrt
from math import exp
from math import fabs
import runge_kutta as rk

# Test the charge_conservation method
class RungeKuttaTests(unittest.TestCase):

    #####
    # DEFINE the test Diff Eq with a known exact solution
    def f1(self, t, y):
        return t * sqrt(y)

    # DEFINE the exact solution of the test Diff Eq above
    def f1_exact(self, t):
        return (1/16) * (t**2 + 4)**2

    # DEFINE the test Diff Eq with a known exact solution
    def f2(self, t, y):
        return y - t**2 + 1

    # DEFINE the exact solution of the test Diff Eq above
    def f2_exact(self, t):
        return t**2 + 2*t + 1 - (1/2) * exp(t)

    #####
    # SETUP Before the tests, run rk4 for a test function and get results
    def setUp(self):

        # Calculate the rk4 solution and save list of t's, y's and a zipped result with both
        t1, y1 = rk.rk4(self.f1, 0, 1, 0.1, 100)
        self.results1 = zip(t1, y1)

        t2, y2 = rk.rk4(self.f2, 0, 0.5, 0.1, 20)
        self.results2 = zip(t2, y2)

    #####
    # TESTS
    def test_1_rk4_is_within_expected_percent_of_exact(self):
        """Verify that the rk4 method calculates a solution to within a certain percentage of the exact solution"""

        for t,y in self.results1:
            exact_y = self.f1_exact(t)
            diff = y - exact_y
            # print("{:.1f}, {:.5f}, {:.5e}".format(t, y, diff))
            self.assertTrue(fabs(diff) < 1e-3)

    def test_2_rk4_is_within_expected_percent_of_exact(self):
        """Verify that the rk4 method calculates a solution to within a certain percentage of the exact solution"""

        for t,y in self.results2:
            exact_y = self.f2_exact(t)
            diff = y - exact_y
            # print("{:.1f}, {:.5f}, {:.5e}".format(t, y, diff))
            self.assertTrue(fabs(diff) < 1e-3)
