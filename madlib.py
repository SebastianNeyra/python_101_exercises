# Start with some defaults

name = ''
subject = ''
result = ''


prompt = 'Please fill in the blanks below: '
fill_in = '_____(name)____\'s favorite subject in school is _____(subject)____.'

print(prompt)
print(fill_in)

# Prompt the user for name and favorite subject
name = input('What is your name? ') 
subject = input('What is your favorite subject? ')

result = f'{name}\'s favorite subject in school is {subject}.'

# Print the madlib
print(result)