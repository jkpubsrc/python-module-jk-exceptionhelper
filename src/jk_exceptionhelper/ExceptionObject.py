

__all__ = (
	"ExceptionObject",
)

import typing
import collections
import traceback

from .StackTraceItem import StackTraceItem
from .StackTraceProcessor import StackTraceProcessor






# def _analyseNestedException(exception) -> ExceptionObject:
# 	print(">4>>", type(exception.__traceback__), exception.__traceback__)
#
# 	exceptionLines = []
# 	for line in str(exception).splitlines():
# 		line = line.strip()
# 		if len(line) > 0:
# 			exceptionLines.append(line)
# 	exceptionTextHR = " ".join(exceptionLines)
# 	if not exceptionTextHR:
# 		exceptionTextHR = None
#
# 	if exception.__context__:
# 		nestedException = _analyseNestedException(exception.__context__)
# 	else:
# 		nestedException = None
#
# 	return ExceptionObject(exception, exception.__class__.__name__, exceptionTextHR, None, nestedException)
# #






#
# This method recursively converts an extra value to a JSON representation.
#
# The following type conversions will be performed:
# * None -> None
# * bool -> bool
# * int -> int
# * float -> float
# * str -> str
# * list -> list (recursively)
# * tuple -> list (recursively)
# * set -> list (recursively)
# * frozenset -> list (recursively)
# * dict -> dict (recursively; keys that are not of type str are skipped.)
# * callable method dumpToStrList() -> { "@class": "RawLines", "lines": .... }
# * callable method toJSON() -> dict
# * callable method _toJSON() -> dict
#
# If something went wrong during conversion, the following dict will be returned:
#
# { "@class": "SerializationError", "errMsg": "...." }
#
def _anyToJSON(value) -> typing.Union[dict,list,int,str,float,bool,None]:
	if value is None:
		return None

	# ----

	if isinstance(value, (bool,int,float,str)):
		return value

	if isinstance(value, (dict,collections.OrderedDict)):
		ret = {}
		for k, v in value.items():
			if not isinstance(k, str):
				continue
			ret[k] = _anyToJSON(v)
		return ret

	if isinstance(value, (set,frozenset,tuple,list)):
		return [
			_anyToJSON(x) for x in value
		]

	# ----

	if hasattr(value, "dumpToStrList"):
		try:
			return {
				"@class": "RawLines",
				"lines": value.dumpToStrList(),
			}
		except Exception as ee:
			return {
				"@class": "SerializationError",
				"errMsg": f"Calling dumpToStrList() failed: {ee}",
			}

	# ----

	if hasattr(value, "toJSON"):
		try:
			toJSONResult = value.toJSON()
			if toJSONResult is not None:
				assert isinstance(toJSONResult, (int,str,bool,float,dict,list))
			return toJSONResult
		except Exception as ee:
			return {
				"@class": "SerializationError",
				"errMsg": f"Calling toJSON() failed: {ee}",
			}

	if hasattr(value, "_toJSON"):
		try:
			toJSONResult = value._toJSON()
			if toJSONResult is not None:
				assert isinstance(toJSONResult, (int,str,bool,float,dict,list))
			return toJSONResult
		except Exception as ee:
			return {
				"@class": "SerializationError",
				"errMsg": f"Calling _toJSON() failed: {ee}",
			}

	# ----

	return {
		"@class": "SerializationError",
		"errMsg": f"Not serializable to JSON: {value.__class__.__name__}",
	}
#







ExceptionObject = typing.NewType("ExceptionObject", object)

