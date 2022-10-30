import unittest
from subprocess import Popen, PIPE
import math


def deg2rad_cpp(x: float) -> float:
    with Popen(["../deg2rad.exe", str(x)], stdout=PIPE) as p:
        output = float(p.stdout.read().decode("utf-8"))
    return output


class Test_deg2rad(unittest.TestCase):
    def test_valid_1(self):
        expected_output = math.radians(10)
        output = deg2rad_cpp(10)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_2(self):
        expected_output = math.radians(57.2958)
        output = deg2rad_cpp(57.2958)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_3(self):
        expected_output = math.radians(-45)
        output = deg2rad_cpp(-45)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_4(self):
        expected_output = math.radians(0)
        output = deg2rad_cpp(0)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_5(self):
        expected_output = math.radians(10000)
        output = deg2rad_cpp(10000)
        self.assertAlmostEqual(expected_output, output, 3)
