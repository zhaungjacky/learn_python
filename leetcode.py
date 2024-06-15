from collections import deque
from typing import List, Optional


class RecentCounter:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        max_profit = 0
        l , r = 0 , 1
        while r < len(prices):
            profit = prices[r] - prices[l] - fee- fee
            if profit <= 0:
                l = r
                
            else:
                max_profit += profit
            r += 1
        # window = {"hello": 1}

        # vvv = window.get("hello",0)

        return max_profit
                




s = RecentCounter()

res = s.maxProfit([1,3,2,8,4,9],2)
print(res)
"""
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
    def predictPartyVictory(self, senate: str) -> str:
        len_s = len(senate)

        r_arr = [i for i in range(len_s) if senate[i] == "R"]
        d_arr = [i for i in range(len_s) if senate[i] == "D"]

        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if(r < d):
                r_arr.append(len_s + r)
            else:
                d_arr.append(len_s + d)
            # print(r_arr)
            # print(d_arr)
        return  'Radiant' if r_arr else 'Dire'
    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        #first add the request to the queue and increment the counter
        self.queue.append(t)
        self.count += 1

        #return the number of request in the range
        while self.queue[0] < t -3000:
            self.queue.popleft()
            self.count -= 1

        return self.count
from cmath import inf
from typing import List


class Solution:


s = Solution()
res = s.asteroidCollision([10, 2, -5])
print(res)
 class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        #first add the request to the queue and increment the counter
        self.queue.append(t)
        self.count += 1

        #return the number of request in the range
        while self.queue[0] < t -3000:
            self.queue.popleft()
            self.count -= 1

        return self.count    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for item in asteroids:
            while stack and item < 0 < stack[-1]:
                if(-item > stack[-1]):
                    stack.pop()
                    continue
                elif -item == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(item)
        return stack

        # for i in range(len(asteroids) - 1):
        #     if asteroids[i] * asteroids[i + 1] > 0:
        #         stack.append(asteroids[i])
        #     elif abs(asteroids[i]) > abs(asteroids[i + 1]):
        #         # asteroids.pop(i + 1)
        #         if(abs(asteroids[i]))
        #         stack.append(asteroids[i])
        #     elif abs(asteroids[i]) == abs(asteroids[i + 1]):
        #         pass
        #         # asteroids.pop(i)
        #         # asteroids.pop(i + 1)
        #     else:
        #         # asteroids.pop(i)
        #         stack.append(asteroids[i + 1])
        #     print(asteroids)
        #     print(i)
        return stack
            
    def removeStars(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    pass
        return "".join(stack)
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_arr =[]
        count = 0
        for i in range(len(grid)):
            tmp_arr = []
            for j in range(len(grid)):
                tmp_arr.append(grid[j][i])
            col_arr.append(tmp_arr)
        for item in grid:
            count += col_arr.count(item)
        # print(col_arr)      
        return count      
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)
        set_diff = len(list(set1 - set2))
        if set_diff > 0:
            return False
        count_arr_1 = []
        count_arr_2 = []

        for item in set1:
            count_arr_1.append(word1.count(item))
        for item in set2:
            count_arr_2.append(word2.count(item))
        
        count_arr_1.sort()
        count_arr_2.sort()
      
        return count_arr_1 == count_arr_2
      
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniq_set= set(arr)
        count_arr = []
        for item in uniq_set:
            count_arr.append(arr.count(item))
        # print(count_arr)
        return len(set(count_arr)) == len(count_arr)
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = list(set1- set2)
        diff2 = list(set2- set1)
        return [diff1,diff2]
    def pivotIndex(self, nums: List[int]) -> int:
        right_sums = sum(nums)

        left = 0
        for i in range(len(nums)):
            right_sums -= nums[i]
            if left == right_sums:
                return i
            left += nums[i]
        return -1
    def largestAltitude(self, gain: List[int]) -> int:
        list_new=[0]
        for i in range(len(gain)):
            list_new.append(gain[i] + list_new[i])
        return max(list_new)
    def longestSubarray(self, nums: List[int]) -> int: 
        left = right =   0
        k=1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left 
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right =   0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1                
    def maxVowels(self, s: str, k: int) -> int:
        max_count = current_count = 0
        vowels = list("aeiou")
        # print(vowels)
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count
        for i in range(k,len(s)):
            if s[i] in vowels :
                current_count += 1
            if  s[i-k] in vowels:
                current_count -= 1

            max_count = max(max_count,current_count)

        return max_count
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = left = 0
        right = len(nums) - 1
        nums.sort()
        while left < right:
            if (nums[left] + nums[right])==k:
                res +=1
                left +=1
                right -=1
            elif (nums[left] + nums[right])>k:
                right -=1
            else:
                left +=1
        
        return res
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            min_height = min(height[left],height[right])
            current_area = min_height * (right - left)
            max_area = max(current_area,max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area 
    def isSubsequence(self, s: str, t: str) -> bool:
        l=r=0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r +=1
        return  l==len(s)
    def moveZeroes(self, nums: List[int]) -> None:
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left += 1
        print(nums)

    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        s = len(chars)

        while l < s:
            n = 0 # record identical number count
            r = l
            while r < s and chars[l] == chars[r]:
                if chars[l] == chars[r]:
                    n += 1
                r += 1
            # print(r,n)

            if n > 1:
                for k in range(l + 1, r):
                    chars.pop(l + 1)
                    s -= 1
                for k in range(len(str(n))):
                    l = l + 1
                    chars.insert(l, str(n)[k])
                    s += 1

            l += 1
            # r = l

        return len(chars)         
    def increasingTriplet(self, nums: List[int]) -> bool:
        first,second = inf,inf
        for third in nums:
            if second < third: return True
            if third <= first: first = third
            else: second = third

        return False
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res:List[int]=[]
        has_zeros= False
        zero_count= 0
        sum_number=1
        for item in nums:   
            if item == 0:
                has_zeros = True
                zero_count +=1
            else:
                sum_number *= item
        if has_zeros and zero_count > 1:
            res = [0  for _ in nums]
        elif has_zeros:
            res = [0 if x != 0 else sum_number for x in nums]
        else:
            res = [sum_number // x  for x in nums]
        return res

    def reverseWords(self, s: str) -> str:
        arr= s.split()
        arr_rev = arr[::-1]
        str_rev = " ".join(arr_rev)
        return str_rev
    def reverseVowels(self, s: str) -> str:

        s=list(s)
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        start=0
        end = len(s) -1
        while start < end:
            while start < end and s[start] not in vowels:
                start +=  1
            while start < end and s[end] not in vowels:
                end -=  1
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        s="".join(s)
        return s
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <=0
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         for i in range(len(flowerbed)):
#             left = i == 0 or flowerbed[i-1] == 0
#             right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
#             if left and right and flowerbed[i] == 0:
#                 flowerbed[i] = 1
#                 n -= 1
#         return n <=0

# class Solution(object):
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    #     max_num=max(candies)

    #     print(max_num)
    #     return [True if x + extraCandies >= max_num else False for x in candies]

# class Solution(object):
#     def gcdOfStrings(self, str1: str, str2: str) -> str:

#         if str1+str2 != str2+str1:
#             return ""
        
#         len1=len(str1)
#         len2=len(str2)

#         if len1 == len2:
#             return str1
        
#         if(len1 > len2):
#             return self.gcdOfStrings(str1[len(str2):],str2)
#         return self.gcdOfStrings(str1,str2[len(str1):])


# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         s=""
#         len1=len(word1)
#         len2=len(word2)
#         n=min(len1,len2)
#         for x in range(n):
#            s=s+word1[x]+word2[x]
#         if(len1 > len2):
#             s = s+ word1[n:]
#         else:
#             s = s+ word2[n:]
#         return s


# s=Solution()
# cool=s.mergeAlternately("abc","edfg")
# print(cool)

# # thislist = ["apple", "banana", "cherry"]
# # [print(x) for x in thislist]

# # print((5 < 3)^(5 > 6))



# # print(9 / 4)
# # print(9 // 4)
# # print(9 % 4)
# # print(9 ** 2)
"""
