


import random


#price=[1000, 1, 1, 10] = [price_value, price_direction, price_move_range_min_%, price_move_range_max_%]


#20% chance for price to change direction
def price_change(price):
    if random.randint(1,5) >= 5:
        price[1] *= -1

    # the square of random.randint() is taken to reduce the likelihood of very high percentage moves
    price[0] += price[0]*price[1]*(random.randint(price[2], price[3])**2)/1000

    return price



