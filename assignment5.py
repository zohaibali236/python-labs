print("/** * Case Conversions * **/")

name_Input = input("Enter a name to convert into total Upper, Lower & title cases ")
txt = f"Name input: {name_Input} \nUpper-case: {name_Input.upper()} \nLower-case: { name_Input.lower()} \n\
Title-case: {name_Input.title()}"

print(txt)