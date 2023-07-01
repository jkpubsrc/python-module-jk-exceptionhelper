

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



def analyseException(exception, ignoreJKTypingCheckFunctionSignatureFrames:bool = False, ignoreJKTestingAssertFrames:bool = False) -> ExceptionObject:
	return ExceptionObject.fromException(exception, ignoreJKTypingCheckFunctionSignatureFrames, ignoreJKTestingAssertFrames)
#






