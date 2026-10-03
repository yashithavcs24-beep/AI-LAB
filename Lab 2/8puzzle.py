def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def dfs(state, goal, visited, path):

    if state == goal:
        print("Goal Found!")
        print("Number of moves:", len(path) - 1)

        for state in path:
            print_board(state)

        return True

    visited.add(state)

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            new_blank = nr * 3 + nc

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            new_state = tuple(new_state)

            if new_state not in visited:

                if dfs(new_state, goal, visited, path + [new_state]):
                    return True

    return False


initial = (1, 2, 3,
           0, 4, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

visited = set()

dfs(initial, goal, visited, [initial])
