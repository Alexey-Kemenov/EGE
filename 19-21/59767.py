def game2(heap, moves, to):
    if heap >= 89:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game2(heap + 2, moves + 1, to), game2(heap + 3, moves + 1, to), game2(heap * 3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'21:{min(s for s in range(1, 89) if not game2(s, 0, 3) and game2(s, 0, 4))}')
