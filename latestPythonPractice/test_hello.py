import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.mark.smoke
def test_assert():
    result = 1 + 2
    assert result == 3


@pytest.mark.regression
def test_true():
    assert True


@pytest.mark.slow
def test_true1():
    assert True


@pytest.mark.regression
def test_regression():
    assert True
