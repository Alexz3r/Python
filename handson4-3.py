def middle_three_chars(str):
  
  if len(str) >= 3:
    return str[3:6]
  else:
    return str


user_input = input("Enter value: ")

print(middle_three_chars(user_input))
   
