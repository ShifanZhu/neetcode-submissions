class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        row = len(grid)
        col = len(grid[0])

        q = deque()

        for i in range(row):
            for j in range(col):
                if (grid[i][j] == 0):
                    q.append((i, j))
        
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        INF = 2**31 - 1
        while q:
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= row or nc < 0 or nc >= col:
                    continue
                if grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
        