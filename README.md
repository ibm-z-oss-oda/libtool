# auto_pip


auto_pip is a Python library for creating a Python library,
and also manages versions and uploading to PyPi with twine

auto_pip runs in Python 3+
auto_pip runs only in Windows
## Instructions
You need to make a
use_file.ini like this(see more options below):
```ini
[info]
# example with if...main that uses all imports from your library
test_file:test.py
# can also be test_file=your_test_file.py
author:test author
email=test.author@mail.com
description = description of the library
url=http://test.author.com
#dependencies
install_requires=mhyt,mhmovie
license:mit
```
and your test.py (Same as test_file above) like this:
```python
from my_test_library.file1 import plus
from my_test_library.file2 import minus
#
if __name__ == "__main__":
    plus(2,2)#4
    # ##############
    minus(11,1)#10
```
To create library from ini:
```
library c {your ini file}
#or
library create {your ini file}
```
And the auto_pip creates the following files automatically:

* setup.py
* __ init __.py
* License.txt 
* README.md

and the auto_pip will ask you if you want to edit readme.

To change version number:
```
library v
```
and the auto_pip ask "enter new version:".

To upload:
```
library upload
#or
library u
#you can add twine options e.g.
library u -r testpypi
```
Twine options [here](https://twine.readthedocs.io/en/latest/#twine-upload)

###Access from python
To access the auto_pip from python file:
```python
from auto_pip._cmd_argv import cmd
cmd.parse(["c", "use_file.ini"])
# or 
cmd.parse( ["u", "-r testpypi"])
#and all commands
```
## Prerequisites
auto_pip depends on the python modules:

Markdown-Editor,
requests,
setuptools,
wheel
and twine

## Installing
To install with pip-
type in terminal:
```
(sudo) pip install auto_pip
```
if this doesn't work try:
```
pip install --upgrade setuptools wheel
```
if there is still an error please open an issue in [github issues](https://github.com/matan-h/auto_pip/issues).

## Additional options
Additional options for ini file (also in "info" key): 
```ini
#foldername with your library in it, then not all imports need
#to be in file
folder=foldername 
#can also be folder:foldername
#the version of the library
start_version:1.0.0
#cmd scripts or other files that you want in path, like in setuptools scripts.
#separate scripts with commas.
scripts:script1.cmd,script2.exe
```

## Custom options
You can also set custom options using Python.
To create a library:
```python
from auto_pip.auto_pip_class import Library

l = Library(
    test_file="test.py",
    email="your.email@your_mail.com",
    description="only for test",
    url = "http://your.url.com",
    pylicense="mit",
    author="author",
    install_requires=["mhyt","mhmovie"],
    #and the additional options:
    folder="foldername",
    start_version="2.7.3",
    scripts=["script1.bat",]
)
#to create __init__.py
l.c_init()
#to create licence.txt
l.c_licence()
#to create setup.py
l.c_setup()
#to create readme.md
l.c_md()
#to edit readme.md
l.edit_md()
```
To change version:
```python
from auto_pip.up_version import UpVersion

u = UpVersion("foldername")
```
To publish to PyPi:
```python
from auto_pip.pypi.up_pypi import up
up("foldername")
#you can add twine options e.g.
up("foldername","-r testpypi")
```
## Built With
* [Markdown-Editor](https://github.com/ncornette/Python-Markdown-Editor.git) - for editing markdown files
* [requests](https://requests.readthedocs.io) - for HTTP request.
* [setuptools](https://github.com/pypa/setuptools) - for setup.py
* [wheel](https://github.com/pypa/wheel) - build help for library
* [twine](https://twine.readthedocs.io/) - for publishing packages on PyPI
## Author
matan h
## License
This project is licensed under the MIT License.
### Created by
This library was created using [auto_pip](https://github.com/matan-h/auto_pip)

