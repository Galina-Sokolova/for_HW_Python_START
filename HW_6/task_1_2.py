from random import sample

BOARD_SIZE = 8


def get_random_pos():
    pos = sample([(x, y) for x in range(1, BOARD_SIZE + 1) for y in range(1, BOARD_SIZE + 1)], BOARD_SIZE)
    return pos


def check_queens_disposition(pos):
    correct = True
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if pos[i][0] == pos[j][0] or pos[i][1] == pos[j][1] \
                    or abs(pos[i][1] - pos[j][1]) == abs(pos[i][0] - pos[j][0]):
                correct = False
                break
        if not correct:
            break
    if correct:
        return True
    else:
        return False


def generate_disposition(row, number_queens, cur_pos):
    for col in range(number_queens):
        if not needed_coord(row, col, cur_pos):
            continue
        else:
            cur_pos[row] = col
            if row == (number_queens - 1):
                options.append(list(zip(range(len(cur_pos)), cur_pos.copy())))
            else:
                generate_disposition(row + 1, number_queens, cur_pos)
    return options


def needed_coord(row, col, cur_pos):
    if row == 0:
        return True
    for r in range(row):
        if col == cur_pos[r] or abs(row - r) == abs(col - cur_pos[r]):
            return False
    return True


options = []

# if __name__ == '__main__':
#     tmp = get_random_pos()
#     print(check_queens_disposition(tmp))
