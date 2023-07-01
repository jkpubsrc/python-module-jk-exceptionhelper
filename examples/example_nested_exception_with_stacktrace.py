#!/usr/bin/python3



from jk_exceptionhelper import ExceptionObject





print()
print("=" * 160)
print("== Nested exception with stacktrace")
print("=" * 160)
print()

def bar():
	a = 0
	b = 5 / a
#

def foo():
	bar()
#

try:
	try:
		foo()
	except Exception as ee1:
		raise Exception("foo() has failed!", ExceptionObject.fromException(ee1))

except Exception as e:
	ee = ExceptionObject.fromException(e)
	ee.dump()



