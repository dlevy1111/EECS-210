# the sudoku player, or sudoker; recursive by nature

class Sudoker:
    def __init__(self, grid_data):
        self.grid = grid_data # grid data is a 2d list
    
    def solve(self): # a public function to kickstart everything
        return self._rec_solve(0, 0)

    def _rec_solve(self, row, col): # a private, recursive function
        if row == 9 and col == 9: # are we done?
            # print("we are done!")
            print(self.print_layout())
            return True

        nextrow = row 
        nextcol = col+1
        if nextrow >= len(self.grid): # taking care of the edge cases of the board
            nextrow = nextrow+1
            nextcol = 0
            
        if col < 9:
            if self.grid[row][col] != "0": # if we're standing on a number, we don't want to change that.
                if self._rec_solve(nextrow, nextcol):
                    return True
                return False
        else:
            try:
                col = 0
                row = row + 1
                if self.grid[row][col] != "0": # like above, we don't want to change any numbers but this is a special case where we need to move between rows.
                    if self._rec_solve(row, col):
                        return True
                    return False
            except:
                # print("all done!")
                self.print_layout()
                return True # I'm going to call this paving away a bug
        
        for i in range(1,10): # looping through all possible numbers for a space
            if self.is_valid_move(row, col, i): # does the spot work with the given number?
                self.mark(row, col, i) # then mark it on the board
                if self._rec_solve(nextrow, nextcol): # move to the next position, asking all of the same questions for this new case
                    return True
   
        self.unmark(row, col) # in the case that no numbers fit in this spot (with respect to the rest of the board)
        return False

    def is_valid_move(self, row, col, num): # assume you're already standing on a "0", and we've picked a number to put on this space
        for testrow in range(0, len(self.grid)):
            if testrow == int(row): # are we looking at the same spot that we're standing on?
                continue
            if self.grid[testrow][col] == "0": # is the spot we're looking at a _?
                continue
            if num == int(self.grid[testrow][col]): # if the item in this spot is the same as the spot in any other rows on the board (in the same column)
                return False # then this is not a valid move
        for testcol in range(0, len(self.grid[0])):
            if testcol == int(col): # are we looking at the same spot that we're standing on?
                continue
            if self.grid[row][testcol] == "0": # is the spot we're looking at a _?
                continue
            if num == int(self.grid[row][testcol]): # if the item in this spot is the same as the spot in any other columns on the board (in the same row)
                return False
        
        section_rowwise = (row) // 3 # a handy formula for computing which section (of the 3) we are in
        section_colwise = (col) // 3

        sr = section_rowwise # shorthand for later
        sc = section_colwise

        # one very long calculation for deducing whether a subgrid (3x3) has some number already
        sum_of_num_top = int(self.grid[sr*3    ][sc*3] == str(num)) + int(self.grid[sr*3    ][sc*3 + 1] == str(num)) + int(self.grid[sr*3    ][sc*3 + 2] == str(num)) # do any of the numbers in the top row equal the number
        sum_of_num_mid = int(self.grid[sr*3 + 1][sc*3] == str(num)) + int(self.grid[sr*3 + 1][sc*3 + 1] == str(num)) + int(self.grid[sr*3 + 1][sc*3 + 2] == str(num)) # do any of the numbers in the middle row equal the number
        sum_of_num_bot = int(self.grid[sr*3 + 2][sc*3] == str(num)) + int(self.grid[sr*3 + 2][sc*3 + 1] == str(num)) + int(self.grid[sr*3 + 2][sc*3 + 2] == str(num)) # do any of the numbers in the bottom row equal the number
        sum_of_num = sum_of_num_top + sum_of_num_mid + sum_of_num_bot
        # print(sum_of_num)
        # print("sr =", sr, "sc =", sc, "row =", row, "col =", col, "num =", num, "sum = ", sum_of_num)

        if sum_of_num == 1:
            return False

        return True

    def mark(self, row, col, num): # marking a spot
        self.grid[row][col] = str(num)

    def unmark(self, row, col): # unmarking a spot
        self.grid[row][col] = "0"

    def print_layout(self): # print the layout
        for item in self.grid:
            print(item)
    
    def return_layout(self):
        return self.grid