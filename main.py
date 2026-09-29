# 1. Contains Duplicate
class Solution1:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


# 2. Unique Prime Factors
class Solution2:
    def primeFac(self, n: int) -> list[int]:
        factors = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.append(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors


# 3. Fizz Buzz
class Solution3:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


# 4. Container With Most Water
class Solution4:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            max_water = max(max_water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


# 5. Valid Palindrome
class Solution5:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# 6. Longest Common Prefix
class Solution6:
    def longestCommonPrefix(self, arr: list[str]) -> str:
        if not arr:
            return ""
        first_str = arr[0]
        for i in range(len(first_str)):
            char = first_str[i]
            for string in arr[1:]:
                if i == len(string) or string[i] != char:
                    return first_str[:i]
        return first_str


# 7. Convert Sentence to Camel Case
class Solution7:
    def convertToCamelCase(self, s: str) -> str:
        words = s.split()
        if not words:
            return ""
        return words[0].lower() + "".join(word.capitalize() for word in words[1:])


# 8. Longest Palindromic Substring
class Solution8:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0

        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            max_len = max(len1, len2)
            if max_len > (end - start + 1):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]


# 9. Group Anagrams
class Solution9:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())


# 10. Two Sum
class Solution10:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# 11. Top K Frequent Elements
class Solution11:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


# 12. Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        current_min = value if not self.min_stack else min(value, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# 13. Intersection of Two Arrays
class Solution13:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


# 14. Roman to Integer
class Solution14:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        return total