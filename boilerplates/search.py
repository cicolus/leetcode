from queue import Queue
from heapq import heappush, heappop

def BFS(graph, target, start):
    work_list = Queue()
    work_list.put(start)
    seen = {start}

    while work_list.qsize() > 0:
        to_visit = work_list.get()
        if to_visit == target:
            return True
        for neighbor in graph[to_visit]:
            if neighbor not in seen:
                seen.add(neighbor)
                work_list.put(neighbor)

    return False

def DFS(graph, target, start):
    work_list = [start]
    seen = {start}

    while work_list:
        to_visit = work_list.pop()
        if to_visit == target:
            return True
        for neighbor in graph[to_visit]:
            if neighbor not in seen:
                seen.add(neighbor)
                work_list.append(neighbor)

    return False

def dijkstra(graph, target, start):
    heap = [(0, start)]
    seen = set()

def bin_search(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return -1


if __name__ == '__main__':
    test_graph = {1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}
    test_arr = [1, 2, 3, 4, 6, 9, 13, 16, 21, 28, 33]
    test_idx = [0, 1, 2, 3, 4, 5, 6,  7,  8,  9,  10]
    print(bin_search(test_arr, 6))
    print(bin_search(test_arr, 21))
    print(bin_search(test_arr, 33))
    print(bin_search(test_arr, 1))
    print(bin_search(test_arr, 5))
    print(bin_search(test_arr, 27))

