#!/usr/bin/python3


import jk_exceptionhelper
import sys
import traceback



def test():
	try:
		a = 0
		b = 5 / a
	except Exception as ee1:
		assert False
#



def analyse():
	type_, value_, traceback_ = sys.exc_info()

	print("--------------------------------")
	print("Type =", type_)
	print("Value =", repr(str(value_)))
	print("Trace =")
	#print("Traceback=", traceback_)
	#print("Trace =", traceback.extract_tb(traceback_))
	for stElement in traceback.extract_tb(traceback_):
		assert isinstance(stElement, traceback.FrameSummary)
		fileName = stElement.filename
		lineNo = stElement.lineno
		moduleName = stElement.name
		code = stElement.line
		print("\t", (fileName, lineNo, moduleName, code))
	print("--------------------------------")
#



try:
	test()
except Exception as ee1:
	jk_exceptionhelper.analyseException().dump()

	try:
		raise type(ee1.__context__) from ee1
	except Exception as ee2:
		jk_exceptionhelper.analyseException().dump()




