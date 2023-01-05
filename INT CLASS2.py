Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ord('a')
97
chr(97)
'a'
ord('c')
99
ord('A')
65
ord('Z')
90
chr(75)
'K'
ord('z')
122
ord('how')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ord('how')
TypeError: ord() expected a character, but string of length 3 found
ord("how")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ord("how")
TypeError: ord() expected a character, but string of length 3 found
str("how")
'how'
ord('H''o''w')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ord('H''o''w')
TypeError: ord() expected a character, but string of length 3 found
ord('H')
72
ord('o')
111
ord(
ord('w')

ord('w')
SyntaxError: '(' was never closed
ord('w')
119
ord('72111119')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ord('72111119')
TypeError: ord() expected a character, but string of length 8 found
bin(72)
'0b1001000'
bin(111)
'0b1101111'
ord(72)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ord(72)
TypeError: ord() expected string of length 1, but int found
chr(72)
'H'
ptint("Hello! \n How are you?")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ptint("Hello! \n How are you?")
NameError: name 'ptint' is not defined. Did you mean: 'print'?
print("Hello! \n How are you?")

Hello! 
 How are you?
>>> print("Hello!" "How are you?")
Hello!How are you?
>>> print("Hello! \nHow are you?")
Hello! 
How are you?
>>> print("Hello!\tHow are you?")
Hello!	How are you?
>>> print("Hello! \bHow are you?")
Hello! How are you?
>>> a="HELLO"
>>> b="How are you?"
>>> c=a+" "+b
>>> c
'HELLO How are you?'
>>> d=a*2
>>> d
'HELLOHELLO'
>>> 
>>> a=2
>>> b=a%2
>>> b==0
True
>>> print("entered number is even")
entered number is even
>>> a=5
>>> b=a%2
>>> b==0
False
>>> a=1
>>> b=a%1
>>> b==0
True
>>> import keyboard
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    import keyboard
ModuleNotFoundError: No module named 'keyboard'
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> print(keyword.iskeyword("alok")
