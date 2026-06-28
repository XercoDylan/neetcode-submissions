class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = {}
        column_nums = {}
        box_nums = {}

        for row in range(len(board)):
            for col in range(len(board[0])):
                
               

                num = board[row][col]

                if num == ".":
                    continue

                if row not in row_nums:
                    row_nums[row] = set()


                if col not in column_nums:
                    column_nums[col] = set()

                box_string = str((col//3)) + str(row//3)

                if box_string not in box_nums:
                    box_nums[box_string] = set()

                if num in row_nums[row]:
                    return False
                else:
                    row_nums[row].add(num)

                if num in column_nums[col]:
                    return False
                else:
                    column_nums[col].add(num)

                if num in box_nums[box_string]:
                    return False
                else:
                    box_nums[box_string].add(num)


        return True
        