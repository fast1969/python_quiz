import random
import time

def welcome():
    print("=============")
    print(" Python Quiz")
    print("=============")

def quiz():
    # Reduced list of questions to three for testing
    questions = [
        {
            "question": "What does the built-in function 'len()' do?",
            "options": ["Returns the number of items in an object", "Returns the last element of a list", "Checks if all elements in an object are True", "Converts a value to a string"],
            "answer": "Returns the number of items in an object",
            "explanation": (
                "The 'len()' function in Python is used to determine the number of items in an object. "
                "This object can be a string, list, tuple, dictionary, or any other iterable. For example, "
                "len([1, 2, 3]) will return 3 because the list contains three elements.\n"
                "- The option 'Returns the last element of a list' is incorrect because that would require using index [-1].\n"
                "- The option 'Checks if all elements in an object are True' refers to the 'all()' function.\n"
                "- The option 'Converts a value to a string' is done by the 'str()' function."
            )
        },
        {
            "question": "Which method is used to add an element at the end of a list?",
            "options": ["insert()", "append()", "extend()", "add()"],
            "answer": "append()",
            "explanation": (
                "The 'append()' method in Python adds a single element to the end of a list. For instance, if you have a list "
                "called my_list = [1, 2, 3] and you call my_list.append(4), the list will become [1, 2, 3, 4].\n"
                "- The 'insert()' method is used to add an element at a specific index, not the end.\n"
                "- The 'extend()' method is used to add multiple elements (from another iterable) to the end of the list.\n"
                "- The 'add()' method does not exist for lists in Python; it's used with sets."
            )
        },
        {
            "question": "What does the 'type()' function return?",
            "options": ["The type of an object", "The value of an object", "The length of an object", "The memory address of an object"],
            "answer": "The type of an object",
            "explanation": (
                "The 'type()' function in Python returns the type of an object, which can help in understanding what kind of data "
                "you are working with. For example, type(42) will return <class 'int'>, indicating it's an integer.\n"
                "- 'The value of an object' is incorrect because the 'type()' function doesn't return values, only types.\n"
                "- 'The length of an object' is found using the 'len()' function.\n"
                "- 'The memory address of an object' is not directly accessible through the 'type()' function."
            )
        },
        {
    "question": "How do you create an empty list?",
    "options": ["[]", "list()", "Both [] and list()", "empty[]"],
    "answer": "Both [] and list()",
    "explanation": (
        "In Python, you can create an empty list in two ways: using empty square brackets '[]' or by calling the 'list()' function. "
        "Both methods will create an empty list that you can later populate with elements.\n"
        "- '[]' is correct but not the only way.\n"
        "- 'list()' is also correct but not the only way.\n"
        "- 'empty[]' is incorrect; it is not valid Python syntax."
    )
},
        {
    "question": "What does the 'if' statement do in Python?",
    "options": ["Runs code conditionally", "Runs code repeatedly", "Imports a module", "Creates a loop"],
    "answer": "Runs code conditionally",
    "explanation": (
        "The 'if' statement in Python is used to run a block of code only if a specified condition is true. "
        "For example, if x > 0: print('Positive') will print 'Positive' only if x is greater than 0.\n"
        "- 'Runs code repeatedly' refers to loops like 'while' or 'for'.\n"
        "- 'Imports a module' is done using the 'import' statement.\n"
        "- 'Creates a loop' is incorrect because 'if' does not create loops."
    )
},
{
    "question": "Which operator is used to check if two values are equal?",
    "options": ["=", "==", "!=", "<>"],
    "answer": "==",
    "explanation": (
        "In Python, '==' is the equality operator used to compare two values. "
        "If the values are equal, it returns True; otherwise, it returns False. "
        "For example, 3 == 3 will return True.\n"
        "- '=' is the assignment operator, not a comparison operator.\n"
        "- '!=' checks if two values are not equal.\n"
        "- '<>' is an old inequality operator, but '!=' is more commonly used."
    )
},
{
    "question": "How do you start a for loop in Python?",
    "options": ["for i in range()", "loop()", "for(){}", "while()"],
    "answer": "for i in range()",
    "explanation": (
        "In Python, 'for i in range()' is the correct syntax to start a loop that iterates over a sequence. "
        "The 'range()' function generates a sequence of numbers, and 'i' takes each value in that sequence one by one.\n"
        "- 'loop()' is not a Python keyword.\n"
        "- 'for(){}' is more common in languages like C or Java.\n"
        "- 'while()' is used to create a 'while' loop, not a 'for' loop."
    )
},
{
    "question": "How do you access the first element in a list called 'my_list'?",
    "options": ["my_list[0]", "my_list[1]", "my_list.first()", "my_list[-1]"],
    "answer": "my_list[0]",
    "explanation": (
        "In Python, list indexing starts at 0, so 'my_list[0]' accesses the first element in the list. "
        "For example, if my_list = [10, 20, 30], then my_list[0] will return 10.\n"
        "- 'my_list[1]' accesses the second element in the list.\n"
        "- 'my_list.first()' is not a valid method in Python.\n"
        "- 'my_list[-1]' accesses the last element in the list."
    )
},
{
    "question": "What is the correct syntax to define a function in Python?",
    "options": ["def function_name():", "function_name[]:", "function function_name[]:", "define function_name[]:"],
    "answer": "def function_name():",
    "explanation": (
        "In Python, you define a function using the 'def' keyword followed by the function name and parentheses. "
        "For example, 'def my_function():' defines a function called 'my_function'.\n"
        "- 'function_name[]:' is incorrect as '[]' is used for list indexing, not function definition.\n"
        "- 'function function_name[]:' is incorrect syntax and mixes up terms from other languages.\n"
        "- 'define function_name[]:' is incorrect; 'define' is not a Python keyword."
    )
},
{
    "question": "How do you add an element to a set?",
    "options": ["set.add()", "set.append()", "set.insert()", "set.push()"],
    "answer": "set.add()",
    "explanation": (
        "In Python, 'set.add()' is used to add an element to a set. A set is an unordered collection of unique elements. "
        "For example, my_set = {1, 2, 3}; my_set.add(4) will add 4 to the set.\n"
        "- 'set.append()' is incorrect because 'append()' is used with lists, not sets.\n"
        "- 'set.insert()' is also incorrect because 'insert()' is a list method, not a set method.\n"
        "- 'set.push()' is incorrect; Python does not have a 'push()' method for sets."
    )
},
{
    "question": "What does 'import' do in Python?",
    "options": ["Includes a module in your program", "Declares a variable", "Starts a loop", "Creates a list"],
    "answer": "Includes a module in your program",
    "explanation": (
        "The 'import' statement in Python is used to include a module in your program. Modules are files containing Python code, "
        "and you can use them to organize your code and reuse it in different programs. For example, 'import math' allows you to use math functions.\n"
        "- 'Declares a variable' is incorrect; variables are declared simply by assignment in Python.\n"
        "- 'Starts a loop' is incorrect; loops are started using 'for' or 'while'.\n"
        "- 'Creates a list' is incorrect; lists are created using '[]' or 'list()'."
    )
},
{
    "question": "Which of the following is a mutable data type?",
    "options": ["list", "tuple", "string", "int"],
    "answer": "list",
    "explanation": (
        "In Python, 'list' is a mutable data type, meaning you can modify the list after it is created. "
        "For example, you can change elements, add elements, or remove elements from a list.\n"
        "- 'tuple' is immutable, meaning once created, it cannot be changed.\n"
        "- 'string' is also immutable, so you cannot change individual characters in a string.\n"
        "- 'int' is a primitive data type and is immutable."
    )
},
{
    "question": "What is the correct way to check if 'x' is greater than 'y'?",
    "options": ["if x > y:", "if x => y:", "if x < y:", "if x =>= y:"],
    "answer": "if x > y:",
    "explanation": (
        "The correct way to check if 'x' is greater than 'y' in Python is to use the '>' operator. "
        "For example, 'if x > y:' will execute the block of code if x is indeed greater than y.\n"
        "- 'if x => y:' is incorrect because '=>' is not a valid Python operator.\n"
        "- 'if x < y:' checks if x is less than y, which is the opposite of what you want.\n"
        "- 'if x =>= y:' is incorrect syntax; '>=', however, checks if x is greater than or equal to y."
    )
},
{
    "question": "How do you open a file named 'example.txt' in read mode?",
    "options": ["open('example.txt', 'r')", "read('example.txt')", "openfile('example.txt')", "file('example.txt')"],
    "answer": "open('example.txt', 'r')",
    "explanation": (
        "To open a file in read mode in Python, you use 'open('example.txt', 'r')'. The 'r' stands for read mode. "
        "Once the file is open, you can use methods like 'read()' to read its contents.\n"
        "- 'read('example.txt')' is incorrect; 'read()' is used after the file is opened.\n"
        "- 'openfile('example.txt')' is incorrect because there is no such function in Python.\n"
        "- 'file('example.txt')' is also incorrect as it does not open files; 'open()' is the correct function."
    )
},
{
    "question": "What does 'len()' function return when applied to a string?",
    "options": ["The number of characters in the string", "The last character in the string", "The first character in the string", "The type of the string"],
    "answer": "The number of characters in the string",
    "explanation": (
        "The 'len()' function in Python returns the number of characters in a string. "
        "For example, len('Hello') will return 5 because there are 5 characters in the string 'Hello'.\n"
        "- 'The last character in the string' is incorrect; you would use indexing like 'my_string[-1]' to get the last character.\n"
        "- 'The first character in the string' is incorrect; you would use indexing like 'my_string[0]' for the first character.\n"
        "- 'The type of the string' is incorrect; to get the type, you would use 'type(my_string)'."
    )
},
{
    "question": "Which method would you use to convert a string to lowercase?",
    "options": ["str.lower()", "str.lowercase()", "str.downcase()", "str.lowerc()"],
    "answer": "str.lower()",
    "explanation": (
        "The 'str.lower()' method in Python converts all characters in a string to lowercase. "
        "For example, 'Hello'.lower() will return 'hello'.\n"
        "- 'str.lowercase()' is incorrect because there is no such method in Python.\n"
        "- 'str.downcase()' is also incorrect; 'downcase' is not a valid method in Python.\n"
        "- 'str.lowerc()' is not a valid method either."
    )
},
{
    "question": "How do you concatenate two strings 'a' and 'b'?",
    "options": ["a + b", "a & b", "a | b", "a * b"],
    "answer": "a + b",
    "explanation": (
        "In Python, you concatenate two strings using the '+' operator. "
        "For example, if a = 'Hello' and b = 'World', then a + b will return 'HelloWorld'.\n"
        "- 'a & b' and 'a | b' are bitwise operators, not used for string concatenation.\n"
        "- 'a * b' is incorrect; '*' is used for repeating strings, not concatenating."
    )
},
{
    "question": "Which of these is used to handle exceptions in Python?",
    "options": ["try/except", "catch/try", "handle/error", "do/try"],
    "answer": "try/except",
    "explanation": (
        "In Python, the 'try/except' block is used to handle exceptions. You put the code that might raise an exception in the 'try' block "
        "and the code to handle the exception in the 'except' block.\n"
        "- 'catch/try' is incorrect; 'catch' is used in other languages like Java, but not in Python.\n"
        "- 'handle/error' is incorrect; this syntax does not exist in Python.\n"
        "- 'do/try' is also incorrect; it mixes syntax from different languages."
    )
},
{
    "question": "How do you remove an element from a list?",
    "options": ["list.remove()", "list.delete()", "list.pop()", "list.clear()"],
    "answer": "list.remove()",
    "explanation": (
        "In Python, 'list.remove(x)' removes the first occurrence of element 'x' from the list. "
        "For example, my_list.remove(3) will remove the first occurrence of 3 from my_list.\n"
        "- 'list.delete()' is incorrect; there is no 'delete()' method in Python.\n"
        "- 'list.pop()' removes an element by index, not by value, and returns it.\n"
        "- 'list.clear()' removes all elements from the list."
    )
},
{
    "question": "What is the keyword used to define a class in Python?",
    "options": ["class", "def", "struct", "define"],
    "answer": "class",
    "explanation": (
        "In Python, the 'class' keyword is used to define a new class. "
        "For example, 'class MyClass:' defines a new class named MyClass.\n"
        "- 'def' is used to define a function, not a class.\n"
        "- 'struct' is used in languages like C for defining structures, not in Python.\n"
        "- 'define' is not a keyword in Python."
    )
},
{
    "question": "What does the 'return' statement do in a function?",
    "options": ["Exits the function and optionally passes back a value", "Continues the function", "Ends the program", "Starts a loop"],
    "answer": "Exits the function and optionally passes back a value",
    "explanation": (
        "In Python, the 'return' statement is used to exit a function and optionally return a value to the caller. "
        "For example, 'return x + y' exits the function and returns the sum of x and y.\n"
        "- 'Continues the function' is incorrect; 'return' exits the function.\n"
        "- 'Ends the program' is incorrect; 'return' only exits the function, not the entire program.\n"
        "- 'Starts a loop' is incorrect; loops are started with 'for' or 'while', not 'return'."
    )
},
{
    "question": "Which operator is used for exponentiation in Python?",
    "options": ["**", "^", "//", "*"],
    "answer": "**",
    "explanation": (
        "In Python, '**' is the exponentiation operator. For example, 2 ** 3 returns 8, which is 2 raised to the power of 3.\n"
        "- '^' is a bitwise XOR operator, not used for exponentiation.\n"
        "- '//' is the floor division operator, not exponentiation.\n"
        "- '*' is the multiplication operator, not exponentiation."
    )
},
{
    "question": "How do you comment a line in Python?",
    "options": ["# Comment", "// Comment", "/* Comment */", "-- Comment"],
    "answer": "# Comment",
    "explanation": (
        "In Python, you comment a line by placing a '#' symbol at the beginning of the line. "
        "For example, '# This is a comment' is a valid comment.\n"
        "- '// Comment' is used in languages like C++ and Java, but not in Python.\n"
        "- '/* Comment */' is used for block comments in C-style languages.\n"
        "- '-- Comment' is used in SQL, not Python."
    )
},
{
    "question": "How do you get the number of elements in a list 'my_list'?",
    "options": ["len(my_list)", "my_list.length()", "my_list.size()", "size(my_list)"],
    "answer": "len(my_list)",
    "explanation": (
        "In Python, the 'len()' function is used to get the number of elements in a list. "
        "For example, len([1, 2, 3]) returns 3 because the list has three elements.\n"
        "- 'my_list.length()' is incorrect; 'length()' is not a method in Python.\n"
        "- 'my_list.size()' is also incorrect; 'size()' is not a method in Python.\n"
        "- 'size(my_list)' is incorrect; 'len()' is the correct function to use."
    )
},
{
    "question": "What will '4 % 2' return?",
    "options": ["0", "2", "1", "4"],
    "answer": "0",
    "explanation": (
        "In Python, the '%' operator is the modulus operator, which returns the remainder of a division. "
        "For example, 4 % 2 equals 0 because 4 is evenly divisible by 2 with no remainder.\n"
        "- '2' is incorrect; it would be the quotient, not the remainder.\n"
        "- '1' is incorrect; this would be the remainder if 4 were divided by 3, not 2.\n"
        "- '4' is incorrect; it's the dividend, not the remainder."
    )
},
{
    "question": "How do you create an infinite loop in Python?",
    "options": ["while True:", "while 1 == 1:", "for i in range(1,10):", "if True:"],
    "answer": "while True:",
    "explanation": (
        "An infinite loop in Python is commonly created using 'while True:'. The loop will continue to run indefinitely because the condition 'True' is always met.\n"
        "- 'while 1 == 1:' is also a valid infinite loop, as '1 == 1' always evaluates to True.\n"
        "- 'for i in range(1,10):' is not infinite; it loops a specific number of times (from 1 to 9).\n"
        "- 'if True:' is a conditional statement, not a loop."
    )
},
{
    "question": "Which function can be used to get user input in Python?",
    "options": ["input()", "get()", "read()", "scan()"],
    "answer": "input()",
    "explanation": (
        "The 'input()' function is used to get user input from the console in Python. The input is always returned as a string.\n"
        "- 'get()' is incorrect; it is a method typically used with dictionaries to get a value by key.\n"
        "- 'read()' is incorrect; it is used to read content from a file.\n"
        "- 'scan()' is incorrect; Python does not have a built-in 'scan()' function."
    )
},
{
    "question": "How do you check if a key exists in a dictionary?",
    "options": ["key in dict", "key of dict", "key.exists(dict)", "dict.has(key)"],
    "answer": "key in dict",
    "explanation": (
        "To check if a key exists in a dictionary in Python, you use the 'in' keyword. For example, 'if key in my_dict:' checks if 'key' exists in 'my_dict'.\n"
        "- 'key of dict' is incorrect; there is no such syntax in Python.\n"
        "- 'key.exists(dict)' is incorrect; there is no 'exists()' method for this purpose.\n"
        "- 'dict.has(key)' is incorrect; Python dictionaries do not have a 'has()' method."
    )
},
{
    "question": "Which built-in Python function is used to sort a list?",
    "options": ["sorted()", "order()", "sort()", "arrange()"],
    "answer": "sorted()",
    "explanation": (
        "The 'sorted()' function in Python returns a new list containing all items from the iterable in ascending order. It does not modify the original list.\n"
        "- 'order()' is incorrect; it is not a Python function.\n"
        "- 'sort()' is a method of list objects that sorts the list in place, but 'sorted()' is the built-in function.\n"
        "- 'arrange()' is incorrect; it is not a Python function."
    )
},
{
    "question": "What is the output of 'print(10//3)'?",
    "options": ["3", "3.33", "4", "0"],
    "answer": "3",
    "explanation": (
        "The '//' operator in Python performs floor division, which divides two numbers and rounds down to the nearest integer. So, '10 // 3' equals 3.\n"
        "- '3.33' would be the result of true division (using '/') and is incorrect for floor division.\n"
        "- '4' is incorrect; 10 divided by 3 is not rounded up to 4 in floor division.\n"
        "- '0' is incorrect because 10 is not less than 3."
    )
},
{
    "question": "Which keyword is used to create a loop that iterates a fixed number of times?",
    "options": ["for", "while", "loop", "repeat"],
    "answer": "for",
    "explanation": (
        "The 'for' keyword in Python is used to create a loop that iterates over a sequence (like a list, tuple, or range) a fixed number of times. "
        "For example, 'for i in range(5):' will loop five times, with 'i' taking values from 0 to 4.\n"
        "- 'while' is used for loops that continue until a condition is met.\n"
        "- 'loop' is not a valid Python keyword.\n"
        "- 'repeat' is not a valid Python keyword for creating loops."
    )
},
{
    "question": "What does 'break' do in a loop?",
    "options": ["Exits the loop immediately", "Skips the next iteration", "Continues to the next iteration", "Restarts the loop"],
    "answer": "Exits the loop immediately",
    "explanation": (
        "The 'break' statement in Python is used to exit a loop immediately, regardless of the loop's condition. "
        "For example, in a 'for' or 'while' loop, 'break' will stop the loop entirely and move to the next line of code outside the loop.\n"
        "- 'Skips the next iteration' is incorrect; this describes the 'continue' statement.\n"
        "- 'Continues to the next iteration' is incorrect; this also describes the 'continue' statement.\n"
        "- 'Restarts the loop' is incorrect; 'break' does not restart loops."
    )
},
{
    "question": "How do you create a new Python virtual environment?",
    "options": ["python -m venv myenv", "python createenv myenv", "venv create myenv", "virtualenv create myenv"],
    "answer": "python -m venv myenv",
    "explanation": (
        "To create a new Python virtual environment, you use the command 'python -m venv myenv'. This creates a directory named 'myenv' "
        "that contains a separate Python environment, isolating your project's dependencies from the system's Python installation.\n"
        "- 'python createenv myenv' is incorrect; there is no such command in Python.\n"
        "- 'venv create myenv' is incorrect; 'venv' is a module, not a standalone command.\n"
        "- 'virtualenv create myenv' is incorrect syntax; while 'virtualenv' is an older tool, the correct command would be 'virtualenv myenv'."
    )
},
{
    "question": "Which of the following statements will correctly print 'Hello World' to the console?",
    "options": ["print('Hello World')", "echo('Hello World')", "display('Hello World')", "console.log('Hello World')"],
    "answer": "print('Hello World')",
    "explanation": (
        "The 'print()' function in Python is used to output text or other information to the console. "
        "For example, 'print('Hello World')' will display 'Hello World' in the console.\n"
        "- 'echo('Hello World')' is incorrect; 'echo' is a command in bash, not Python.\n"
        "- 'display('Hello World')' is incorrect; 'display' is not a Python function.\n"
        "- 'console.log('Hello World')' is incorrect; 'console.log' is used in JavaScript, not Python."
    )
},
{
    "question": "What does 'str.strip()' do?",
    "options": ["Removes leading and trailing whitespace from the string", "Removes all whitespace from the string", "Converts the string to lowercase", "Removes leading whitespace only"],
    "answer": "Removes leading and trailing whitespace from the string",
    "explanation": (
        "The 'str.strip()' method in Python removes any leading (spaces at the beginning) and trailing (spaces at the end) whitespace characters from a string. "
        "For example, '  Hello World  '.strip() will return 'Hello World'.\n"
        "- 'Removes all whitespace from the string' is incorrect; 'strip()' does not remove whitespace in the middle of the string.\n"
        "- 'Converts the string to lowercase' is incorrect; this is done using 'str.lower()'.\n"
        "- 'Removes leading whitespace only' is incorrect; 'strip()' removes both leading and trailing whitespace."
    )
},
{
    "question": "How do you reverse a string 'my_string'?",
    "options": ["my_string[::-1]", "reverse(my_string)", "my_string.reverse()", "str.reverse(my_string)"],
    "answer": "my_string[::-1]",
    "explanation": (
        "To reverse a string in Python, you can use slicing with 'my_string[::-1]'. This slicing technique reverses the string by stepping backwards through the string.\n"
        "- 'reverse(my_string)' is incorrect; 'reverse()' is not a built-in function for strings in Python.\n"
        "- 'my_string.reverse()' is incorrect; 'reverse()' is a method for lists, not strings.\n"
        "- 'str.reverse(my_string)' is incorrect; there is no 'reverse()' method in the 'str' class."
    )
},
{
    "question": "What will '2 == 2' return?",
    "options": ["True", "False", "None", "2"],
    "answer": "True",
    "explanation": (
        "In Python, '==' is the equality operator, which compares two values. If the values are equal, it returns 'True'. "
        "So, '2 == 2' will return 'True' because 2 is equal to 2.\n"
        "- 'False' is incorrect; '2 == 2' is true, not false.\n"
        "- 'None' is incorrect; '==' returns a boolean value, not 'None'.\n"
        "- '2' is incorrect; the expression evaluates to a boolean, not a number."
    )
},
{
    "question": "How do you raise an exception in Python?",
    "options": ["raise Exception('Error message')", "throw Exception('Error message')", "error('Error message')", "raise('Error message')"],
    "answer": "raise Exception('Error message')",
    "explanation": (
        "In Python, you use the 'raise' keyword to raise an exception manually. You can specify the type of exception (like 'Exception') "
        "and provide an error message. For example, 'raise Exception('Error message')' will raise a generic exception with the message 'Error message'.\n"
        "- 'throw Exception('Error message')' is incorrect; 'throw' is used in languages like Java, not Python.\n"
        "- 'error('Error message')' is incorrect; 'error()' is not a function in Python.\n"
        "- 'raise('Error message')' is incorrect; you need to specify the exception type, such as 'Exception'."
    )
},
{
    "question": "How do you iterate through a dictionary's keys and values?",
    "options": ["for key, value in dict.items()", "for key, value in dict.keys()", "for key in dict.items()", "for value in dict.values()"],
    "answer": "for key, value in dict.items()",
    "explanation": (
        "In Python, you can iterate through a dictionary's keys and values using the 'items()' method, which returns key-value pairs. "
        "For example, 'for key, value in dict.items():' allows you to access both the keys and values in each iteration.\n"
        "- 'for key, value in dict.keys()' is incorrect; 'keys()' returns only the keys, not values.\n"
        "- 'for key in dict.items()' is incorrect; 'items()' returns key-value pairs, not just keys.\n"
        "- 'for value in dict.values()' is incorrect; 'values()' returns only the values, not the keys."
    )
},
{
    "question": "How do you check if a list 'my_list' is empty?",
    "options": ["if not my_list:", "if my_list is empty:", "if empty(my_list):", "if len(my_list) == None:"],
    "answer": "if not my_list:",
        "explanation": (
        "In Python, you can check if a list is empty by using 'if not my_list:'. An empty list is considered False in a boolean context, "
        "so 'not my_list' will be True if the list is empty.\n"
        "- 'if my_list is empty:' is incorrect; 'is empty' is not a valid Python syntax.\n"
        "- 'if empty(my_list):' is incorrect; 'empty()' is not a Python function.\n"
        "- 'if len(my_list) == None:' is incorrect; 'len(my_list)' would return 0 for an empty list, not 'None'."
    )
},
{
    "question": "Which method would you use to remove the first occurrence of an element in a list?",
    "options": ["list.remove()", "list.pop(0)", "list.delete(0)", "list.pop_first()"],
    "answer": "list.remove()",
    "explanation": (
        "The 'list.remove()' method in Python removes the first occurrence of a specified element from the list. "
        "For example, if you have a list [1, 2, 3, 2], and you call list.remove(2), the first '2' will be removed, resulting in [1, 3, 2].\n"
        "- 'list.pop(0)' removes and returns the element at index 0, not by value.\n"
        "- 'list.delete(0)' is incorrect; 'delete()' is not a method in Python.\n"
        "- 'list.pop_first()' is incorrect; 'pop_first()' is not a method in Python."
    )
},
{
    "question": "How do you create a tuple with one element?",
    "options": ["(element,)", "(element)", "[element]", "{element}"],
    "answer": "(element,)",
    "explanation": (
        "To create a tuple with a single element in Python, you need to include a comma after the element inside the parentheses. "
        "For example, '(element,)' creates a tuple with one element. Without the comma, it would be interpreted as just a value in parentheses, not a tuple.\n"
        "- '(element)' is incorrect; it creates a value in parentheses, not a tuple.\n"
        "- '[element]' creates a list, not a tuple.\n"
        "- '{element}' creates a set, not a tuple."
    )
},
{
    "question": "Which of the following is a built-in function in Python?",
    "options": ["len()", "print()", "type()", "All of the above"],
    "answer": "All of the above",
    "explanation": (
        "In Python, 'len()', 'print()', and 'type()' are all built-in functions:\n"
        "- 'len()' returns the number of items in an object.\n"
        "- 'print()' outputs text to the console.\n"
        "- 'type()' returns the type of an object.\n"
        "Therefore, the correct answer is 'All of the above'."
    )
},
{
    "question": "How do you append multiple elements to a list at once?",
    "options": ["list.extend([element1, element2])", "list.append([element1, element2])", "list.add([element1, element2])", "list.merge([element1, element2])"],
    "answer": "list.extend([element1, element2])",
    "explanation": (
        "The 'list.extend()' method in Python allows you to append multiple elements from an iterable (such as a list) to the end of another list. "
        "For example, 'my_list.extend([element1, element2])' adds both elements to 'my_list'.\n"
        "- 'list.append([element1, element2])' would add the entire list [element1, element2] as a single element, not as separate elements.\n"
        "- 'list.add([element1, element2])' is incorrect; 'add()' is a method used for sets, not lists.\n"
        "- 'list.merge([element1, element2])' is incorrect; 'merge()' is not a Python method."
    )
},
{
    "question": "What does 'continue' do in a loop?",
    "options": ["Skips the current iteration and continues with the next", "Exits the loop immediately", "Restarts the loop", "Skips all remaining iterations"],
    "answer": "Skips the current iteration and continues with the next",
    "explanation": (
        "The 'continue' statement in Python is used to skip the rest of the code inside the loop for the current iteration and move on to the next iteration. "
        "It does not stop the loop entirely, just the current cycle.\n"
        "- 'Exits the loop immediately' describes the 'break' statement, not 'continue'.\n"
        "- 'Restarts the loop' is incorrect; 'continue' does not restart the loop, it just skips to the next iteration.\n"
        "- 'Skips all remaining iterations' is incorrect; 'continue' only skips the current iteration, not all."
    )
},
{
    "question": "How do you sort a list 'my_list' in reverse order?",
    "options": ["sorted(my_list, reverse=True)", "my_list.sort(reverse=True)", "Both sorted(my_list, reverse=True) and my_list.sort(reverse=True)", "sort(my_list, descending=True)"],
    "answer": "Both sorted(my_list, reverse=True) and my_list.sort(reverse=True)",
    "explanation": (
        "In Python, there are two ways to sort a list in reverse order:\n"
        "- 'sorted(my_list, reverse=True)' returns a new list that is sorted in reverse order, leaving the original list unchanged.\n"
        "- 'my_list.sort(reverse=True)' sorts the original list in place in reverse order.\n"
        "Both methods are correct for sorting a list in reverse order.\n"
        "- 'sort(my_list, descending=True)' is incorrect; 'descending=True' is not a valid parameter in Python."
    )
},
{
    "question": "How do you handle an unknown number of arguments in a function?",
    "options": ["Using *args", "Using **kwargs", "Both *args and **kwargs", "Using default arguments"],
    "answer": "Both *args and **kwargs",
    "explanation": (
        "In Python, '*args' is used to pass a variable number of non-keyword arguments to a function, while '**kwargs' is used to pass a variable number of keyword arguments. "
        "Both can be used together to handle an unknown number of arguments in a function.\n"
        "- '*args' alone handles non-keyword arguments.\n"
        "- '**kwargs' alone handles keyword arguments.\n"
        "- 'Using default arguments' is incorrect; default arguments are used for optional parameters, not an unknown number of parameters."
    )
},
{
    "question": "How do you read the contents of a file named 'data.txt'?",
    "options": ["with open('data.txt', 'r') as file: content = file.read()", "file.read('data.txt')", "read('data.txt')", "file('data.txt').read()"],
    "answer": "with open('data.txt', 'r') as file: content = file.read()",
    "explanation": (
        "To read the contents of a file in Python, you typically use a 'with' statement to open the file, ensuring that it is properly closed after reading. "
        "The correct syntax is 'with open('data.txt', 'r') as file: content = file.read()'. This opens the file in read mode ('r'), reads its content, "
        "and stores it in the variable 'content'.\n"
        "- 'file.read('data.txt')' is incorrect; 'file.read()' reads from an already opened file, not by passing a filename directly.\n"
        "- 'read('data.txt')' is incorrect; 'read()' is not a standalone function for reading files.\n"
        "- 'file('data.txt').read()' is incorrect; 'file()' is not a function in Python."
    )
},
{
    "question": "Which method is used to add a key-value pair to a dictionary?",
    "options": ["dict[key] = value", "dict.add(key, value)", "dict.insert(key, value)", "dict.push(key, value)"],
    "answer": "dict[key] = value",
    "explanation": (
        "In Python, you add a key-value pair to a dictionary by assigning a value to a key using the syntax 'dict[key] = value'. "
        "If the key already exists, its value is updated; if not, a new key-value pair is created.\n"
        "- 'dict.add(key, value)' is incorrect; there is no 'add()' method for dictionaries in Python.\n"
        "- 'dict.insert(key, value)' is incorrect; dictionaries do not have an 'insert()' method.\n"
        "- 'dict.push(key, value)' is incorrect; 'push()' is not a method for dictionaries."
    )
},
{
    "question": "What is a correct way to define a class named 'Dog'?",
    "options": ["class Dog:", "define Dog:", "Dog class:", "class(Dog):"],
    "answer": "class Dog:",
    "explanation": (
        "In Python, you define a class using the 'class' keyword followed by the class name and a colon. "
        "For example, 'class Dog:' correctly defines a class named 'Dog'.\n"
        "- 'define Dog:' is incorrect; 'define' is not a keyword in Python.\n"
        "- 'Dog class:' is incorrect; the class name should follow the 'class' keyword, not precede it.\n"
        "- 'class(Dog):' is incorrect; this syntax is used for inheritance, not for defining a class."
    )
},
{
    "question": "How do you catch multiple exceptions in Python?",
    "options": ["except (TypeError, ValueError):", "except TypeError or ValueError:", "except [TypeError, ValueError]:", "except TypeError, ValueError:"],
    "answer": "except (TypeError, ValueError):",
    "explanation": (
        "In Python, you can catch multiple exceptions by specifying them as a tuple in an 'except' block. "
        "The correct syntax is 'except (TypeError, ValueError):', which will catch both 'TypeError' and 'ValueError' exceptions.\n"
        "- 'except TypeError or ValueError:' is incorrect; 'or' cannot be used in this context.\n"
        "- 'except [TypeError, ValueError]:' is incorrect; exceptions must be specified as a tuple, not a list.\n"
        "- 'except TypeError, ValueError:' is incorrect; this syntax was valid in older versions of Python, but it is not recommended."
    )
},
{
    "question": "How do you create a list of squares from 0 to 9?",
    "options": ["[i**2 for i in range(10)]", "squares([0-9])", "[0..9]**2", "range(10).squares()"],
    "answer": "[i**2 for i in range(10)]",
    "explanation": (
        "List comprehensions provide a concise way to create lists in Python. The correct syntax to create a list of squares from 0 to 9 is "
        "'[i**2 for i in range(10)]'. This expression iterates over the numbers 0 through 9, squares each one, and collects the results in a list.\n"
        "- 'squares([0-9])' is incorrect; this syntax is not valid in Python.\n"
        "- '[0..9]**2' is incorrect; '..' is not valid syntax in Python.\n"
        "- 'range(10).squares()' is incorrect; 'range()' does not have a 'squares()' method."
    )
},
{
    "question": "What will be the result of 'my_dict.get('key', 'default')' if 'key' is not present?",
    "options": ["'default'", "None", "KeyError", "False"],
    "answer": "'default'",
    "explanation": (
        "The 'get()' method of a dictionary in Python returns the value of the specified key if it exists. "
        "If the key does not exist, it returns the specified default value. So, 'my_dict.get('key', 'default')' will return 'default' "
        "if 'key' is not present in 'my_dict'.\n"
        "- 'None' is incorrect; 'None' would be returned if no default value were specified.\n"
        "- 'KeyError' is incorrect; 'KeyError' would be raised if you accessed a non-existent key directly (e.g., 'my_dict['key']').\n"
        "- 'False' is incorrect; 'False' is not the specified default value in this context."
    )
},
{
    "question": "How do you sort a list of tuples based on the second element?",
    "options": ["sorted(list_of_tuples, key=lambda x: x[1])", "list_of_tuples.sort_by_second()", "sort(list_of_tuples, by=second)", "list_of_tuples.sort(key=2)"],
    "answer": "sorted(list_of_tuples, key=lambda x: x[1])",
    "explanation": (
        "To sort a list of tuples based on the second element, you can use the 'sorted()' function with a 'key' argument that specifies a lambda function. "
        "The lambda function 'lambda x: x[1]' extracts the second element of each tuple (index 1) for comparison. This approach returns a new sorted list.\n"
        "- 'list_of_tuples.sort_by_second()' is incorrect; there is no 'sort_by_second()' method in Python.\n"
        "- 'sort(list_of_tuples, by=second)' is incorrect; this is not valid Python syntax for sorting.\n"
        "- 'list_of_tuples.sort(key=2)' is incorrect; 'key' expects a function, not an index."
    )
},
{
    "question": "How do you remove duplicates from a list?",
    "options": ["list(set(my_list))", "my_list.remove_duplicates()", "my_list = unique(my_list)", "my_list = list(my_list.unique())"],
    "answer": "list(set(my_list))",
    "explanation": (
        "To remove duplicates from a list in Python, you can convert the list to a set (which automatically removes duplicates) and then convert it back to a list. "
        "This is done using 'list(set(my_list))'.\n"
        "- 'my_list.remove_duplicates()' is incorrect; there is no 'remove_duplicates()' method in Python.\n"
        "- 'my_list = unique(my_list)' is incorrect; 'unique()' is not a built-in function in Python.\n"
        "- 'my_list = list(my_list.unique())' is incorrect; 'unique()' is not a method available for lists."
    )
},
{
    "question": "What is the output of '2 ** 3 ** 2' in Python?",
    "options": ["512", "64", "256", "8"],
    "answer": "512",
    "explanation": (
        "In Python, the '**' operator is used for exponentiation, and it is right-associative. This means '2 ** 3 ** 2' is evaluated as '2 ** (3 ** 2)', "
        "which is '2 ** 9'. Since 2 raised to the power of 9 is 512, the correct answer is 512.\n"
        "- '64' is incorrect; it would be the result of '8 ** 2'.\n"
        "- '256' is incorrect; it would be the result of '2 ** 8'.\n"
        "- '8' is incorrect; it would be the result of '2 ** 3'."
    )
},
{
    "question": "What does 'finally' do in a try-except block?",
    "options": ["Executes code after the try and except blocks, regardless of exceptions", "Only executes if an exception is raised", "Terminates the program", "Executes before the try block"],
    "answer": "Executes code after the try and except blocks, regardless of exceptions",
    "explanation": (
        "In Python, the 'finally' block is used to execute code after the 'try' and 'except' blocks, no matter what happens in the preceding blocks. "
        "This is useful for cleanup tasks, such as closing files or releasing resources.\n"
        "- 'Only executes if an exception is raised' is incorrect; the 'finally' block runs whether or not an exception is raised.\n"
        "- 'Terminates the program' is incorrect; 'finally' does not terminate the program; it ensures the block of code is executed.\n"
        "- 'Executes before the try block' is incorrect; 'finally' executes after 'try' and 'except'."
    )
},
{
    "question": "Which of the following is the correct way to create an empty set?",
    "options": ["set()", "{}", "[]", "set([])"],
    "answer": "set()",
    "explanation": (
        "In Python, the correct way to create an empty set is by using 'set()'. "
        "Using '{}' would create an empty dictionary, not a set. '[]' creates an empty list, and 'set([])' creates an empty set but is less direct.\n"
        "- '{}' is incorrect because it creates an empty dictionary, not a set.\n"
        "- '[]' is incorrect because it creates an empty list, not a set.\n"
        "- 'set([])' is valid but less direct than simply using 'set()' to create an empty set."
    )
},
{
    "question": "What is a lambda function?",
    "options": ["An anonymous function expressed as a single statement", "A function with no arguments", "A function that does not return a value", "A function used only in lists"],
    "answer": "An anonymous function expressed as a single statement",
    "explanation": (
        "A lambda function in Python is a small anonymous function that is defined using the 'lambda' keyword. "
        "It can take any number of arguments but only has one expression. The expression is evaluated and returned. "
        "For example, 'lambda x: x + 1' is a lambda function that adds 1 to its argument.\n"
        "- 'A function with no arguments' is incorrect; lambda functions can have arguments.\n"
        "- 'A function that does not return a value' is incorrect; lambda functions return the result of the expression.\n"
        "- 'A function used only in lists' is incorrect; lambda functions can be used anywhere a function is needed, not just in lists."
    )
},
{
    "question": "How do you capitalize the first letter of a string?",
    "options": ["str.capitalize()", "str.upper()", "str.capitalize_first()", "str.cap()"],
    "answer": "str.capitalize()",
    "explanation": (
        "The 'str.capitalize()' method in Python returns a copy of the string with the first character capitalized and the rest of the string in lowercase. "
        "For example, 'hello'.capitalize() returns 'Hello'.\n"
        "- 'str.upper()' converts all characters in the string to uppercase, not just the first letter.\n"
        "- 'str.capitalize_first()' is incorrect; this is not a valid Python method.\n"
        "- 'str.cap()' is incorrect; this is not a valid Python method."
    )
},
{
    "question": "How do you convert a string '123' to an integer?",
    "options": ["int('123')", "convert('123')", "to_int('123')", "str.to_int()"],
    "answer": "int('123')",
    "explanation": (
        "In Python, you convert a string to an integer using the 'int()' function. "
        "For example, 'int('123')' converts the string '123' to the integer 123.\n"
        "- 'convert('123')' is incorrect; 'convert()' is not a built-in Python function.\n"
        "- 'to_int('123')' is incorrect; 'to_int()' is not a built-in Python function.\n"
        "- 'str.to_int()' is incorrect; there is no 'to_int()' method for strings."
    )
},
{
    "question": "How do you reverse a list 'my_list'?",
    "options": ["my_list[::-1]", "reverse(my_list)", "my_list.reverse()", "reversed(my_list)"],
    "answer": "my_list[::-1]",
    "explanation": (
        "In Python, the most common way to reverse a list is by using slicing. 'my_list[::-1]' creates a new list that is the reverse of 'my_list'. "
        "This is a concise and efficient way to reverse a list.\n"
        "- 'reverse(my_list)' is incorrect; 'reverse()' is not a standalone function, but a method of list objects.\n"
        "- 'my_list.reverse()' reverses the list in place, but does not return a new list, which is different from the slicing method.\n"
        "- 'reversed(my_list)' returns an iterator that can be converted into a list, but 'my_list[::-1]' is more commonly used for this purpose."
    )
},
{
    "question": "Which method removes and returns the last item in a list?",
    "options": ["list.pop()", "list.remove()", "list.delete()", "list.drop()"],
    "answer": "list.pop()",
    "explanation": (
        "The 'list.pop()' method in Python removes and returns the last item in the list. If you specify an index, it will remove and return the item at that index. "
        "For example, if 'my_list = [1, 2, 3]', then 'my_list.pop()' will return 3 and 'my_list' will become [1, 2].\n"
        "- 'list.remove()' removes the first occurrence of a specified value but does not return it.\n"
        "- 'list.delete()' is incorrect; there is no 'delete()' method in Python.\n"
        "- 'list.drop()' is incorrect; there is no 'drop()' method in Python."
    )
},
{
    "question": "What does the 'pass' keyword do in Python?",
    "options": ["It does nothing and is used as a placeholder", "It exits the loop", "It returns a value", "It raises an exception"],
    "answer": "It does nothing and is used as a placeholder",
    "explanation": (
        "The 'pass' keyword in Python does nothing and is used as a placeholder in code. It is often used in situations where you need a statement syntactically but don't want to execute any code. "
        "For example, you might use 'pass' inside a loop or function that you haven't implemented yet.\n"
        "- 'It exits the loop' is incorrect; to exit a loop, you would use the 'break' statement.\n"
        "- 'It returns a value' is incorrect; 'return' is used to return values from functions.\n"
        "- 'It raises an exception' is incorrect; exceptions are raised using the 'raise' statement."
    )
},
{
    "question": "Which method is used to update a dictionary with another dictionary?",
    "options": ["dict.update()", "dict.add()", "dict.append()", "dict.merge()"],
    "answer": "dict.update()",
    "explanation": (
        "The 'dict.update()' method in Python is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs. "
        "If a key already exists, its value is updated; if it doesn't exist, the key-value pair is added to the dictionary.\n"
        "- 'dict.add()' is incorrect; there is no 'add()' method for dictionaries in Python.\n"
        "- 'dict.append()' is incorrect; 'append()' is a method used with lists, not dictionaries.\n"
        "- 'dict.merge()' is incorrect; 'merge()' is not a built-in method for dictionaries in Python."
    )
},
{
    "question": "How do you check the type of an object 'x'?",
    "options": ["type(x)", "check(x)", "x.type()", "x.checktype()"],
    "answer": "type(x)",
    "explanation": (
        "In Python, the 'type(x)' function is used to check the type of an object 'x'. It returns the type of the object as a type object. "
        "For example, 'type(42)' returns <class 'int'>, indicating that 42 is an integer.\n"
        "- 'check(x)' is incorrect; there is no 'check()' function in Python.\n"
        "- 'x.type()' is incorrect; 'type()' is a built-in function, not a method of objects.\n"
        "- 'x.checktype()' is incorrect; 'checktype()' is not a method in Python."
    )
},
{
    "question": "What does the 'enumerate()' function do?",
    "options": ["Returns both index and value as you iterate through a list", "Enumerates elements of a set", "Reverses a list", "Sorts a list in place"],
    "answer": "Returns both index and value as you iterate through a list",
    "explanation": (
        "The 'enumerate()' function in Python adds a counter to an iterable and returns it as an enumerate object. "
        "This is often used in loops to retrieve both the index and the value of each item in the iterable.\n"
        "- 'Enumerates elements of a set' is incorrect; 'enumerate()' is typically used with lists and other iterables, not specifically with sets.\n"
        "- 'Reverses a list' is incorrect; reversing a list is done using 'list[::-1]' or 'list.reverse()'.\n"
        "- 'Sorts a list in place' is incorrect; sorting a list in place is done using 'list.sort()', not 'enumerate()'."
    )
},
{
    "question": "How do you access all elements of a dictionary?",
    "options": ["dict.items()", "dict.values()", "dict.keys()", "dict.all()"],
    "answer": "dict.items()",
    "explanation": (
        "The 'dict.items()' method in Python returns a view object that displays a list of a dictionary's key-value tuple pairs. "
        "This allows you to iterate over both keys and values in a dictionary.\n"
        "- 'dict.values()' returns only the values in the dictionary, not the keys.\n"
        "- 'dict.keys()' returns only the keys in the dictionary, not the values.\n"
        "- 'dict.all()' is incorrect; 'all()' is not a method for dictionaries in Python."
    )
},
{
    "question": "What does 'assert' do in Python?",
    "options": ["Tests if a condition is true, and raises an error if it is not", "Ends the program", "Continues the loop", "Checks the type of a variable"],
    "answer": "Tests if a condition is true, and raises an error if it is not",
    "explanation": (
        "The 'assert' statement in Python is used to test if a condition is true. If the condition is false, an 'AssertionError' is raised. "
        "This is commonly used for debugging purposes, to ensure that conditions expected to be true at a certain point in the program actually are.\n"
        "- 'Ends the program' is incorrect; 'assert' raises an exception but does not directly end the program unless the exception is unhandled.\n"
        "- 'Continues the loop' is incorrect; 'assert' does not control loop execution.\n"
        "- 'Checks the type of a variable' is incorrect; to check the type, you would use the 'type()' function."
    )
},
{
    "question": "Which keyword is used to create a generator in Python?",
    "options": ["yield", "return", "generate", "produce"],
    "answer": "yield",
    "explanation": (
        "The 'yield' keyword in Python is used to create a generator. A generator is a function that returns an iterator that yields values one at a time. "
        "Each time 'yield' is called, the function's state is saved, and the value is returned to the caller. When 'next()' is called on the generator, "
        "the function resumes where it left off.\n"
        "- 'return' is incorrect; 'return' is used to return a value from a function and exit the function completely.\n"
        "- 'generate' is incorrect; 'generate' is not a Python keyword.\n"
        "- 'produce' is incorrect; 'produce' is not a Python keyword."
    )
},
{
    "question": "How do you create a shallow copy of a list 'my_list'?",
    "options": ["my_list.copy()", "my_list[:]", "list(my_list)", "All of the above"],
    "answer": "All of the above",
    "explanation": (
        "In Python, there are several ways to create a shallow copy of a list:\n"
        "- 'my_list.copy()' uses the 'copy()' method to create a shallow copy of the list.\n"
        "- 'my_list[:]' uses slicing to create a shallow copy of the entire list.\n"
        "- 'list(my_list)' creates a new list from the elements of 'my_list', which is also a shallow copy.\n"
        "All of these methods create a shallow copy of the list, meaning that the new list will have references to the same elements as the original."
    )
},
{
    "question": "What will be the output of 'print([1, 2, 3] * 2)'?",
    "options": ["[1, 2, 3, 1, 2, 3]", "[2, 4, 6]", "[6, 4, 2]", "[1, 2, 3, 3, 2, 1]"],
    "answer": "[1, 2, 3, 1, 2, 3]",
    "explanation": (
        "In Python, when you multiply a list by an integer, it repeats the elements of the list that many times. "
        "So, '[1, 2, 3] * 2' will result in the list '[1, 2, 3, 1, 2, 3]'. The elements of the list are repeated twice in order.\n"
        "- '[2, 4, 6]' is incorrect; this would result from multiplying each element by 2, not repeating the list.\n"
        "- '[6, 4, 2]' is incorrect; this is a reversed and multiplied list, not a repeated one.\n"
        "- '[1, 2, 3, 3, 2, 1]' is incorrect; this is a palindromic sequence, not the result of repeating the list."
    )
},
{
    "question": "Which of the following will correctly merge two lists 'a' and 'b'?",
    "options": ["a + b", "a.extend(b)", "a.append(b)", "a.add(b)"],
    "answer": "a + b",
    "explanation": (
        "To merge two lists 'a' and 'b' in Python, you can use the '+' operator, which concatenates the two lists into a new list. "
        "For example, if 'a = [1, 2]' and 'b = [3, 4]', then 'a + b' will result in '[1, 2, 3, 4]'.\n"
        "- 'a.extend(b)' adds the elements of list 'b' to list 'a' but does not create a new list, so it modifies 'a' in place.\n"
        "- 'a.append(b)' adds the entire list 'b' as a single element to the end of list 'a'.\n"
        "- 'a.add(b)' is incorrect; there is no 'add()' method for lists in Python."
    )
},
{
    "question": "What does the 'zip()' function do?",
    "options": ["Aggregates elements from two or more iterables (lists, tuples, etc.)", "Compresses files", "Creates a dictionary", "Appends elements to a list"],
    "answer": "Aggregates elements from two or more iterables (lists, tuples, etc.)",
    "explanation": (
        "The 'zip()' function in Python aggregates elements from two or more iterables (such as lists, tuples, etc.) and returns an iterator of tuples. "
        "Each tuple contains elements at the same index from the input iterables. For example, 'zip([1, 2], [3, 4])' results in '[(1, 3), (2, 4)]'.\n"
        "- 'Compresses files' is incorrect; file compression is not the purpose of 'zip()' in Python.\n"
        "- 'Creates a dictionary' is incorrect; while you can use 'zip()' in conjunction with 'dict()', 'zip()' alone does not create dictionaries.\n"
        "- 'Appends elements to a list' is incorrect; 'zip()' does not modify the original lists."
    )
},
{
    "question": "How do you format a string 'name' to include a variable 'user'?",
    "options": ["f'{user}'", "'%s' % user", "'{}'.format(user)", "All of the above"],
    "answer": "All of the above",
    "explanation": (
        "In Python, there are several ways to format a string to include a variable:\n"
        "- 'f'{user}'' uses an f-string (formatted string literal) to directly embed the value of 'user' into the string.\n"
        "- ''%s' % user'' uses the old-style string formatting, where '%s' is a placeholder replaced by the value of 'user'.\n"
        "- ''{}'.format(user)'' uses the 'str.format()' method to insert 'user' into the string.\n"
        "All these methods are valid for formatting strings."
    )
},
    {
        "question": "What happens if you try to open a file that does not exist using 'open()' in read mode ('r')?",
        "options": [
            "A new file is created.",
            "An empty string is returned.",
            "A FileNotFoundError is raised.",
            "The program crashes without an error."
        ],
        "answer": "A FileNotFoundError is raised.",
        "explanation": (
            "When you try to open a file that does not exist in read mode ('r'), Python raises a FileNotFoundError. "
            "This is because the 'r' mode is for reading, and it expects the file to already exist. If the file is "
            "not found, the exception is raised to indicate that the operation could not be completed.\n"
            "- The option 'A new file is created.' is incorrect because this would only happen if you opened the file in write mode ('w').\n"
            "- The option 'An empty string is returned.' is incorrect because 'open()' does not return an empty string if the file doesn't exist; it raises an error.\n"
            "- The option 'The program crashes without an error.' is incorrect because Python will raise a specific exception (FileNotFoundError), and the program will not crash silently."
        )
    },
    {
        "question": "How do you write data to a file named 'output.txt' in Python?",
        "options": [
            "open('output.txt', 'r').write('data')",
            "with open('output.txt', 'w') as file: file.write('data')",
            "write('output.txt', 'data')",
            "file.write('output.txt', 'data')"
        ],
        "answer": "with open('output.txt', 'w') as file: file.write('data')",
        "explanation": (
            "To write data to a file in Python, you should open the file in write mode ('w') using the open() function. "
            "The correct syntax is 'with open('output.txt', 'w') as file: file.write('data')'. This ensures that the file "
            "is opened, written to, and then properly closed. The 'w' mode will also create the file if it doesn't exist "
            "or truncate it if it does.\n"
            "- The option 'open('output.txt', 'r').write('data')' is incorrect because 'r' mode is for reading, not writing.\n"
            "- The option 'write('output.txt', 'data')' is incorrect because 'write()' is not a standalone function; it needs to be called on a file object.\n"
            "- The option 'file.write('output.txt', 'data')' is incorrect because it suggests that 'write()' takes a filename, which it does not."
        )
    },
    {
        "question": "What is the main advantage of using a generator in Python?",
        "options": [
            "Generators are faster than regular functions.",
            "Generators automatically optimize your code.",
            "Generators allow you to iterate over large datasets without using much memory.",
            "Generators can generate random numbers."
        ],
        "answer": "Generators allow you to iterate over large datasets without using much memory.",
        "explanation": (
            "The main advantage of using a generator is that it allows you to iterate over large datasets "
            "without loading the entire dataset into memory. Generators produce items one at a time and "
            "only when required, making them memory-efficient. This is especially useful when working "
            "with large data streams or files.\n"
            "- The option 'Generators are faster than regular functions.' is incorrect because generators are not necessarily faster; they are more memory-efficient.\n"
            "- The option 'Generators automatically optimize your code.' is incorrect because generators do not optimize code automatically; they just provide a way to generate values on the fly.\n"
            "- The option 'Generators can generate random numbers.' is incorrect because generators are not specifically designed for generating random numbers; they yield values based on the logic within the generator function."
        )
    },
    {
        "question": "Which of the following is NOT true about generators?",
        "options": [
            "Generators maintain their state between calls.",
            "You can use the 'next()' function to retrieve the next value from a generator.",
            "Generators can only yield values once.",
            "Generators can be converted to lists."
        ],
        "answer": "Generators can only yield values once.",
        "explanation": (
            "The statement 'Generators can only yield values once' is not true. Generators yield values "
            "one at a time, and you can continue calling 'next()' on a generator to retrieve the next value "
            "until the generator is exhausted. While it's true that each value is yielded only once, the "
            "generator itself can produce multiple values over time.\n"
            "- The option 'Generators maintain their state between calls.' is true because the generator function's state is saved after each 'yield'.\n"
            "- The option 'You can use the 'next()' function to retrieve the next value from a generator.' is true because 'next()' is the standard way to get the next value from a generator.\n"
            "- The option 'Generators can be converted to lists.' is true because you can pass a generator to the 'list()' function, which will exhaust the generator and store its values in a list."
        )
    },
    {
        "question": "Which of the following is the correct syntax to create a lambda function that multiplies its argument by 2?",
        "options": [
            "lambda x: x * 2",
            "lambda x => x * 2",
            "def lambda x: return x * 2",
            "lambda(x) * 2"
        ],
        "answer": "lambda x: x * 2",
        "explanation": (
            "The correct syntax to create a lambda function in Python that multiplies its argument by 2 is 'lambda x: x * 2'. "
            "This lambda function takes one argument 'x' and returns the value of 'x * 2'.\n"
            "- The option 'lambda x => x * 2' is incorrect because '=>' is not the correct syntax for lambda functions in Python.\n"
            "- The option 'def lambda x: return x * 2' is incorrect because lambda functions are defined using the 'lambda' keyword, not 'def', and they do not use the 'return' keyword.\n"
            "- The option 'lambda(x) * 2' is incorrect because the correct syntax for lambda functions does not use parentheses around the argument in this way."
        )
    },
    {
        "question": "What will be the output of the following code: list(map(lambda x: x + 2, [1, 2, 3]))?",
        "options": [
            "[3, 4, 5]",
            "[2, 3, 4]",
            "[1, 2, 3, 4]",
            "[4, 6, 8]"
        ],
        "answer": "[3, 4, 5]",
        "explanation": (
            "The expression 'list(map(lambda x: x + 2, [1, 2, 3]))' applies the lambda function 'lambda x: x + 2' "
            "to each element in the list [1, 2, 3]. The lambda function adds 2 to each element, resulting in the list [3, 4, 5].\n"
            "- The option '[2, 3, 4]' is incorrect because it adds 1 instead of 2 to each element, which is not what the lambda function does.\n"
            "- The option '[1, 2, 3, 4]' is incorrect because the lambda function does not add any new elements to the list; it only modifies existing elements.\n"
            "- The option '[4, 6, 8]' is incorrect because these values would result from multiplying the elements by 2, not adding 2."
        )
    },
    {
        "question": "Which of the following is NOT a common use case for lambda functions in Python?",
        "options": [
            "Sorting lists with custom keys",
            "Filtering elements in a list",
            "Creating anonymous functions for one-time use",
            "Defining complex multi-line functions"
        ],
        "answer": "Defining complex multi-line functions",
        "explanation": (
            "Lambda functions in Python are typically used for short, simple operations that can be expressed in a single line of code. "
            "They are often used in places where you need a small function for a short period of time, such as sorting lists with custom keys, "
            "filtering elements, or creating simple anonymous functions.\n"
            "- The option 'Sorting lists with custom keys' is a common use case, where you might use a lambda function to define the key for sorting.\n"
            "- The option 'Filtering elements in a list' is another common use case where lambda functions are used with the 'filter()' function to determine which elements to include.\n"
            "- The option 'Creating anonymous functions for one-time use' is exactly what lambda functions are designed for. "
            "However, they are not suitable for 'Defining complex multi-line functions' because lambda functions are limited to a single expression and cannot include statements or multiple lines."
        )
    },
    {
        "question": "What does the following lambda function return when called with the argument 5? lambda x: x**2",
        "options": [
            "10",
            "25",
            "x squared",
            "5"
        ],
        "answer": "25",
        "explanation": (
            "The lambda function 'lambda x: x**2' takes a single argument 'x' and returns 'x' raised to the power of 2. "
            "When called with the argument 5, it returns '5**2', which is 25.\n"
            "- The option '10' is incorrect because the lambda function does not add or multiply, it squares the input.\n"
            "- The option 'x squared' is incorrect because the lambda function returns a numerical value, not a symbolic expression.\n"
            "- The option '5' is incorrect because the lambda function squares the input, it doesn't return the input unchanged."
        )
    },
    {
        "question": "What will be the output of the following code: my_list = [1, 2, 3]; my_list[1:2] = [4, 5, 6]?",
        "options": [
            "[1, 4, 5, 6, 3]",
            "[1, 4, 5, 6, 2, 3]",
            "[1, 4, 5, 6]",
            "[1, 2, 3, 4, 5, 6]"
        ],
        "answer": "[1, 4, 5, 6, 3]",
        "explanation": (
            "In this code, the slice 'my_list[1:2]' refers to the sublist containing the element at index 1. "
            "Assigning '[4, 5, 6]' to this slice replaces the element at index 1 with the new list. "
            "So, the original list '[1, 2, 3]' is modified to '[1, 4, 5, 6, 3]'.\n"
            "- The option '[1, 4, 5, 6, 2, 3]' is incorrect because the elements 2 and 3 are not kept in the same order; 2 is replaced by the new elements.\n"
            "- The option '[1, 4, 5, 6]' is incorrect because the last element (3) is not removed; it remains after the inserted elements.\n"
            "- The option '[1, 2, 3, 4, 5, 6]' is incorrect because this would only happen if the new elements were appended at the end, not inserted at the slice position."
        )
    },
    {
        "question": "How do you create a shallow copy of a list in Python?",
        "options": [
            "list.copy()",
            "list.clone()",
            "copy(list)",
            "list.deepcopy()"
        ],
        "answer": "list.copy()",
        "explanation": (
            "To create a shallow copy of a list in Python, you can use the 'copy()' method. This creates a new list that is a shallow copy of the original list.\n"
            "- The option 'list.clone()' is incorrect because 'clone()' is not a method for lists in Python.\n"
            "- The option 'copy(list)' is incorrect because 'copy' is not a built-in function in Python; you need to use the 'copy' module for that.\n"
            "- The option 'list.deepcopy()' is incorrect because 'deepcopy()' is used for deep copying, not shallow copying, and it requires importing the 'copy' module."
        )
    },
    {
        "question": "How do you add a new key-value pair to an existing dictionary in Python?",
        "options": [
            "dict.add('key', 'value')",
            "dict['key'] = 'value'",
            "dict.insert('key', 'value')",
            "dict.append({'key': 'value'})"
        ],
        "answer": "dict['key'] = 'value'",
        "explanation": (
            "To add a new key-value pair to an existing dictionary in Python, you can use the syntax 'dict['key'] = 'value''. "
            "This assigns the value to the specified key in the dictionary. If the key already exists, it updates the value; if not, it adds a new key-value pair.\n"
            "- The option 'dict.add('key', 'value')' is incorrect because there is no 'add()' method for dictionaries in Python.\n"
            "- The option 'dict.insert('key', 'value')' is incorrect because 'insert()' is not a method for dictionaries; it's used with lists.\n"
            "- The option 'dict.append({'key': 'value'})' is incorrect because 'append()' is not a method for dictionaries; it's used with lists."
        )
    },
    {
        "question": "What will be the output of the following code: d = {'a': 1, 'b': 2}; d['c'] = d.get('b') + 3?",
        "options": [
            "{'a': 1, 'b': 2, 'c': 2}",
            "{'a': 1, 'b': 2, 'c': 3}",
            "{'a': 1, 'b': 2, 'c': 5}",
            "{'a': 1, 'b': 2, 'c': 6}"
        ],
        "answer": "{'a': 1, 'b': 2, 'c': 5}",
        "explanation": (
            "The code 'd['c'] = d.get('b') + 3' retrieves the value associated with the key 'b' in the dictionary 'd' using the 'get()' method. "
            "Since 'd['b']' is 2, the expression 'd.get('b') + 3' evaluates to 2 + 3, which is 5. "
            "This value is then assigned to the key 'c' in the dictionary, resulting in the dictionary '{'a': 1, 'b': 2, 'c': 5}'.\n"
            "- The option '{'a': 1, 'b': 2, 'c': 2}' is incorrect because it suggests that the value of 'c' was assigned the same value as 'b', but 3 is added to 'b'.\n"
            "- The option '{'a': 1, 'b': 2, 'c': 3}' is incorrect because it implies that 'c' is just the value of 3, without considering the value of 'b'.\n"
            "- The option '{'a': 1, 'b': 2, 'c': 6}' is incorrect because it suggests that the value of 'b' is added twice (2+2+3), which is not the case here."
        )
    },
    {
    "question": "What happens if you try to open a file in write mode ('w') that already exists?",
    "options": [
        "The file is opened, and new data is appended to the existing content.",
        "The file is opened, and its content is deleted before writing new data.",
        "The file is opened, and a FileExistsError is raised.",
        "The file is opened, but you cannot write to it."
    ],
    "answer": "The file is opened, and its content is deleted before writing new data.",
    "explanation": (
        "When you open a file in write mode ('w'), Python opens the file and deletes its existing content. "
        "This is because write mode is designed to start fresh, so it overwrites any data already in the file.\n"
        "- The option 'The file is opened, and new data is appended to the existing content.' is incorrect because appending is done in append mode ('a'), not write mode ('w').\n"
        "- The option 'The file is opened, and a FileExistsError is raised.' is incorrect because Python does not raise an error when opening an existing file in write mode; it simply overwrites the file.\n"
        "- The option 'The file is opened, but you cannot write to it.' is incorrect because write mode allows you to write to the file, starting with an empty file."
    )
},
{
    "question": "Which method is used to read a file line by line in Python?",
    "options": [
        "file.readlines()",
        "file.read()",
        "file.readline()",
        "file.read_lines()"
    ],
    "answer": "file.readline()",
    "explanation": (
        "The 'readline()' method is used to read a file line by line. Each call to 'readline()' returns the next line from the file as a string, including the newline character at the end.\n"
        "- The option 'file.readlines()' is incorrect because 'readlines()' reads all lines in the file and returns them as a list of strings, not one line at a time.\n"
        "- The option 'file.read()' is incorrect because 'read()' reads the entire content of the file as a single string, not line by line.\n"
        "- The option 'file.read_lines()' is incorrect because there is no 'read_lines()' method in Python; the correct method is 'readline()'."
    )
},
{
    "question": "What will be the output of the following code: x = 10; if x > 5: print('x is greater than 5'); elif x < 5: print('x is less than 5'); else: print('x is equal to 5')?",
    "options": [
        "'x is greater than 5'",
        "'x is less than 5'",
        "'x is equal to 5'",
        "No output"
    ],
    "answer": "'x is greater than 5'",
    "explanation": (
        "The code checks the value of 'x' with an if-elif-else statement. Since 'x' is 10, which is greater than 5, "
        "the condition 'if x > 5' evaluates to True, and the corresponding print statement 'x is greater than 5' is executed.\n"
        "- The option ''x is less than 5'' is incorrect because the first condition is true, so the elif block is not evaluated.\n"
        "- The option ''x is equal to 5'' is incorrect because the first condition is true, so the else block is not evaluated.\n"
        "- The option 'No output' is incorrect because the first condition is true, so there is an output."
    )
},
{
    "question": "What will be the output of the following code: i = 0; while i < 3: print(i); i += 1?",
    "options": [
        "0 1 2",
        "1 2 3",
        "0 1 2 3",
        "Infinite loop"
    ],
    "answer": "0 1 2",
    "explanation": (
        "The while loop runs as long as the condition 'i < 3' is True. The loop starts with 'i = 0' and increments 'i' by 1 after each iteration.\n"
        "- On the first iteration, i is 0, so it prints 0.\n"
        "- On the second iteration, i is 1, so it prints 1.\n"
        "- On the third iteration, i is 2, so it prints 2.\n"
        "The loop stops when i becomes 3, so the output is '0 1 2'.\n"
        "- The option '1 2 3' is incorrect because the loop starts from 0, not 1, and stops before reaching 3.\n"
        "- The option '0 1 2 3' is incorrect because the loop stops when i equals 3, so 3 is not printed.\n"
        "- The option 'Infinite loop' is incorrect because the loop condition eventually becomes False, and the loop exits."
    )
},
{
    "question": "What will be the output of the following code: def func(a, b=2): return a + b; result = func(3)?",
    "options": [
        "3",
        "5",
        "2",
        "TypeError"
    ],
    "answer": "5",
    "explanation": (
        "The function 'func' is defined with two parameters: 'a' and 'b', where 'b' has a default value of 2. "
        "When 'func(3)' is called, the argument '3' is passed to 'a', and since no value is provided for 'b', the default value of 2 is used. "
        "The function returns the sum of 'a' and 'b', which is 3 + 2 = 5.\n"
        "- The option '3' is incorrect because the function adds 'a' and 'b', not just returns 'a'.\n"
        "- The option '2' is incorrect because it represents the default value of 'b', not the sum.\n"
        "- The option 'TypeError' is incorrect because the function is called correctly with one argument, and 'b' uses its default value."
    )
},
{
    "question": "What will be the output of the following code: x = 5; def func(): x = 10; return x; result = func(); print(x, result)?",
    "options": [
        "5 10",
        "10 10",
        "10 5",
        "5 5"
    ],
    "answer": "5 10",
    "explanation": (
        "In the code, 'x = 5' defines a global variable 'x'. Inside the function 'func()', 'x = 10' defines a local variable 'x', "
        "which is independent of the global 'x'. The function returns the local 'x', which is 10. "
        "However, when 'print(x, result)' is called, 'x' refers to the global 'x' which is still 5, and 'result' is the return value of the function, which is 10.\n"
        "- The option '10 10' is incorrect because the global 'x' remains 5, and only the local 'x' inside the function is 10.\n"
        "- The option '10 5' is incorrect because the function returns 10, so 'result' is 10, not 5.\n"
        "- The option '5 5' is incorrect because the function returns 10, and the global 'x' remains 5."
    )
},
{
    "question": "What is polymorphism in Python?",
    "options": [
        "Polymorphism allows functions or methods to process objects differently depending on their data type or class.",
        "Polymorphism is a way to hide data from unauthorized access.",
        "Polymorphism is a technique to modify a class by adding new attributes.",
        "Polymorphism refers to the inheritance of multiple classes."
    ],
    "answer": "Polymorphism allows functions or methods to process objects differently depending on their data type or class.",
    "explanation": (
        "Polymorphism in Python allows functions or methods to operate on objects of different types or classes. "
        "It enables the same method to be used on different objects and perform different actions depending on the object's class.\n"
        "- The option 'Polymorphism is a way to hide data from unauthorized access.' is incorrect because that describes encapsulation, not polymorphism.\n"
        "- The option 'Polymorphism is a technique to modify a class by adding new attributes.' is incorrect because that refers to class modification, not polymorphism.\n"
        "- The option 'Polymorphism refers to the inheritance of multiple classes.' is incorrect because that describes multiple inheritance, not polymorphism."
    )
},
{
    "question": "What will be the output of the following code: class Animal: def sound(self): return 'Some sound'; class Dog(Animal): def sound(self): return 'Bark'; dog = Dog(); print(dog.sound())?",
    "options": [
        "'Some sound'",
        "'Bark'",
        "'Animal sound'",
        "Error: sound() method not defined"
    ],
    "answer": "'Bark'",
    "explanation": (
        "In this code, the 'Dog' class inherits from the 'Animal' class and overrides the 'sound()' method. "
        "When 'dog.sound()' is called, the 'sound()' method of the 'Dog' class is executed, which returns 'Bark'. "
        "This demonstrates method overriding in Python.\n"
        "- The option ''Some sound'' is incorrect because the 'Dog' class overrides the 'Animal' class's 'sound()' method.\n"
        "- The option ''Animal sound'' is incorrect because this is not a method defined in either class.\n"
        "- The option 'Error: sound() method not defined' is incorrect because the 'sound()' method is defined in both the parent and child classes."
    )
},
{
    "question": "What does it mean when an attribute in a class is prefixed with a single underscore (e.g., _attribute)?",
    "options": [
        "It indicates that the attribute is intended to be private and should not be accessed directly.",
        "It makes the attribute accessible only within the class.",
        "It automatically protects the attribute from being modified.",
        "It is used for class-level attributes."
    ],
    "answer": "It indicates that the attribute is intended to be private and should not be accessed directly.",
    "explanation": (
        "In Python, an attribute prefixed with a single underscore (e.g., '_attribute') is a convention that indicates the attribute is intended to be private and should not be accessed directly from outside the class. "
        "However, this is just a convention and does not enforce access restrictions.\n"
        "- The option 'It makes the attribute accessible only within the class.' is incorrect because the single underscore does not enforce this; it is just a convention.\n"
        "- The option 'It automatically protects the attribute from being modified.' is incorrect because the single underscore does not provide automatic protection; it is merely a hint.\n"
        "- The option 'It is used for class-level attributes.' is incorrect because class-level attributes are not indicated by a single underscore."
    )
},
{
    "question": "What is the purpose of the __init__ method in a Python class?",
    "options": [
        "It is a constructor that initializes an object’s state when a new object is created.",
        "It is used to delete an object.",
        "It is called when an object is destroyed.",
        "It is used to define class-level attributes."
    ],
    "answer": "It is a constructor that initializes an object’s state when a new object is created.",
    "explanation": (
        "The '__init__' method is a special method in Python that is automatically called when a new object of the class is created. "
        "It is used to initialize the object's state by assigning values to the object's attributes.\n"
        "- The option 'It is used to delete an object.' is incorrect because '__init__' does not delete an object; '__del__' is used for cleanup before an object is destroyed.\n"
        "- The option 'It is called when an object is destroyed.' is incorrect because '__init__' is used for initialization, not destruction.\n"
        "- The option 'It is used to define class-level attributes.' is incorrect because '__init__' is used for instance-level attributes, not class-level attributes."
    )
},
{
    "question": "How do you call a method from a parent class in a subclass?",
    "options": [
        "super().method_name()",
        "this.method_name()",
        "parent.method_name()",
        "method_name()"
    ],
    "answer": "super().method_name()",
    "explanation": (
        "To call a method from a parent class in a subclass, you use 'super().method_name()'. "
        "The 'super()' function returns a temporary object of the superclass, allowing you to call its methods.\n"
        "- The option 'this.method_name()' is incorrect because 'this' is not a keyword in Python; 'self' is used for instance methods, but not for calling parent methods.\n"
        "- The option 'parent.method_name()' is incorrect because there is no 'parent' keyword in Python; 'super()' is the correct way to refer to the parent class.\n"
        "- The option 'method_name()' is incorrect because this would call a method in the current class, not the parent class."
    )
},
{
    "question": "Which of the following is true about encapsulation in Python?",
    "options": [
        "Encapsulation refers to the bundling of data and methods that operate on the data within one unit, usually a class.",
        "Encapsulation means creating functions in Python.",
        "Encapsulation is about inheriting methods from a parent class.",
        "Encapsulation is a method used to encrypt data in Python."
    ],
    "answer": "Encapsulation refers to the bundling of data and methods that operate on the data within one unit, usually a class.",
    "explanation": (
        "Encapsulation is one of the fundamental principles of OOP. It refers to the bundling of data (attributes) and methods that operate on the data within a single unit (usually a class). "
        "It also restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of the methods and attributes.\n"
        "- The option 'Encapsulation means creating functions in Python.' is incorrect because encapsulation is about bundling data and methods, not just creating functions.\n"
        "- The option 'Encapsulation is about inheriting methods from a parent class.' is incorrect because this describes inheritance, not encapsulation.\n"
        "- The option 'Encapsulation is a method used to encrypt data in Python.' is incorrect because encapsulation is not related to encryption; it's about data hiding and access restriction."
    )
},
{
    "question": "What is inheritance in Python?",
    "options": [
        "A mechanism that allows a class to inherit attributes and methods from another class.",
        "A function that returns the sum of all attributes in a class.",
        "A way to combine two or more classes into one.",
        "A method for converting data types in Python."
    ],
    "answer": "A mechanism that allows a class to inherit attributes and methods from another class.",
    "explanation": (
        "Inheritance is a key feature of OOP in Python that allows a class (the child or subclass) to inherit attributes and methods from another class (the parent or superclass). "
        "This allows for code reuse and the creation of a hierarchical class structure.\n"
        "- The option 'A function that returns the sum of all attributes in a class.' is incorrect because inheritance does not sum attributes; it allows for the reuse of attributes and methods.\n"
        "- The option 'A way to combine two or more classes into one.' is incorrect because inheritance doesn't combine classes; it creates a relationship where one class derives from another.\n"
        "- The option 'A method for converting data types in Python.' is incorrect because inheritance is not about data type conversion; it's about creating a new class based on an existing class."
    )
}
    
    ]

    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, 1):
        # Display progress bar
        progress = f"[{'#' * i}{'.' * (total_questions - i)}] {i}/{total_questions}"
        print(f"\n{progress}")
        
        print(f"Question {i}/{total_questions}:")
        print(question["question"])

        # Shuffle the options so that they appear in a different order each time
        options = question["options"]
        random.shuffle(options)

        # Display the shuffled options
        option_map = {chr(65 + idx): option for idx, option in enumerate(options)}  # Create a map from A, B, C, D to options
        for key, value in option_map.items():
            print(f"{key}) {value}")

        # Get the user's answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        time.sleep(1)  # Add a 2-second pause after each answer 

        if option_map.get(user_answer) == question["answer"]:
            print("CORRECT : ")
            print(question["explanation"])  # Add the explanation
            score += 1
        else:
            correct_option = [key for key, value in option_map.items() if value == question["answer"]][0]
            print(f"INCORRECT! The correct answer is {correct_option} : ")
            print(question["explanation"])  # Add the explanation

        # Wait for user to press Enter before proceeding to the next question
        input("\nPress Enter to continue to the next question...")


        #time.sleep(5)  # Add a 3-second pause after each answer

    print(f"\nQuiz completed! Your score: {score}/{total_questions}")

def main():
    welcome()
    while True:
        quiz()
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
