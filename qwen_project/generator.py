import random
import sys
import os


def generate_solvable_case(n, max_val=10 ** 9):
    """Generate a solvable test case"""
    target = random.randint(max_val // 4, max_val // 2)
    arr = [target] * n

    # Perform valid operations to create variation
    ops_count = random.randint(n, n * 3)
    for _ in range(ops_count):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i == j:
            continue
        k = random.randint(0, 30)
        if arr[i] + (1 << k) <= max_val and arr[j] - (1 << k) >= 1:
            arr[i] += (1 << k)
            arr[j] -= (1 << k)

    random.shuffle(arr)
    return arr


def generate_unsolvable_case(n, max_val=10 ** 9):
    """Generate an unsolvable test case"""
    # Either make sum not divisible
    if random.choice([True, False]):
        arr = [random.randint(1, max_val) for _ in range(n)]
        total = sum(arr)
        if total % n == 0:
            arr[0] += 1  # Make sum non-divisible
        return arr

    # Or make prefix sum not power of two
    target = random.randint(max_val // 4, max_val // 2)
    arr = [target] * n

    # Introduce a problematic prefix
    pos = random.randint(1, n - 2)
    bad_value = 3  # Not a power of two
    for i in range(pos):
        arr[i] += bad_value

    # Balance later elements to maintain total sum
    arr[pos] -= bad_value * pos

    # Shuffle to hide pattern
    random.shuffle(arr)
    return arr


def main():
    if len(sys.argv) > 1:
        random.seed(int(sys.argv[1]))
    else:
        random.seed(42)

    # Create test_cases directory if it doesn't exist
    os.makedirs("test_cases", exist_ok=True)

    test_cases = [
        # 1 — small mixed cases
        ([1, 3, 5, 7, 4], True),
        ([1, 2, 3], False),
        ([10], True),

        # 2 — equal / almost equal
        ([4, 4, 4, 4], True),
        ([1, 1, 1, 16], False),

        # 3 — power-of-two looking but wrong
        ([2, 4, 6, 8, 10, 6], False),

        # 4 — large solvable + obvious unsolvable
        (generate_solvable_case(100000), True),
        ([10 ** 9, 1, 10 ** 9, 1, 10 ** 9], False),

        # 5 — alternating-ish
        ([1, 3, 5, 7, 9, 11, 6], True),

        # 6 — zeros pattern
        ([0, 8, 0, 8, 0, 8, 0, 8], True),

        # 7 — classic small unsolvable
        ([1, 2, 4, 9], False),
    ]

    # Write test cases
    for idx, (arr, solvable) in enumerate(test_cases, 1):
        n = len(arr)
        total = sum(arr)

        # Write input
        with open(f'test_cases/{idx}.in', 'w') as f:
            f.write(f"1\n{n}\n")
            f.write(' '.join(map(str, arr)) + '\n')

        # Write output
        with open(f'test_cases/{idx}.out', 'w') as f:
            if total % n != 0:
                f.write("NO\n")
            else:
                # Quick check for solvable cases we generated
                if solvable:
                    f.write("YES\n")
                else:
                    f.write("NO\n")

    print(f"Generated {len(test_cases)} test cases in test_cases/ directory")


if __name__ == "__main__":
    main()