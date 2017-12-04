# 312. Burst Balloons

## Description

Given `n` balloons, indexed from `0` to `n-1`. Each balloon is painted with a 
number on it represented by array nums. You are asked to burst all the balloons. 
If the you burst balloon `i` you will get `nums[left] * nums[i] * nums[right]` 
coins. Here left and right are adjacent indices of `i`. After the burst, the left 
and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
* (1) You may imagine `nums[-1] = nums[n] = 1`. They are not real therefore you can not burst them.
* (2) `0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100`

Example:

Given `[3, 1, 5, 8]`

Return `167`

```haskell
    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

## Solution

Note that this problem has a subtle recurrence relation. If we naively take the subproblem
structure in `(i, j)` to be `(i, k - 1), [k], (k + 1, j)`, the recurrence will be incorrect
because once we remove the `k` element, the boundary of `k+1` element will change and thus
the subproblem we have solved before doesn't help us. 

The correct subproblem to consider is if range `(i, j)` (inclusive) are burst last in the 
whole array. The boundary defined are thus `i-1` and `j+1`. Note that in this way we don't
need to worry about changing the subproblem, becuase we know that when a balloon `k` in the
range is burst last, the coin we are going to collect is `[k] * [i - 1] * [j + 1]`.  And
the boundary for the two smaller subproblems are the same. 

Take the sample input for example, we first examine the length 1 subproblems:

```haskell
[3] -> 1 * 3 * 1 = 3 (with boundary 1, 1)
[1] -> 3 * 1 * 5 = 15 (with boundary 3, 5)
[5] -> 1 * 5 * 8 = 40 (with boundary 1, 8)
[8] -> 5 * 8 * 1 = 40 (with boundary 5, 1)
```

Next, we consider the length 2 subproblems:

```haskell
[3, 1] = max(1 * 3 * 5 + 15, 3 + 1 * 1 * 5) = 30
[1, 5] = max(3 * 1 * 8 + 40, 15 + 3 * 5 * 8) = 135
[5, 8] = max(1 * 5 * 1 + 40, 40 + 1 * 8 * 1) = 48
```

And so on and so forth, the final memoization table would be:
```pythonstub
[[3,   30,  159, 167],
 [0,   15,  135, 159],
 [0,   0,   40,  48 ],
 [0,   0,   0,   40 ]]
```