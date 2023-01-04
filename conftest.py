import pytest


@pytest.fixture()
def get_name():
    name = "this is a good new"
    return name
