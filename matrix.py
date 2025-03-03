import numpy as np
def input_matrix():
    print('Матрица 2x2 (комплексные числа обозначаются например: 2+3j или 0+7j): \n')
    while True:
        first_line = input('Введите 1 строку (3 числа через пробел): ').split(" ")
        second_line = input('Введите 2 строку (3 числа через пробел): ').split(" ")
        print(len(first_line),len(second_line))
        if len(first_line)==3 and len(second_line)==3:
            for i in range(len(first_line)):
                if 'j' in first_line[i]:
                    real = int(first_line[i].split("+")[0])
                    imag =int(first_line[i].split("+")[1][:-1])
                    first_line[i] = complex(real,imag)
                else:
                    first_line[i] = int(first_line[i])
            for i in range(len(second_line)):
                if 'j' in second_line[i]:
                    real = int(second_line[i].split("+")[0])
                    imag =int(second_line[i].split("+")[1][:-1])
                    second_line[i] = complex(real,imag)
                else:
                    second_line[i] = int(second_line[i])
            return [first_line, second_line]
        else:
            print('неправильный ввод, введите ещё раз \n')



def determinant(matrix):
    res = np.linalg.det(matrix)
    return res
def solve_matrix(matrix):
    array1 = [[matrix[0][2],matrix[0][1]],[matrix[1][2],matrix[1][1]]]
    array2 = [[matrix[0][0],matrix[0][2]],[matrix[1][0],matrix[1][2]]]
    return [np.linalg.det(array1),np.linalg.det(array2)]








if __name__ == '__main__':
    matrix = input_matrix()
    print(matrix)
    det = determinant([matrix[0][:-1],matrix[1][:-1]])
    if det == 0:
        print('нет решений')
        exit()
    delta_det = solve_matrix(matrix)
    print(f'x1 = {delta_det[0]/det}  x2 = {det/delta_det[1]/det})')