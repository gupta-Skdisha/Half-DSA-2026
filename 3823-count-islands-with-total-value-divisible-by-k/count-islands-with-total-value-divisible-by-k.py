from collections import deque

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):

                if grid[r][c] > 0 and (r, c) not in visited:
                    queue = deque([(r, c)])
                    visited.add((r, c))
                    total = 0

                    while queue:
                        row, col = queue.popleft()
                        total += grid[row][col]

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if (0 <= nr < m and
                                0 <= nc < n and
                                grid[nr][nc] > 0 and
                                (nr, nc) not in visited):

                                visited.add((nr, nc))
                                queue.append((nr, nc))

                    if total % k == 0:
                        count += 1

        return count