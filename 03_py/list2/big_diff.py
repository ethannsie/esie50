def big_diff(nums):
  min1 = 10000
  max1 = -10000
  for i in range(len(nums)):
    min1 = min(min1, nums[i])
    max1 = max(max1, nums[i])
  return max1 - min1
