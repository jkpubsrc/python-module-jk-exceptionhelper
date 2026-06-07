

from .ExceptionObject import ExceptionObject





#
# Parse a Python exception object and constructs an <c>ExceptionObject</c> instance from it.
#
# @param	BaseException exception								(required) The exception object.
# @param	bool ignoreJKTypingCheckFunctionSignatureFrames		(required) Flag to ignore stack frames from "jk_typing/checkFunctionSignature.py".
# 																Such stacking frames don't help but distract from the essentials.
# @param	bool ignoreJKTestingAssertFrames					(required) Flag to ignore stack frames from "jk_testing/Assert.py".
# 																Such stacking frames don't help but distract from the essentials.
# @param	bool ignoreJKLoggingFrames							(required) Flag to ignore stack frames from "jk_logging".
# 																Such stacking frames don't help but distract from the essentials.
#
def analyseException(
		exception,
		*,
		ignoreJKTypingCheckFunctionSignatureFrames:bool = True,
		ignoreJKTestingAssertFrames:bool = True,
		ignoreJKLoggingFrames:bool = True,
		ignoreJKPrettyPrintObjFrames:bool = True,
	) -> ExceptionObject:
	return ExceptionObject.fromException(exception, ignoreJKTypingCheckFunctionSignatureFrames, ignoreJKTestingAssertFrames, ignoreJKLoggingFrames, ignoreJKPrettyPrintObjFrames)
#






