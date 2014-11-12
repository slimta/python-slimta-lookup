#### [Project Homepage][1]

--------------------

About
=====

Provides a simple way to control [`slimta`][3] actions and policies with
external lookups. This extension is for convenience and does not provide any
new functionality. It was inspired by and is mostly compatible with [Dovecot's
password database][4] concept.

[![Build Status](http://ci.slimta.org/job/python-slimta-lookup/badge/icon)](http://ci.slimta.org/job/python-slimta-lookup/)

Getting Started
===============

If you haven't yet installed [`python-slimta`][2], refer to the "Getting
Started" section. Once inside your virtualenv:

    (.venv)$ python setup.py develop

To run the suite of included unit tests:

    (.venv)$ nosetests

[1]: http://slimta.org/
[2]: https://github.com/slimta/python-slimta
[3]: http://slimta.org/latest/manual/slimta.html
[4]: http://wiki2.dovecot.org/PasswordDatabase

