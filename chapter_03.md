# Introduction to python - Basic Data types and Data structures

Python has various in-built data types. They are one of the foundational building blocks in python.

Data Types :
1. Numbers
    + int
    + float
    + complex numbers
2. Text
    + strings

 

### 1. Numbers :
+ int or _integer_ data type can hold all the integer values between -2<sup>31</sup> to 2<sup>31</sup>.
+ Since python acts as a simple calculator we can perform arithmatic tasks easily.
``` python
>>> 2 + 2
4
>>> 50 - 5*6 #preference is according to BODMAS
20
```
+ When using `/` operator we have to be causious, because the division operator returns float valued output.
+ To get _int_ output we can use **_floor division_** operator `//` and to calculate the remainder of division we can use **_Modulus operator_** that is `%`.
```python
>>> 17 / 3
5.66666666666667
>>> 17 // 3
5
>>> 17 % 3
2
```

+ We can use `**` operator to calculate powers.
+ Before using any variable we first have to define it.
+ Since Type casting in python is done automatically due to its _dynamic_ nature , we don't explicitly have to give type to any variable.


### 2. Text :
+ Everything that is written inside `""` or `''` is treated as _strings_.
They are represented by type str.
+ We concat two or more strings simply by `+` operator.
+ There are various built-in functions present in python standard library for strings like `replace()`,`join()`,`zfill()`,`upper()`,`lower()`,`split()`,`strip()`,...... and many more.
+ We can also use strings as a multi-line comment, because python interpreter will just ignore the strings.
+ We can access strings by slicing just like we do it in array.
```python
>>> word = "python"
>>> word[0]
"p"
>>> word[::-1]
"nohtyp"
```

## Mixed type Experimentation

```python
>>> 5 + 5.2 #Any operation between integer and float will always generate float as result.
10.2
>>> "Hii" + 2 #This will generate an error beacause we the + operator in strings acts as a concatanation character
>>> "hii" * 2 #The * operator is the only operator that we can use with strings and INT ONLY.
"hiihii"
```
