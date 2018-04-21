[![Build Status](https://travis-ci.org/AurelienLourot/lsankidb.svg?branch=master)](https://travis-ci.org/AurelienLourot/lsankidb)
[![Coverage Status](https://codecov.io/gh/AurelienLourot/lsankidb/branch/master/graph/badge.svg)](https://codecov.io/gh/AurelienLourot/lsankidb)
[![Requirements Status](https://requires.io/github/AurelienLourot/lsankidb/requirements.svg?branch=master)](https://requires.io/github/AurelienLourot/lsankidb/requirements/?branch=master)
[![PyPI version](https://badge.fury.io/py/lsankidb.svg)](https://badge.fury.io/py/lsankidb)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lsankidb.svg)](https://badge.fury.io/py/lsankidb)

[<img src="https://rawgit.com/AurelienLourot/lsankidb/master/thirdparty/logo.png" align="left" width="64" height="64">](https://github.com/AurelienLourot/lsankidb)

# lsankidb

`ls` for your local [Anki](https://apps.ankiweb.net/) database.

Dump/Print all your Anki terms in order to save them, search them, `grep` them or `diff` them.

```bash
$ lsankidb
Listing /home/me/.local/share/Anki2/User 1/collection.anki2 ...

German
    ['Hello', 'Hallo']
    ['How are you?', "Wie geht's?"]
French
    ['Hello', 'Bonjour']
    ['How are you?', 'Comment ça va ?']
```

## Installation

```bash
$ sudo pip3 install lsankidb
```

Validated against Anki 2.0.50 on Ubuntu 14.04.

## Team

This project is maintained by the following person(s) and a bunch of
[awesome contributors](https://github.com/AurelienLourot/lsankidb/graphs/contributors).

[![AurelienLourot](https://avatars0.githubusercontent.com/u/11795312?v=4&s=70)](https://github.com/AurelienLourot) |
--- |
[Aurelien Lourot](https://github.com/AurelienLourot) |

## Changelog

**1.0.0** (2018-04-21):
  * Removed duplicate cards from the output.

**0.0.2** (2018-04-20):
  * Cosmetic improvements to the [PyPI page](https://pypi.org/pypi/lsankidb/).

**0.0.1** (2018-04-20):
  * Initial version.
