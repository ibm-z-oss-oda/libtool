# auto_pip


auto_pip is a Python library for creating library

auto_pip runs in Python 3
## examples
all you need is to make
use_file.ini like this:
```ini
[info]
test_file:test.py
author:test author
email=test.author@@
description =only for test
url=http://test.author.com
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
###created by
if you want more examples:

this library created by [auto_pip](https://github.com/matan-h/auto_pip)
## Author
matan h
## License
This project is licensed under the mit License.

