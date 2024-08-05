# TIPS
# Use dict as map

def containsDuplicate(nums):
	nMap = {}
	for num in nums:
		if num in nMap:
			return True
		else:
			nMap[num] = True
	return False


print(str(containsDuplicate([1, 2, 4])));