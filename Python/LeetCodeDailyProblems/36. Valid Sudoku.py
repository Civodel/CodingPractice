from typing import List


class Solution:
    def valid_row_col_miniboard(self, row_col_miniboard)->bool:
        for index in range(9):
            for j_index in range(index + 1, 9):
                if row_col_miniboard[index] == row_col_miniboard[j_index] and row_col_miniboard[index] != '.':
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if board !=[]:

            #sudoku row vaalidation
            for sudoku_row in board:
                if self.valid_row_col_miniboard(sudoku_row) ==False:
                    return False
            #sudoku col validation
            for sudoku_col in zip(*board):
                if self.valid_row_col_miniboard(sudoku_col) ==False:
                    return False
            #sudoku block validation
            for sudoku_block in range(9):
                miniboard=[]
                for index in (0,3,6):
                    for j_index in (0,3,6):
                        miniboard = [board[x][y] for x in range(index,index+3) for y in range(j_index,j_index+3)]
                        if self.valid_row_col_miniboard(miniboard) == False:
                            return False

        return True





if __name__ == '__main__':
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))