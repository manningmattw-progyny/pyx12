# Pyx12

[![Build Status](https://travis-ci.org/azoner/pyx12.png?branch=master)](https://travis-ci.org/azoner/pyx12)
<!-- [![Coverage Status](https://coveralls.io/repos/azoner/pyx12/badge.png?branch=master)](https://coveralls.io/r/azoner/pyx12?branch=master) -->

Pyx12 is a HIPAA X12 document validator and converter.  It parses an ANSI X12N data file and validates it against a representation of the Implementation Guidelines for a HIPAA transaction.  By default, it creates a 997 response for 4010 and a 999 response for 5010. It can create an html representation of the X12 document or can translate to and from an XML representation of the data file.

# Usage

As a command line tool

    x12valid <filename>

To fix common X12 structural errors

    x12norm --fix --eol <filename>

# Code Examples

    Iterate over a loop.  Alter children. Show changes
```python
    src = pyx12.x12context.X12ContextReader(param, errh, fd_in)
    for datatree in src.iter_segments('2300'):
        # do something with a 2300 claim loop
        # we have access to the 2300 loop and all its children
        for loop2400 in datatree.select('2400'):
            print(loop2400.get_value('SV101'))
            # update something
            loop2400.set_value('SV102', 'xx')
            # delete something
            if loop2400.exists('PWK'):
                loop2400.delete('PWK')
        # iterate over all the child segments
        for seg_node in datatree.iterate_segments():
            print(seg_node.format())
```

# Prerequisites

## Python <= 3.7 (setuptools needed)
Pyx12 uses setuptools for build/install on these versions. If you use pip to install, all is good. If not, install setuptools first.
- Get setuptools <http://pypi.python.org/pypi/setuptools/>
- Get pip <http://www.pip-installer.org/en/latest/installing.html>

## Python >= 3.8 (only stdlib needed)
Pyx12 functions as expected in all known modern versions of Python and setuptools is no longer required.

# Install

Install system-wide

- `pip install pyx12`

Or install in a virtual environment

- `virtualenv my_env`
- `pip -E my_env install pyx12`

# Development (tests, build, upload)

The commands below are split by Python version because the build backend differs.

### Python <= 3.7 (setuptools build)

- Create and activate a virtual environment.
- Install dev/test dependencies.
  - `pip install -r requirements.dev.txt`
- Run tests.
  - `nosetests --with-coverage --cover-tests --cover-package=pyx12 --cover-erase`
- Build source and wheel distributions.
  - `python setup.py sdist`
  - `python setup.py bdist_wheel`
- Upload (legacy setuptools upload commands). **Only codeowners with access to the pyx12 PyPI project should run uploads.**
  - `python setup.py sdist upload -r pypitest`
  - `python setup.py bdist_wheel upload -r pypitest`
  - `python setup.py sdist upload`
  - `python setup.py bdist_wheel upload`

### Python >= 3.8 (hatchling build)

- Create and activate a virtual environment.
- Install build tool.
  - `pip install build`
- Run tests (same as above).
  - `pip install -r requirements.dev.txt`
  - `nosetests --with-coverage --cover-tests --cover-package=pyx12 --cover-erase`
- Build source and wheel distributions.
  - `python -m build`
- Upload (twine recommended). **Only codeowners with access to the pyx12 PyPI project should run uploads.**
  - `python -m pip install twine`
  - `python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
  - `python -m twine upload dist/*`

### Release (optional)

- Update version strings in `setup.py`, `pyx12/__init__.py`, and `pyx12/version.py`
- Verify CI is green
- Tag the release and push the tag
  - `git tag vX.Y.Z`
  - `git push origin vX.Y.Z`

# Licensing

Pyx12 has a BSD license. The full license text is included with the source code for the package.
