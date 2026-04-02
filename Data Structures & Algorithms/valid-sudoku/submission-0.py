class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for rows in board:
            row_check = []
            for element in rows:
                if element in row_check and element != "." and element not in range(1, 9):
                    return False
                row_check.append(element)

        # col check
        for idx_rows, _ in enumerate(board):
            col_check = []
            for rows in board:
                if rows[idx_rows] in col_check and rows[idx_rows] != ".":
                    return False
                col_check.append(rows[idx_rows])         

        # grid check
        c = 0
        for _ in range(3):
            grid = [board[c*3], board[(c*3)+1], board[(c*3)+2]]
            c= c + 1

            cc = 0
            for __ in range(3):
                seen = []
                for rows in grid:
                    for ___ in range(3):
                        if rows[(cc * 3) + ___] in seen and rows[(cc * 3) + ___] != ".":
                            return False
                        seen.append(rows[(cc * 3) + ___])
                    
                cc = cc + 1
                    
                     
                

        return True
        