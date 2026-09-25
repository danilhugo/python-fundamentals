#text lines#
print("This is a text line")
print("Paris rabbit has your back :) !")
print('testing single quotes')
print()

#Single quotes and special characters#
print('doesn\'t')
print("\'Yes,\' they said")
print('"Isn\'t," they said')
print()

#variable and text lines#
s = "This is a text line.\nThis is another text line."
print(s)
#directory path#
print('C:\this\name')
print(r'C:\some\name')
print()

#multiple lines , \ at end of line continues line#
print("""\
Usage: thingy [OPTIONS]\
-h
-H hostname
""")

#math and text#
print(3*'un'+'ium')
print('Py''thon')
print('Py'+'thon')
text = ('Put several strings within parentheses ' 'to have them joined together.')
print(text)
prefix = 'Py'
print(prefix + 'thon')
print()

#strinbg and positions#
word = "Daniel"
print(word[0])
print(word[5])
print(word[-1])
print(word[-5])
print()
print(word[0:2])
print(word[2:5])
print()
print(word[:2])
print(word[4:])
print(word[-3:])
print()
print("W"+word[-3:])
s2 = "This is a longer string."
print(s2)
print(len(s2))
