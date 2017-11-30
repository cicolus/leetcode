# Welcome to Facebook!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!



# Given a collection of points, in 2-D space, and a number k, find the k closest
# points to 0,0 (closest as defined by Euclidean distance). As an example the
# point (3,4) would have distance 5


from heapq import heappush, heappop
from typing import List


def solution(points: List[(int, int)], k: int):
    heap = []
    for point in points:
        if len(heap) < k:
            heappush(heap, (-(point[0] * point[0] + point[1] * point[1]), point))
        else:
            max_distance, max_point = heappop(heap)
            max_distance *= -1
            new_distance = point[0] * point[0] + point[1] * point[1]
            if new_distance < max_distance:
                heappush(heap, (-new_distance, point))
            else:
                heappush(heap, (-max_distance, max_point))
    return heap


def solution_1(points: List[(int, int)], k: int):
    pivot = points[0]
    pivot_distance = pivot[0] * pivot[0] + pivot[1] * pivot[1]
    left = list(filter(lambda x: (x[0] * x[0] + x[1] * x[1] <= pivot_distance), points))
    right = list(filter(lambda x: (x[0] * x[0] + x[1] * x[1] > pivot_distance), points))
    if len(left) == k - 1:
        return left + [pivot]
    elif len(left) == k:
        return left
    elif len(left) < k - 1:
        return left + [pivot] + solution_1(right, k - len(left) - 1)
    else:
        return solution_1(left, k)


# n ^ 2 - worst case
# T(n) = T(n / 2) + O(n)

