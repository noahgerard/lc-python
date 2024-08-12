# TIPS
# You can do list(nums) instead of nums.copy() to copy a list

# O(n^2) solution (INVALID)
""" 
def productExceptSelf(nums):
	idx = 0;
	new_nums = []
	for n in nums:
		p = 1
		copy = list(nums)
		copy.pop(idx)

		for x in copy:
			p *= x
		new_nums.append(p)
		idx += 1

	return new_nums
"""


# 1st Solution based on https://www.youtube.com/watch?v=bNvIQI2wAjk
# This one only beats 5% of submissions. Time to make it better :)
"""
def productExceptSelf(nums):
	prefix = []
	postfix = []

	for n in nums:
		if len(prefix) > 0:
			prefix.append(prefix[-1] * n)
		else:
			prefix.append(n)

	for n in nums[::-1]:
		if len(postfix) > 0:
			postfix.insert(0, postfix[0] * n)
		else:
			postfix.append(n)

	print(str(prefix))
	print(str(postfix))

	n_len = len(nums)
	for idx in range(0, n_len):
		nums[idx] = (prefix[idx - 1] if idx - 1 >= 0 else 1) * (postfix[idx + 1] if idx + 1 < n_len else 1)

	return nums
"""

# Same concept as above but, no reverse and instead using fixed array instead of dynamic array
# Exact copy of NeetCode's solution but I understand it better now
def productExceptSelf(nums):
	result = [1] * len(nums)

	prefix = 1
	for n in range(len(nums)):
		result[n] = prefix
		prefix *= nums[n]
	
	postfix = 1
	for n in range(len(nums) - 1, -1, -1):
		result[n] *= postfix
		postfix *= nums[n]

	return result

print(productExceptSelf([1, 2, 3, 4]))