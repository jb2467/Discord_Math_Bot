from matrix import Matrix
import matrix
def matching_parentheses(string):
    opening = []
    pairs = []
    for o, c in enumerate(string):
        if c == ')':
            if len(opening) == 0:
                return False
            else:
                temp = []
                temp.append(opening.pop())
                temp.append(o)
                pairs.append(tuple(temp))
                return pairs
        elif c == '(':
            opening.append(o)
def calculate(arr:list):
    steps = []
    text = ''
    for element in arr:
        text += element
    steps .append(text +'\n')
    m = matching_parentheses(text)
    while(m):
        num = m[0][0]
        num2 = m[0][1]
        if not text[num-1].isdigit():
            new_str = text[0:num] + str(eval(text[num+1:num2])) + text[num2+1:]
        else:
            new_str = text[0:num] + '* ' + str(eval(text[num + 1:num2])) + text[num2 + 1:]
        text = new_str
        steps.append( text + '\n')
        m = matching_parentheses(text)
    return (steps)
def add_matrices(matrices):
    matrix1 = matrices[0]
    matrix2 = matrices[1]
    new_data = []
    steps = f'Step 0 : \n{matrix1} + \n{matrix2}\n'
    i = 1
    if matrix1.row_count == matrix2.row_count and matrix1.col_count == matrix2.col_count:
        for r in range (matrix1.row_count):
            for c in range(matrix1.col_count):
                steps += f'Step {i} : New matrix at ({r}) ({c}) = {matrix1.data_set[r][c]} + {matrix2.data_set[r][c]} \n'
                i += 1
                new_data.append(matrix1.data_set[r][c] + matrix2.data_set[r][c])
        m = Matrix(matrix1.row_count,matrix1.col_count,new_data)
        return m,steps
    else:
        return False, False
def subtract_matrices(matrices):
    matrix1 = matrices[0]
    matrix2 = matrices[1]
    new_data = []
    steps = f'Step 0 : \n{matrix1} minus \n{matrix2}\n'
    i = 1
    if matrix1.row_count == matrix2.row_count and matrix1.col_count == matrix2.col_count:
        for r in range (matrix1.row_count):
            for c in range(matrix1.col_count):
                steps += f'Step {i} : New matrix at ({r}) ({c}) = {matrix1.data_set[r][c]} - {matrix2.data_set[r][c]} \n'
                i += 1
                new_data.append(matrix1.data_set[r][c] - matrix2.data_set[r][c])
        m = Matrix(matrix1.row_count,matrix1.col_count,new_data)
        return m,steps
    else:
        return False, False
def multiply_matrices(matrices):
    matrix1 = matrices[0]
    matrix2 = matrices[1]
    new_data = []
    steps = f'Step 0 : \n{matrix1} _times_ \n{matrix2}\n'
    i = 1
    x = 0
    y = 0
    if matrix2.row_count == matrix1.col_count:
        for r in range (matrix1.row_count):
            for c in range(matrix2.col_count):
                sum = 0
                steps += f'Step {i} : in the new matrx at ({x},{y}) = '
                for k in range (matrix2.row_count):
                    steps += f'{matrix1.data_set[r][k]} * {matrix2.data_set[k][c]}'
                    if k == matrix2.row_count-1:
                        pass
                    else:
                         steps += ' + '
                    sum += matrix1.data_set[r][k] * matrix2.data_set[k][c]
                new_data.append(sum)
                v = i - 1
                i += 1
                y+=1
                steps += f' = {new_data[v]}\n'
            x+=1
            y=0
        m = Matrix(matrix1.row_count,matrix2.col_count,new_data)
        steps += '\n'
        return m, steps
    else:
        return False, False
def matrix_power_to(matrix, power):
    m1 = matrix
    m2 = matrix
    steps = ''
    # It needs to be one less because the program uses ( power + 1 ) amount of matrix mulitplication 
    count = power -1
    j = 0
    for i in range (count):
        print(i)
        l = []
        print(m1)
        l.append(m1)
        l.append(m2)
        m1,s = multiply_matrices(l)
        j = i +2
        steps += f'Power : {j} \n{s}{m1} '
    return m1,steps
def matrix_transpose(matrix):
    new_data = []
    steps = f'Step 0 :Transpose\n{matrix}\n'
    i = 1
    for c in range(matrix.col_count):
        for r in range(matrix.row_count):
            steps += f'Step {i} : New matrix at ({c}) ({r}) = {matrix.data_set[r][c]}\n'
            i+=1
            new_data.append(matrix.data_set[r][c])
    steps += '\n'
    m = Matrix(matrix.col_count,matrix.row_count,new_data)
    return m,steps
def matrix_determinant(matrix):
    steps = f'Step 0 : Determinant of\n{matrix}\n'
    x = 1
    row = matrix.row_count
    new_matrix = (matrix)
    for fd in range(row): 
        for i in range(fd+1,row): 
            if new_matrix.data_set[fd][fd] == 0:
                new_matrix.data_set[fd][fd] == 0 
            crScaler = new_matrix.data_set[i][fd] / new_matrix.data_set[fd][fd] 
            for j in range(row): 
                steps+= f'Step {x}: {new_matrix.data_set[i][j]} - ({new_matrix.data_set[i][fd]} / {new_matrix.data_set[fd][fd]}) * {new_matrix.data_set[fd][j]}'
                new_matrix.data_set[i][j] = new_matrix.data_set[i][j] - crScaler * new_matrix.data_set[fd][j]
            steps+= f'\n'
            x+=1
    steps += f'Step {x} : '
    product = 1
    for i in range(row):
        steps += f'{product} * {new_matrix.data_set[i][i]}'
        product *= new_matrix.data_set[i][i] 
    steps += f'\nFinal answer: {product}'
    return steps





    