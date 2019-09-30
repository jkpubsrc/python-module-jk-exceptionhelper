

# import collections

# StackTraceItem = collections.namedtuple("StackTraceItem", [
#	"filePath", "lineNo", "callingScope", "sourceCodeLine"
# ])


class StackTraceItem(object):
	
	def __init__(self, filePath:str, lineNo:int, callingScope:str, sourceCodeLine:str):
		assert isinstance(filePath, str)
		assert isinstance(lineNo, int)
		assert isinstance(callingScope, str)
		assert isinstance(sourceCodeLine, str)

		self.filePath = filePath
		self.lineNo = lineNo
		self.callingScope = callingScope
		self.sourceCodeLine = sourceCodeLine
	#

	def __str__(self):
		# return "(" + (self.callingScope if self.callingScope is not None else "(none)") + ", " + self.filePath + ":" + str(self.lineNo) + ", " + repr(self.sourceCodeLine) + ")"
		return "(" + self.filePath + ":" + str(self.lineNo) + ", " + repr(self.sourceCodeLine) + ")"
	#

	def __repr__(self):
		# return "(" + (self.callingScope if self.callingScope is not None else "(none)") + ", " + self.filePath + ":" + str(self.lineNo) + ", " + repr(self.sourceCodeLine) + ")"
		return "(" + self.filePath + ":" + str(self.lineNo) + ", " + repr(self.sourceCodeLine) + ")"
	#

	def toJSON(self) -> dict:
		return {
			"file": self.filePath,
			"line": self.lineNo,
			# "callingscope": self.callingScope,
			"sourcecode": self.sourceCodeLine,
		}
	#

	@staticmethod
	def fromJSON(data:dict):
		return StackTraceItem(
			data["file"],
			data["line"],
			# data["callingscope"],
			data["sourcecode"]
		)
	#

#


