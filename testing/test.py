#!/usr/bin/python3



import jk_exceptionhelper






print()
print("=" * 160)
print("== Regular exception")
print("=" * 160)
print()

try:

	a = 0
	b = 5 / a

except Exception as ee:
	jk_exceptionhelper.analyseException(ee).dump()



print()
print("=" * 160)
print("== Nested exception")
print("=" * 160)
print()

try:

	a = 0
	b = 5 / a

except Exception as ee1:
	try:

		assert False
	
	except Exception as ee:
		jk_exceptionhelper.analyseException(ee).dump()








"""
This example program will output the following lines:

 1
 2	================================================================================================================================================================
 3	== Regular exception
 4	================================================================================================================================================================
 5
 6	ZeroDivisionError
 7	: exceptionText:
 8	:       division by zero
 9	: stackTrace:
10	:       StackTraceItem(filePath='./test.py', lineNo=46, moduleName='<module>', sourceCodeLine='dumpException(ee)')
11	\-
12
13	================================================================================================================================================================
14	== Nested exception
15	================================================================================================================================================================
16
17	AssertionError
18	: stackTrace:
19	:       StackTraceItem(filePath='./test.py', lineNo=67, moduleName='<module>', sourceCodeLine='dumpException(ee)')
20	\- nested exception:
21			ZeroDivisionError
22			: exceptionText:
23			:       division by zero
24			: stackTrace:
25			:       StackTraceItem(filePath='./test.py', lineNo=67, moduleName='<module>', sourceCodeLine='dumpException(ee)')
26			\-
"""



















