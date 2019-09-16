# Python-String-Alphanum-Sort
[![Python](https://img.shields.io/badge/python-2.7.1-blue.svg?style=popout)](https://www.python.org/downloads/release/python-271/)
[![Python](https://img.shields.io/badge/python-3.4.0-blue.svg?style=popout)](https://www.python.org/downloads/release/python-340/)
[![build](https://travis-ci.org/dyhe83/Python-String-Alphanum-Sort.svg?branch=master)](https://travis-ci.org/dyhe83/Python-String-Alphanum-Sort)


## Introduction
* A python version alphanumeric sorter.
* this program is modified from http://www.davekoelle.com/files/alphanum.py_v2.4
* [Alphanum algorithm](http://www.davekoelle.com/alphanum.html)
* Support
  * Python 2
  * Python 3


## How to use
```sh
git clone https://github.com/dyhe83/Python-String-Alphanum-Sort.git --depth=1
cd Python-String-Alphanum-Sort

python alphanum.py
# python3 alphanum.py
```


## Example
```sh
test_strings = ['1', '10', '2', '3']

# after sort
1
2
3
10
```

```sh
test_strings = ['1', '2', '3', '10', '1a1', '1a2', '1b', '1a', '1 a 2', '1 a 1', '1 b', '1 a']

# after sort
1
1 a
1 a 1
1 a 2
1 b
1a
1a1
1a2
1b
2
3
10
```
