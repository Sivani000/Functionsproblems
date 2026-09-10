# 1. Longest substring without repeating characters
def longest_unique_substring(s):
    seen = {}
    start = 0
    max_len = 0
    max_str = ""
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_str = s[start:i+1]
    return max_str

print(longest_unique_substring("abcabcbb"))  



def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  



def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string("hello"))  


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return all(v == 0 for v in count.values())

print(is_anagram("listen", "silent"))  



def first_non_repeating(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in s:
        if count[ch] == 1:
            return ch
    return None

print(first_non_repeating("swiss"))  



def move_zeros(nums):
    result = [n for n in nums if n != 0]
    result += [0] * (len(nums) - len(result))
    return result

print(move_zeros([0, 1, 0, 3, 12]))  



def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    return second

print(second_largest([10, 5, 20, 8, 20]))  



def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

print(is_palindrome(121))     
print(is_palindrome("racecar")) 



def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for n in nums:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 1]))  



def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, [5]]]))  



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0

st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.pop())   
print(st.peek())  

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  


def majority_element(nums):
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate

print(majority_element([2, 2, 1, 1, 1, 2, 2]))  



def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0

print(is_balanced("{[()]}"))  
print(is_balanced("{[(])}"))  



def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))  


def count_frequency(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq

print(count_frequency([1, 2, 2, 3, 3, 3])) 


def compress_consecutive(s):
    result = ""
    i = 0
    while i < len(s):
        ch = s[i]
        count = 0
        while i < len(s) and s[i] == ch:
            count += 1
            i += 1
        result += ch + str(count)
    return result

print(compress_consecutive('aabbaaccdd'))  # Output: a2b2a2c2d2