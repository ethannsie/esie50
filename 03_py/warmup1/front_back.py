def front_back(str):
  if len(str) < 2:
    return str
  if len(str) == 2:
    return str[1] + str[0]
  return str[len(str)-1] + str[1:len(str)-1] + str[0]
