# 🚀 Day 1: Two Number Sum

### 📝 1. Problem Statement Understanding
**The Goal:** You are given an array of numbers and a "target" sum. Find two different numbers in that array that, when added together, equal exactly that target sum.

**Example:**
*   **Input:** `Numbers: [3, 5, -4, 8, 11, 1, -1, 6]`, `Target: 10`
*   **Output:** `[11, -1]` (Because $11 + (-1) = 10$)

---

### ⚙️ 2. Solution Evolution (The 3 Approaches)

In an interview, never jump straight to the best answer. Show the interviewer how you can optimize a solution.

#### 🔴 Approach 1: Brute Force (The "Check Everything" Way)
**Logic:** Use two nested loops. The first loop picks a number, and the second loop checks every other number in the list to see if they sum to the target.
*   **Pseudo Code:**
    1. For each number `i` in the list:
    2. For each number `j` that comes after `i`:
    3. If `i + j == target`, return `[i, j]`.
*   **Time Complexity:** $O(n^2)$ (Very slow for large lists).
*   **Space Complexity:** $O(1)$ (No extra memory used).

#### 🟡 Approach 2: Sorting & Two Pointers (The $O(n \log n)$ Way)
**Logic:** Sort the list first. Place one pointer at the `left` (smallest) and one at the `right` (largest). If the sum is too high, move the right pointer left. If the sum is too low, move the left pointer right.
*   **Pseudo Code:**
    1. Sort the array.
    2. While `left` pointer < `right` pointer:
    3. If `sum == target`, return pair.
    4. If `sum < target`, `left++`.
    5. If `sum > target`, `right--`.
*   **Time Complexity:** $O(n \log n)$ (Because sorting takes this much time).
*   **Space Complexity:** $O(1)$ or $O(n)$ depending on the sorting algorithm.

#### 🟢 Approach 3: Hash Map (The $O(n)$ Optimal Way)
**Logic:** As you walk through the list, calculate the "Complement" (Target - Current Number). If the complement is already in your "Seen" dictionary, you've found the pair instantly.
*   **Pseudo Code:**
    1. Create an empty dictionary `seen`.
    2. For each `num` in the list:
    3. `complement = target - num`.
    4. If `complement` is in `seen`, return `[complement, num]`.
    5. Else, add `num` to `seen`.
*   **Time Complexity:** $O(n)$ (We only walk through the list once).
*   **Space Complexity:** $O(n)$ (We use extra memory to store the dictionary).

---




### 📝 1. Problem Statement Understanding
**The Goal:** Given an array of numbers and a target sum, find two different numbers that add up to that target.

**Example:**
*   **Input:** `[3, 5, -4, 8, 11, 1, -1, 6]`, `Target: 10`
*   **Output:** `[11, -1]`

---

### ⚙️ 2. Solution Evolution & Implementations

#### 🔴 Approach 1: Brute Force (The "Check Everything" Way)
**Logic:** We use a "Nested Loop." We pick one number and then scan the rest of the array to see if any other number completes the sum.

```python
def two_number_sum_brute(nums, target_sum):
    # Outer loop picks the first number
    for i in range(len(nums)):
        # Inner loop picks the second number (starting after the first one)
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                return [nums[i], nums[j]]
    return []

# Complexity: Time O(n^2) | Space O(1)
```
**Code Breakdown:**
*   **`range(len(nums))`**: We use indices instead of values so we can ensure we don't pick the same element twice.
*   **`i + 1`**: The inner loop starts at `i + 1` to avoid checking the same pair twice or adding a number to itself.
*   **Why this is "Bad":** If you have 1 million numbers, this code might perform 1 trillion checks.

---

#### 🟡 Approach 2: Sorting & Two Pointers (The $O(n \log n)$ Way)
**Logic:** We sort the array first. This allows us to use the "Squeeze" technique: if the sum is too small, we move the left pointer to a bigger number; if too big, we move the right pointer to a smaller number.

```python
def two_number_sum_pointers(nums, target_sum):
    # Step 1: Sort the array (This takes O(n log n) time)
    nums.sort() 
    
    left = 0
    right = len(nums) - 1
    
    # Step 2: Squeeze the pointers until they meet
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target_sum:
            return [nums[left], nums[right]]
        elif current_sum < target_sum:
            left += 1  # Need a larger sum, move left pointer right
        else:
            right -= 1 # Need a smaller sum, move right pointer left
            
    return []

# Complexity: Time O(n log n) | Space O(1)
```
**Code Breakdown:**
*   **`.sort()`**: This is the most expensive part of the code. It organizes the numbers in ascending order.
*   **`while left < right`**: We stop once the pointers cross, meaning no pair was found.
*   **`left += 1` / `right -= 1`**: Because the list is sorted, we can logically decide which direction to move without checking every combination.

---

#### 🟢 Approach 3: Hash Map (The $O(n)$ Optimal Way)
**Logic:** We trade memory for speed. We store every number we visit in a dictionary. Before storing a number, we check if its "needed partner" (the complement) is already in the dictionary.

```python
def two_number_sum_optimal(nums, target_sum):
    # Step 1: Create the 'memory log'
    seen = {}
    
    for num in nums:
        # Step 2: Calculate what we NEED to reach the target
        complement = target_sum - num
        
        # Step 3: Instant check in the dictionary
        if complement in seen:
            return [complement, num]
        
        # Step 4: Store the current number for future partners
        seen[num] = True
        
    return []

# Complexity: Time O(n) | Space O(n)
```
**Code Breakdown:**
*   **`seen = {}`**: A dictionary used to store numbers we've already passed.
*   **`if complement in seen`**: This is an $O(1)$ operation. It doesn't matter if the dictionary has 10 or 10 million items; the check is nearly instant.
*   **`seen[num] = True`**: We don't care about the value (True), only that the key (the number) exists.

---

### 📊 3. Comparison & Differences

| Feature | Brute Force | Two Pointers | Hash Map |
| :--- | :--- | :--- | :--- |
| **Runtime** | $O(n^2)$ (Slowest) | $O(n \log n)$ (Medium) | $O(n)$ (Fastest) |
| **Memory** | $O(1)$ (Best) | $O(1)$ (Best) | $O(n)$ (Worst) |
| **Requirement** | None | Requires Sorted Data | Requires Extra RAM |
| **Best Use Case** | Tiny arrays (< 100 items) | Memory-constrained systems | Performance-critical systems |

---

### 🔍 4. Definitions for the Engineer

1.  **Nested Loop:** A loop inside a loop. This usually multiplies the time complexity (e.g., $n \times n = n^2$).
2.  **Pointers:** Variables that hold the index (position) of an element in an array.
3.  **Complement:** The value required to reach a target sum ($\text{Target} - \text{Current}$).
4.  **Time-Space Trade-off:** The act of using more memory (Space) to make a program run faster (Time). The Hash Map is a classic example of this.

---

### ❓ 5. Follow-up Questions & Answers

**Q: If the array is already sorted, which code should I use?**
**A:** Use the **Two Pointers** code. Since sorting is already done, the $O(n \log n)$ cost disappears, and it becomes $O(n)$ time and $O(1)$ space, beating the Hash Map.

**Q: What is the "Worst Case" for the Hash Map?**
**A:** When the two target numbers are at the very end of the array. We would have to store almost every element in the dictionary before finding the match.

**Q: Can you solve this in $O(1)$ space and $O(n)$ time?**
**A:** No. To find a pair in one pass, you must either sort first (which takes $O(n \log n)$ time) or use a map (which takes $O(n)$ space). You cannot optimize both simultaneously for this problem.

***



