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
        possible = True

        for x in arr:
            if (x - target) % 2 != 0:
                possible = False
                break

        print("YES" if possible else "NO")


if __name__ == "__main__":
    solve()