from emr.db import load_db, del_db, dbfile
from emr.main import _calculate_price, buy_ticket, check_ticket, get_total
import pytest
import emr

def test_del_db():
    del_db()
    emr.data = load_db()
    assert dbfile.exists()


def test_calculate_48():
    price = _calculate_price(48)
    assert price == (48 - 4) * 50
    

def test_calculate_3():
    price = _calculate_price(3)
    assert price == 3 * 50


def test_check_ticket():
    price = check_ticket(1, 30)
    assert price == 27 * 50


def test_check_ticket_error():
    with pytest.raises(ValueError) as e:
        price = check_ticket(1, 80)
    assert e.type == ValueError


def test_main_buy_ticket():
    buy_ticket(1,30)
    emr.data = load_db()
    assert emr.data[1]['ticket'] == 18


def test_get_total():
    ticket, price = get_total()
    print(ticket, price)
    assert ticket == 30 and price == 50 * 27