# Control Flow Tools

+ There are several control flow tools like _while_ , _for_ ,_if_ , _break_ , _continue_ , _pass_ , _match_ and `range()`.
+ We can also make use of functions.


### 1. `if` statement :

+ `if` statement is used to control the program flow.
+ It checks the condition , if the that is true then the `if` block gets executed.
+ It also has `elif` and `else` statements, which we can be nested.
 ```python
if '''Condition1''' :
    #code if Condition1 is true
elif '''Condition2''' :
    #if Condition2 is True
else :
    #if none of the conditions are true
```

### 2. `for` statement :
+ `for` helps very much. Almost every coder uses atleast one for loop in their program.
+ We can iterate over an iterable using for loop like _list_ , _dict_ , _tuple_ , etc.
+ We generally use for loops with the `range()` function.
+ syntax : `for i in range()`

### 3. `range()` function :
+ We can iterate over a sequence of number using `range()`.
```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

+ We can also specify start of the sequence and increment value by `range(1,15,2)`.
+ If we try to directly print the `range()` function it will generate the address of the iterable. Because that's what python does to save the memory.

### 4. `break` , `pass` , `continue` and `else` with loop :

+ `break` statement is used to break out of the loop.
+ In nested loops situations `break` will only work on the loop which contains it and all the inner loops , but not the outer loops.
+ `continue` statement will skip the current execution of the loop and it will **ignore** all the statements that are below it.
+ `pass` statement is similar to `continue` , the only difference is that even if use `pass` the lines below it will get executed.
+ `match` is the python's version of `switch-case` statement. We provide some value to it and it compares that value with every `case`, if found `True` then that code gets executed.


### 5. Functions :
+ Functions are the block of code that can be reused over and over again.
+ We can define functions by `def` keyword.
+ syntax :
```python
def _function_name_(*args):
    #code
    return #something , default is None
```
+ After defining functions we can call it unlimited number of times. We can pass some arguments to it.
+ `*args` can be used when we don't know how many number of arguments are gonna be passed into the function.
+ We can also make use of keyword arguments, to reduce the error `def func(a=5,b=6)` and when the arguments are passed these values will get overwritten.
+ `lambda` functions are the short hand functions(alsocalled short hand anonymous functions). They are very fast than normal functions.