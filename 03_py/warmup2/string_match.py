def string_match(a, b):
  counter = 0
  for i in range(min(len(a)-1, len(b)-1)):
    if a[i:2+i] == b[i:i+2]:
      counter += 1
  return counter
