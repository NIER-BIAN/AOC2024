#=========================================================
# Pt1
        
matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append([char for char in line.strip()])

# [[1, 2, 3],      [[3, 6, 9],
#  [4, 5, 6],  to   [2, 5, 8], 
#  [7, 8, 9]]       [1, 4, 7]]
def rotate_matrix(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])

    # initialise empty matrix of same dimensions
    new_matrix = [[" " for _ in range(rows)] for _ in range(cols)]

    # rotate 90 deg anti-clockwise
    for i in range(rows):
        for j in range(cols):
            new_matrix[cols - 1 - j][i] = matrix[i][j]
            
    return new_matrix


rows = len(matrix)
cols = len(matrix[0])
        
# Find the starting position of '^'
start_row, start_col = -1, -1
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '^':
            start_row, start_col = r, c
            break

# Main loop
while True:
    
    # Check for edge condition
    if start_row == 0 or start_col == 0 or start_row == rows or start_col == cols:
        break

    # If obstacle, rotate.
    if matrix[start_row-1][start_col] == '#':

        # Rotate the matrix 90 degrees anti-clockwise
        matrix = rotate_matrix(matrix)
        
        # Update dimensions after rotation
        rows, cols = cols, rows
        
        # Re-find the '^' position after rotation
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '^':
                    start_row, start_col = r, c
                    break
                
    # If no obstacle, keep moving.
    else:
        
        # Place next '^'
        matrix[start_row-1][start_col] = "^"
        
        # Replace prev '^' position with 'X'
        matrix[start_row][start_col] = "X"
        
        # Update current position of '^'
        start_row -= 1

ans = [item for sublist in matrix for item in sublist].count("X")+1 # include final pos

# show final matrix with newline after each row
# for row in rotate_matrix(rotate_matrix(matrix)):
#    print(row)
#    print() # newline

#=========================================================
# Pt2

matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append([char for char in line.strip()])

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = temp

rows = len(matrix)
cols = len(matrix[0])
        
# Find the starting position of '^'
start_row, start_col = -1, -1
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '^':
            start_row, start_col = r, c
            break

temp_steps = 0
ans = 0
# Main loop
while True:
    
    # Check for edge condition
    if start_row == 0 or start_col == 0 or start_row == rows or start_col == cols:
        break

    #------------- SIMULATION
    
    sim_matrix = [row[:] for row in matrix] # deep copy
    sim_rows = len(sim_matrix)
    sim_cols = len(sim_matrix[0])

    # initialise conditions
    sim_matrix[start_row-1][start_col] = '0' # add new blocker
    rotate_matrix(sim_matrix) # introduce point we'd like to get back to
                
    for r in range(sim_rows):
        for c in range(sim_cols):
            if sim_matrix[r][c] == '^':
                circle_start_row, circle_start_col = r, c # this will stay the same
                sim_start_row, sim_start_col = r, c # this will change with iters
                break

    corners_hit_in_loop = 0

    # Inner loop
    while True:
        
        # Check for edge condition
        if sim_start_row == 0 or sim_start_col == 0 or sim_start_row == sim_rows or sim_start_col == sim_cols:
            break
        
        # Check if looped
        if sim_start_row == circle_start_row and sim_start_col == circle_start_col and corners_hit_in_loop%4 == 0 and corners_hit_in_loop > 0:
            # print(f"found at step {temp_steps}!")
            ans += 1
            break
    
        # If obstacle, rotate.
        if sim_matrix[sim_start_row-1][sim_start_col] == '#' or sim_matrix[sim_start_row-1][sim_start_col] == '0':

            corners_hit_in_loop += 1
        
            # Rotate the matrix 90 degrees anti-clockwise
            rotate_matrix(sim_matrix)
        
            # Update dimensions after rotation
            sim_rows, sim_cols = sim_cols, sim_rows
        
            # Re-find the '^' position after rotation
            for r in range(sim_rows):
                for c in range(sim_cols):
                    if sim_matrix[r][c] == '^':
                        sim_start_row, sim_start_col = r, c
                        break
            
        # If no obstacle, keep moving.
        else:
            # Place next '^'
            sim_matrix[sim_start_row-1][sim_start_col] = "^"
        
            # Replace prev '^' position with 'X'
            sim_matrix[sim_start_row][sim_start_col] = "X"
        
            # Update current position of '^'
            sim_start_row -= 1
    
    #------------- SIMULATION
    
    # If obstacle, rotate.
    if matrix[start_row-1][start_col] == '#':

        # Rotate the matrix 90 degrees anti-clockwise
        rotate_matrix(matrix)
        
        # Update dimensions after rotation
        rows, cols = cols, rows
        
        # Re-find the '^' position after rotation
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '^':
                    start_row, start_col = r, c
                    break
                
    # If no obstacle, keep moving.
    else:
        
        # Place next '^'
        matrix[start_row-1][start_col] = "^"
        
        # Replace prev '^' position with 'X'
        matrix[start_row][start_col] = "X"

        temp_steps += 1
        
        # Update current position of '^'
        start_row -= 1

print(ans)
