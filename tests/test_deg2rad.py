import unittest
import subprocess
import math


class Test_deg2rad(unittest.TestCase):
    def test_valid_1(self):
        p = subprocess.Popen(["./test", "10"], stdout=subprocess.PIPE)
        output = float(p.stdout.read().decode("utf-8"))
        expected_output = math.radians(10)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_2(self):
        p = subprocess.Popen(["./test", "57.2958"], stdout=subprocess.PIPE)
        output = float(p.stdout.read().decode("utf-8"))
        expected_output = math.radians(57.2958)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_3(self):
        p = subprocess.Popen(["./test", "-45"], stdout=subprocess.PIPE)
        output = float(p.stdout.read().decode("utf-8"))
        expected_output = math.radians(-45)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_4(self):
        p = subprocess.Popen(["./test", "0.0"], stdout=subprocess.PIPE)
        output = float(p.stdout.read().decode("utf-8"))
        expected_output = math.radians(0)
        self.assertAlmostEqual(expected_output, output, 3)

    def test_valid_5(self):
        p = subprocess.Popen(["./test", "10000"], stdout=subprocess.PIPE)
        output = float(p.stdout.read().decode("utf-8"))
        expected_output = math.radians(10000)
        self.assertAlmostEqual(expected_output, output, 3)
