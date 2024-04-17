# Data Structures

+ There are various data types in python like `list()` , `tuple()`,`set()` and `dictionary()`.
+ Understanding of Data structures is a crucial step to optimize your code.

### 1. List :
+ Lists are _compound_ data types. Meaning they can store multipple comma - separated values. We can also net multiple lists together.
+ We can access elements by slicing `[]`.
+ Unlike arrays, List can store multiple data types at a time.
+ There are various built-in methods present in the `list()` class.
+ `append()` to append any value at the end of the list.
+ `insert()` to insert value at any specified index.
+ `pop()` will remove and return the last element of any list. We can also delete an element at specified index.
+ `clear()` will delete the entire list.
+ We can also use `del` keyword to delete element or any variable.
+ `index()` will give us the index of given element. If there are multiple copies then it will return the lowest index.
+ `reverse()` will reverse the entire list in-place.
+ `copy()` makes a _shallow_ copy of the list.
+ `sort()` and `sorted()` both are used to sort the list but `sort()` will do it in-place while the other one will return a copy.

#### Lists as stacks , Queues and list comprehensions

+ **Stack** is a data structure which follows the LIFO(Last In First Out) Principle.
+ We can use lists to implement the stack.
+ We will use the `append()` function to add the elements into the stack and `pop()` function to remove them.

+ **Queue** data structure follows the FIFO(First In First Out) principle.
There is standard function called `deque()` in the `collections` module.
+ It has `popleft()` and `append()` functions to implement removal and addition of elements respectively.


#### List comprehensions
+ List comprehensions makes the code more readable and One Liner.
+ List comprehensions are also more efficient than the traditional way.
+ We can also do nested list comprehensions.



### 2. Tuple :
+ Tuples are the immmutable data type. That means they cannot be changed once they are written.
+ Tuples can be nested and also like list they can contain multiple data types at any time.
+ While creating singular tuple we have to put a `,` otherwise it will be treated as a `int` data type.
+ Tuples are instance of `tuple()` class.


### 3. Set :
+ Sets are mutable data types just like list. They can also have multiple type of elements in them.
+ The only difference is that _Sets_ don't contain any duplicate entries in them.
+ Even if try to add them, Interpreter will automatically remove them.
+ They are the instance of `set()` class.
+ Sets has methods like `add()` to add the elements in them.
+ Sets are unordered, we cannot access them by slicing.




### 4. Dictionary :
+ Dictionaries are ordered, _key-value_ paired, changeable data types.
+ Dictionaries also do not allow duplicates.
+ We can have any data type as the _value_ in the dictionary.
+ We can access any element by using keys.
+ Like list comprehensions, We can also use Dictionary shorthands.
+ `dict()` constructor builds dictionaries from key-value pairs.
+ There are various methods like `get()` , `keys()` , `values()` , `items()` present in the `dict()` class.