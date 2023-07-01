#!/usr/bin/python3


import json

from jk_exceptionhelper import ExceptionObject





print()
print("=" * 160)
print("== Serialize a nested exception with stacktrace")
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

	linesOrg = ee.toStrList()
	jData = ee.toJSON()






ee = ExceptionObject.fromJSON(jData)
lines2 = ee.toStrList()

assert len(linesOrg) ==  len(lines2)
for lineOrg, line2 in zip(linesOrg, lines2):
	if lineOrg != line2:
		print("lineOrg: " + repr(lineOrg))
		print("  line2: " + repr(line2))
		assert False








