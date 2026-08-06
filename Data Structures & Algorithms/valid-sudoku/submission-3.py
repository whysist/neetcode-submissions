class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowCheck():
            check=set()
            for i in range(9):
                check.clear()
                for j in range(9):
                    if board[i][j]==".":
                        continue
                    else:
                        if board[i][j] in check:
                            return False
                        check.add(board[i][j])
            return True
        def colCheck():
            check=set()
            for j in range(9):
                check.clear()
                for i in range(9):
                    if board[i][j]==".":
                        continue
                    else:
                        if board[i][j] in check:
                            return False
                        check.add(board[i][j])
            return True
        
        def squareCheck():
            check=set()
            for row in range(0,9,3):
                for col in range(0,9,3):
                    check.clear()
                    for i in range(row,row+3):
                        for j in range(col,col+3):
                            if board[i][j]==".":
                                continue
                            else:
                                if board[i][j] in check:
                                    return False
                                check.add(board[i][j])
            return True

        return rowCheck() and colCheck() and squareCheck()
        