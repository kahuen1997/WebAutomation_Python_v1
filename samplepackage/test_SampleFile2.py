import pytest

@pytest.mark.smoke
def test_sample_file_two():
    print("Inside sample file two")

def test_module(setup):
    print("Hello I am in file 2")