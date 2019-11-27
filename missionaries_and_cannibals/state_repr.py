from __future__ import annotations

from sys import path
from os.path import dirname as dir
path.append(dir(path[0]) + '\\generic_searches')

from typing import List, Optional
from generic_searches import node_to_path, bfs
from generic_data_structures import Node

MAX_NUM: int = 3

class MC_state:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.left_m: int = missionaries
        self.left_c: int = cannibals
        self.right_m: int = MAX_NUM - self.left_m
        self.right_c: int = MAX_NUM - self.left_c
        self.boat: bool = boat

    def __str__(self) -> str:
        return (f'On the west bank there are {self.left_m} missionaries and {self.left_c} cannibals.\nOn the east bank there are {self.right_m} missionaries and {self.right_c} cannibals.\nThe self.boat is on the {"left" if self.boat else "right"} bank.')

    def goal_test(self) -> bool:
        return self.islegal and self.right_m == MAX_NUM and self.right_c == MAX_NUM

    @property
    def islegal(self) -> bool:
        if self.right_m < self.right_c and self.right_m > 0:
            return False
        if self.left_m < self.left_c and self.left_m > 0:
            return  False
        return True
    
    def successors(self) -> List[MC_state]:
        result: List[MC_state] = []
        if self.boat:
            if self.left_m > 0:
                result.append(MC_state(self.left_m - 1, self.left_c, not self.boat))
            if self.left_c > 0:
                result.append(MC_state(self.left_m, self.left_c - 1, not self.boat))
            if self.left_c > 0 and self.left_m > 0:
                result.append(MC_state(self.left_m - 1, self.left_c - 1, not self.boat))    
        else:
            if self.right_m > 0:
                result.append(MC_state(self.left_m + 1, self.left_c, not self.boat))
            if self.right_c > 0:
                result.append(MC_state(self.left_m, self.left_c + 1, not self.boat))
            if self.right_m > 0 and self.right_c > 0:
                result.append(MC_state(self.left_m + 1, self.left_c + 1, not self.boat))
        return [x for x in result if x.islegal]
        