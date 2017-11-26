from typing import List
from queue import Queue

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        q = Queue()
        original_color = image[sr][sc]
        start = (sr, sc)
        width = len(image[0])
        height = len(image)
        seen = set()
        seen.add(start)
        def check_point(x : (int, int)) -> bool:
            return x[0] >= 0 and x[0] < height and x[1] >= 0 and x[1] < width \
                   and image[x[0]][x[1]] == original_color and x not in seen

        q.put(start)
        while q.qsize() > 0:
            to_process = q.get()
            image[to_process[0]][to_process[1]] = newColor
            neighbors = [(to_process[0] - 1, to_process[1]), (to_process[0], to_process[1] + 1),
                         (to_process[0] + 1, to_process[1]), (to_process[0], to_process[1] -1)]
            for point in neighbors:
                if check_point(point):
                    q.put(point)
                    seen.add(point)
        return image

if __name__ == '__main__':
    test = Solution()
    print(test.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))