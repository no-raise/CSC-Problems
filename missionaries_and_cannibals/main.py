from sys import path
from os.path import dirname as dir
path.append(dir(path[0]) + '\\generic_searches')

from state_repr import MAX_NUM, MC_state
from generic_searches import bfs, node_to_path
from generic_data_structures import Node
from typing import List, Optional


def display_solution(path: List[MC_state]) -> None:
    if len(path) == 0:
        return 
    
    old_state: MC_state = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(f'{old_state.right_m - current_state.right_m} missionaries and {old_state.right_c - current_state.right_c} cannibals moved from left to right bank')
        else:
            print(f'{old_state.left_m - current_state.left_m} missionaries and {old_state.left_c - current_state.left_c} cannibals moved from right to left bank')
        print(current_state)
        old_state = current_state
    
if __name__ == "__main__":
    start: MC_state = MC_state(3, 3, True)
    solution: Optional[Node[MC_state]] = bfs(start, MC_state.goal_test, MC_state.successors)
    if solution is None:
        print("No solution found.")
    else:
        path = node_to_path(solution)
        display_solution(path)

    

        