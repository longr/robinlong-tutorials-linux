******************************************
Files and Directories
******************************************


We learn in the previous chapter how to list the contents of directories, and how the file system was structured. We also learnt how to navigate from one directory to another.  Now we need to be able to create and delete these files and directories ourselves; we also will want to modify these files and directories by moving, renaming, and copying them.  The final part will introduce the nano editor and how to use it to create text files.

Overview
======================

In this chapter you will learn:

* how to create, copy, move and delete files and directories
* how to edit files.

Creating directories
======================
The first thing we will probably want to do when starting a new project is to create a new directory.  This is done simply with the make directory command, ``mkdir``. This take a single argument, the name of the directory we wish to create:

.. code-block:: bash
   :linenos:

   $ ls -F
   Public/     Private/     Documents/
   Thesis/     Research/    contacts.txt
   $ mkdir Projects
   $ ls -F
   Public/     Private/    Projects/
   Documents/  Thesis/     Research/
   contacts.txt

% Should we mention paths and mkdir -p
If we wished, we could also provide a path which includes the name of the new directory. 

.. code-block:: bash
   :linenos:

   $ ls -F
   Public/     Private/     Documents/
   Thesis/     Research/    contacts.txt
   $ mkdir Projects/polonium/data
   mkdir: cannot create directory ‘Projects/polonium/data’: No such file or directory

The error is a little strange, however it is caused by the fact that we have a path that does not exists. Whilst ``Projects`` exists, ``Projects/polonium`` does not.  We can use the ``-p`` flag, which creates the parent directories if they do not already exist.

.. code-block:: bash
   :linenos:

   $ mkdir -p Projects/polonium/data
   $ ls -F -a Projects
   .  ..
   $ ls -F Projects
   polonium/
   $ ls -F Projects/polonium


.. touch and rmdir?

Copying file and directories
============================

At some point we may want to copy files or directories - perhaps to create a back up, or we are reusing part for a new project.  Either way we will need ``cp``, the copy command.

This takes the form:

.. code-block:: none

   cp [options] <source_path> <destination_path>

``cp`` has a many options available and we shall look at some later, however it is still worth looking at the man pages to see what else it can do.

.. code-block:: bash
   :linenos:

   $ ls
   report.txt
   $ cp report.txt backup_report.txt
   $ ls
   backup_report.txt  report.txt

We mentioned earlier that **<source_path>** and **<destination_path>** are paths.  We used relative paths in the example above, but we could also use full paths, or other relative paths such as:

.. code-block:: bash
   :linenos:

   $ cp ~/report.txt /home/rel/backup_report.txt
   $ cp /home/rel/report.txt ../../backup/backup_report.txt
   $ cp report.txt /backup/.
   $ ls /backup
   backup_report.txt report.txt

Line 3 is the more interesting of these examples.  Instead of specifying a full path that included a destination file name, we provided just a path to a directory.  When we do this ``cp`` assumes we want to keep the name of the file the same.

.. tip::
   ``cp`` also accepts the format ``cp [options] <multiple_sources> <directory>``. In this format, you can pass a whole list of files as arguments to ``cp``, and as along as the final argument is a directory (or path to one) they will be copied (with their original names) into that directory.

   This is especially useful when combined with **wildcards** which we will cover later.

Without passing any options to ``cp``, it will not copy directories.  To copy directories and their contents we need to use the ``-r`` flag which tells ``cp`` to *recursively* copy the directory and its contents.

.. code-block:: bash
   :linenos:

   $ ls
   backup_report.txt data report.txt
   $ cp data bk_data
   cp: omitting directory 'data'
   $ cp -r data bk_data
   $ ls
   backup_report.txt bk_data data report.txt

.. tip::
   Another useful flag is ``-p`` which preserves the owner, permissions and timestamps of the file (don't worry about these yet.)


Moving files and directories.
=============================

To move files (and directories) we use the move command, ``mv``.  This has the same syntax as the ``cp`` command, with the exception that the ``-r`` flag is not needed to move directories.

.. code-block:: bash
   :linenos:

   $ ls
   backup_report.txt bk_data data report.txt                                                                        
   $ mv backup_report.txt data/
   $ ls 
   bk_data data report.txt
   $ ls data/
   backup_report.txt

Renaming files and directories
------------------------------

Since ``mv`` requires a source and a destination, it can be used to rename files by moving them to the same location with a different name.

.. code-block:: bash
   :linenos:

   $ mv data/backup_report.txt old_report.txt
   $ ls
   old_report.txt bk_data data report.txt
   $ mv old_report.txt backup_report.txt
   $ ls
   backup_report.txt bk_data data report.txt

On **line 1** we renamed the file and moved it in the same line.  On **line 4** we renamed the file.  We can do the same with directories without the need for flags.


Deleting files and directories
=========================================

To delete files we use the remove command, ``rm``.  One very important thing to remember, is that unlike when using the GUI, there is no undo command when you delete a file on the command line, so be very careful. This syntax is:

.. code-block:: none

   rm [options] <path_to_file>

As with the previous commands, ``rm`` accepts an absolute or relative file name.  Lets see some examples:

.. code-block:: bash
   :linenos:

   $ ls
   backup_report.txt bk_data data report.txt
   $ rm backup_report.txt
   $ rm /home/rel/report.txt
   $ ls
   bk_data data

Deleting directories
--------------------

When it comes to deleting directories we have two choices.  Firstly their is the remove directories command (``rmdir``). This only works on empty directories; this is useful as it forces us to be careful and check what is in the directory first.  The second option is to use ``rm``.  Like many commands, this has additional options. In this case (as with  ``cp``) we want the recursive option, ``-r``. This will delete a non-empty directory, so it is quicker than ``rm``, but we need to be more careful.

.. code-block:: bash
   :linenos:

   $ ls
   bk_data data
   $ rmdir bk_data
   rmdir: failed to remove 'bk_data': Directory not empty
   $ rm -r bk_data
   $ ls
   data

Notice how on line 4 we are warned that ``bk_data`` is not empty, but we are not warned when we use the ``rm -r`` command.


Summary
=======

Commands
--------

* ``mkdir`` - creates directories.
* ``cp`` - copies files/directories.
* ``mv`` - moves or renames files/directories
* ``rm`` - removes (deletes) files and directors.
* ``rmdir`` - removes (deletes) empty directors.

Concepts
--------

* **No undo**.  There is no undo when we delete files and directories on the command line.


Further Reading
======================

`Linux Documentation Project - Files and the Filesystem <http://www.tldp.org/LDP/intro-linux/html/chap_03.html>`_
