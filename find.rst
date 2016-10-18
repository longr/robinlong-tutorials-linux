*********************
Finding files
*********************

At somepoint we will lose something, or know that there is something we want, but not know where it is.  Linux has very powerful tools built into it to find files and even things in files.  This chapter will give a brief overview of how to find files based on their names and other attributes (but not contents).  

Overview
========

In this chapter you will learn:

* how to use the find command to search for files.
* how to use the locate command to search for files.
* how to find where binaries are located.

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

.. talk about locate?

Summary
=======

Concepts
--------

  
Commands
--------
   
Further Reading
===============

`Linux Documentation Project - Complex Commands, find <http://tldp.org/LDP/abs/html/moreadv.html>`_
