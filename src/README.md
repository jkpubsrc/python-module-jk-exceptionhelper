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
	ee = jk_exceptionhelper.analyseException(ex)
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
	ee = jk_exceptionhelper.analyseException(ex)
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
		raise Exception("Something has failed!", jk_exceptionhelper.analyseException(e2))

except Exception as e:
	ee = jk_exceptionhelper.analyseException(e)
	ee.dump()
```

Now `ee` contains an instance of `ExceptionObject`. `ExceptionObject` itself contains not only standard exception data but a reference to the nested `ExceptionObject`.
The trick is here to get a model of the original exception immediately so that the current stack trace is captured. Then a new exception can be raised.
If at a later step `jk_exceptionhelper.analyseException(...)` is invoked again, the method `fromException()` will automatically find the appended `ExceptionObject` and
use it as a nested exception.

Extra values
------------

Raising exceptions with extra values
------------------------------------

For assisting with debugging an exception object may be associated with extra values.
This feature is based on the idea that when an exception occurs, it is associated with the information that will be essential for analyzing the problem.

To associate an exception object with extra values just add a field `extraValues` to it. Example:

```python
try:
	with open(filePath, "r") as fin:
		....
except FileNotFoundError as ee:
	ee.extraValues = {
		"filePath": filePath
	}
	raise ee
```

If `jk_exceptionhelper.analyseException(...)` is invoked later this module will represent these extra values in the resulting `ExceptionObject` instance.

Serializing exception objects with extra values
-----------------------------------------------

However, attention must be paid to a conceptual detail here: Those extra values are not intendet to accurately model internal data structures of a program.
Extra values are intended to assist with debugging only.

On printing such values the printing logic will not know and shold not know about every kind of type of a program.
While typically an error message is intended for a user of a software to understand roughly what the problem is, these extra values are intendet as hints for the programmer.
Therefore these extra values should be considered as being hints in addition to a regular error message, providing more details for a quick analysis of the problem.
Therefore if you provide extra values, provide them in a way they can easily be printed later to a log file (or some other kind of repository).
Therefore those extra values should be compatible to the printing or serialization logic of errors.
These values are not intendet to exactly model internal data of the program.

To sum up: You should provide data values that can be easily converted to some kind of JSON representation.
This is considered being fundamental to this module and therefore is implemented in this module. Such conversion will occur immediately if you invoke `analyseException(...)`.
The resulting `ExceptionObject` will therefore already contain a JSON serializable interpretation of these extra values you might have provided.

At present values of `extraValues` you provide must adher to the following standard:

* standard JSON serializable types
	* `None` -> `None`
	* `bool` -> `bool`
	* `int` -> `int`
	* `float` -> `float`
	* `str` -> `str`
	* `list` -> `list` (recursively)
	* `dict` -> `dict` (recursively; keys that are not of type str are skipped.)
* additional JSON serializable types
	* `tuple` -> `list` (recursively)
	* `set` -> `list` (recursively)
	* `frozenset` -> `list` (recursively)
	* `OrderedDict` -> `dict` (recursively; keys that are not of type str are skipped.)
* callable method `dumpToStrList()` -> `{ "@class": "RawLines", "lines": .... }`
* callable method `toJSON()` -> `dict` or `list`
* callable method `_toJSON()` -> `dict` or `list`

Interpretation is performed in exactly the order listed above.

However, if something went wrong during conversion, the following `dict` will be returned:

```JavaScript
{ "@class": "SerializationError", "errMsg": "...." }
```

To give you an idea here is a more complex example:

```python
try:
	....
except Exception as ee:
	ee.extraValues = {
		"contextID": ctxID,
		"filePath": filePath,
		"user": user,
		"whatever": whatever,
	}
	raise ee
```

Let's asume that ...
* the context ID is an `int`,
* `filePath` is of type `str`,
* `user` contains an object that has a `toJSON()` method, and
* `whatever` has a special method `dumpToStr()` and `dumpToStrList()` to convert itself to a string and a string list.

Then after conversion to `ExceptionObject` you will contain to following extra values:

* for `contextID`: an integer value (as provided)
* for `filePath`: a string (as provided)
* for `user`: a `dict` that has been returned by `toJSON()`
* for `whatever`: a `dict` containing `{ "@class": "RawLines", "lines": .... }` that contains all text lines as returned by `dumpToStrList()`

As all extra values are JSON values the entire object `ExceptionObject` is JSON serializable.
This assists during printing or any kind of processing of such errors for debugging purposes.

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
	ee = jk_exceptionhelper.analyseException(ex)
	edata = ee.toJSON()
```

#### Method `dict toJSON_flat()`

`dict toJSON_flat()`

Same as `toJSON(False)`.

Arguments:

* (none)

Contact Information
-------------------

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



