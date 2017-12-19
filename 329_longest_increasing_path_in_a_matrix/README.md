## 329. Longest Increasing Path in a matrix

This is a very well-written question, very effectice to use in interview
to test candidate's understanding of basic graph algorithm and 
dynamic programming (noticeable subproblem), yet not too dependant
on the two techniques.

The key observation in this problem is that the length of the longest
increasing path __starting__ from one fixed point is fixed. To reiterate
my point, observe that when you point out an entry in the matrix,
the length of the longest increasing path that starts at this point, is known.
And if this point has a neighbor whose value is smaller, we don't need
to recalculate the length of the path that go through this point:
we just add 1 to this length. This observation becomes an effective
subproblem that we can continuously reuse once we have calculated the
value.

### _But how do we calculate the value of subproblem?_

This is where __DFS__ comes in. For each _uncalculated_ entry in the matrix, we do
a DFS following a path of increasing values. Notice that the subproblem we 
observe above is effective in the sense that each time we recurse
in the graph (a.k.a. matrix in this context), the problem becomes a
subproblem and we can store the value calculated. To give a more
concrete sense, when we recurse to an entry in the matrix that is
larger than all of its neighbors, than the DP value of this entry
is simple going to be 1, i.e. the following loop in the solution:
```pythonstub
for i, j in neighbors:
    if matrix[i][j] > matrix[x][y]:
        dp[x][y] = max(dp[x][y], 1 + DFS(i, j))
```
will not execute because `if` condition will not be true.

So core of the algorithm is thus:

* DFS on the entries that's not calculated yet
* Store the value of the subproblems in a matrix.

To elaborate on my thinking process, I initially thought of using
BFS, but BFS and DFS achieve the same goal in this problem and
BFS is harder to harness in this particular problem because we 
have a very obvious recursion pattern. 