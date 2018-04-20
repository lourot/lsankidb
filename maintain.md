# Release a new version

## Increase the version number

In [lsankidb/\__init\__.py](lsankidb/__init__.py) to `7.8.9` in this example.

## Generate the package to be published

```
$ python3 setup.py sdist
```

And check that the resulting `dist/lsankidb-7.8.9.tar.gz` looks well-formed.

## Install the package locally

```
$ sudo -H pip3 install --upgrade dist/lsankidb-7.8.9.tar.gz
```

and test it briefly, e.g.

```
$ lsankidb --version
$ lsankidb
```

## Commit your changes, create a git tag and push

```
$ git add -u
$ git commit -m "Version 7.8.9"
$ git push
$ git tag "7.8.9"
$ git push --tags
```

## Push the package to PyPI Test

Create `~/.pypirc` as follows:

```
[distutils]
index-servers =
    pypiprod
    pypitest

[pypiprod]
repository: https://upload.pypi.org/legacy/
username:lourot
password:mypassword

[pypitest]
repository: https://test.pypi.org/legacy/
username:lourot
password:mypassword
```

and push:

```
$ python3 setup.py sdist upload -r pypitest
```

Finally check that the package looks well-formed at `https://test.pypi.org/pypi/lsankidb/7.8.9`

## Push the package to PyPI

```
$ python3 setup.py sdist upload -r pypiprod
```

and check that the package looks well-formed at `https://pypi.org/pypi/lsankidb/7.8.9`

Finally check that the package can be installed from PyPI:

```
$ sudo -H pip3 uninstall lsankidb
$ sudo -H pip3 install --upgrade lsankidb
```

## Add release notes

to [https://github.com/AurelienLourot/lsankidb/tags](https://github.com/AurelienLourot/lsankidb/tags)