def sum67(nums):
  total = 0
  booly = True
  for i in range(len(nums)):
    if nums[i] == 6:
      booly = False
    if booly:
      total += nums[i]
    if nums[i] == 7:
      booly = True
  return total
