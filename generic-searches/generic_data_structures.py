from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol, Generic
from heapq import heappush, heappop

T = TypeVar('T')

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...
    def __lt__(self: C, other: C) -> bool:
        ...
    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other
    def __ge__(self: C, other: C) -> bool:
        return not self < other

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()
    
    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.popleft()
    
    def __repr__(self) -> str:
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0,
     heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic
    
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T):
        heappush(self._container, item)

    def pop(self, item: T) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)