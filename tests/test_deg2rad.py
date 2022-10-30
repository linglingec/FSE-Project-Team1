import unittest
from subprocess import Popen, PIPE
import math


class Test_deg2rad(unittest.TestCase):
    def test_valid_1(self):
        with Popen(["./deg2rad.exe", "10"], stdout=PIPE) as p:
            output = float(p.stdout.read().decode("utf-8"))
            expected_output = math.radians(10)
            self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_2(self):
        with Popen(["./deg2rad.exe", "57.2958"], stdout=PIPE) as p:
            output = float(p.stdout.read().decode("utf-8"))
            expected_output = math.radians(57.2958)
            self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_3(self):
        with Popen(["./deg2rad.exe", "-45"], stdout=PIPE) as p:
            output = float(p.stdout.read().decode("utf-8"))
            expected_output = math.radians(-45)
            self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_4(self):
        with Popen(["./deg2rad.exe", "0"], stdout=PIPE) as p:
            output = float(p.stdout.read().decode("utf-8"))
            expected_output = math.radians(0)
            self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_5(self):
        with Popen(["./deg2rad.exe", "10000"], stdout=PIPE) as p:
            output = float(p.stdout.read().decode("utf-8"))
            expected_output = math.radians(10000)
            self.assertAlmostEqual(expected_output, output, 3)
