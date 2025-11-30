#!/usr/bin/python3


import traceback


def test():
    try:
        a = 0
        b = 5 / a
    except Exception as ee1:
        assert False



try:
	test()
except Exception as ee:
	print("|A|\t", repr(ee))
	stackTraceList = traceback.extract_stack(ee.__traceback__.tb_frame)
	#del stackTraceList[0]
	for frame in stackTraceList:
		print("|B|\t\t", frame)

	if ee.__context__:
		print("|C|\t", repr(ee.__context__))
		stackTraceList = traceback.extract_stack(ee.__context__.__traceback__.tb_frame)
		#del stackTraceList[0]
		for frame in stackTraceList:
			print("|D|\t\t", frame)









