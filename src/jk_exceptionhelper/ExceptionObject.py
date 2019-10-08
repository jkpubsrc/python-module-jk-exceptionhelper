


from .StackTraceItem import StackTraceItem




class ExceptionObject(object):

	def __init__(self, exceptionClass, exceptionClassName:str, exceptionTextHR:str, stackTrace:list, nestedException):
		self.exceptionClass = exceptionClass

		self.exceptionClassName = exceptionClassName

		if exceptionTextHR is not None:
			assert isinstance(exceptionTextHR, str)
		self.exceptionTextHR = exceptionTextHR

		if stackTrace is not None:
			assert isinstance(stackTrace, (list, tuple))
			for item in stackTrace:
				assert isinstance(item, StackTraceItem)
			self.stackTrace = stackTrace
		else:
			self.stackTrace = None

		if nestedException is not None:
			assert isinstance(nestedException, ExceptionObject)
		self.nestedException = nestedException
	#

	def toStrList(self):
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
			if e.nestedException:
				e = e.nestedException
				outStrList.append(indent + "\- nestedException:")
				indent += "\t"
			else:
				outStrList.append(indent + "\-")
				break

		return outStrList
	#

	def dump(self):
		e = self
		indent = ""
		while True:
			print(indent + e.exceptionClassName)
			if e.exceptionTextHR is not None:
				print(indent + ": exceptionTextHR:")
				print(indent + ":\t" + e.exceptionTextHR)
			if e.stackTrace is not None:
				print(indent + ": stackTrace:")
				for item in reversed(e.stackTrace):
					print(indent + ":\t" + str(item))
			if e.nestedException:
				e = e.nestedException
				print(indent + "\- nestedException:")
				indent += "\t"
			else:
				print(indent + "\-")
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
		if self.stackTrace is not None:
			ret["stacktrace"] = [ x.toJSON() for x in self.stackTrace ]
		if bRecursive and self.nestedException:
			ret["nested"] = self.nestedException.toJSON()
		else:
			ret["stacktrace"] = None
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
		if self.stackTrace is not None:
			ret["stacktrace"] = [ x.toJSON() for x in self.stackTrace ]
		else:
			ret["stacktrace"] = None
		return ret
	#

	@staticmethod
	def fromJSON(data:dict) -> StackTraceItem:
		return ExceptionObject(
			None,
			data["exception"],
			data["text"],
			([ StackTraceItem.fromJSON(x) for x in data["stacktrace"] ]) if data.get("stacktrace") else None,
			ExceptionObject.fromJSON(data["nested"]) if data.get("nested") else None
		)
	#

#












