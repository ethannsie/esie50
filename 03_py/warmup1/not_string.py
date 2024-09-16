def not_string(str):
  if str[0:3] != "not":
    str = "not " + str
  return str
