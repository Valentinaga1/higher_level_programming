# 0x09. Python - Everything is object

## About this project:
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Requirements  

### Python Scripts  

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc

### .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## File Descriptions

### Mandatory

### [0-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/0-answer.txt "0-answer.txt")
What function would you use to print the type of an object?  
Write the name of the function in the file, without ().

### [1-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/1-answer.txt "1-answer.txt")
How do you get the variable identifier (which is the memory address in the CPython implementation)?  
Write the name of the function in the file, without ().

### [2-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/2-answer.txt "2-answer.txt")
In the following code, do a and b point to the same object? Answer with Yes or No
```
>>> a = 89
>>> b = 100
```
### [3-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/3-answer.txt "3-answer.txt")
In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 89
```

### [4-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/4-answer.txt "4-answer.txt")
In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a
```

### [5-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/5-answer.txt "5-answer.txt")
In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1a =
```

### [6-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/6-answer.txt "6-answer.txt")
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

### [7-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/7-answer.txt "7-answer.txt")
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

### [8-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/8-answer.txt "8-answer.txt")
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

### [9-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/9-answer.txt "9-answer.txt")
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

### [10-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/10-answer.txt "10-answer.txt")
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

### [11-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/11-answer.txt "11-answer.txt")
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

### [12-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/12-answer.txt "12-answer.txt")
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

### [13-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/13-answer.txt "13-answer.txt")
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

### [14-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/14-answer.txt "14-answer.txt")
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

### [15-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/15-answer.txt "15-answer.txt")
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

### [16-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/16-answer.txt "16-answer.txt")
What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

### [17-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/17-answer.txt "17-answer.txt")
What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

### [18-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/18-answer.txt "18-answer.txt")
What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

### [19-copy_list.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/19-copy_list.py "19-copy_list.py")
Write a function def copy_list(l): that returns a copy of a list.
- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module
```
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
```

### [20-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/20-answer.txt "20-answer.txt")
```
a = ()
```
Is a a tuple? Answer with Yes or No.

### [21-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/21-answer.txt "21-answer.txt")
```
a = (1, 2)
```
Is a a tuple? Answer with Yes or No.

### [22-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/22-answer.txt "22-answer.txt")
```
a = (1)
```
Is a a tuple? Answer with Yes or No.

### [23-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/23-answer.txt "23-answer.txt")
```
a = (1, )
```
Is a a tuple? Answer with Yes or No.

### [24-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/24-answer.txt "24-answer.txt")
What does this script print?
```
a = (1)
b = (1)
a is b
```

### [25-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/25-answer.txt "25-answer.txt")
What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

### [26-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/26-answer.txt "26-answer.txt")
What does this script print?
```
a = ()
b = ()
a is b
```

### [27-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/27-answer.txt "27-answer.txt")
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

### [28-answer.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/28-answer.txt "28-answer.txt")
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.
### 106

```
guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):  

### [106-line1.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/106-line1.txt "106-line1.txt")
How many string objects are created by the execution of the first line of the script? 

### [106-line2.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/106-line2.txt "106-line2.txt")
How many string objects are created by the execution of the second line of the script

### [106-line3.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/106-line3.txt "106-line3.txt")
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No

### [106-line4.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/106-line4.txt "106-line4.txt")
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No

### [106-line5.txt](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x09-python-everything_is_object/106-line5.txt "106-line5.txt")
How many string objects are created by the execution of the last line of the script

