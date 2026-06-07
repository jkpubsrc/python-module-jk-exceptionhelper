#!/usr/bin/python3


import json

from jk_exceptionhelper import ExceptionObject





JSON_EXCEPTION_DATA = """
{
	"text": "foo() has failed!",
	"exception": "Exception",
	"stacktrace": [
		{
			"file": "./example_serialize.py",
			"line": 31,
			"callingscope": "<module>",
			"sourcecode": "raise Exception(\\"foo() has failed!\\", ExceptionObject.fromException(ee1))"
		}
],
"nested": {
		"text": "division by zero",
		"exception": "ZeroDivisionError",
		"stacktrace": [
			{
				"file": "./example_serialize.py",
				"line": 29,
				"callingscope": "<module>",
				"sourcecode": "foo()"
			},
			{
				"file": "./example_serialize.py",
				"line": 24,
				"callingscope": "foo",
				"sourcecode": "bar()"
			},
			{
				"file": "./example_serialize.py",
				"line": 20,
				"callingscope": "bar",
				"sourcecode": "b = 5 / a"
			}
		],
		"nested": null
	}
}
"""

JSON_EXCEPTION = json.loads(JSON_EXCEPTION_DATA)

ee = ExceptionObject.fromJSON(JSON_EXCEPTION)
ee.dump()







