#!/usr/bin/python3
""" Prime Game """


def check_prime(num):
    """ check if a number is a prime number """
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num/2)):
            if num % i == 0:
                return False
            else:
                continue
    return True


def modify_set(num, num_set):
    """ modify the set, remove num and multiples """
    new_set = []
    for x in num_set:
        if x % num == 0:
            continue
        else:
            new_set.append(x)

    return new_set


def playgame(num_set):
    """ simulate the game play """
    turns = 0

    for num in num_set:
        print(num, num_set, 'player', turns % 2)
        if check_prime(num):
            num_set = modify_set(num, num_set)
            # increment player
            turns += 1
        else:
            continue
    # if turns is an even number, then Maria is current player
    # meaning she has nothing to play, so Ben wins, and vice versa
    current = turns % 2
    # so, if current is 1, Maria (player_0) has won, and vice versa
    return 0 if current else 1


def isWinner(x, nums):
    """ entry point of the program """
    maria = 0
    ben = 0

    if (x < 1):
        return None

    for i in range(x):
        winner = playgame([j for j in range(1, nums[i]+1)])
        # 0 is returned if Maria wins
        if winner:
            ben += 1
        else:
            maria += 1
    # print('Scoreline: Maria', maria, '-', ben, 'Ben')
    return 'Maria' if maria > ben else 'Ben'
