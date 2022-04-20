# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def check_row(row, vector):
    for r in range(size):
        sum = 0
        for r1 in range(size):
            if r == r1:
                continue
            else:
                sum += row[r1]
        if sum < row[r]:
            mat_dict[r] = row
            vec_dict[r] = vector
            return

def dominant_diagonal():
    for n in range(size):
        check_row(matrixA[n], vectorB[n])
    for n in range(size):
        if mat_dict[n] == 0:
            print("There is not a dominant diagonal in this matrix")
            return False
    return True

def arrange_matrix():
    if dominant_diagonal() == True:
        matrixA_help = []
        vectorB_help = []
        for r in range(size):
            matrixA_help.append(mat_dict[r])
            vectorB_help.append(vec_dict[r])
        matrixA = matrixA_help
        vectorB = vectorB_help
    return


def yaakoby(mat1, vec):
    e = 0.001
    for row in range(size):
        for col in range(size):
            if row == col:
                continue
            mat1[row][col] = -1 * mat1[row][col] / mat1[row][row]
        vec[row] = vec[row] / mat1[row][row]
    the_previous = []
    for m in range(size):
        the_previous.append(0)
    print(the_previous)
    for row in range(size):
        sum = 0
        for col in range(size):
            if row == col:
                continue
            sum += mat1[row][col] * the_previous[col]
        sum += vec[row]
        the_previous.append(helper[row])
        helper[row] = sum
    index = 1
    while abs(helper[size-1] - the_previous[index * size - 1]) > e:
        for row in range(size):
            sum = 0
            for col in range(size):
                if row == col:
                    continue
                sum += mat1[row][col] * the_previous[(index * size) + col]
            sum += vec[row]
            helper[row] = sum
        index += 1
        for t in range(size):
            the_previous.append(helper[t])
        print(helper)
    return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrixA = [[2, 4, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [2, 6, 5]
    size = 3
    mat_dict = {}
    vec_dict = {}
    helper = []
    for i in range(size):
        mat_dict[i], vec_dict[i],  = 0, 0
        helper.append(0)
    arrange_matrix()
    yaakoby(matrixA, vectorB)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
