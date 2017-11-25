from typing import List, Dict, Tuple


def solution(A : str, B : str) -> int:
    initial = A
    counter = 1
    while len(initial) < len(B) + 2 * len(A):
        if initial.find(B) < 0:
            counter += 1
            initial += A
        else:
            return counter
    return -1




if __name__ == '__main__':
    pass