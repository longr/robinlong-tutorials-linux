***************
Getting started
***************

In the previous chapters we looked at how we interact with the computer using the shell, which allows us to pass commands to the computer which are then run. We also looked at what files are in linux, and that directories contain files. These directories are stored in a common hierarchy. If we want to find our files, or run programs, then we will need to have an idea of what that hierarchy is, how to navigate around it, and what paths are. Since we want to run programs, we shall start looking at how to pass commands to the shell, and how to enable optional extras in those commands.

Overview
=========

In this chapter you will learn:

* how to find out where you are in the directory structure.
* how to view what files and directories are in our current directory.
* the difference between relative and absolute paths.
* how to move around the filesystem.
* how linux directory structure is layed how
* the differences between command, flag and arguments.


Where are we?
=============

The first thing we will want to know is where we are in the system.  We can find this out by using the "print working directory" command, ``pwd`` (Like many commands in linux, its name is an abbreviation of what it does.  The command lists the name of the directory that we are currently in; let's give it a try:

.. code-block:: bash
   :linenos:

   $ pwd
   /home/rel


What is in our current location?
================================

Now that we know where we are, we will want to know what files we have in our directory. Again, there is a command to do this, ``ls`` (it *lists* the directories contents). Lets have a look.

.. code-block:: bash
   :linenos:

   $ ls
   Documents Private Public shopping_list.txt

Whilst ``pwd`` was enter as a command by itself, ``ls`` is more powerful and has more functions.  As such, it has optional arguments and options (called flags) that can be passed to it to achieve more.

.. code-block:: bash

   ls [options] [location]
   
In this example square brackets, ``[]``,  represent something that is optional.  We can pass a location to ``ls`` and it will list the contents of that location. Additionally we can pass options (in the form of flags) that will modify the behaviour or output.  There are some examples below.

.. code-block:: bash
   :linenos:

   $ ls 
   Documents Public Private shopping_list.txt
   $ ls -l
   drwxr-xr-x. 14 longr longr 4096 Jun  3 11:16 Documents
   drwxr-x---. 10 longr longr 4096 Jul 13 09:54 Private
   drwxr-xr-x.  9 longr longr 4096 Jul 13 09:52 Public
   drwxrwxr-x.  3 longr longr 4096 Aug 12 14:03 test
   $ ls /usr
   bin  games  include  lib  lib64  libexec  local  sbin  share  src  tmp
   $ ls -l /usr
   dr-xr-xr-x.   2 root root  65536 Aug 22 15:08 bin
   drwxr-xr-x.   2 root root   4096 Feb  3  2016 games
   drwxr-xr-x.  39 root root   4096 Aug 12 09:46 include
   dr-xr-xr-x.  46 root root   4096 Aug 12 09:46 lib
   ...

Lets see what's going on here:

* Line 1 - We run the ``ls`` command without any arguments, and it lists the contents of our current directory on line 2.
* Line 3 - We run the ``ls`` command with the flag (``-l``) which changes the output to a long listing.  This displays extra information on the files. It has the following format:
  - ``d`` at the beginning indicates that it is a directory, ``-`` indicates it is a file.
  - The next 9 characters represent the permissions on the file.  We shall read more about this in section ooooooo.
  - The next field is the number of links to the file or directory (do not worry about this).
  - The third field is the owner of the file (in this case **rel**).
  - The forth field is the group the file or directory belongs to (in this case **atlas**).
  - The fifth field is the size.
  - Fields six to eight are the modification time.
  - The final field is the name of the file or directory.
* Line 8 - We run ``ls`` with the optional location ``/usr``. This tells ``ls`` not to list the contents of our current directory, but that of the location we have specified.
* Line 10 - We run ``ls`` again, but this time with the (``-l``) flag and an argument (``/usr``); this tells ``ls`` to printout a long listing of the contents of ``/usr``.
* Line 15 - just indicates that we have cut off the output and not printed the full amount.


Paths
=====

In the previous section we passed an argument to ``ls`` of ``/usr``.  This was a location of the filesystem. In linux whenever we pass a file name or a location to a command, we are passing it a path.  A path describes how to get to a file or directory.

Relative vs Absolute paths
--------------------------

There are two types of paths in linux, **relative** and **absolute**.  We always use one of these when refereeing to a file.

In linux the file system has a defined hierarchy, the top (or root) of this hierarchy is called the **root** directory, and is represented by a single forward slash, ``/``.  This contains subdirectories, which may contains subdirectories and so on.  Every file and directory on linux is located somewhere is here.

**Absolute paths** are paths that begin with a ``/`` and specify a file/directories position with relation to the root directory.

**Relative paths** specify a files location relative to the current directory, and as such never begin with a ``/``.

Lets look at a an example of both types:

.. code-block:: bash
   :linenos:

   $ pwd
   /home/rel
   $ ls Documents
   report.txt paper.txt presentation.pdf
   ...
   $ ls /home/rel/Documents
   report.txt paper.txt presentation.pdf
   ...

* line 1 - We use ``pwd`` to get our current location.
* line 3 - We run the ``ls`` command and give it the name of a directory in our current locations. This result could give a different output depending on where we are in the system.  The directory may not exist, or we may be in another directory that also contains a directory called ``Documents``.
* line 6 - We run ``ls`` again, but this time we use an absolute instead of relive path.  As this is an absolute path it will provide the same output regardless of where we are on the system.

More paths
----------

There are several short cuts that you mind find helpful with paths:

* ~ (tilde) - This is a short cut for your homer directory.  In the examples above our home directory is ``/home/rel``.  We could therefore refer to the directory *Documents* with either ``/home/rel/Documents`` or ``~/Documents``.
* . (dot) - This refers to the current directory.  In the example above, when using a relative path we could use either ``Documents`` or ``./Documents``.
* \.. (double dot, or dot dot) - This refers to the parent directory. This can be used multiple times to keep going up the file hierarchy. The command  ``ls ../../`` would print out the contents of the root directory (assuming we are in /home/rel).


As you can now see, there are many ways to refer to directories and files.  We can therefore use the one that is most convenient or practical.  Lets see a few examples:

.. code-block:: bash
   :linenos:

   $ pwd
   /home/rel
   $ ls
   Documents Private Public shopping_list.txt
   $ ls ~
   Documents Private Public shopping_list.txt
   $ ls Documents
   report.txt paper.txt presentation.pdf
   $ ls ./Documents
   report.txt paper.txt presentation.pdf
   $ ls ..
   rel
   $ ls /home
   rel
   $ ls ../..
   bin boot dev etc home lib var
   $ ls /
   bin boot dev etc home lib var

   
Moving around
===================

To move around the system, we use a command to *change directory*, ``cd`` It takes the following format:

.. code-block:: bash

   cd [location]

Given that the job of ``cd`` is to change to a new directory, it might seem strange that the location is optional.  If ``cd`` is ran without an argument, it takes you back to your home directory.

The location we pass to ``cd`` is a path, and as such may be relative or absolute. It can also use any of the paths listed above.

.. tip:: The change directory command also has another shortcut that we can use, ``cd -``. This will take you to the directory you were in before you changed directory.

.. code-block:: bash
   :linenos:

   $ pwd
   /home/rel
   $ cd Public
   $ pwd
   /home/rel/Public
   $ cd /
   $ pwd
   /
   $ cd ~/Public
   $ pwd
   /home/rel/Public
   $ cd ../../..
   $ pwd
   /
   $ cd
   $ pwd
   /home/rel
   $ cd -
   $ pwd
   /

.. tip:: Tab completion
   Typing out long paths can be tiring and time consuming.  Sometimes you also forget what the name of a directory is in your paths, stopping to do an ``ls`` is annoying.  This is where *tab completion* comes in useful.

   When you start typing a path in a terminal, pressing the tab key will result in the name of the file or directory being automatically completed for you.  If nothing happens, this means there is no unique solution, and pressing it a second time will result in a list of possible completions.

   
Summary
=======

Concepts
--------
* All files in linux are inside the root directory ``/``
* Paths consist of one of more directories.
* Absolute paths begin a the root directory ``/``.
* Relative paths do not begin with  ``/``.
* ``.``, ``..``, and ``~``; are alias' that refer to the current directory, the directory above, and the home directory.

Commands
--------
* ``pwd`` - prints the current working directory.
* ``ls`` - lists files and directories.
* ``cd`` - move between directories.

Exercise
========

* Use ``ls`` and ``cd`` to look and move around the system.  Don't forget to use relative and absolute paths.
* How many way are there to get to your home area? try all of them.
* Practise using tab completion
  
Further Reading
===================

`Introduction to Linux - Chapter 3. About files and the file system <http://www.tldp.org/LDP/intro-linux/html/chap_03.html>`_

