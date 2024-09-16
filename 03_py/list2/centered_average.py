def centered_average(nums):
  max1 = -10000
  min1 = 100000
  sum = 0
  for i in range(len(nums)):
    min1 = min(min1, nums[i])
    max1 = max(max1, nums[i])
    sum += nums[i]
  return (sum - min1 - max1)/(len(nums)-2)
  
