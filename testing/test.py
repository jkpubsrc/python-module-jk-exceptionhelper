#!/usr/bin/python3



import jk_exceptionhelper



def _dumpException(exceptionClassName, exceptionText, stackTrace, indent=""):
	print(indent + exceptionClassName)
	if exceptionText is not None:
		print(indent + ": exceptionText:")
		print(indent + ":\t" + exceptionText)
	print(indent + ": stackTrace:")
	for item in stackTrace:
		print(indent + ":\t" + str(item))
#

def dumpException(e):
	indent = ""
	while True:
		exceptionClassName, exceptionText, stackTrace, e = jk_exceptionhelper.getExceptionData(e)
		_dumpException(exceptionClassName, exceptionText, stackTrace, indent)
		if e:
			print(indent + "\- nested exception:")
			indent += "\t"
		else:
			print(indent + "\-")
			break
#



print()
print("=" * 160)
print("== Regular exception")
print("=" * 160)
print()

try:

	a = 0
	b = 5 / a

except Exception as ee:
	dumpException(ee)



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
		dumpException(ee)








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



















