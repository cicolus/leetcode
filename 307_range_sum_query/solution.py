from typing import List
from math import log2, ceil

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.size = len(nums)
        self.nums = nums
        if self.size > 0:
            segment_tree_size = (1 << int(ceil(log2(self.size)) + 1)) - 1
        else:
            segment_tree_size = 0
        self.segment_tree = [0] * segment_tree_size
        self._construct_segment_tree(0, self.size-1, 0)


    def _construct_segment_tree(self, lo, hi, idx):
        """
        :type lo: int
        :type hi: int
        """
        if lo == hi:
            self.segment_tree[idx] = self.nums[lo]
        elif lo < hi:
            md = (lo + hi) // 2
            self._construct_segment_tree(lo, md, idx*2+1)
            self._construct_segment_tree(md+1, hi, idx*2+2)
            self.segment_tree[idx] = self.segment_tree[idx*2+1] + self.segment_tree[idx*2+2]


    def _query(self, target_i, target_j, curr_i, curr_j, idx):
        """
        :type target_i: int
        :type target_j: int
        :type curr_i: int
        :type curr_j: int
        """
        if target_i == curr_i and target_j == curr_j:
            return self.segment_tree[idx]
        else:
            md = (curr_i + curr_j) // 2
            if target_j <= md:
                return self._query(target_i, target_j, curr_i, md, idx*2+1)
            elif target_i > md:
                return self._query(target_i, target_j, md+1, curr_j, idx*2+2)
            else:
                return self._query(target_i, md, curr_i, md, idx*2+1) + \
                       self._query(md+1, target_j, md+1, curr_j, idx*2+2)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self._update(i, val-self.nums[i], 0, self.size-1, 0)
        self.nums[i] = val

    def _update(self, i, diff, lo, hi, idx):
        """
        :type i: int
        :type val: int
        :type lo: int
        :type hi: int
        """
        self.segment_tree[idx] += diff
        if lo < hi:
            md = (lo + hi) // 2
            if i <= md:
                self._update(i, diff, lo, md, idx*2+1)
            else:
                self._update(i, diff, md+1, hi, idx*2+2)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._query(i, j, 0, self.size - 1, 0)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    test = NumArray([1, 3, 5, 7, 9, 11])
    print(test.segment_tree)
    print(test.sumRange(0, 5))
    print(test.sumRange(1, 5))
    print(test.sumRange(2, 5))
    print(test.sumRange(3, 5))
    print(test.sumRange(0, 4))
    print(test.sumRange(0, 3))
    print(test.sumRange(0, 2))
    print(test.sumRange(1, 4))
    test.update(2, 10)
    print(test.segment_tree)

