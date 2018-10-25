*********************
Finding files
*********************

At somepoint we will lose something, or know that there is something we want, but not know where it is.  Linux has very powerful tools built into it to find files and even things in files.  This chapter will give a brief overview of how to find files based on their names and other attributes (but not contents).  

Overview
========

In this chapter you will learn:

* how to use the find command to search for files.

.. * how to use the locate command to search for files.
.. * how to find where binaries are located.

Finding files with ``find``
===========================

In this section we introduce the ``find`` command for finding files on your system.  This can search the filesystem for any files and directories using many different tests to find the files.

Searching with ``find``
When we need to search for files the main command to use is ``find``. Find has many options, however we shall focus on a few examples which will cover most of what you will need.

Suppose we want to find a file, we know that it is called ``data.txt``, and know it is somewhere in our ``/home`` directory, but cannot remember where:

.. code-block:: bash
   :linenos:
   
   $ find . -name 'data.txt'
   ./Public/analysis/data.txt

Lets look at this in more detail.

* ``find`` -  - this is the name of the command we want to use, it is then followed by a path and an expression.
* ``.`` -  - this is the path, we have old find to look in the current directory.  It will also look in any directories inside this one.
* ``-name 'data.txt'`` -  - this is the expression, in this case we have told find to look for a file name that matches what is in the quotes.


The expression is a test with an optional argument, or series of tests and arguments.  In the example above the test tells find to look at the name of the file (we could also use iname which looks at the name but ignores the case).  We then provide a pattern (inside quotes) for find to match the name to. Whilst we provided a full name, we can use wildcards as we would in bash. A quick reminder is listed(see chapter \ref{wildcards} for more detail).


* ``*`` -  - matches multiple characters.
* ``?`` -  - matches a single character.
* ``[]`` -  - matches an characters between the brackets.
* ``[\^{}]`` -  - matches an characters not between the brackets.


Searching by age
----------------

Perhaps we have some code that worked yesterday, but does not work today. In this case we could search for any file modified in the last 24 hours. We can do this using the test ``mtime``:

.. code-block:: bash
   :linenos:

   $ find . -mtime -1 
   ./Public/analysis/analysis.sh
   ./Public/analysis/output.txt


The ``mtime`` takes an integer($n$) as its argument, this can be:


* ``-n`` -  - less than n days ago.
* ``+n`` -  - greater than n days ago.
* ``n`` -  - exactly n days ago.


If we wanted finer control, we could use ``mmin`` which uses the same arguments, but uses minutes as its units.

Searching by size
-----------------

Another example might be that we are running out of disk space and want to find the largest files over a certain size in our home directory.

.. code-block:: bash
   :linenos:

   $ find ~ -size +500M -exec ls -sh {} \;
   ./Public/analysis/analysis.sh
   ./Public/analysis/output.txt


Lets look at this bit by bit:


* ``find``  - the program we are using
* ``~`` - the path we want to look in, in this case our home directory.
* ``-size +500M`` - the expression. This has two parts, the test (size) and the condition (+500M), greater than 500 mb.
* ``-exec`` - This tells find that once it has found a match, in stead of printing it to the screen it should run command on it. In this case the command is ``ls -sh \{\}\\;``, which causes find to print the file name and size. ``{}`` is replaced with the file found, and we end exec with a \command{;}, but as this means something to bash we have to escape it with a ``\`` - . 


We could also combine tests to look for files bigger than 500mb and older than 5 days:

.. code-block:: bash
   :linenos:

   $ find ~ -mtime 5 -size +500M -exec ls -sh {} \\;


There are many more tests that can be used with find, a comprehensive list is given in the man pages.

Finding files quickly with ``locate``
=====================================

The ``locate`` command is faster than ``find``, however this comes at a price.  Locate works by searching through a database which is usually built everynight.  This means that is does not usually find newly created files, or those on external devices.  To find a file you just type:

.. code-block:: bash
   :linenos:

   $ locate pattern

Pattern can be a file name, a pattern including globbing character. Locate matches against the full path a file name, so if you use globbing characters, but do not start the expression with a full path or wildcard, you will not match anything.

Which
=====

Sometimes, especially when writing a script it is useful to know where the command (such as ``ls``) is actualy located. This means you can then run the command with out any local modifications (you can configure your shell to add certain flags to a command by default, unless you then run the command from its full path, those flags will always be included).

The ``which`` command will tell you the full path of any command on your system (it will also tell you which flags are enabled by default).

The syntax is just ``which <command>``.

.. talk about which?



Summary
=======

Concepts
--------

* Meta-data about files, such as access and modification times is searchable. We can use this to find files of a certain age, or access within the last n minutes.

Commands
--------

* ``find path_to_search [options]`` 

  
Exercises
=========

* Find all files ending with **.txt** in your home directory.
* Find all files greater than 5Mb in size in your home directory.
* Find all files less than 10 minutes old in your home directory (use ``ls`` to verfiy their age).
* Find all files in your home directory that have not been accessed for 1 week.
* Have a play with ``locate`` and ``which``.


Further Reading
===============

`Linux Documentation Project - Complex Commands, find <http://tldp.org/LDP/abs/html/moreadv.html>`_
