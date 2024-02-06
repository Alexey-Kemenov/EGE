def game(heap, moves, to):
    if heap >= 95:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap + 1, moves + 1, to)]
    if heap % 2 == 0:
        h.append(game(heap + (heap // 2), moves + 1, to))
    if heap % 3==0:
        h.append(game(heap + (heap // 3), moves + 1, to))
    if heap %3!=0 and heap %2!=0:
        h.append(game(heap * 2, moves + 1, to))
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'19:{min(s for s in range(1, 95) if not game(s, 0, 1) and game(s, 0, 2))}')
