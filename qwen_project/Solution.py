def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        total = sum(arr)
        if total % n != 0:
            print("NO")
            continue

        target = total // n
        excess = 0
        possible = True

        for i in range(n):
            excess += arr[i] - target

            if excess != 0:
                # Check if excess is power of 2
                abs_excess = abs(excess)
                if abs_excess & (abs_excess - 1) != 0:
                    possible = False
                    break

        print("YES" if possible else "NO")


if __name__ == "__main__":
    solve()