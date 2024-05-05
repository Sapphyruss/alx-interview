#!/usr/bin/python3
""" given a pile of coins, determine the fewest number of coins
    needed to meet a given amount total
"""


def makeChange(coins, total):
    """ function to determine change """
    if total <= 0:
        return 0
    """ sort coins so the coins can be taken in order """
    coins.sort()
    coins.reverse()
    count = 0

    """ check each coin+ """
    for coin in coins:
        div = int(total / coin)
        count += div
        total = (total - (div * coin))
        if total == 0:
            break
    # if all available coin options are considered,
    # and change isn't complete, then it can't be done
    if total > 0:
        return -1
    return count
