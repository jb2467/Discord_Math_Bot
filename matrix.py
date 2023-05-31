class Matrix():
    row_count : int
    col_count : int
    data_set : list
    def __init__(self,row,col,data):
        self.row_count = row
        self.col_count = col
        self.data_set = self.createMatrix(data)
        
    def createMatrix(self,dataList):
        mat = []
        index = 0
        for i in range(self.row_count):
            rowList = []
            for j in range(self.col_count):
                rowList.append(int(dataList[index]))
                index += 1
            mat.append(rowList)
        return mat
    def __str__(self) -> str:
        string = ''
        for r in range (self.row_count):
            for c in range(self.col_count):
                string += f'{self.data_set[r][c]} '
            string += '\n'
        return f'{string}'
    
'''
This is a helper function for all of the addition,substraction and mulitplication operations
This will belong to the file not the class.
'''
def make_matrices(arr):
    temp = ''
    for element in arr:
        temp += str(element) + ' '
    count = temp.count(',') + 1
    l = []
    for i in range (count):
        spl = temp.split(' , ')
        m = spl[i]
        i = m.find('x')
        j = m.find(' ')
        row = int(m[:i])
        col = int(m[i+1:j])
        data_set = m[j+1:].split(' ')
        matrix = Matrix(row,col,data_set)
        l.append(matrix)
    return l,count
    
