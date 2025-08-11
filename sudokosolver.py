def print_sudoku(grid):
    """Prints the Sudoku grid in a readable format"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def is_valid(grid, row, col, num):
    """Checks if a number can be placed in a given cell"""
    # Check row
    if num in grid[row]:
        return False
    
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
                
    return True

def find_empty_cell(grid):
    """Finds the next empty cell (represented by 0)"""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking"""
    empty_cell = find_empty_cell(grid)
    
    # If no empty cells, puzzle is solved
    if not empty_cell:
        return True
        
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
                
            # Backtrack if solution not found
            grid[row][col] = 0
            
    return False

def main():
    print("SUDOKU SOLVER")
    print("=============")
    print("Enter your Sudoku puzzle row by row.")
    print("Use 0 to represent empty cells, separate numbers with spaces.")
    
    # Get input from user
    grid = []
    for i in range(9):
        while True:
            row_input = input(f"Enter row {i+1}: ")
            try:
                row = list(map(int, row_input.split()))
                if len(row) != 9:
                    print("Please enter exactly 9 numbers per row.")
                    continue
                if any(num < 0 or num > 9 for num in row):
                    print("Numbers must be between 0 and 9.")
                    continue
                grid.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    
    print("\nYour puzzle:")
    print_sudoku(grid)
    
    if solve_sudoku(grid):
        print("\nSolution:")
        print_sudoku(grid)
    else:
        print("\nNo solution exists for this puzzle.")

if __name__ == "__main__":
    main()
