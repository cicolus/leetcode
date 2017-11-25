from typing import List, Dict

def solution(A : List[int], E : List[int]) -> int:

    label_of = [None] + A # fix offset in indexing
    children_of = {} # type: Dict[int, List[int]]
    non_root = set()

    for parent, child in [(E[i], E[i+1]) for i in range(0, len(E), 2)]:
        non_root.add(child)
        if parent in children_of:
            children_of[parent].append(child)
        else:
            children_of[parent] = [child]

    root = list(set(children_of.keys()).difference(non_root))[0]

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

    return max(helper(root)) - 1 # count edges, not nodes



if __name__ == '__main__':
    A = [1, 1, 1, 2, 2]
    E = [1, 2, 1, 3, 2, 4, 2, 5]
    print(solution(A, E)) # 2
    A_1 = [1, 2, 2, 1, 2, 1, 2, 1]
    E_1 = [6, 8, 4, 7, 4, 5, 4, 6, 2, 3, 1, 2, 1, 4]
    test_1 = [A_1, E_1]
    print(test_1)
    print(solution(A_1, E_1)) # 3
    A_2 = [4, 4, 4, 4, 4, 3, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1]
    E_2 = [2, 1, 3, 2, 3, 4, 4, 5, 6, 3, 6, 7, 7, 8, 6, 9, 9, 10, 10, 11, 10, 12, 10, 14, 12, 13, 15, 16, 9, 15]
    test_2 = [A_2, E_2]
    print(test_2)
    print(solution(A_2, E_2)) # 5
    A_3 = A_2 + [5, 2, 3, 5, 2, 5, 2, 5, 5, 5, 5, 5]
    E_3 = E_2 + [16, 20, 16, 19, 20, 22, 20, 18,
                 22, 17, 22, 24, 17, 27, 24, 25,
                 25, 26, 26, 28, 18, 21, 21, 23]
    print(solution(A_3, E_3)) # 6
    test_3 = [A_3, E_3]
    print(test_3)