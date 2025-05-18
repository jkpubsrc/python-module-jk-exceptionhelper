

__all__ = (
	"ExceptionObject",
)

import typing

from .StackTraceItem import StackTraceItem





#
# A stack trace processor that can return a modified version of the stack trace (e.g. a shortened one).
# The stack is listed from the bottom: The trace item at position <c>0</c> is the lowest stack trace item,
# the item at position <c>length-1</c> is the top most item.
#
StackTraceProcessor = typing.Callable[[
	BaseException,
	typing.List[StackTraceItem]
],
	typing.List[StackTraceItem]
]








