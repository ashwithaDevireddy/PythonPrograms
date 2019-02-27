address=["flat floor street","18","new york"]
>>> print(address[0])
flat floor street
>>> print(address[1])
18
>>> print(address[2])
new york
>>> address=["flat floor street",18,"new york"]
>>> print(address[1])
18
>>> address=["flat floor street",18,new york]
  File "<stdin>", line 1
    address=["flat floor street",18,new york]
                                           ^
SyntaxError: invalid syntax
>>> address=["flat floor street",18,'new york']
>>> print(address[2])
new york
>>> hello[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> print(hello[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> 'hello'[0]
'h'
>>> print("Hello","Hi")
Hello Hi

