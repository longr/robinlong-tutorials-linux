******************
Wildcards
******************

In previous sections we have used commands that act on a single file.  Part of the power of the command line is being able to act on many files at once.  Wildcards allow us to specify patterns instead of individual file names.

Overview
========

In this chapter you will learn:

* what globbing and wildcards are.
* how the shell expands wildcards.
* about the types of wildcards and how to use them.


What are wildcards?
===================

Wildcards are characters with special meanings. They can represent letters or numbers, sets of characters or even many characters.  When we put a wildcards in place of a filename, bash will expand these wildcards out to any matching file name (this is known as file name expansion, or  `globbing. <http://www.tldp.org/LDP/abs/html/globbingref.html>`_).


Wildcards
=========

Bash only has few wildcards that it recognises, but these are very powerful.

* **?** - represents a single character.
* ***** - represents zero or more characters.
* **[]** - represents a range or set of characters.
* **{}** - represents a comma separated list of terms.
* **[!]** - represents any character not in range or set.
* **\\** - this is used to escape any of the above characters so that you can search for them in a filename.

We use these like so:

.. code-block:: bash
   :linenos:

   $ ls
   file1.jpg file2.jpg figure.png report.txt facts.txt
   $ ls f*
   file1.jpg file2.jpg figure.png facts.txt
   $ ls *.txt
   report.txt facts.txt

   
What's going on?
================

When we execute commands such as ``ls *.txt`` bash expands this and replaces ``*.txt`` with any file or directory in that matches the pattern (in this case, zero or more characters followed by '.txt').

.. caution:: Unless we place an explicit path, or path separator (``/``) into our patterns, bash will not expand to file names outside the current directory.

More examples
=============

The best way to understand these is with examples.

Matching many, one and zero characters (``?`` and ``*``)
---------------------------------------------------------

To match zero or many, or exactly one of any character, we use the ``*`` and ``?`` wildcards.

.. code-block:: bash
   :linenos:
   
   $ ls
   abc abc1 abc2 abc3 xyz xyz1 xyz2 xyz3
   $ ls abc*
   abc abc1 abc2 abc3
   $ ls abc?
   abc1 abc2 abc3

Notice how ``*`` matches both **abc** and **abc1, abc2, abc3**, whilst ``?`` does not match **abc**.  This is because ``*`` is for zero or more of any character whilst ``?`` is for exactly one of any character.  If we wanted to match against one or more characters, ``*`` would not work.  However if we combined the two, ``?*`` would match one of more characters.

Sets and ranges, ``[]``
-----------------------

Square brackets (``[]``) allow us to do two types of matches. We can match against a list of characters, or a range separated by a hyphen ``-``.

If we wanted to list all files that are three letters long, we could do.

.. code-block:: bash
   :linenos:
      
   $ ls [a-z][a-z][a-z]
   abc xyz
   $ ls [abcxyz][abcxyz][abcxyz]
   $ ls [a-y][a-y][a-y]
   abc
   $ ls [A-Z][A-Z][A-Z]
   $

On line 1 we gave bash three ranges to match.  Each range will only match a single character, so three ranges were needed to match three characters. Also note how the last command did not match up against anything as linux is case sensitive.

Lines 1 and 3 give the same output, but where as line 1 uses a range, line 3 uses sets. We could combine ranges in the set.  To match all letters and numbers, both upper and lowercase we would use ``[a-zA-Z0-9]``.
   
By placing an ``!`` at the beginning of a set or range, we tell bash to match anything except the characters listed in the set.

.. warning::
   All special characters lose their meaning inside of square brackets (``[]``), with the exception of ``-`` which gains special meaning. i.e. [?*] will only match a question mark or an exclamation mark, these will not be used a wildcards.

Lists, ``{}``
-------------

Curly brackets ``{}`` are used to hold a comma separated list of terms that can be matched

.. code-block:: bash
   :linenos:

   $ ls {abc,xyz}1
   abc1 xyz1
   $ ls abc{1,3}
   abc1 abc3

Everyday examples
=================

* ``cp filename{,.bak}`` - Create a backup of a file called "filename.bak" -
* ``cp *{,.bak}`` - Create a backup of all files in the local directory called "filename.bak" -
* ``cp *{.txt,.jpg} ~`` - copy all files ending in ``.txt`` and ``.jpg`` to the home area.
* ``rm *~`` - delete all emacs backups.

--------

Summary
=======

Concepts
--------
* Bash will expand wildcards, and replace them with all matching files and directories in the current directory.
* This is known as globbing.

Commands
--------

* **?** - represents a single character.
* ***** - represents zero or more characters.
* **[]** - represents a range or set of characters.
* **{}** - represents a comma separated list of terms.
* **[!]** - represents any character not in range or set.
* **\\** - this is used to escape any of the above characters so that you can search for them in a filename.

Exercises
=========

The following questions ask you to consider what globbing pattern would match the following groups of files.  Feel free to create the files using the ``touch`` command, and then use ``ls`` and globbing to try and match.

* What pattern would match any jpeg, or png file (but not files with other extensions)?
* What pattern would match only files that started with two letters followed by a number?
* What pattern would match files that started with only a capital letter?
* Look around your home directory, and try matching files with a few different patterns.

Further Reading
===============

`Linux Documentation Project - Wildcards <http://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm>`_
