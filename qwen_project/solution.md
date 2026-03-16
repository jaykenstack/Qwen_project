# Solution Explanation

## Key Insight
The problem reduces to checking if every prefix sum of (a[i] - target) is a power of two (including zero), where target = sum(a) / n.

## Mathematical Foundation

Let target = (∑a[i]) / n. Define d[i] = a[i] - target.

When processing from left to right, at position i, the cumulative sum S[i] = d[1] + d[2] + ... + d[i] represents the net amount that must be transferred from the first i elements to the remaining elements.

Since each operation transfers exactly 2^k, and we can only use future elements to balance the current prefix, S[i] must be achievable as a single transfer. Therefore, |S[i]| must be a power of two (or zero).

## Algorithm
1. If sum(a) not divisible by n → "NO"
2. target = sum(a) // n
3. excess = 0
4. For each element x in a:
   - excess += (x - target)
   - if excess ≠ 0 and (excess & (excess - 1)) ≠ 0 → "No"
5. "Yes"

## Complexity
- Time: O(n) per test case
- Space: O(1)

## Proof of Sufficiency
If all prefixes are powers of two, we can construct a solution:
1. Process from left to right
2. When excess = +2^k at position i, find any future j with deficit
3. Perform operation: subtract 2^k from a[i], add 2^k to a[j]
4. This maintains all prefix properties and eventually reaches equilibrium