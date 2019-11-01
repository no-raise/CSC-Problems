from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol, Generic
from generic_data_structures import Stack, Node, Comparable, Queue

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar('C', bound="Comparable")

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

def dfs(initial: T, goal_test: Callable[[T], bool], 
     successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
        #Setting up frontier
        frontier: Stack[Node[T]] = Stack()
        frontier.push(Node(initial, None))
        #Creating a set for explored nodes
        explored: Set[T] = {initial}

        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state
            #Check for goal
            if goal_test(current_state):
                return current_node
            for child in successors(current_state):
                if child in explored:
                    continue
                explored.add(child)
                frontier.push(Node(child, current_node))
        return None  

def bfs(initial: T, goal_test: Callable[[T], bool], 
     successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
        #Setting up frontier
        frontier: Queue[Node[T]] = Queue()
        frontier.push(Node(initial, None))
        #Creating a set for explored nodes
        explored: Set[T] = {initial}

        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state
            #Check for goal
            if goal_test(current_state):
                return current_node
            for child in successors(current_state):
                if child in explored:
                    continue
                explored.add(child)
                frontier.push(Node(child, current_node))
        return None      
            
def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
        


if __name__ == "__main__":
    print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5))