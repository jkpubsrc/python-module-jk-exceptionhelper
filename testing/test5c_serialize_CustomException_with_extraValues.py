#!/usr/bin/python3


import typing

import jk_exceptionhelper
import jk_json
import jk_prettyprintobj






class WhateverUnserializable(object):
	pass
#



class WhateverDumpable(jk_prettyprintobj.DumpMixin):
	def __init__(self):
		self.whatever = "whatever"
	#

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"whatever",
		]
	#
#



class WhateverDumpableWithError(jk_prettyprintobj.DumpMixin):
	def __init__(self):
		self.whatever = "whatever"
	#

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"whateverXYZ",
		]
	#
#



class WhateverToJSONConvertable(object):
	def __init__(self):
		self.whatever = "whatever"
	#

	def toJSON(self) -> dict:
		return {
			"whatever": self.whatever,
		}
	#
#



class WhateverToJSONConvertableWithError(object):
	def __init__(self):
		self.whatever = "whatever"
	#

	def toJSON(self) -> dict:
		raise Exception("Foo!")
	#
#



class CustomException(Exception):

	def __init__(self):
		super().__init__("Custom exception!")
		self.extraValues = {
			"aStr": "foo",
			"aFloat": 3.1415927,
			"anInt": 123,
			"aBool": True,
			"aList": [ "foo", "bar" ],
			"aDict": { "foo": "bar" },
			"anUnserializable": WhateverUnserializable(),
			"aDumpable": WhateverDumpable(),
			"aConvertable": WhateverToJSONConvertable(),
			"erroneousConvertable": WhateverToJSONConvertableWithError(),
			"erroneousDumpable": WhateverDumpableWithError(),
		}
	#

#



print()
print("=" * 160)
print("== Custom exception")
print("=" * 160)
print()

try:

	raise CustomException()

except Exception as ee:
	eo = jk_exceptionhelper.analyseException(ee)
	jDict = eo.toJSON()
	jk_json.prettyPrint(jDict)










"""
This example program will output the following lines:

 1
 2	================================================================================================================================================================
 3	== Custom exception
 4	================================================================================================================================================================
 5
 6	ZeroDivisionError
 7	: exceptionText:
 8	:       Custom exception!
 9	: stackTrace:
10	:       ./test5.py:29 :: 'raise CustomException(3.1415927)'
11  :       /usr/local/lib/python3.8/dist-packages/jk_exceptionhelper/exception_helper.py:11 :: 'return ExceptionObject.fromException(exception, ignoreJKTypingCheckFunctionSignatureFrames, ignoreJKTestingAssertFrames, ignoreJKLoggingFrames)'
12  :       ./test5.py:32 :: 'jk_exceptionhelper.analyseException(ee).dump()'
13  : extraValues:
14  :       aFloat = 3.1415927
15	\-
"""



















