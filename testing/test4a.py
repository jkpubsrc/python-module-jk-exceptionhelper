#!/usr/bin/python3


import sys
import traceback



def test():
	try:

		a = 0
		b = 5 / a

	except Exception as ee1:
		try:

			assert False

		except Exception as ee:
			type_, value_, traceback_ = sys.exc_info()

			print(">>>>")
			print(type_)
			print(value_)
			print(traceback_)

			stackTraceList = traceback.extract_stack(traceback_.tb_frame)
			print(stackTraceList)

			#nestedExceptionStackTraceList = traceback.extract_stack(ee.__context__.__traceback__.tb_frame)
#


test()





