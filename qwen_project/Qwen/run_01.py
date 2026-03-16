# First incorrect attempt - Greedy adjacent approach
def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())

    def read_array():
        return list(map(int, input().split()))

    for _ in range(t):
        arr = read_array()
        n = len(arr)

        total = sum(arr)
        if total % n != 0:
            print("NO")
            continue

        target = total // n
        arr_copy = arr[:]

        # Wrong: Trying to balance only adjacent elements
        possible = True
        for i in range(n - 1):
            diff = arr_copy[i] - target
            if diff > 0:
                # Try to give to next element
                if diff & (diff - 1) != 0:  # Not power of 2
                    possible = False
                    break
                arr_copy[i] -= diff
                arr_copy[i + 1] += diff
            elif diff < 0:
                # Try to take from next element
                if (-diff) & (-diff - 1) != 0:  # Not power of 2
                    possible = False
                    break
                arr_copy[i] -= diff
                arr_copy[i + 1] += diff

        # Check if all elements are equal
        if possible and all(x == target for x in arr_copy):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()