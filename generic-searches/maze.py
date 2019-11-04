from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, node_to_path, bfs
from generic_data_structures import Node


class Cell(str, Enum):
    EMPTY = " "
    START = "S"
    GOAL = "G"
    PATH = "*"
    BLOCKED = "X"

directions = [(0,1), (1,0), (0,-1), (-1,0)]

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
     start: MazeLocation = MazeLocation(0,0), goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # Initializing grid with cells
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # Add blocked cells to the grid
        self._randomnly_fill(rows, columns, sparseness)
        #Set up start and goal points in the grid
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomnly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join(c.value for c in row) + "\n"
        return output

    def goal_test(self, current_location: MazeLocation) -> bool:
        return current_location == self.goal

    def successors(self, current_location: MazeLocation) -> List[MazeLocation]:
        moves: List[MazeLocation] = []
        for d in directions:
            new_row: int = current_location.row + d[0]
            new_column: int = current_location.column + d[1]
            if 0 <= new_row < self._rows and 0 <= new_column < self._columns and self._grid[new_row][new_column] != Cell.BLOCKED:
                moves.append(MazeLocation(new_row, new_column))
        return moves

    def mark(self, path: List[MazeLocation]) -> None:
        for ml in path:
            self._grid[ml.row][ml.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    
    def clear(self, path: List[MazeLocation]) -> None:
        for ml in path:
            self._grid[ml.row][ml.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
        
    def euclidean_distance(self,)

if __name__ == "__main__":
    m: Maze = Maze()
    print(m)
    #Testing depth first search
    solution_dfs: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successors)
    if solution_dfs == None:
        print("No solution using dfs")
    else:
        path_dfs: List[MazeLocation] = node_to_path(solution_dfs)
        m.mark(path_dfs)
        print(m)
        m.clear(path_dfs)

    #Testing breadth first search
    solution_bfs: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successors)
    if solution_bfs == None:
        print("No solution using bfs")
    else:
        path_bfs: List[MazeLocation] = node_to_path(solution_bfs)
        m.mark(path_bfs)
        print(m)
        m.clear(path_bfs)