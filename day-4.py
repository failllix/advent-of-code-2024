f = open("./day-4.txt", "r")
x = f.read()

lines = x.split("\n")[:-1]
grid = [[char for char in line] for line in lines]

len_x = len(lines[0])
len_y = len(lines)

print(f"dimensions: {len_x} x {len_y}")


def search_up(x, y):
    if y < 3:
        return False

    if grid[y - 1][x] == "M" and grid[y - 2][x] == "A" and grid[y - 3][x] == "S":
        return True

    return False


def search_down(x, y):
    if y > len_y - 4:
        return False

    if grid[y + 1][x] == "M" and grid[y + 2][x] == "A" and grid[y + 3][x] == "S":
        return True

    return False


def search_right(x, y):
    if x > len_x - 4:
        return False

    if grid[y][x + 1] == "M" and grid[y][x + 2] == "A" and grid[y][x + 3] == "S":
        return True

    return False


def search_left(x, y):
    if x < 3:
        return False

    if grid[y][x - 1] == "M" and grid[y][x - 2] == "A" and grid[y][x - 3] == "S":
        return True

    return False


def search_top_left(x, y):
    if x < 3 or y < 3:
        return False

    if (
        grid[y - 1][x - 1] == "M"
        and grid[y - 2][x - 2] == "A"
        and grid[y - 3][x - 3] == "S"
    ):
        return True

    return False


def search_top_right(x, y):
    if x > len_x - 4 or y < 3:
        return False

    if (
        grid[y - 1][x + 1] == "M"
        and grid[y - 2][x + 2] == "A"
        and grid[y - 3][x + 3] == "S"
    ):
        return True

    return False


def search_down_left(x, y):
    if x < 3 or y > len_y - 4:
        return False

    if (
        grid[y + 1][x - 1] == "M"
        and grid[y + 2][x - 2] == "A"
        and grid[y + 3][x - 3] == "S"
    ):
        return True

    return False


def search_down_right(x, y):
    if x > len_x - 4 or y > len_y - 4:
        return False

    if (
        grid[y + 1][x + 1] == "M"
        and grid[y + 2][x + 2] == "A"
        and grid[y + 3][x + 3] == "S"
    ):
        return True

    return False


result = 0

for y in range(len_y):
    for x in range(len_x):
        if grid[y][x] == "X":
            result = result + sum(
                [
                    search_up(x, y),
                    search_down(x, y),
                    search_left(x, y),
                    search_right(x, y),
                    search_top_right(x, y),
                    search_top_left(x, y),
                    search_down_right(x, y),
                    search_down_left(x, y),
                ]
            )

print(result)


# --- 2nd star solution


def check_cross_mas(x, y):

    if x < 1 or x > len_x - 2 or y < 1 or y > len_y - 2:
        return False

    # S.S
    # .A.
    # M.M
    if (
        grid[y - 1][x - 1] == "S"
        and grid[y - 1][x + 1] == "S"
        and grid[y + 1][x - 1] == "M"
        and grid[y + 1][x + 1] == "M"
    ):
        return True

    # S.M
    # .A.
    # S.M
    if (
        grid[y - 1][x - 1] == "S"
        and grid[y - 1][x + 1] == "M"
        and grid[y + 1][x - 1] == "S"
        and grid[y + 1][x + 1] == "M"
    ):
        return True

    # M.S
    # .A.
    # M.S
    if (
        grid[y - 1][x - 1] == "M"
        and grid[y - 1][x + 1] == "S"
        and grid[y + 1][x - 1] == "M"
        and grid[y + 1][x + 1] == "S"
    ):
        return True

    # M.M
    # .A.
    # S.S
    if (
        grid[y - 1][x - 1] == "M"
        and grid[y - 1][x + 1] == "M"
        and grid[y + 1][x - 1] == "S"
        and grid[y + 1][x + 1] == "S"
    ):
        return True

    return False


result = 0

for y in range(len_y):
    for x in range(len_x):
        if grid[y][x] == "A":
            result = result + check_cross_mas(x, y)

print(result)
