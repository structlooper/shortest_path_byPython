
def minimum_path(matrix,m,n):
    mini_path = [[0 for x in range(n+1)] for y in range(m+1)]
     
    #  intialing path of 8X8 matrix (0,0).............
    mini_path[0][0] = matrix[0][0]
  
    # vertical path value X...........................
    for i in range(1,n+1):
        ver_path = mini_path[i-1][0]
        mini_path[i][0]=ver_path + matrix[i][0]
    
    # Horizontal path value Y.........................
    for j in range(1,m+1):
        hor_path = mini_path[0][j-1]
        mini_path[0][j] = hor_path + matrix[0][j]
    
    # Daigonal path value Z............................
    for i in range(1,n+1):
        for j in range(1,m+1):
            ver_path = mini_path[i-1][j]
            hor_path = mini_path[i][j-1]
            cross_path = mini_path[i-1][j-1]
            
            # final Path.............................
            mini_path[i][j] = matrix[i][j] + min(ver_path,hor_path,cross_path)
        return mini_path[m][n]

boad = [[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],[2,3,4,4,6,7,8,1],]

short_path = minimum_path(boad,8,8)
print(f"Shortest path : {short_path}")