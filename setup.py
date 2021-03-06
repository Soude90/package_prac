import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'package_prac', #this should be unique
	include_package_data=True,
	version = '0.1.3',
	author = 'Soumyadeep Barman',
	author_email = 'soumronaldo09@gmail.com',
	description = 'This is preprocessing package for checking',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)