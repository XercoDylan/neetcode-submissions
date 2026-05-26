class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_items = {

        }

        grid_items = {

        }

        for r in range(len(board)):
            row_items = set()
            for c in range(len(board[0])):
                num = board[r][c]

                if num.isdigit():
                    if num in row_items:
                        return False
                    
                    row_items.add(num)
                    
                    if not c in col_items:
                        col_items[c] = set()
                    
                    if num in col_items[c]:
                        return False
                        
                    col_items[c].add(num)
                    
                    if not f"{r//3}x{c//3}" in grid_items:
                        grid_items[f"{r//3}x{c//3}"] = set()
                        
                    if num in grid_items[f"{r//3}x{c//3}"]:
                        return False
                        
                    grid_items[f"{r//3}x{c//3}"].add(num)
                
        return True


        