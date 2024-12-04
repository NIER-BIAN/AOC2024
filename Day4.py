#=========================================================
# Pt1

matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(line.strip())

def find_xmas(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    xmas_occurrences = []

    # Helper function to check for "XMAS" in a given direction
    def check_xmas(row, col, dr, dc):
        for i in range(4):
            r = row + i * dr
            c = col + i * dc
            # reject case if search is going out of bounds
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            # reject case as soon as pattern breaks
            if matrix[r][c] != "XMAS"[i]:
                return False
        return True

    # Check all directions for each cell
    for row in range(rows):
        for col in range(cols):

            # Check horizontal (forward and backward)
            if check_xmas(row, col, 0, 1) or check_xmas(row, col + 3, 0, -1):
                xmas_occurrences.append((row, col))

            # Check vertical (forward and backward)
            if check_xmas(row, col, 1, 0) or check_xmas(row + 3, col, -1, 0):
                xmas_occurrences.append((row, col))

            # Check diagonals (SE direction and NW direction)
            if check_xmas(row, col, 1, 1) or check_xmas(row + 3, col + 3, -1, -1):
                xmas_occurrences.append((row, col))

            # Check diagonals (SW direction and NE direction)
            if check_xmas(row, col + 3, 1, -1) or check_xmas(row + 3, col, -1, 1):
                xmas_occurrences.append((row, col))

    return xmas_occurrences

occurrences = find_xmas(matrix)
print(len(occurrences))

#=========================================================
# Pt2

matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(line.strip())

def find_mas_patterns(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    results = []

    # do not look for central As on the edge of matrix
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            
            if matrix[r][c] == 'A':

                # Check horizontal and vertical --- apparently these are not X's
                
                #Check diagonals (top-left to bottom-right i.e. SE direction)
                diagonal_match_SE = False
                diagonal_SE = "".join([matrix[r-1][c-1], matrix[r][c], matrix[r+1][c+1]])
                if diagonal_SE == "MAS" or diagonal_SE == "SAM":
                    diagonal_match_SE = True
                
                #Check diagonals (top-right to bottom-left i.e. SW direction)
                diagonal_match_SW = False
                diagonal_SW = "".join([matrix[r-1][c+1], matrix[r][c], matrix[r+1][c-1]])
                if diagonal_SW == "MAS" or diagonal_SW == "SAM":
                    diagonal_match_SW = True

                if diagonal_match_SE and diagonal_match_SW:
                    results.append((r,c))

    return results

results = find_mas_patterns(matrix)
print(len(results))
