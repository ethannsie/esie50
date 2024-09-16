def sum13(nums):
  total = 0
  for i in range(len(nums)):
    if nums[i] != 13 and (i == 0 or nums[i-1] != 13):
      total += nums[i]
  return total
  
