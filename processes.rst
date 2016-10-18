***************************
Managing Processes
***************************

Early we learnt that almost everything in Linux is a file, if it is not a file, then it is a process. Aprocesses carry out tasks on the computer; A program is code and instructions for the computer to run, when it runs these instructions it is carrying out a process.

The command line gives us a lot of control over these processes. We can stop them, pause them, and even kill them. Being able to control these processes and what jobs are runnign gives us even better control of the system.  Sometimes programs that we are running go wrong, or we want to pause them whilst we do something else. This section will look at how to control jobs and processes, and what they are.


Overview
========

In this chapter you will learn:

* what processes are.
* how to see what is running on your system.
* how to control processes.
* what jobs are, and how to control them.
    
What are processes
==================
When we run programs on linux, each one takes up an amount of processing power and memory.  Linux manages these programs and grants them access to the resources on the system.  When a program is running it is called a process (sometimes a daemon).



What is running
===============
We can see what is currently running on our system by using the ``top`` command.   This displays the process running on the system ordered by percentage of the CPU that they are using (then can be ordered by other fields if we wish).  Typing ``top`` into the terminal and pressing ``return`` and you should be presented with something that looks like this:

.. code-block:: bash
   :linenos:

   top - 12:57:54 up  3:45,  1 user,  load average: 0.35, 0.23, 0.26
   Tasks: 307 total,   1 running, 299 sleeping,   7 stopped,   0 zombie
   %Cpu(s):  1.8 us,  1.0 sy,  0.0 ni, 97.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
   KiB Mem :  8066744 total,  1897928 free,  2048852 used,  4119964 buff/cache
   KiB Swap:  8388604 total,  8388604 free,        0 used.  5050556 avail Mem 

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND     
   2100 user     20   0  568740 120908 103240 S   4.3  1.5   3:26.42 Xorg        
   3108 user     20   0 2371504 773616 176456 S   4.3  9.6  31:40.68 firefox     
   2214 user     20   0 2189232 166192  64576 S   3.6  2.1   3:29.37 gnome-shell 
   2786 user     20   0 1246196 290288  87348 S   2.3  3.6   7:23.17 thunderbird 
   4030 user     20   0  750548  41684  25452 S   2.3  0.5   0:42.35 gnome-term+ 

Lets look at the important bits in some more detail:

