import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("千里之外")
    yield
    print("周杰倫")