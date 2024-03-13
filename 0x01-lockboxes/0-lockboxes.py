#!/usr/bin/python3
""" lockboxes """


def join(B, K):
    """ helper """
    result = []
    for k in K:
        result += B[k]
    return result


def canUnlockAll(boxes):
    """ check each box """
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    return len(total) == len(boxes)
