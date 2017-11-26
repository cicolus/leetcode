class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for point in asteroids:
            case_1 = False
            while result and point < 0 and result[-1] > 0  and abs(point) >= abs(result[-1]):
                if  abs(point) == abs(result[-1]):
                    result.pop(-1)
                    case_1 = True
                    break
                else:
                    result.pop(-1)
            if case_1:
                continue
            elif result and point < 0 and result[-1] > 0 and -point < result[-1]:
                continue
            else:
                result.append(point)
        return result



if __name__ == '__main__':
    test = Solution()
    print(test.asteroidCollision([5, 10, -5])) # [5, 10]
    print(test.asteroidCollision([8, -8])) # []
    print(test.asteroidCollision([10, 2, -5])) # [10]
    print(test.asteroidCollision([-2,-2,-2,2])) # [-2,-2,-2,2]