# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def sd(row):

def dominant_diagonal():
    for i in range(size):
        for j in range(i,size-1):
            if(matrix[i][i] < matrix[i][j] + matrix[i][j+1]):
                #for k in range(j, size-2):




            if matrix[i][i] < matrix[i][j]+matrix[i][j+1]:
                sd(i+1)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vector = [[2], [6], [5]]
    size = 3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
