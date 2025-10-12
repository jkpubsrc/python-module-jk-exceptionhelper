#!/usr/bin/python3



import jk_exceptionhelper




class CustomException(Exception):

	def __init__(self, extraFloatValue:float):
		super().__init__("Custom exception!", extraFloatValue)
	#

#



print()
print("=" * 160)
print("== Custom exception")
print("=" * 160)
print()

try:

	raise CustomException(3.1415927)

except Exception as ee:
	jk_exceptionhelper.analyseException(ee).dump()










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
15	\\-
"""



















