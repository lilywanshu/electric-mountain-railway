#=================================
# emr = electric mountain railway
# author: Lily
# created: 2022.2.1
#=================================


UNIT_PRICE = 50
PURCHASING_TIME = 4
GROUP_DISCOUNT = 10
DISCOUNT_MAX_ACOUNT = 80

AVAILABLE_INNITIAL = 48
SOLD_INITIAL = 0
PRICE_INITIAL = 50
TICKETS_INITIAL = 1

TRAIN_SEAT = 48

INITIAL_DATA = [
    { 'ticket': TRAIN_SEAT, 'price': 0 },
    { 'ticket': TRAIN_SEAT, 'price': 0 },
    { 'ticket': TRAIN_SEAT, 'price': 0 },
    { 'ticket': TRAIN_SEAT, 'price': 0 }
]

SCHEDULE = {
    'up': ['09: 00', '11: 00', '13: 00', '15: 00'],
    'down': ['10: 00', '12: 00', '13: 00', '16: 00']
}

data = None
