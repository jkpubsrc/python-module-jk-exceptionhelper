#!/usr/bin/python3



from jk_exceptionhelper import ExceptionObject



print()
print("=" * 160)
print("== Exception in deeper level")
print("=" * 160)
print()


def main3():
	a = 0
	b = 5 / a
#

def main2():
	main3()
#

def main1():
	main2()
#

try:
	main1()
except Exception as e:
	ee = ExceptionObject.fromException(e)
	ee.dump()

















"""
This example program will output the following lines:

 1
 2	================================================================================================================================================================
 3	== Regular exception
 4	================================================================================================================================================================
 5
 6	ZeroDivisionError
 7	: exceptionTextHR:
 8	:       division by zero
 9	: stackTrace:
10	:	(./test2.py:18, 'b = 5 / a')
11	\-
12
13	================================================================================================================================================================
14	== Nested exception
15	================================================================================================================================================================
16
17	AssertionError
18	: stackTrace:
19	:	(./test2.py:39, 'assert False')
20	\- nested exception:
21			ZeroDivisionError
22			: exceptionTextHR:
23			:       division by zero
26			\-
27
28	================================================================================================================================================================
29	== Exception in deeper level
30	================================================================================================================================================================
31
32	ZeroDivisionError
33	: exceptionTextHR:
34	:	division by zero
35	: stackTrace:
36	:	(./test2.py:55, 'b = 5 / a')
37	:	(./test2.py:59, 'main3()')
38	:	(./test2.py:63, 'main2()')
39	:	(./test2.py:67, 'main1()')
40	\-
"""



















