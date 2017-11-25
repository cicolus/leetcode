from typing import List, Dict

def sample(S : str, K : int) -> str:
    S = S.replace("-", "")
    i = 0
    result = [] # type: List[str]
    for c in reversed(S): # type: str
        if i == 0:
            result.append("-")
        i = (i + 1) % 4
        if c.isupper():
            result.append(c)
        else:
            result.append(c.upper())
    if result[0] == '-':
        result.pop(0)
    return "".join(reversed(result))


def solution(A : List[int], E : List[int]) -> int:

    label_of = [None] + A # fix offset in indexing
    children_of = {} # type: Dict[int, List[int]]

    for parent, child in [(E[i], E[i+1]) for i in range(0, len(E), 2)]:
        if parent in children_of:
            children_of[parent].append(child)
        else:
            children_of[parent] = [child]

    print(children_of)

    def helper(parent : int) -> (int, int, int):
        if parent not in children_of:
            return (1, 1, label_of[parent])
        subtree_max = []
        extensible_max = []
        extensible_max_label = []
        children = children_of[parent]
        for idx in range(len(children)):
            subtree_max_i, extensible_max_i, extensible_max_label_i = helper(children_of[parent][idx])
            subtree_max.append(subtree_max_i)
            extensible_max.append(extensible_max_i)
            extensible_max_label.append(extensible_max_label_i)
        curr_extensible = 1
        for i in range(len(children)):
            if extensible_max_label[i] == label_of[parent]:
                curr_extensible = max(curr_extensible, 1 + extensible_max[i])
            for j in range(i+1, len(children)):
                if extensible_max_label[i] == extensible_max_label[j] \
                        and extensible_max_label[i] == label_of[parent]:
                    subtree_max.append(1 + extensible_max[i] + extensible_max[j])
        return (max(subtree_max), curr_extensible, label_of[parent])

    return max(helper(1)) - 1 # count edges, not nodes


if __name__ == '__main__':
    A = [1,1,1,2,2]
    E = [1,2,1,3,2,4,2,5]
    print(solution(A, E))
    print(sample("2-4A0r7-4k", 4))
