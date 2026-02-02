# Module 4: Data Structures and Algorithms

## Arrays and Strings

### Array Operations

Arrays are fundamental data structures that store elements of the same type in contiguous memory locations.

#### Searching Arrays

**Linear Search:**
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Example
numbers = [5, 3, 8, 1, 9, 2]
index = linear_search(numbers, 8)  # Returns 2
```

**Binary Search (for sorted arrays):**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example (array must be sorted)
sorted_numbers = [1, 2, 3, 5, 8, 9]
index = binary_search(sorted_numbers, 5)  # Returns 3
```

#### Sorting Arrays

**Bubble Sort:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(unsorted)  # [11, 12, 22, 25, 34, 64, 90]
```

**Selection Sort:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Insertion Sort:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

#### Array Manipulation

```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle k > n
    return arr[-k:] + arr[:-k]

def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
```

### String Manipulation

String operations are essential for text processing and manipulation.

#### Basic String Operations

```python
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
```

#### String Searching

```python
def find_substring(s, pattern):
    n, m = len(s), len(pattern)
    
    for i in range(n - m + 1):
        if s[i:i+m] == pattern:
            return i  # Return starting index
    return -1  # Pattern not found

def count_occurrences(s, pattern):
    count = start = 0
    while True:
        start = s.find(pattern, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move past this occurrence
    return count
```

#### String Transformations

```python
def remove_duplicates(s):
    result = []
    seen = set()
    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

def compress_string(s):
    if not s:
        return s
    
    compressed = []
    count = 1
    current = s[0]
    
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            compressed.append(f"{current}{count}")
            current = char
            count = 1
    
    compressed.append(f"{current}{count}")
    compressed_str = ''.join(compressed)
    
    return compressed_str if len(compressed_str) < len(s) else s
```

## Linked Lists

Linked lists are linear data structures where elements are not stored in contiguous memory locations.

### Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        current = self.head
        
        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            return  # Key not found
        
        prev.next = current.next
        current = None
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
```

### Doubly Linked List

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = DoublyNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def prepend(self, data):
        new_node = DoublyNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete(self, key):
        current = self.head
        
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                return True
            current = current.next
        
        return False
    
    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    
    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return " -> ".join(elements)
```

## Stacks and Queues

### Stack Implementation

Stacks follow Last-In-First-Out (LIFO) principle.

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Applications
def reverse_string_with_stack(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

def is_balanced_parentheses(s):
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty():
                return False
            opening = stack.pop()
            if pairs[opening] != char:
                return False
    
    return stack.is_empty()
```

### Queue Implementation

Queues follow First-In-First-Out (FIFO) principle.

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from empty queue")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Applications
from collections import deque

def hot_potato(names, num):
    queue = deque(names)
    
    while len(queue) > 1:
        for _ in range(num):
            queue.append(queue.popleft())
        queue.popleft()  # Eliminate player
    
    return queue[0]

def reverse_queue(queue):
    stack = []
    
    # Dequeue all elements and push to stack
    while not queue.is_empty():
        stack.append(queue.dequeue())
    
    # Pop from stack and enqueue back to queue
    while stack:
        queue.enqueue(stack.pop())
```

## Trees and Graphs

### Binary Trees

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)
```

### Tree Traversal Algorithms

```python
def inorder_traversal(root):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    
    traverse(root)
    return result

def preorder_traversal(root):
    result = []
    
    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
    
    traverse(root)
    return result

def postorder_traversal(root):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
    
    traverse(root)
    return result

# Iterative traversals
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result
```

### Binary Search Tree Operations

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        
        return node
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)
    
    def delete(self, val):
        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            node.val = self._min_value(node.right).val
            node.right = self._delete(node.right, node.val)
        
        return node
    
    def _min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current
```

### Graph Data Structures

```python
class Graph:
    def __init__(self, vertices=0):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}
    
    def add_edge(self, u, v, directed=False):
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)
    
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = [start]
        visited[start] = True
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        visited = [False] * self.vertices
        result = []
        
        def dfs_recursive(node):
            visited[node] = True
            result.append(node)
            
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def dfs_iterative(self, start):
        visited = [False] * self.vertices
        stack = [start]
        visited[start] = True
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node)
            
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        return result
```

## Recursion

### Recursive Problem-Solving Techniques

Recursion is a problem-solving approach where a function calls itself to solve smaller instances of the same problem.

#### Factorial

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Iterative version for comparison
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

#### Fibonacci Sequence

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Optimized version with memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
```

#### Tower of Hanoi

```python
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Example usage
# tower_of_hanoi(3, 'A', 'B', 'C')
```

### Recursive Tree Traversals

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

def invert_binary_tree(root):
    if not root:
        return None
    
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root
```

### Backtracking

```python
def generate_subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

def generate_permutations(nums):
    result = []
    
    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current, used)
                current.pop()
                used[i] = False
    
    backtrack([], [False] * len(nums))
    return result
```

## Algorithm Analysis

### Time and Space Complexity

```python
# O(1) - Constant time
def get_first_element(arr):
    return arr[0] if arr else None

# O(n) - Linear time
def find_maximum(arr):
    max_val = arr[0] if arr else None
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(log n) - Logarithmic time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Practice Exercises

### Arrays and Strings
1. Implement a function to find the maximum subarray sum (Kadane's algorithm)
2. Write a function to check if two strings are anagrams
3. Implement a function to rotate an array by k positions
4. Create a function to find the longest palindromic substring

### Linked Lists
1. Implement a function to detect a cycle in a linked list
2. Write a function to merge two sorted linked lists
3. Create a function to find the middle element of a linked list
4. Implement a function to remove duplicates from a linked list

### Stacks and Queues
1. Implement a stack using queues
2. Create a queue using two stacks
3. Implement a function to evaluate postfix expressions
4. Create a function to check if parentheses are balanced

### Trees and Graphs
1. Implement binary tree level order traversal
2. Write a function to validate a binary search tree
3. Create a function to find the lowest common ancestor
4. Implement Dijkstra's algorithm for shortest path

### Recursion
1. Solve the N-Queens problem using backtracking
2. Implement a function to generate all valid parentheses combinations
3. Create a function to solve the Sudoku puzzle
4. Write a function to find all paths in a maze

## Key Takeaways

- Arrays and strings are fundamental data structures with various manipulation techniques
- Linked lists provide dynamic memory allocation and efficient insertions/deletions
- Stacks (LIFO) and queues (FIFO) are essential for many algorithms
- Trees and graphs are hierarchical data structures with various traversal methods
- Recursion is a powerful technique for solving problems with subproblems
- Understanding time and space complexity is crucial for writing efficient algorithms
- Practice implementing these data structures to build strong programming fundamentals