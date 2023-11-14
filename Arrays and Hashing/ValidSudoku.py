# Nov 14 23
# Approach - declare 3 lists - where each entity is a set for rows , cols and grids.
# ie., rows = [set(), set(),..] these lists are of length 9
# if the cell is blank, just continue.

# Then, iterate through each of the elements in the given board matrix, and if it's a number -  see if its present in
# the row, col or grid set. If yes return false, else add the number to the respective row, col and grid lists..

# formula for identifying the grid is grid# = row//3)*3 + ()col//3)



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [set() for row in range(N)]
        cols = [set() for col in range(N)]
        grids = [set() for grid in range(N)]

        for r in range(N):
            for c in range(N):
                grid_num = r//3 *3 + c//3
                val = board[r][c]

                if val == ".":
                    continue
                else:
                    if val in rows[r]:
                        return False
                    
                    elif val in cols[c]:
                        return False
                    
                    elif val in grids[grid_num]:
                        return False

                    else:
                        rows[r].add(val)
                        cols[c].add(val)
                        grids[grid_num].add(val)
        
        return True
                    
# Actually, if the sudoku is N*N - even then the size of the sudoku that needs to be checked remains 
#constant -so still
# TC: O(1) - same constant run time
# SC: O(1) - same constant extra space needed