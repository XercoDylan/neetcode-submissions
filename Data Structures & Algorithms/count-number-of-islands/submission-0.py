class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0
        islands_considered = {}
        rows = len(grid[0])
        columns = len(grid)

        def within_bounds(cordinate):
            if (cordinate[0] >= 0 and cordinate[0] <= columns - 1) and (cordinate[1] >= 0 and cordinate[1] <= rows - 1):
                return True

            return False

        def get_neighbors(cordinate):
            changes = [[1,0],[-1,0],[0,1],[0,-1]]
                

            for change in changes:
                new_cordinate = (cordinate[0] + change[0], cordinate[1] + change[1])

                if not new_cordinate in islands_considered and within_bounds(new_cordinate) and grid[new_cordinate[0]][new_cordinate[1]] == "1":
                    islands_considered[new_cordinate] = True
                    get_neighbors(new_cordinate)
                        



        for row in range(rows):
            for column in range(columns):
                coordinate = (column, row)
                if not coordinate in islands_considered and grid[column][row] == "1":
                    total_islands += 1
                    islands_considered[coordinate] = True
                    get_neighbors(coordinate)

         

        return total_islands