file = open('README.md', 'w')
file.write('test!')
file.close()

file = open('README.md', 'r')
print(file.read())
file.close()