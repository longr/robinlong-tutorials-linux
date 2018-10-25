********************
Getting Help
********************

There are many different programs on linux, all of which have many different options. Remembering all these commands is not easy. Fortunately there are manuals or help commands for nearly all the programs on linux.

Overview
========

In this chapter you will learn:

* how to use the manual pages and search them.
* how to search the manual pages.
* how to use the help flags.

Man Pages
=================

The man pages are a series of pages or manuals that detail almost every program on the system and what it does (some programs are very extensive and have multiple man pages).


Viewing the man pages
---------------------

You access the man pages by typing man, and then the command you want help with, for example:

.. code-block:: none

   $ man <command_you_want_to_use>

   This will produce an out put similar to this:
   
   LS(1)                            User Commands                           LS(1)
   
   NAME
          ls - list directory contents
   
   SYNOPSIS
          ls [OPTION]... [FILE]...
   
   DESCRIPTION
          List  information  about  the FILEs (the current directory by default).
          Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
          fied.
   
          Mandatory  arguments  to  long  options are mandatory for short options
          too.
   
          -a, --all
                 do not ignore entries starting with .
   
          -A, --almost-all
                 do not list implied . and ..

Navigating the man pages
------------------------

The ``man`` command displays the manual pages using the ``less`` viewer, this means we can use the same navigation commands to look through the man pages.

To navigate up and down we can either uses the arrow keys to go up and down by one line at a time, or use the page up and page down keys to do whole pages at a time.

More often than not you will want to search for a key phrase or word, this can be done by typing ``/`` followed by the key word or phrase and pressing ``enter``.  Pressing ``n`` will move to the match of the pattern, and pressing ``shift + n`` will go to the previous match.

Searching the man pages
-----------------------

Sometimes you will not know what the command is that you need, in this case you can search through the man pages.  All ``man`` pages have a short description, and we can search for keywords or patterns in this.  To search for man pages, we type:

.. code-block:: none

   $ man -k compress
   bunzip2 (1)          - a block-sorting file compressor, v1.0.6
   bzcat (1)            - decompresses files to stdout
   bzcmp (1)            - compare bzip2 compressed files
   bzdiff (1)           - compare bzip2 compressed files
   bzegrep (1)          - search possibly bzip2 compressed files for a regular e...

As you can see this prints out two columns: the first is the name of the man page, and the second is the short description.

More help, and flags
====================

Some commands lack a help file, or the man pages are not installed. In this case we can just type the command with a ``-h`` flag and press ``enter``.  This will display limited help about the command such as what arguments it takes, and what flags it has.

There are two types of flags: short and long.  Short flags are one character long and start with a ``-``.  These can be chained together like so:

.. code-block:: bash

   $ ls -a -d
   drwx------. 52 user  user       12288 Aug 11 15:14 .
   drwxr-xr-x.  4 root  root        4096 Feb  3  2016 ..
   $ ls -ad
   drwx------. 52 user  user       12288 Aug 11 15:14 .
   drwxr-xr-x.  4 root  root        4096 Feb  3  2016 ..

Long flags start with two hyphens (``--``) and are whole words. Sometimes a command has a ``-h`` flag, and sometimes it has a ``--help`` flag, or even both (a good example if ``ls`` which uses ``-h`` for human readable units, so it has ``--help`` instead.


Summary
=======

Concepts
--------

* Man pages contain information on many different commands
* Some commands also have a help flag.
* Short flags are one letter long, start with a single hyphen (``-``), and can be merged together.
* Long commands are words, start with two hyphens (``--``), and cannot be merged.
  
Commands
--------

* ``man <command>`` - to display the man page for a command.
* ``man -k <pattern>`` - to search the short description for a pattern.
* ``/ <pattern>`` to search for a pattern whilst in a man page.
  - ``n`` - to move to the next pattern whilst searching
  - ``shift + n`` - to move to the previous pattern whilst searching

Exercises
=========

Using the man pages, find out how to modify ``ls`` to:

* Print file sizes.
* Print file sizes in a human readable format.
* Sort the files by size, largets first (you might want to have the size displayed so you can confirm this)
* Sort the files by size, smallest first.
    
Further Reading
===============

`Linux Documentation Project - Getting Help <http://www.tldp.org/LDP/intro-linux/html/sect_02_03.html>`_