class ExceptionObject(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor.
	#
	# @param	type? exceptionClass				(optional) The exception class this object will represent.
	#												Typically this parameter contains a value.
	#												However, if an instance of ExceptionObject is reconstructed from JSON or other data this value might not be available any more.
	# @param	str exceptionClassName				(required) The name of the exception calss this object will represent.
	# @param	str exceptionTextHR					(required) A human readable (= HR) text message.
	# @param	StackTraceItem[] stackTrace			(required) The stack trace of this exception in descending order: The last entry will be the top of the stack.
	# @param	ExceptionObject? nestedException	(optional) A nested exception (if any)
	# @param	dict<str,any>? extraValues			(optional) An optional dictionary with extra values.
	#												These values should be JSON serializable for printing.
	#
	def __init__(self,
			exceptionClass:type|None,
			exceptionClassName:str, 
			exceptionTextHR:str,
			stackTrace:typing.List[StackTraceItem],
			nestedException:ExceptionObject|None,
			extraValues:typing.Union[typing.Dict[str,typing.Any],None] = None,
		):
		self.exceptionClass:type|None = exceptionClass

		self.exceptionClassName:str = exceptionClassName

		if exceptionTextHR is not None:
			assert isinstance(exceptionTextHR, str)
		self.exceptionTextHR:str = exceptionTextHR

		if stackTrace is not None:
			assert isinstance(stackTrace, (list, tuple))
			for item in stackTrace:
				assert isinstance(item, StackTraceItem)
			self.stackTrace:typing.List[StackTraceItem] = stackTrace
		else:
			self.stackTrace:typing.List[StackTraceItem] = None

		if nestedException is not None:
			assert isinstance(nestedException, ExceptionObject)
		self.nestedException = nestedException

		if extraValues is not None:
			assert isinstance(extraValues, dict)
		self.extraValues = extraValues
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def toStrList(self) -> typing.List[str]:
		outStrList = []

		e = self
		indent = ""
		while True:
			outStrList.append(indent + e.exceptionClassName)

			if e.exceptionTextHR is not None:
				outStrList.append(indent + ": exceptionTextHR:")
				outStrList.append(indent + ":\t" + e.exceptionTextHR)

			if e.stackTrace is not None:
				outStrList.append(indent + ": stackTrace:")
				for item in reversed(e.stackTrace):
					outStrList.append(indent + ":\t" + str(item))

			if e.extraValues:
				outStrList.append(indent + ": extraValues:")
				for k,v in e.extraValues.items():
					outStrList.append(indent + f":\t{k} = {v!r}")

			if e.nestedException:
				e = e.nestedException
				outStrList.append(indent + "\\- nestedException:")
				indent += "\t"
			else:
				outStrList.append(indent + "\\-")
				break

		return outStrList
	#

	def dump(self, prefix:str = "") -> None:
		e = self
		indent = prefix
		while True:
			print(indent + e.exceptionClassName)

			if e.exceptionTextHR is not None:
				print(indent + ": exceptionTextHR:")
				print(indent + ":\t" + e.exceptionTextHR)

			if e.stackTrace is not None:
				print(indent + ": stackTrace:")
				for item in reversed(e.stackTrace):
					print(indent + ":\t" + str(item))

			if e.extraValues:
				print(indent + ": extraValues:")
				for k,v in e.extraValues.items():
					print(indent + f":\t{k} = {v!r}")

			if e.nestedException:
				e = e.nestedException
				print(indent + "\\- nestedException:")
				indent += "\t"
			else:
				print(indent + "\\-")
				break
	#

	#
	# Convert this object to JSON (recursively).
	#
	# @param	bool bRecursive		If `True` (which is the default) nested exceptions are serialized as well. If `False` these get skipped.
	#
	def toJSON(self, bRecursive:bool = True) -> dict:
		ret = {
			"text": self.exceptionTextHR,
			"exception": self.exceptionClassName,
		}

		if self.stackTrace is None:
			ret["stacktrace"] = None
		else:
			ret["stacktrace"] = [ x.toJSON() for x in self.stackTrace ]

		if self.extraValues is not None:
			ret["extraValues"] = self.extraValues

		if bRecursive and self.nestedException:
			ret["nested"] = self.nestedException.toJSON()
		else:
			ret["nested"] = None

		return ret
	#

	#
	# Convert this object to JSON (only this level).
	#
	def toJSON_flat(self):
		ret = {
			"text": self.exceptionTextHR,
			"exception": self.exceptionClassName,
		}

		if self.stackTrace is None:
			ret["stacktrace"] = None
		else:
			ret["stacktrace"] = [ x.toJSON() for x in self.stackTrace ]

		if self.extraValues is not None:
			ret["extraValues"] = self.extraValues

		return ret
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

	@staticmethod
	def fromJSON(data:dict):
		assert isinstance(data, dict)
		return ExceptionObject(
			None,
			data["exception"],
			data["text"],
			([ StackTraceItem.fromJSON(x) for x in data["stacktrace"] ]) if data.get("stacktrace") else None,
			ExceptionObject.fromJSON(data["nested"]) if data.get("nested") else None,
			data.get("extraValues")
		)
	#

	#
	# This method parses a Python exception object and constructs an <c>ExceptionObject</c> instance from it.
	#
	# @param	BaseException exception								(required) The exception object.
	# @param	bool ignoreJKTypingCheckFunctionSignatureFrames		(required) Flag to ignore stack frames from "jk_typing/checkFunctionSignature.py".
	# 																Such stacking frames don't help but distract from the essentials.
	# @param	bool ignoreJKTestingAssertFrames					(required) Flag to ignore stack frames from "jk_testing/Assert.py".
	# 																Such stacking frames don't help but distract from the essentials.
	# @param	bool ignoreJKLoggingFrames							(required) Flag to ignore stack frames from "jk_logging".
	# 																Such stacking frames don't help but distract from the essentials.
	# @param	bool _bWithFullStackTrace							(required) ???
	# @param	StackTraceProcessor? stackTraceProcessor			(optional) An optional stack trace processor that can return a modified version of the stack trace (e.g. a shortened one).
	#																If specified the stack trace will be passed through the stack trace processor before an instance of <c>ExceptionObject</c> is constructed.
	#
	@staticmethod
	def fromException(
			exception:BaseException,
			ignoreJKTypingCheckFunctionSignatureFrames:bool = False,
			ignoreJKTestingAssertFrames:bool = False,
			ignoreJKLoggingFrames:bool = False,
			_bWithFullStackTrace:bool = True,
			stackTraceProcessor:typing.Union[StackTraceProcessor,None] = None
		) -> ExceptionObject:

		assert isinstance(exception, BaseException)
		assert isinstance(ignoreJKTypingCheckFunctionSignatureFrames, bool)
		assert isinstance(ignoreJKTestingAssertFrames, bool)
		assert isinstance(ignoreJKLoggingFrames, bool)

		# ----

		_args = exception.args
		nestedException = None
		if _args and isinstance(_args[-1], ExceptionObject):
			nestedException = _args[-1]
			_args = _args[:-1]

		if len(_args) == 0:
			sArgs = ""
		elif len(_args) == 1:
			sArgs = str(_args[0])
		else:
			sArgs = str(_args)

		exceptionLines:typing.List[str] = []
		for line in sArgs.splitlines():
			line = line.strip()
			if len(line) > 0:
				exceptionLines.append(line)
		exceptionTextHR = " ".join(exceptionLines)
		if not exceptionTextHR:
			exceptionTextHR = None

		# ----

		stackTrace1:typing.List[StackTraceItem] = []
		for stElement in traceback.extract_tb(exception.__traceback__):
			if ignoreJKTypingCheckFunctionSignatureFrames:
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
			if ignoreJKLoggingFrames:
				if (
						(stElement.filename.find("jk_logging/") >= 0) or
						(stElement.filename.find("jk_logging\\") >= 0)
					):
					continue
			stackTrace1.append(StackTraceItem(
				stElement.filename,
				stElement.lineno,
				stElement.name,
				stElement.line
			))

		stackTrace2:typing.List[StackTraceItem] = []
		if _bWithFullStackTrace:
			for stElement in traceback.extract_stack():
				if ignoreJKTypingCheckFunctionSignatureFrames:
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
				if ignoreJKLoggingFrames:
					if (
							(stElement.filename.find("jk_logging/") >= 0) or
							(stElement.filename.find("jk_logging\\") >= 0)
						):
						continue
				stackTrace2.append(StackTraceItem(
					stElement.filename,
					stElement.lineno,
					stElement.name,
					stElement.line
				))

			# remove last stacktrace item as it represents a line in the current method
			del stackTrace2[-1]

		stackTrace = stackTrace2
		stackTrace.extend(stackTrace1)

		# ----

		if stackTraceProcessor:
			stackTrace = stackTraceProcessor(exception, stackTrace)

		# ----

		_exceptionArgs = exception.args[1:]
		# NOTE: we don't do anything with these values right now.

		# ----

		extraValues:typing.Union[dict,None] = None
		_extraValues = getattr(exception, "extraValues", None)
		if _extraValues:
			if isinstance(_extraValues, dict):
				extraValues = _anyToJSON(_extraValues)

		# ----

		# if not nestedException:
		# 	if hasattr(exception, "cause"):
		# 		_n = exception.cause
		# 		if isinstance(_n, ExceptionObject):
		# 			nestedException = _n
		# 		else:
		# 			if exception.__context__:
		# 				nestedException = _analyseNestedException(exception.__context__)
		if not nestedException:
			if exception.__context__:
				nestedException = ExceptionObject.fromException(
					exception.__context__,
					ignoreJKTypingCheckFunctionSignatureFrames,
					ignoreJKTestingAssertFrames,
					ignoreJKLoggingFrames,
					False,
					stackTraceProcessor,
				)

		return ExceptionObject(exception, type(exception).__name__, exceptionTextHR, stackTrace, nestedException, extraValues)
	#

#












