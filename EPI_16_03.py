# Enumerate all non-attacking Queen placements


def enum_placements(n):
    def place_queen(n, row, col_placement, result):
        if n == row:
            result.append(create_result(col_placement))

        for i in range(n):
            if is_feasible(col_placement, i, row):
                col_placement.append(i)
                place_queen(n, row + 1, col_placement, result)
                col_placement.pop()

    def create_result(col_placement):
        res_string = ""
        for ndx, i in enumerate(col_placement):
            str_row = "." * len(col_placement)
            str_row = str_row[:i] + "Q" + str_row[i + 1:]
            res_string += str_row + "\n"
        return res_string

    def is_feasible(col_placement, i, row):
        for ndx, col in enumerate(col_placement):
            if col == i or abs(float(row - ndx) / (col - i)) == 1:
                return False
        return True

    result, col = [], []
    place_queen(n, 0, col, result)
    return result


if __name__ == '__main__':
    test_cases = [
        1, 2, 3, 4

    ]
    for test_case in test_cases:
        print "testcase%i=========\n" % test_case
        for line in enum_placements(test_case):
            print line
            # print enum_placements(4)







