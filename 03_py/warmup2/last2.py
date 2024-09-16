def last2(str):
  end = str[len(str)-2:len(str)]
  count = 0
  for i in range(len(str)-2):
    if end == str[i:i+2]:
      count += 1
  return count
