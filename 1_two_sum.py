class Solution:
	def twoSum(self, nums, target):
		result = []
		for i in range(len(nums)):
			remainder = target

			if nums[i] > abs(target):
				continue
			else:
				remainder -= nums[i]
				result.append(i)
			for j in range(len(nums)):
				if i == j:
					continue
				if nums[j] == remainder:
					result.append(j)
					return result
			result.clear()


class SolutionTwo:
	def twoSum(self, nums, target):
		seen = {}

		for i, el in enumerate(nums):
			remainder = target - el
			if remainder in seen:
				return [seen[remainder], i]
			seen[el] = i


nums = [2, 5, 2, 5]
target = 10

test = Solution()
test_2 = SolutionTwo()

# print(test.twoSum(nums, target))
print(test_2.twoSum(nums, target))