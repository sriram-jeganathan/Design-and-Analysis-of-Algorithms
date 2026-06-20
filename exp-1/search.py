import matplotlib.pyplot as plt
import numpy as np
import time
import random

# ── Linear Search ──────────────────────────────────────────────────────────────
# Receives a list and a target, returns the number of comparisons made.
# Time complexity  O(n)
# Space complexity O(1)
def linear_search(numbers, target):
    comparisons = 0
    for i in range(len(numbers)):
        comparisons += 1
        if numbers[i] == target:
            return i, comparisons
    return -1, comparisons

# ── Binary Search ──────────────────────────────────────────────────────────────
# Requires a sorted list. Returns the index and number of comparisons made.
# Time complexity  O(log n)
# Space complexity O(1)
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid, comparisons
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# ── Measure actual comparisons across increasing input sizes ───────────────────
# We use a worst-case target (one that is not in the list) so each run
# exercises the full algorithm rather than stopping early.
input_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
linear_comparisons = []
binary_comparisons = []

for n in input_sizes:
    numbers = list(range(n))           # sorted list 0 … n-1
    sorted_numbers = numbers.copy()    # binary search needs sorted input
    target = n + 1                     # not in the list → worst case for both

    _, lc = linear_search(numbers, target)
    _, bc = binary_search(sorted_numbers, target)

    linear_comparisons.append(lc)
    binary_comparisons.append(bc)

# ── Plot ───────────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_comparisons,
         label='Linear Search O(n)', color='blue', marker='o', markersize=4)
plt.plot(input_sizes, binary_comparisons,
         label='Binary Search O(log n)', color='orange', marker='s', markersize=4)

plt.title('Actual Comparisons: Linear Search vs Binary Search')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Comparisons')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which='both', ls='-', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig('search_complexity.png', dpi=150)
plt.show()
print("Plot saved.")

# ── Print a sample result table ────────────────────────────────────────────────
print(f"\n{'Input Size':>12} {'Linear':>10} {'Binary':>10}")
print("-" * 35)
for n, lc, bc in zip(input_sizes, linear_comparisons, binary_comparisons):
    print(f"{n:>12,} {lc:>10,} {bc:>10,}")