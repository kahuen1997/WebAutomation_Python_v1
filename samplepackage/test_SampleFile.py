import pytest

@pytest.mark.smoke
def test_sample_one():
    print("one")

@pytest.mark.UAT
def test_sample_two():
    print("two")

@pytest.mark.regression
def test_sample_three():
    print("three")

@pytest.mark.skip
def test_sample_four():
    print("four")

@pytest.mark.xfail
def test_sample_five():
    print("fail")
    assert False

@pytest.mark.xfail
def test_sample_six():
    print("pass")

@pytest.mark.parametrize("username, password",[("Edmond", "123"), ("Edwin", "456")])
def test_sample_seven(username,password):
    print(username + " " + password)

