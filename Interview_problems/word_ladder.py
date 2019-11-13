from sys import path
from os.path import dirname as dir
from __future__ import annotations
from generic_data_structures import Queue
from typing import List, Dict
path.append(dir(path[0]) + '\\generic_searches')

def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    graph: Dict = make_graph(word_list)



def make_graph():
    graph: Dict = {}


if __name__ == "__main__":
    begin_word: str = "hit"
    end_word: str = "cog"
    word_list: str = ["hot","dot","dog","lot","log","cog"]

    print(ladder_length(begin_word, end_word))