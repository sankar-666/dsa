class RiverGraph:    
    def check_river_size(self, matrix):
        num_of_rows = len(matrix)
        num_of_col = len(matrix[0]) if matrix else 0
        visited = [[False for _ in range(num_of_col)] for _ in range(num_of_rows)]
        res = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if visited[i][j]:
                    continue
                else:
                    self.trverse_through_river(i, j, matrix, visited, res)
        return res
    
    def trverse_through_river(self, i, j, matrix, visited, res):
        current_river_size = 0
        stack = [(i, j)]

        while stack:
            i, j = stack.pop()
            if visited[i][j]:
                continue
            visited[i][j] = True

            if matrix[i][j] == 0:
                continue
            current_river_size+=1
            nearest = self.get_naerest_nodes(i, j, matrix, visited)
            stack.extend(nearest)
        if current_river_size > 0:
            res.append(current_river_size)
            
    def get_naerest_nodes(self, i, j, matrix, visited):
        nearest = []
        if i > 0 and not visited[i-1][j]:
            nearest.append((i-1, j))
        if i < len(matrix) - 1 and not visited[i+1][j]:
            nearest.append((i+1, j)) 
        if j > 0 and not visited[i][j-1]:
            nearest.append((i, j-1))
        if j < len(matrix[0]) - 1 and not visited[i][j+1]:
            nearest.append((i, j+1)) 
        return nearest

r = RiverGraph()
matrix = [[1, 0, 0, 1, 1], 
          [0, 1, 1, 1, 0], 
          [0, 0, 0, 0, 1], 
          [1, 0, 0, 0, 1]]

result = r.check_river_size(matrix)
print(result)



# optimised solution 

class RiverGraph:
    def check_river_size(self, matrix):
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        river_sizes = []
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    size = self.traverse_through_river(matrix, i, j)
                    river_sizes.append(size)
        
        return river_sizes
    
    def traverse_through_river(self, matrix, i, j):
        stack = [(i, j)]
        size = 0
        
        while stack:
            row, col = stack.pop()
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 1:
                size += 1
                matrix[row][col] = 0  # Mark cell as visited
                stack.extend([(row+1, col), (row-1, col), (row, col+1), (row, col-1)])
        
        return size

# Example usage:
r = RiverGraph()
matrix = [[1, 0, 0, 1, 1], 
          [0, 1, 1, 1, 0], 
          [0, 0, 0, 0, 1], 
          [1, 0, 0, 0, 1]]

result = r.check_river_size(matrix)
print(result) 