import sys
from collections import deque


def can_reach_target(arr, target):
    n = len(arr)
    if n > 6:
        return None

    start = tuple(arr)
    target_state = tuple([target] * n)

    if start == target_state:
        return True

    visited = {start}
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        curr_list = list(curr)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(31):
                    new_list = curr_list[:]
                    new_list[i] += (1 << k)
                    new_list[j] -= (1 << k)

                    if min(new_list) < 0:
                        continue

                    new_state = tuple(new_list)

                    if new_state == target_state:
                        return True

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)

    return False


def main():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        total = sum(a)
        if total % n != 0:
            print("NO")
            continue

        target = total // n
        result = can_reach_target(a, target)

        if result is None:
            print("SKIP (n too large for brute force)")
        else:
            print("YES" if result else "NO")


if __name__ == "__main__":
    main()