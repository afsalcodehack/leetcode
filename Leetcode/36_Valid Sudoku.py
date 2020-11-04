from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_larg = {}

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in list_larg.keys():
                    list_larg[board[i][j]] = [];
                    list_larg[board[i][j]].append((i, j));
                else:
                    for t in list_larg[board[i][j]]:
                        if t[0] == i or t[1] == j:
                            return False;
                    list_larg[board[i][j]].append((i, j));
        return True


service = Solution();
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]];

print(service.isValidSudoku(board));
