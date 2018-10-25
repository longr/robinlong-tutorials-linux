********************
Working Remotely
********************

Over the previous chapters we have learnt how to run commands and programs on the command line, how to conrtol the jobs, edit files and bend it to our will. However all of this is on one machine (probably you local one).

At somepoint you will move beyond what your machine can do, and will want to run your code on more powerful machines, or pehaps your files are saved on a different machine and you want to access them. What ever the reason, you will need *remote access* to another linux machines, this is easy under Linux.

Linux has many built in tools to do this.  ``ssh`` lets us access remote machines, ``scp`` and ``rsync`` let transfer files, and ``screen`` can be used to run commands in a remote environment.

Overview
========

In this chapter you will learn:

 * how to use ``ssh`` to access remote machines.
 * how to use ``scp`` to copy remote files.
 * how and when to use ``rsync`` to copy remote files.
 * how to use screen to work remotely.
   

SSH
===

This is the most basic command for working remotely.  SSH stands for Secure SHell, and is used to connect to a remote machine.  The syntax for ssh is:

.. code-block:: bash

   $ ssh username@name_or_remote_machine
   
Here we supply the username we wish to login with on the remote system, and the full name of the remote machines, such as ``ius.lancs.ac.uk``.

This will then prompt for our password to login.

From here we will have a terminal to run any command we would do locally.  Typing ``exit`` will kill the remote session.

If we want to display graphics from the remote machine we will need to enable "X Forwarding".  To do this we need the ``-X`` flag with ssh:

.. code-block:: bash

   $ ssh -X username@name_or_remote_machine


Transferring files
==================

Inevitably, once we start working with remote machines, we will want to transfer files between them.  This can be done with both ``scp`` and ``rsync``.  ``scp`` is the more basic one, so we shall look at this first.

Secure Copy - ``scp``
---------------------

``scp`` stands for Secure CoPy.  It is the version of the ``cp`` command used to transfer files to and from remote machines.  It has a simple syntax, very similar to ``cp``.

.. code-block:: bash

   $ scp path_of_source path_of_destination

``scp`` takes two arguments, the path of the source and destination files.  These can be absolute or relative paths.  To copy from or too a remote machine, the source or destination needs to be prefixed with the address of the machine followed by a colon (``:``).


.. code-block:: bash

   $ scp ius.lancs.ac.uk:Public/myData .

   $ scp Public/myData ius.lancs.ac.uk:Public/.

In the first line we copy the file ``myData`` from the directory ``Public`` on our remote machine to the current directory on our local machine.   In the second line we copy the file ``myData`` from the directory ``Public`` on our local to the directory ``Public`` on the remote machine.

Synchronising files - ``rsync``
-------------------------------

RSync can be used to transfer files locally or remotely.  It is more efficient than ``scp`` as it only transfers files if they were modified more recently on the source than the destination, in which case it only transfers the difference - this reduces the time taken to transfer files.

The syntax is:

.. code-block:: bash

   rsync options source destination

The source and destination must be full paths.  If one of them is a remote machine, this needs to be prefixed with the address of the machine followed by a colon (``:``).

Some useful options are:

* ``-v`` - verbose, this prints out what files it is copying.
* ``-r`` - recursive, this will copy directories as well.
* ``-a`` - archive, this preserves symlinks, permissions and timestamps; and does recursive.
* ``-e ssh`` - this tells rsync to use ssh for the remote connections, this ensure that the connection is encrypted and secure.
* ``-z`` - this tells rsync to compress the files, this helps speed up the transfer at the expense of CPU power.

To transfer **Public** from the remote machine to the local we would do this: 
.. code-block:: bash

   $ rsync -avz -e ssh ius.lancs.ac.uk:Public .

#nohup
   
Screen
======

Screen can do many things, but it is most useful when you need to have long running programs on a remote connection, but do not want to leave a terminal open all that time, or your connection might end.   ``screen`` allows you to create a new terminal session, and "detach" it, keeping your program alive even if you log out.

To use screen, ssh into a machine, and then start screen:

.. code-block:: bash

   $ ssh user@ius.lancs.ac.uk
   $ screen
   $


This will start a new instance of bash.  You can then run any commands or scripts you want in there.

Detaching and reattaching screen sessions
-----------------------------------------

To detach the screen, we use ``Ctrl+a d`` - if your connection ends, or your close the terminal, the screen session will detach itself.  To reattach the screen, restart the connection and type ``screen -r``.   If there are multiple screens, you will get a warning:

.. code-block:: bash
   :linenos:
   
   $ screen -r
   There are several suitable screens on:
	16447.pts-2.dyn-191-235	(Detached)
	16381.pts-2.dyn-191-235	(Detached)
   Type "screen [-d] -r [pid.]tty.host" to resume one of them.
   $ screen -r 16447
   $

We are then given a list of screens, we can reconnect by using the first 5 digits of the "screen" as an argument.  We can also get a list of screens using ``screen -ls``.

To kill a screen completely, type ``Ctrl+a k``

Summary
=======

Concepts
--------
* `ssh` allows you to access a machine remotely
* `scp` and `rsync` allow us to transfer files, `rsync` only transfers files that are newer on the source.
* `screen` allows us to keep sessions alive.

Commands
--------

Connect to remote host
^^^^^^^^^^^^^^^^^^^^^^^
* `ssh user@remote_host`

Transfer files
^^^^^^^^^^^^^^^
* ``scp source destination``
* ``rsync -vaz -e ssh source destination``

Screen
^^^^^^^

* To start: `screen`
* To detach: `Ctrl+a d`
* To reattach: `screen -r <screen_id>`
* Get list of screen sessions: `screen -ls`
* To kill a session: `Ctrl+a k`

Exercises
=========

* Try opening, detaching, reattaching and then killing at least 2 screen sessions.
* If you have access, copy a file to a remote machine, and then backagain.
  
  
Further Reading
===============

`Screen Examples <http://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/>`_
