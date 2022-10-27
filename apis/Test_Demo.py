import unittest

import pytest


class test_sample(unittest.TestCase):

    @pytest.mark.smoke
    def test_sqrt(self):
        print("Sample Test")

    @pytest.mark.regression
    def test_a(self):
        print("Sample Test a")

    @pytest.mark.skip
    def test_a1(self):
        print("Sample Test a1")

    def setUp(self) -> None:
        print("class level Setup")

    def tearDown(self) -> None:
        print("class level teardown")

    @classmethod
    def setUpClass(cls) -> None:
        print("Suite level Setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Suite level TeamDown")