* **line 2** - Tasks are just another name for processes. We can see that there are a few different states (running, sleeping, stopped, and zombie).  Sleeping processes are ones that are waiting for an event to occur before they can run again.  Stopped jobs are waiting to be told to run again. Zombies are processes that have been killed, but have not been cleaned up properly.
* **line 4/5** - This lists how much memory there is in the system(total), how much is free to be used (free), and how much is actually being used (used).  **line 5** is the same but for swap; this is memory that has been copied to disk (usually when the OS runs out of physical memory. If too much swap is being used, the system will be slow.
* **lines 7-12** - This is a table of process. The import columns here are: PID, which is the unique id given to each process; %CPU and %MEM, which is the percentage of CPU and memory being used by the process; TIME, which is how long the process has been running for; and COMMAND, which is the command (or program) which is running.

``top`` will give a real time view of what is running on the system.  This is useful for finding what is taking up all the CPU and memory, but more often we will want to see a full list of everything that is running, not just the top processes.  In which case, we use the command ``ps``.


``ps`` will show the programs currently running in that terminal.  To display all running processes on the system  we need to type ``ps aux``.  This will produce a lot of output. Usually we pipe it to ``grep`` so that we can find information on specific process.

   
Killing a process
=================

Occasionally a program crashes, or it is taking too long and we want to kill it.  In this case we use ``ps`` and ``grep`` to find the *PID* of the process.  Then we can kill the process with the ``kill`` command.  Lets assume that firefox has stopped working and we want to kill it.

.. code-block:: bash
   :linenos:

   $ ps aux | grep firefox
   user     3108 14.8 10.2 2396440 825772 tty2   Sl+  09:17  40:29 /usr/lib64/firefox/firefox
   user    11283  0.0  0.0 118496   896 pts/1    S+   13:49   0:00 grep --color firefox
   $ kill 3108
   $

* **line 1** - here we pipe ``ps aux`` to grep and search for *firefox*.
* **line 2-3** - these are the lines that matched our grep request. Line 2 is our *firefox* process, whilst line 3 is the command we ran on line 1.  There may be more than one instance of a program running on a system so be careful.
* **line 4** - we pass the PID from the second column on line 2 to the ``kill`` command.

Using ``kill`` like this asks the process to shutdown nicely, if for some reasons the process is not able to shutdown, we can reissue the command with a ``-9`` as a brute force method:

.. code-block:: bash
   :linenos:

   $ kill -9 3108
   $


.. tip::
   If you are working on a linux machine locally, and the whole system freezes, and you cannot access a terminal, try pressing ``ctrl + alt + F2``. This should bounce you to a new command line session. From here you can log in and kill the troublesome process.

.. danger::
   Normally a user can only kill a process they own, one that either they started, or was started when the logged in.  However, **root** can kill any and all processes.

Jobs
====

Jobs are process started interactively in the terminal.  They can be displayed by typing ``jobs`` in the command line.  Usually when we run programs in the terminal, we cannot use the terminal again until that process has finished - in this case the job is in the **foreground**.  When a job runs in the background, it releases the terminal back to you, and then outputs its results when done.  Lets look at this with the ``sleep`` command:

.. code-block:: bash
   :linenos:

   $ sleep 10
   $

The above command runs for 10 seconds and then releases the terminal back.  To run a command in the background we put an ``&`` after it:

.. code-block:: bash
   :linenos:

   $ sleep 10 &
   [1] 10244
   $
   [1]+  Done                    sleep 10
   $

Lets look at this line by line:

* **line 1** - we enter the command, are then given the terminal back as soon as we press ``return``.
* **line 2** - This is the output from putting the job in the background. **``[1]``** is the number of the job, which is unique to this terminal only, and **``10244``** is the global PID which is unique to the system.
* **line 3** - pressing ``return`` after 10 second wait, which gives the process time to finish.
* **line 4** - the job has finished, and the terminal is notified.  Again the job number and command are shown.

If we start running a command, and then wish to move it to the background we can do.  First you have to press ``ctrl + z`` - this will pause the currently running process. We can then either bring it back to the foreground or send it into the background to continue running.

.. code-block:: bash
   :linenos:

   $ sleep 30
   ^Z
   [1]+  Stopped                 sleep 30
   $ bg %1
   [1]+ sleep 30 &
   $ fg %1
   sleep 30

Lets look at the line by line:

* **line 1** - we run the command ``sleep 30``.
* **line 2** - we press ``ctrl + z`` to pause the command and move it into the background.
* **line 3** - the job id (``[1]``) is printed to the terminal along with the command.
* **line 4** - we use the command ``bg %1``, where **1** is the job id, and **%** tell the terminal this is a job id and not a process id.
* **line 5** - the job id (``[1]``) is printed to the terminal along with the command followed by an **&** to tell us that it is running in the background.
* **line 6** - we use the command ``fg %1`` similar to line 4 where we used the ``bg`` command, except that this brings the job to the foreground instead.

.. tip::
   If no job id is passed to ``bg`` or ``fg`` they will default to the most recently executed process, that is the one with the highest job id.
  
Killing jobs
-------------

Sometimes well will set a job running in the background
To get a list of all the jobs running in a terminal we use the ``jobs`` command. Then we can just use the kill command with the job id (don't forget the ``%`` to show that it is a job and not a PID).

.. code-block:: bash
   :linenos:

   $ sleep 30&
   [1] 12487
   $ jobs
   [1]+  Running                 sleep 30 &
   $ kill %1
   [1]+  Terminated              sleep 30
   $ 

----
   
Summary
=======

Concepts
--------
* All programs have a unique **process (PID)**.
* All processes started in a terminal have a job id unique to that terminal.
* Jobs can run in the foreground or the background.

Commands
--------
* ``top`` will show the top few processes ranked by CPU usage.
* ``ps aux`` will show all processes running on the system.
* ``jobs`` will list all jobs in the current terminal.  
* ``kill <pid>`` or ``kill %<job id>`` will terminate a process based on process or job id.
* ``bg %<job id>`` and ``fg %<job id`` will move a program between background and foreground.
* pressing ``ctrl + z`` will send a foreground job to the background.
   
Further Reading
===============

`Linux Documentation Project - Chapter 4, Processes <http://www.tldp.org/LDP/tlk/kernel/processes.html>`_
