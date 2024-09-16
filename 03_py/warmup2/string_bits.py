def string_bits(str):
  newString = "";
  for index in range(len(str)):
    if index%2 == 0:
      newString += str[index]
  return newString
