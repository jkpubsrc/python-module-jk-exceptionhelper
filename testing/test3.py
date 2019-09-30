#!/usr/bin/python3



import sys
import traceback

from jk_exceptionhelper import parseException, ExceptionObject

import jk_json



def test2():
	try:

		a = 0
		b = 5 / a

	except Exception as ee1:
		try:

			assert False

		except Exception as ee:
			etype_, value_, traceback_ = sys.exc_info()
			print(">>X>>>>X>>>>X>>>>X>>")
			#t = traceback.TracebackException(type(value_), value_, traceback_, limit=None)
			#print(traceback.format_exception(etype_, value_, traceback_))
			#print(t.exc_traceback)
			stackTraceList = traceback.extract_tb(traceback_)
			print(stackTraceList)
			print(">>X>>>>X>>>>X>>>>X>>")

			# store as JSON
			jsonData = parseException(ee).toJSON()
			# now let's output that JSON data
			jk_json.prettyPrint(jsonData)
			# now a test to parse JSON
			obj = ExceptionObject.fromJSON(jsonData)
#


def test1():
	test2()
#

test1()




"""
This example program will output the following JSON data:

{
	"exception": "AssertionError",
	"text": null
	"stacktrace": [
		{
			"file": "./test3.py",
			"line": 29,
			"module": "<module>",
			"sourcecode": "test()"
		},
		{
			"file": "./test3.py",
			"line": 23,
			"module": "test",
			"sourcecode": "jsonData = parseException(ee).toJSON()"
		}
	],
	"nested": {
		"exception": "ZeroDivisionError",
		"text": "division by zero"
		"stacktrace": [
			{
				"file": "./test3.py",
				"line": 29,
				"module": "<module>",
				"sourcecode": "test()"
			},
			{
				"file": "./test3.py",
				"line": 23,
				"module": "test",
				"sourcecode": "jsonData = parseException(ee).toJSON()"
			}
		],
	},
}
"""



















