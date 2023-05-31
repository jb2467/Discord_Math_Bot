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
    if matrix2.row_count == matrix1.col_count:
        for r in range (matrix1.row_count):
            for c in range(matrix2.col_count):
                sum = 0
                steps += f'Step {i} : '
                for k in range (matrix2.row_count):
                    steps += f'{matrix1.data_set[r][k]} * {matrix2.data_set[k][c]}'
                    if k == matrix2.row_count-1:
                        pass
                    else:
                         steps += ' + '
                    sum += matrix1.data_set[r][k] * matrix2.data_set[k][c]
                i += 1
                steps += '\n'
                new_data.append(sum)
        m = Matrix(matrix1.row_count,matrix2.col_count,new_data)
        steps += '\n'
        return m, steps
    else:
        return False, False

    