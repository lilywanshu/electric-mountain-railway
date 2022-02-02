#=================================
# the main code for emr
# author: Lily
# created: 2022.2.2
#=================================

from emr.db import load_db, update_db
import emr
from emr import AVAILABLE_INNITIAL, INITIAL_DATA, GROUP_DISCOUNT, DISCOUNT_MAX_ACOUNT, PURCHASING_TIME, UNIT_PRICE, GROUP_DISCOUNT

emr.data = load_db()

def _calculate_price(ticket):
    if ticket >= GROUP_DISCOUNT:
        max_discount_time = DISCOUNT_MAX_ACOUNT // GROUP_DISCOUNT
        discount_time = min(ticket // GROUP_DISCOUNT, max_discount_time)
        return (ticket - discount_time) * UNIT_PRICE
    return ticket * UNIT_PRICE

def check_ticket(index, ticket):
    train = emr.data[index]
    available = train['ticket']
    if ticket > available:
        raise ValueError(f'You must purchase tickets within the range of {available}!')
    return _calculate_price(ticket)

def buy_ticket(index, ticket):
    price = check_ticket(index, ticket)
    train = emr.data[index]
    train['ticket'] -= ticket
    train['price'] += price
    update_db(emr.data)

def get_total():
    price = 0
    available = 0
    for train in emr.data:
        price += train['price']
        available += train['ticket']
    return AVAILABLE_INNITIAL * PURCHASING_TIME - available, price