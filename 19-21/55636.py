"""
def game(heap1, heap2, moves, to):
    if heap1 + heap2 > 46:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    if heap1 > heap2:
        h = [game(heap1 + 1, heap2, moves + 1, to), game(heap1 + 2, heap2, moves + 1, to),
             game(heap1 + 3, heap2, moves + 1, to),
             game(heap1, heap2 * 2, moves + 1, to)]
    if heap1 < heap2:
        h = [game(heap1, heap2 + 1, moves + 1, to), game(heap1, heap2 + 2, moves + 1, to),
             game(heap1, heap2 + 3, moves + 1, to),
             game(heap1 * 2, heap2, moves + 1, to)]
    if heap1 == heap2:
        h = [game(heap1 + 1, heap2, moves + 1, to), game(heap1 + 2, heap2, moves + 1, to),
             game(heap1 + 3, heap2, moves + 1, to), game(heap1, heap2 + 1, moves + 1, to),
             game(heap1, heap2 + 2, moves + 1, to),
             game(heap1, heap2 + 3, moves + 1, to)]
    return any(h)


b = 44
for s in range(1, 23):
    for a in range(1, 23):
        if game(s, a, 0, 1):
            b = min(a + s, b)
print(b)
"""


def game2(heap1, heap2, moves, to):
    if heap1 + heap2 > 46:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    if heap1 > heap2:
        h = [game2(heap1 + 1, heap2, moves + 1, to), game2(heap1 + 2, heap2, moves + 1, to),
             game2(heap1 + 3, heap2, moves + 1, to),
             game2(heap1, heap2 * 2, moves + 1, to)]
    if heap1 < heap2:
        h = [game2(heap1, heap2 + 1, moves + 1, to), game2(heap1, heap2 + 2, moves + 1, to),
             game2(heap1, heap2 + 3, moves + 1, to),
             game2(heap1 * 2, heap2, moves + 1, to)]
    if heap1 == heap2:
        h = [game2(heap1 + 1, heap2, moves + 1, to), game2(heap1 + 2, heap2, moves + 1, to),
             game2(heap1 + 3, heap2, moves + 1, to), game2(heap1, heap2 + 1, moves + 1, to),
             game2(heap1, heap2 + 2, moves + 1, to),
             game2(heap1, heap2 + 3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


"""
b = 0
for s in range(1, 42):
    if not game2(s, 5, 0, 1) and game2(s, 5, 0, 3):
        b = max(s, b)
print(b)
"""
for s in range(1, 25):
    if not game2(s, 22, 0, 2) and game2(s,22,0,4):
        print(s)
