jk_exceptionhelper
==================

Introduction
------------

This python module wraps around python exceptions. As the python exception API is quite a bit obscure this python module provides a clean API for analysis and logging purposes.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_exceptionhelper)

Why this module?
----------------

As the python exception API is quite a bit obscure this python module tries to solve this problem. By focusing on this problem in an isolated way improvements can easily be made without breaking and adapting a variety of implementations.

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_exceptionhelper
```

### Analyse the exeption

Example:

```python
try:
	a = 0
	b = 5 / a
except Exception as ex:
	ee = jk_exceptionhelper.analyseException(ex)
```

Now `ee` contains an instance of `ExceptionObject`. `ExceptionObject` contains all relevant information from the exception for your convenience to work with. (For details about the `ExceptionObject` API see below.)

### Output the exception data

Example:

```python
try:
	a = 0
	b = 5 / a
except Exception as ex:
	jk_exceptionhelper.analyseException(ex).dump()
```

This will print all data collected to STDOUT. Example:

```
ZeroDivisionError
: exceptionTextHR:
:	division by zero
: stackTrace:
:	(<stdin>:3, '')
\-
```

API: Functions
--------------

### Function `analyseException()`

`ExceptionObject analyseException()`

This function should be called at the first statement within an `except` block. It returns an object of type `ExceptionObject` containing all relevant information from the exception for your convenience to work with.

API: Classes
------------

## Class 'ExceptionObject'

### Fields

| Type	| Name	| Required?	| Description	|
| ----- | ----- | --------- | ------------- |
| `class`				| `exceptionClass`		| optional	| The original exception class. This instance will only be present if `analyseException()` was called within an `except` block.	|
| `str`					| `exceptionClassName`	| required	| The class name of the exception.														|
| `str`					| `exceptionTextHR`		| optional	| A human readable text that was contained within the exception.						|
| `StackTraceItem[]`	| `stackTrace`			| optional	| The stack trace. The last item of the list is the topmost stack element.				|
| `ExceptionObject`		| `nestedException`		| optional	| The parent exception object if this exception has been caught in an `except` block.	|

### Static Methods

#### Static Method `StackTraceItem fromJSON(dict data)`

`StackTraceItem fromJSON(dict data)`

Deserialize a data structure created by `toJSON()`.

### Methods

#### Method `void dump()`

`void dump()`

Print the contents of the exception to STDOUT.

Example:

```python
try:
	a = 0
	b = 5 / a
except:
	analyseException().dump()
```

This will print something like this:

```
ZeroDivisionError
: exceptionTextHR:
:	division by zero
: stackTrace:
:	(./test2.py:55, 'b = 5 / a')
:	(./test2.py:59, 'main3()')
:	(./test2.py:63, 'main2()')
:	(./test2.py:67, 'main1()')
```

#### Method `dict toJSON(bool bRecursive = True)`

`dict toJSON(bool bRecursive = True)`

Serialize the exception object to JSON format.

Arguments:

* `bool bRecursive` : If `True` (which is the default) nested exceptions are serialized as well. If `False` these get skipped.

Example:

```python
try:
	a = 0
	b = 5 / a
except:
	edata = analyseException().toJSON()
```

#### Method `dict toJSON(bool bRecursive = True)`

`dict toJSON_flat()`

Same as `toJSON(False)`.

Arguments:

* (none)

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



