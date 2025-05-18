

from .ExceptionObject import ExceptionObject






def analyseException(exception, ignoreJKTypingCheckFunctionSignatureFrames:bool = False, ignoreJKTestingAssertFrames:bool = False, ignoreJKLoggingFrames:bool = False) -> ExceptionObject:
	return ExceptionObject.fromException(exception, ignoreJKTypingCheckFunctionSignatureFrames, ignoreJKTestingAssertFrames, ignoreJKLoggingFrames)
#






