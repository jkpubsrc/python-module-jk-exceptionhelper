################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: Apache Software License",
		"Topic :: Software Development :: Testing",
	],
	description = "As the python exception API is quite a bit obscure this python module wraps around python exceptions to provide a clean interface for analysis and logging purposes.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-exceptionhelper/tarball/0.2020.3.4",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"exception handling",
		"debugging",
	],
	license = "Apache 2.0",
	name = "jk_exceptionhelper",
	packages = [
		"jk_exceptionhelper",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-exceptionhelper",
	version = "0.2020.9.3",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
