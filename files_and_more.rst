***************
Files and Names
***************

Before we dive deeper into linux and how to use it, we need to pause to look at files and theirs names a little longer. This chapter will introduce you to a brief view of the linux file system and how files are named.  I would advise that you do not skip this section, as there are many things may trip you up later on if you have not grasped the basics of how the files systems and files work.

Overview
========

In this chapter you will learn:

* what a file is in linux
* how to find out what type a file is.
* how to deal with special characters in file names.
* what constitutes a good file name.

Everything is a file
====================

It is said of linux that *"... everything is a file; if it is not a file, it is a process."*

This describes linux quite well, there are some special files, but these are still just files.  Directories are just files that contain names of files, programs are files that the system reads and then runs, keyboards are files that the system reads from, screens are files, and so on.

Extensionless
-------------
You are probably used to seeing files with file extensions, the 2-4 characters after a full sop in the files name.  Some operating systems such as windows require this extension to know what the file is.  Linux is an extensionless system, it does not need the file extension, and instead looks inside the file to see what type of file it is.

Using the ``path`` command we can find out what type of file something is.

.. code-block:: bash

   file [path]
		
Whilst Linux does not the extension, we humans prefer it.  Sometimes it is useful to know what type of file something is. If we are compiling code, it is nice to have the source code and the executable with the same name, in which case an extension helps identify them.  Some common ones are:

* file.exe - an executable or program.
* file.txt - plain text file.
* file.png, file.jpg, file.svg - an image file.
* file.cxx, file.hxx - c++ source and header files.
* file.tex - LaTeX file.
* file.py - python script.
* file.pdf - A PDF file. (Sometimes known as a Acrobat file)

Case sensitive
================

Another common source of problems on linux is file names. Linux is case sensitive, as such you can have two files with the same name, but one starts with a capital letter.

.. warning::
   Commands and command line options are also case sensitive. ``ls`` is the correct command, ``LS`` is not.  Also many commands have flags with different cases ``-s`` and ``-S`` do very different things.

Spaces and Quotes
=================

Having a space in a file name is allowed, but we have to be careful.  On the command line we use spaces to separate commands and arguments.  If we have a space in a filename, and don't do anything the command line will assume it separates arguments.

.. code-block:: bash
   :linenos:

   $ ls
   Public Private My Files
   $ cd My Files
   bash: cd: My: No such file or directory

Here bash assumed the space separtated two arguments, ``My`` and ``Files``.  As such cd ignored the second argument (it only takes one) and tried to change into the directory ``My`` which does not exist.  There are two ways to solve this list below.

Escape Character
----------------

One option is to use an escape character; these are characters that are used before a special character to cancel out its special meaning.  In bash the escape character is the backslash (``\``).

.. code-block:: bash
   :linenos:

   $ cd My\ Files
   $ pwd
   /home/user/My Files

We can use the escape character on any character that has special meanings in bash such as: ``$``, ``"``, ``'``, and even ``\``.


If you use tab completion, and the file is unique, then bash will auto-complete and include the escape character.

Quotes
------

The second option is to use quotes.  This is useful if there are lots of special characters or spaces in the file name and we do not want to escape them all individually.

.. code-block:: bash
   :linenos:

   $ cd "My Files"
   $ pwd
   /home/user/My Files

.. important::

   Linux has two types of quotes, ``"`` (Double quotes) and ``'`` (single quotes).  These behave differently.
   
   * Single quotes remove all special characters meanings, anything inside them is interpreted as regular text.
   * Double quotes remove the special meaning of all characters expect ``$`` and `````. These will be expanded by the shall first (see Bash scripts and Variables).


Hidden files and directories
============================

Linux has a simple way of hiding files and directories.  Any file or directory whose name starts with a full stop (``.``) is hidden from normal view.  To view these on the command line we need to pass the ``-a`` flag to ``ls``.

.. code-block:: bash
   :linenos:

   $ ls
   Public   Private
   $ ls -a Public
   .  .. Public Private .bashrc bash_history

Passing the flag to ``ls`` results in the hidden files being displayed.  In your home directory you will find many hidden files such as **.bashrc** which hold configuration information for the programs you use.   You will also see two more files, ``.`` and ``..``, these are discussed in the section on Paths in Getting Started.

   



Summary
=======

Concepts
--------

* Everything is a file in linux, even the directories.
* Linux is extensionless, files do not need extensions for the system to know what they are.
* Linux is case sensitive.
* Spaces have a special meaning, so we need to escape or quote them in the command line.

Commands
--------

``file`` - tells you what type a file is.
``ls -a`` - displays hidden files.

Further Reading
===============
`Linux Documentation Project - Chapter 4, About files and the file system <http://www.tldp.org/LDP/intro-linux/html/sect_03_01.html>`_
