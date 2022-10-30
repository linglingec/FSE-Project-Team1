import unittest
from subprocess import Popen, PIPE
import math


def executor(x: str) -> (float, float):
    with Popen(["./deg2rad.exe", x], stdout=PIPE) as p:
        output = float(p.stdout.read().decode("utf-8"))
        expected_output = math.radians(float(x))
    return expected_output, output


class Test_deg2rad(unittest.TestCase):
    def test_valid_1(self):
        expected_output, output = executor("10")
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_2(self):
        expected_output, output = executor("57.2958")
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_3(self):
        expected_output, output = executor("-45")
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_4(self):
        expected_output, output = executor("0")
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_5(self):
        expected_output, output = executor("10000")
        self.assertAlmostEqual(expected_output, output, 3)
