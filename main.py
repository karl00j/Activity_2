import queue


def print_maze(passed_map, path):
    start = 0
    for x, pos in enumerate(passed_map[0]):
        if pos == "X":
            start = x

    i = start
    k = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            k -= 1

        elif move == "D":
            k += 1
        pos.add((k, i))

    for k, row in enumerate(passed_map):
        for i, col in enumerate(row):
            if (k, i) in pos:
                if passed_map[k][i] == "0":
                        print("0  ", end="")
                else:
                        print(".  ", end="")
            else:
                print(col + "  ", end="")
        print()
    print("Route from X to 0: ", path)


def validate(passed_map, moves):
    start = 0
    for x, pos in enumerate(passed_map[0]):
        if pos == "X":
            start = x

    i = start
    k = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            k -= 1

        elif move == "D":
            k += 1

        if not (0 <= i < len(passed_map[0]) and 0 <= k < len(passed_map)):
            return False
        elif passed_map[k][i] == "#":
            return False

    return True


def find_end(passed_map, moves):
    start = 0
    for x, pos in enumerate(passed_map[0]):
        if pos == "X":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if passed_map[j][i] == "0":
        print_maze(passed_map, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""

maze = [["#", "#", "#", "#", "#", "X", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", "#", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#"],
        ["#", " ", " ", "#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#", " ", "#", "#", "#"],
        ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", " ", "#", " ", "#", "#", " ", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "0", "#", "#"]]

while not find_end(maze, add):
    add = nums.get()

    for j in ["L", "R", "U", "D"]:
        put = add + j
        if validate(maze, put):
            nums.put(put)