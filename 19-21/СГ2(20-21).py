def game2(heap, moves, to):
    if heap >= 95:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game2(heap + 1, moves + 1, to)]
    if heap % 2 == 0:
        h.append(game2(heap + (heap // 2), moves + 1, to))
    if heap % 3==0:
        h.append(game2(heap + (heap // 3), moves + 1, to))
    if heap %3!=0 and heap %2!=0:
        h.append(game2(heap * 2, moves + 1, to))
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'20:{[s for s in range(1, 95) if not game2(s, 0, 1) and game2(s, 0, 3)]}')
print(f'21:{max(s for s in range(1, 95) if not game2(s, 0, 2) and game2(s, 0, 4))}')