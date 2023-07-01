jk_exceptionhelper
==================

Introduction
------------

This python module provides a way to model python exceptions in a clean object oriented way. It is then easy to work with these exception objects.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-exceptionhelper)
* [pypi.python.org](https://pypi.python.org/pypi/jk_exceptionhelper)

Why this module?
----------------

Though the python exception API has improved over time it still is quite complex and a bit confusing because of its complexity. This module tries to solve this problem by modeling exceptions in a very defined, clean, object oriented way similar to other programming languages such as Java, C# and others.

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
	ee = ExceptionObject.fromException(ex)
```

Now `ee` contains an instance of `ExceptionObject`. `ExceptionObject` contains all relevant information from the exception for your convenience to work with.

### Output the exception data

For testing or debugging there is an easy way to write all exception data to STDOUT:

Example:

```python
try:
	a = 0
	b = 5 / a
except Exception as ex:
	ee = ExceptionObject.fromException(ex)
	ee.dump()
```

This will print the following lines to STDOUT:

```
ZeroDivisionError
: exceptionTextHR:
:       division by zero
: stackTrace:
:       ./example_simple.py:18 :: 'b = 5 / a'
\-
```

### Nested exeptions

Example:

```python
try:
	try:
		... do something that fails ...
	except Exception as e2:
		raise Exception("Something has failed!", ExceptionObject.fromException(e2))

except Exception as e:
	ee = ExceptionObject.fromException(e)
	ee.dump()
```

Now `ee` contains an instance of `ExceptionObject`. `ExceptionObject` itself contains not only standard exception data but a reference to the nested `ExceptionObject`.
The trick is here to get a model of the original exception immediately so that the current stack trace is captured. Then a new exception can be raised.
If at a later step `ExceptionObject.fromException(...)` is invoked again, the method `fromException()` will automatically find the appended `ExceptionObject` and
use it as a nested exception.

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
| `ExceptionObject`		| `nestedException`		| optional	| Another exception object the current exception could refer to if it replaces the other exception.	|

### Static Methods

#### Static Method `StackTraceItem fromJSON(dict data)`

`StackTraceItem fromJSON(dict data)`

Deserialize a data structure created by `toJSON()`.

#### Static Method `ExceptionObject fromException(BaseException exception)`

`ExceptionObject fromException(BaseException exception)`

Capture all python exception information and represent it as `ExceptionObject` for later processing.

### Methods

#### Method `void dump()`

`void dump()`

Print the contents of the exception to STDOUT.

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
except Exception as ex:
	ee = ExceptionObject.fromException(ex)
	edata = ee.toJSON()
```

#### Method `dict toJSON_flat()`

`dict toJSON_flat()`

Same as `toJSON(False)`.

Arguments:

* (none)

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



