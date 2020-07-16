# auto_pip


auto_pip is a Python library for creating a Python library,
and also manages versions and uploading to PyPi with twine

auto_pip runs in Python 3
## examples
you need to make
use_file.ini like this(see more options below):
```ini
[info]
# example with if...main that uses all imports from your library
test_file:test.py
author:test author
email=test.author@@
description =only for test
url=http://test.author.com
//dependencies
install_requires=mhyt,mhmovie
license:mit
```
and test.py like this:
```python
from my_test_library.file1 import plus
from my_test_library.file2 import minus
#
if __name__ == "__main__":
    plus(2,2)#4
    # ##############
    minus(11,1)#10
```

and the auto_pypi creates the following files automatically:
* setup.py
* __ init __.py
* License.txt 
* README.md

additional options for ini file (also in "info" key): 
```ini
#foldername with your library in it, then not all imports need
#to be in file
folder=foldername
#the version of the library
start_version:1.0.0
#cmd scripts or other files that you want in path, like in setuptools scripts.
#seperate scripts with commas.
scripts:script1.cmd,script2.exe
```

### Prerequisites
auto_pip depends on the python modules:

Markdown-Editor,
requests,
setuptools,
wheel
and twine

### Installing
To install with pip-
type in terminal:
```
(sudo) pip install auto_pip
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
This project is licensed under the mit License.
###created by
this library created by [auto_pip](https://github.com/matan-h/auto_pip)

