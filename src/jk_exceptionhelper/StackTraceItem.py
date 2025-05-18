

__all__ = (
	"ExceptionObject",
)





class StackTraceItem(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

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

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self):
		return self.filePath + ":" + str(self.lineNo) + " :: " + repr(self.sourceCodeLine)
	#

	def __repr__(self):
		return self.filePath + ":" + str(self.lineNo) + " :: " + repr(self.sourceCodeLine)
	#

	def toJSON(self) -> dict:
		return {
			"file": self.filePath,
			"line": self.lineNo,
			"callingscope": self.callingScope,
			"sourcecode": self.sourceCodeLine,
		}
	#

	def __eq__(self, other):
		if isinstance(other, StackTraceItem):
			return (other.filePath == self.filePath) and (other.lineNo == self.lineNo)
		else:
			return False
	#

	def __ne__(self, other):
		if isinstance(other, StackTraceItem):
			return (other.filePath != self.filePath) or (other.lineNo != self.lineNo)
		else:
			return True
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

	@staticmethod
	def fromJSON(data:dict):
		assert isinstance(data, dict)
		return StackTraceItem(
			data["file"],
			data["line"],
			data["callingscope"],
			data["sourcecode"]
		)
	#

#


