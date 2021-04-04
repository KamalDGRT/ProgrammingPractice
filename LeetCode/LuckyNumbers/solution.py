# Lucky numbers Problem

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        col_max = []
        result = []

        for row in matrix:            
            smallest = row[0]
            row_size = len(row)
            for index in range(1, row_size):
                if row[index] < smallest:
                    smallest = row[index]
            row_min.append(smallest)
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(0, n):
            col = []
            for j in range(0, m):
                col.append(matrix[j][i])
            largest = col[0]
            col_size = len(col)
            for index in range(1, col_size):
                if col[index] > largest:
                    largest = col[index]
            col_max.append(largest)
        
        for element in row_min:
            if element in col_max:
                result.append(element)
        
        return result
