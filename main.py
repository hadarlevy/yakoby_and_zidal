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
        return True
    return False


def yaakoby(mat1, vec):
    e = 0.00001
    for row in range(size):
        for col in range(size):
            if row == col:
                continue
            mat1[row][col] = -1 * mat1[row][col] / mat1[row][row]
        vec[row] = vec[row] / mat1[row][row]
    the_previous = []
    for m in range(size):
        the_previous.append(0)
    print(f'{0}: {the_previous}')
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

        for t in range(size):
            the_previous.append(helper[t])
        print(f'{index}: {helper}')
        index += 1
    print(f'------------------Results--------------------')
    for i in range(size):
        print(f'x{i+1}: {helper[i]}')
    return

def zidel(mat1, vec):
    e = 0.00001
    for row in range(size):
        for col in range(size):
            if row == col:
                continue
            mat1[row][col] = -1 * mat1[row][col] / mat1[row][row]
        vec[row] = vec[row] / mat1[row][row]
    the_previous = []
    for m in range(size):
        the_previous.append(0)
    print("0:", the_previous)
    for row in range(size):
        sum = 0
        for col in range(size):
            if row == col:
                continue
            sum += mat1[row][col] * helper[col]
        sum += vec[row]
        helper[row] = sum
    index = 0

    while abs(helper[size-1] - the_previous[index * size - 1]) > e:
        print(f'{index+1}: {helper}')
        for row in range(size):
            sum = 0
            for col in range(size):
                if row == col:
                    continue
                sum += mat1[row][col] * helper[col]
            sum += vec[row]
            helper[row] = sum
        index += 1
        for t in range(size):
            the_previous.append(helper[t])
    print(f'{index+1}: {helper}')
    print(f'------------------Results--------------------')
    for i in range(size):
        print(f'x{i+1}: {helper[i]}')
    return
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [2, 6, 5]
    size = 3
    t_mat = tuple(matrixA[0])
    t_vec = vectorB[0]
    mat_dict = {}
    vec_dict = {}
    helper = []
    sum1 = 0.0
    for i in range(size):
        mat_dict[i], vec_dict[i] = 0, 0
        helper.append(0)
    x = int(input("Press your choice: 1- for Yaakoby method 2- for Zidel method\n"))
    check = arrange_matrix()
    if x == 1:
        yaakoby(matrixA, vectorB)
    if x == 2:
        zidel(matrixA, vectorB)
    if check == False:
        for i in range(size):
            sum1 += round(t_mat[i] * helper[i])
        if sum1 != t_vec:
            print("This matrix does not converge")
        else:
            print("Although there is no dominant diagonal, This matrix converges")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/