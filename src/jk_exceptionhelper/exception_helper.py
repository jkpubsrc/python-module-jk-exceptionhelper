

import collections
import traceback
import json
import sys


from .StackTraceItem import StackTraceItem
from .ExceptionObject import ExceptionObject





"""
def dump(obj, name=None, indent=""):
	if name:
		s = name + "="
	else:
		s = ""

	if obj is None:
		print(indent + s + "(none)")
		return

	if callable(obj):
		#print(indent + s + "(callable)")
		return

	if name in [ "f_builtins" ]:
		return

	if isinstance(obj, (int, str, bool, list, tuple, dict)):
		print(indent + s + repr(obj))
		return

	print(indent + s + obj.__class__.__name__)
	for p in dir(obj):
		if p in [ "__call__", "__class__" ]:
			continue
		dump(getattr(obj, p), p, indent + "\t")
#
"""


"""
#
# Processes the exception.
#
# @param	Exception exception		The exception to parse
#
def getExceptionData(exception:Exception):
	assert isinstance(exception, Exception)

	exceptionClassName = exception.__class__.__name__

	exceptionLines = []
	for line in str(exception).splitlines():
		line = line.strip()
		if len(line) > 0:
			exceptionLines.append(line)
	exceptionTextHR = " ".join(exceptionLines)
	if not exceptionTextHR:
		exceptionTextHR = None

	stackTrace = []
	stackTraceList = traceback.extract_stack(exception.__traceback__.tb_frame)
	for stackTraceComponent in stackTraceList:
		stackTrace.append(StackTraceItem(
			stackTraceComponent.filename,
			stackTraceComponent.lineno,
			stackTraceComponent.name,
			stackTraceComponent.line
			))

	return exceptionClassName, exceptionTextHR, stackTrace, exception.__context__
#
"""



def _analyseNestedException(exception) -> ExceptionObject:
	exceptionLines = []
	for line in str(exception).splitlines():
		line = line.strip()
		if len(line) > 0:
			exceptionLines.append(line)
	exceptionTextHR = " ".join(exceptionLines)
	if not exceptionTextHR:
		exceptionTextHR = None

	if exception.__context__:
		nestedException = _analyseNestedException(exception.__context__)
	else:
		nestedException = None


	return ExceptionObject(exception, exception.__class__.__name__, exceptionTextHR, None, nestedException)
#




def analyseException(exception, ignoreJKTypingCheckFunctionSignatureFrames:bool = False, ignoreJKTestingAssertFrames:bool = False) -> ExceptionObject:
	assert isinstance(ignoreJKTypingCheckFunctionSignatureFrames, bool)
	assert isinstance(ignoreJKTestingAssertFrames, bool)

	_type, _exception, _traceback = sys.exc_info()

	if _exception is None:
		_exception = exception
		_type = type(exception)

	exceptionLines = []
	for line in str(_exception).splitlines():
		line = line.strip()
		if len(line) > 0:
			exceptionLines.append(line)
	exceptionTextHR = " ".join(exceptionLines)
	if not exceptionTextHR:
		exceptionTextHR = None

	stackTrace = []
	#print("-X-------------------------------")
	#print("Type =", _type)
	#print("Value =", repr(str(_exception)))
	##print("Trace =")
	##print("Traceback=", _traceback)
	#print("Trace =", traceback.extract_tb(_traceback))
	for stElement in traceback.extract_tb(_traceback):
		#assert isinstance(stElement, traceback.FrameSummary)
		# print(">", repr(stElement.filename), "|", repr(stElement.name))
		if ignoreJKTypingCheckFunctionSignatureFrames:
			#if (stElement.name == "wrapped") \
			#	and (
			#		(stElement.filename.find("jk_typing/checkFunctionSignature.py") >= 0) or
			#		(stElement.filename.find("jk_typing\\checkFunctionSignature.py") >= 0)
			#	):
			if (
					(stElement.filename.find("jk_typing/checkFunctionSignature.py") >= 0) or
					(stElement.filename.find("jk_typing\\checkFunctionSignature.py") >= 0)
				):
				continue
		if ignoreJKTestingAssertFrames:
			if (
					(stElement.filename.find("jk_testing/Assert.py") >= 0) or
					(stElement.filename.find("jk_testing\\Assert.py") >= 0)
				):
				continue
		stackTrace.append(StackTraceItem(
			stElement.filename,
			stElement.lineno,
			stElement.name,
			stElement.line
			))
	#print("-X-------------------------------")

	if _exception.__context__:
		nestedException = _analyseNestedException(_exception.__context__)
	else:
		nestedException = None


	return ExceptionObject(_exception, _type.__name__, exceptionTextHR, stackTrace, nestedException)
#






