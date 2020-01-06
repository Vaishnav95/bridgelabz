import pytest
from object_oriented_programs.stock_account import Portfolio

share = Portfolio()


def test_type():
    hasattr(share.enter_stock("Samsung", 25, 120), "name, price, number")


@pytest.mark.parametrize('name, price, number',
                         [
                             ('Samsung', 25, 120),
                             ('Apple', 35, 100)
                         ])
def test_enter_stock(name, price, number):
    share.enter_stock(name, price, number)
    assert type(name) == str
    assert type(price) == int and type(number) == int


pytest.main()
