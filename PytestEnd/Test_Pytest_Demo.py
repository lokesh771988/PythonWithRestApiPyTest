import pytest


@pytest.mark.usefixtures("testData")
class Test_Demo:

    def test_demo(self, testData):
        print("Hellow")
        print(testData)
