name = ('What is your name? ')
name_upper = input(name.upper())

greeting = f'Hello, {name_upper}!'
print(greeting.upper())

name_len = f'your name has {len(name_upper)} letters in it! awesome!'
upper_name_len = name_len.upper()
print(upper_name_len)