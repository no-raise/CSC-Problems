from __future__ import annotations
from typing import List, Dict, Deque
from collections import defaultdict

def make_graph(word_list: List[str]) -> Dict[str]:
    graph: Dict[str] = defaultdict(list)
    for word1 in word_list:
        # if word1 not in graph:
        #     graph[word1] = list()
        for word2 in word_list:
            if is_one_away(word1, word2):
                graph[word1].append(word2)
    return graph
            
def is_one_away(word1: str , word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    count: int = 0
    for i, char in enumerate(word1):
        if word1[i] != word2[i]:
            count += 1
    return count == 1

class Node:
    def __init__(self, parent: Node , word: str):
        self.parent = parent
        self.word = word

def to_path(node) -> None:
    path: List[str] = [node.word]
    
    while node.parent is not None:
        node = node.parent
        path.append(node.word)

    for node in reversed(path):
        print(f'-- {node} --')

def path_len(node) -> int:
    count: int = 1
    
    while node.parent is not None:
        count += 1
        node = node.parent
    
    print(count)
    



def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    if end_word not in word_list:
        return 0
    
    if begin_word not in word_list:
        word_list.append(begin_word)
    # Making graph
    graph: Dict[str] = make_graph(word_list)
    # Initializing Queue
    queue: Deque[Node] = Deque()
    queue.append(Node(None, begin_word))
    #initializing visited
    visited: set[str] = set(begin_word)
    
    while queue:
        curr_node: Node = queue.popleft()
        curr_word: str = curr_node.word

        # Check for goal       
        if curr_word == end_word:
            return curr_node
        
        for child in graph[curr_word]:
            if child in visited:
                continue
            queue.append(Node(curr_node, child))
            visited.add(curr_word)
    return 0

if __name__ == "__main__":
    begin_word: str = "hit"
    end_word: str = "cog"
    
    word_list: str = ["hot","dot","dog","lot","log", "cog"]

    solution_node: Node = ladder_length(begin_word, end_word, word_list)

    if solution_node != 0:
        to_path(solution_node)
        path_len(solution_node)
    else:
        print(f"No path was found.")
