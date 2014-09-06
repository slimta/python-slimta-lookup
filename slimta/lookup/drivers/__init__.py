# Copyright (c) 2014 Ian C. Good
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""This package contains several implementations of the slimta lookup
mechanism, which provides a simple interface to control actions and policies
with external lookups. Under normal circumstances, slimta lookup drivers do
not modify their backend data source.

Drivers must implement this interface:

.. py:class:: LookupInterface

   This class demonstrates the methods that a class implementing slimta lookup
   must implement. Note, this class exists in documentation only, it does not
   need to be a inherited.

   .. py:method:: lookup(**kwargs)

      The keyword arguments will be used by the lookup driver to return a
      dictionary-like object that will be used to affect actions or policy. For
      some drivers, these keywords may be used with a template to produce a
      lookup key. For SQL-style drivers, they might be used in a ``WHERE``
      clause of a ``SELECT`` query.

      :param kwargs: Used by the driver to lookup records.
      :type kwargs: keyword arguments
      :returns: A dictionary if a record was found, ``None`` otherwise.

"""

# vim:et:fdm=marker:sts=4:sw=4:ts=4
