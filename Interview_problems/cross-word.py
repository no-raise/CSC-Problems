
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def findWords(board, words):

    def dfs(i, j, word, nextChar, visited):
        if len(word) <= nextChar:
            return True

        wordFound = False

        for d in directions:
            newi = i + d[0]
            newj = j + d[1]

            # if new coordinates are valid
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and (newi, newj) not in visited:
                if word[nextChar] == board[newi][newj]:
                    visited.append((i, j))
                    wordFound = dfs(newi, newj, word, nextChar + 1, visited)
                    if wordFound:
                        return True

        return wordFound

    res = set()

    # for every word find the first char in the board and do dfs
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    if dfs(i, j, word, 1, list()):
                        res.add(word)

    return res


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]

words = ["oath", "pea", "eat", "rain"]


print(findWords(board, words))
