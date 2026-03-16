# Second incorrect attempt - BFS approach (times out)
def solve():
    import sys
    from collections import deque

    input = sys.stdin.readline

    def can_reach_target(values, target_value):
        length = len(values)
        state = tuple(values)
        target_state = (target_value,) * length

        if state == target_state:
            return True

        visited = {state}
        queue = deque([(state, 0)])

        while queue:
            curr, steps = queue.popleft()
            if steps > 100:  # Arbitrary limit, wrong approach
                continue

            curr_list = list(curr)

            # Try all possible operations
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    for k in range(31):
                        new_list = curr_list[:]
                        new_list[i] += (1 << k)
                        new_list[j] -= (1 << k)

                        # Check bounds (wrong assumption)
                        if min(new_list) < 0:
                            continue

                        new_state = tuple(new_list)
                        if new_state == target_state:
                            return True
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, steps + 1))
        return False

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        total = sum(arr)
        if total % n != 0:
            print("NO")
            continue

        target = total // n
        print("YES" if can_reach_target(arr, target) else "NO")


if __name__ == "__main__":
    solve()