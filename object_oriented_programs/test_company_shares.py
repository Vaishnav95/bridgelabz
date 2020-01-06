import re
import pytest
from object_oriented_programs.company_shares import StockAccount
from object_oriented_programs.company_shares import time_transaction

company = StockAccount()


@pytest.mark.parametrize("name, number",
                         [
                             ("Oppo", 225),
                             ("Blackberry", 190)
                         ])
def test_add_shares(name, number):
    company.add_shares(name, number)
    assert type(name) == str
    assert type(number) == int


def test_time():
    pattern = re.compile(r"[0-2]\d:[0-6]\d:[0-6]\d")
    assert pattern.match(time_transaction())


def test_methods():
    company.buy("Oppo", 120)
    company.sell("Oppo", 60)
    company.print_report()


pytest.main()
