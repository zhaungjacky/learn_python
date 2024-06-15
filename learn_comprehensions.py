from typing import List


nums: List[int] = [1,2,3,4,5,6,7,8,9]

pow_nums = [x*x if x > 5 else x*x*x for x in nums if x % 2 != 0]

print(pow_nums)