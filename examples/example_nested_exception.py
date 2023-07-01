#!/usr/bin/python3



from jk_exceptionhelper import ExceptionObject





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

	except Exception as e:
		ee = ExceptionObject.fromException(e)
		ee.dump()




