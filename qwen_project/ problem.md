# D. Power Balance Array

**Time limit per test: 2 seconds**  
**Memory limit per test: 256 megabytes**  
**Input: standard input**  
**Output: standard output**

You are given an array  of an integers. In one operation, you can:

- Choose three integers i, j, and k (1 ≤ i, j ≤ n, i ≠ j, 0 ≤ k ≤ 30)
- Increase a[i] by 2^k and decrease a[j] by 2^k

You can perform this operation any number of times (possibly zero). Determine if it's possible to make all elements of the array equal.

## Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The description of each test case follows:
- The first line contains an integer n (1 ≤ n ≤ 10^5)
- The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9)

It is guaranteed that the sum of n over all test cases doesn't exceed 2⋅10^5.

## Output
For each test case, print "YES" if it's possible to make all elements equal, and "NO" otherwise.

## Example

### Input