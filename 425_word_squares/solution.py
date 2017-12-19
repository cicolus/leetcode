from pprint import pprint
from collections import defaultdict
from typing import List, DefaultDict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        trie = defaultdict(list) # type: DefaultDict[str, List[str]]
        for word in words:
            for i in range(1,n):
                trie[word[:i]].append(word)

        result = []

        def build(square: List[str]) -> None:
            if len(square) == n:
                result.append(square)
            else:
                for word in trie["".join([s[len(square)] for s in square])]:
                    build(square + [word])

        for word in words:
            build([word])
        return result


if __name__ == '__main__':
    test = Solution()
    pprint(test.wordSquares(["abat", "baba", "atan", "atal"]), width=10)
    pprint(test.wordSquares(["area", "lead", "wall", "lady", "ball"]), width=10)
    pprint(test.wordSquares(["ball", "area", "lead", "lady"]), width=10)