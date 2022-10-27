import pytest


@pytest.fixture()
def setup():
    print("Class level Setup")
    yield
    print("After method execution")


@pytest.fixture()
def testData():
    return ["Lokesh", "Gorantla", "lokesh.ust@gmail.com"]
