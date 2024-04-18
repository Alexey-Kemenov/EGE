"""
def game(heap1, heap2, moves, to):
    if heap1 + heap2 >= 123:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap1 + 1, heap2, moves + 1, to), game(heap1 * 2, heap2, moves + 1, to),
         game(heap1, heap2 + 1, moves + 1, to), game(heap1, heap2 * 2, moves + 1, to)]
    return any(h)


heap1 = 13
for heap2 in range(1, 110):
    if not game(heap1, heap2, 0, 1) and game(heap1, heap2, 0, 2):
        print(heap2)

"""


def game2(heap1, heap2, moves, to):
    if heap1 + heap2 >= 123:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game2(heap1 + 1, heap2, moves + 1, to), game2(heap1 * 2, heap2, moves + 1, to),
         game2(heap1, heap2 + 1, moves + 1, to), game2(heap1, heap2 * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


"""
heap1 = 13
for heap2 in range(0, 110):
    if not game2(heap1, heap2, 0, 1) and game2(heap1, heap2, 0, 3):
        print(heap2)
"""
heap1 = 13
for heap2 in range(0, 110):
    if (game2(heap1, heap2, 0, 2) or game2(heap1, heap2, 0, 4)) and not game2(heap1, heap2, 0, 2):
        print(heap2)
