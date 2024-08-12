
# Based on neetcode: https://www.youtube.com/watch?v=KLlXCFG5TnA
def twoSum(nums, target):
	store = {}
	
	for n in range(len(nums)):
		d = target - nums[n]
		if (d in store and store[d] != n):
			return [store[d], n]
		else:
			store[nums[n]] = n


print(twoSum([0, 4, 3, 0], 0))