from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()

        # Encontramos todos los tesoros
        for i, fila in enumerate(grid):
            for j, celda in enumerate(fila):
                if celda == 0:
                    queue.append((i, j))

        # BFS
        while queue:
            i, j = queue.popleft()

            # Los 4 movimientos posibles
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj

                # Comprobamos los límites
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):

                    # Si es terreno que todavía no hemos visitado
                    if grid[ni][nj] == INF:

                        # Su distancia es la actual + 1
                        grid[ni][nj] = grid[i][j] + 1

                        # Guardamos su posición para explorarla después
                        queue.append((ni, nj))