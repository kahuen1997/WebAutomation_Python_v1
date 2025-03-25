import pytest

@pytest.fixture(autouse=True, scope="module")
def setup():
    print("Launch Browser")
    print("Open Application")
    yield #the running code
    print("Logout from application")
    print("close browser")
def test_login_with_Valid_Credential(setup):
    print("Testing 1")

def test_login_with_Valid_Email_and_invalid_password(setup):
    print("Testing 2")


