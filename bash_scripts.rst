********************
Bash Scripts
********************

One of the beauties of using the command line is that we can automate the more tidious or repetative tasks.  We do this by using scripts. These are exactly what they say they are, scripts for the command line to follow.  This chapter will introduce the idea of scripts, how to run them, and some of the features of bash we may want to use in them.  Hopefully I will write a more comprehensive tutorial on bash scripts and the more advanced features at some point. Please let me know if you would be interested as this will help raise the priority of it in my ever increasing to-do list.

Overview
========

In this chapter you will learn:

* what a script is.
* how to run scripts.
* how to pass variables to a script.
* how to use conditionals.
* how to use loops.
  
What is a Bash Script?
======================

Bash scripts are files that contain a series of commands for the shell to execute.  Any command you run in the terminal can be ran in a bash shell, and any command you run in a script can be ran in the terminal.

Bash or shell scripts, can be used to automate many of the tasks we do on the command line, they can be also take inputs to make them more generic and reusable.

Basics
======

Creating and running bash scripts (should) follow a common basic form.  All scripts should start with a shebang (this is explained below), and then they should include some code and comments. To run, or execute, a bash script we need to make sure it has the correct permissions an then run in it in the correct way.  All of this is detailed below, and an example script is given as well.

Example Script
--------------

.. code-block:: bash
   :linenos:

   #!/bin/bash

   # Print out hello world.
   echo "Hello World!"

Shebang!
--------

In the example above, the first line begins with a shebang (``#!``).  This is then followed by the path to an interpretor that can read the code in the script.  As we are writing a bash script, this is line points to the bash shell (``/bin/bash``).  It could point to any interpretor, including other scripting languages such as python.

Code and Comments
-----------------

After the shebang (and a blank line for readability) comes the code. Any commands that you can type into the terminal and run can be used in here. In the example above we use ``echo "Hello World!"``.  The echo command takes a string as input and print it to the command line.  This script, when run, will just print ``hello World!`` out to the terminal.

It is good to have comments in our code to tell people what it will do.  To write comments in bash, we just put a hash, ``#``, at the beginning of the line.

Permissions
------------

To run the code, the file must have executable permissions. This is looked at in detail in ``sec: perms``.  For our bash scripts, running ``chmod 755 my_script.sh``, "my_script.sh" is the name of your script should be fine.  This will grant the user read, write, and execute permissions; and grant other users read and execute permissions.

What's in a name?
-----------------

Linux is an extentionless system.  This means that the file extension (the 2-4 characters after the fullstop) do not control how the file is treated.  We do not need file names to end in ``.exe`` to be able to execute them, that is done by permissions.  Likewise we do not need scripts to end in ``.sh``; However, giving files a name with an extension helps in knowing how to run them without opening them.  By convention bash scripts end in ``.sh``.


Running the code
----------------

To run the code we just need to type the following in a terminal:

.. code-block:: bash
   :linenos:

   ./my_script.sh

This will then (hopefully) run the code and print "Hello World!" to the terminal.

.. important::

   Notice the ``./`` at the beginning of the text command?  This tells the shell that the command is in our current directory.  When we run commands, the shell searches our ``PATH``.  This contains a list of directories that hold executables that we can run. As our current directory is not in one of these, we need to explicitly tell the shell where it is.

Variables
=========

Variables allow us to store a piece of data for use at a latter date, or part of the script.  They can contain both static values, or command argument to be evaluated. They are very useful: they can save us time by having one variable to edit that is then called later in the script, they can store data from a command, or they can allow us to pass data and inputs to our scripts.

It is easy to create and call variables in bash.  To create them we specify the variables name followed by an equals sign,``=``, and then the value we wish it to hold.  To get the out put of the variable, we call it by its name, with a dollar sign infront, ``$``.   Let's look at our simple script again, this time with variables.

.. code-block:: bash
   :linenos:

   #!/bin/bash

   myString="Hello World!"
   # Print out hello world.
   echo $myString

Storing commands - backticks
----------------------------
   
We mention above that we can also use variables to store commands to be evaluated.  To do this we use backticks.  When we create a variable then anything inside backticks ````` will be evaluated on the command line, that is the command will be processed and the output will be stored in the variable.

.. code-block:: bash
   :linenos:

   #!/bin/bash

   todaysDate=`date +%F`
   # Print out the date
   echo "Todays date is: " $todaysDate

Inbuilt variables - Command line arguments
-------------------------------------------
Bash has many inbuilt variables that are set automatically. Some are only set when we are using scripts.  These are the ones that are most useful to us at the minute.

There are four variables set when we run a script:

* ``$0`` - This returns the name of the script.
* ``$#`` - This returns the number of command line arguments given to the script.
* ``$1 - $9`` - These return the 1st to 9th command line arguments.
* ``$*`` - This returns all the command line arguments.

These allow us to pass arguments to our scripts, and use them. Lets look at another example to see more:

.. code-block:: bash
   :linenos:

   #!/bin/bash

   echo "You just ran " $0
   echo "You entered " $# " names."
   echo "The third name is " $3
   echo "All the names are: " $*

We can then run this with arguments on the command line.

.. code-block:: bash
   :linenos:
      
   $ ./sith_lords.sh Vader Sidious Maul
   You just ran  ./sith_lords.sh
   You entered  3  names.
   The third name is  Maul
   All the names are:  Vader Sidious Maul


Conditionals
============

As our scripts progress and get more advanced, we will want to add some flow control to them. This helps to make them more "intelligent".  We do not want our script to output the third name if there are only 2, or we do not want to access a file that does not exist.  To guard against this we can use if statements to test whether something is true before we run the code.

If statements take the following minimal form:

.. code-block:: bash
   :linenos:
      
   if [ <expression> ]
   then
      <action_if true>
   fi

All `if`` statements start with a test, this consists of an expression placed inside square brackets.  On a new line we then have the command ``then`` followed by the code to run if the test is passed - this can be multiple lines, it is terminated by ``fi``.

We can also use the if-else conditional:

.. code-block:: bash
   :linenos:
      
   if [ <expression> ]
   then
      <action_if true>
   else
      <action_if false>
   fi

Let's look at an example.

.. code-block:: bash
   :linenos:

   #!/bin/bash

   echo "You just ran " $0

   # Check if there are less than 3 
   if [ $# -lt 3 ]
   then
      echo "You only entered " $#" names, this script requires at least 3".
   else
      echo "You entered " $# " names."
      echo "The third name is " $3
      echo "All the names are: " $*
   fi

.. note::

   There are many comparison operators in bash such as the ``-lt`` that we used above which test if one value is less than another.  A comprehensive list can be found `here. <http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html>`_

Loops
=====

One of the main reasons to use shell scripts is to automate boring and repetitive jobs.  To help do this bash has loops to aid in repeating jobs. The ``for`` loop allows us to repeat certain blocks of code as we count through a sequence - this could be a list of files etc.

.. code-block:: bash
   :linenos:

   #!/bin/bash

   for planet in "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto;
   do
      echo $planet
   done

Here we provide the ``for`` loop with a list of planets.  Each one is then assigned to the variable ``planet`` one by one, and the code after ``do`` is executed for each item in order.

Suppose we had an analysis code to run called "myAnalysis".  This takes one input, a data set and prints its output to the screen.  Using a for loop, and redirect we can save this data.

.. code-block:: bash
   :linenos:

   #!/bin/bash

   for dataset in `ls *.data`;
   do
      ./myAnalysis $dataset > $dataset.out
   done

Here we passed the loop the command ```ls *.data```, this was expanded out to a list of files ending in ".data".  For each file in the list, the code ``./myAnalysis $dataset > $dataset.out`` is ran. This runs over the dataset, and produces an output file of the same name as the dataset, but with ".out" on the end.

Summary
=======
  
Concepts
--------
 * **Scripts** - these are a series of commands that can be run from a file.
 * To run a script we need to give the full path of the script, this means it must start with **``./``**
 
Commands
--------
* `` mvVar="some value"`` - variables are created by specifying a variable name, followed by the equals sign and then the value.
* ``$myVar`` - variables are accessed by placing a  ``$`` in front of their name.
  
Further Reading
===============

`Developing good scripts - Bash Guide for Beginners <http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_01_05.html>`_

`If statements - Bash Guide for Beginners <tldp.org/LDP/Bash-Beginners-Guide/html/chap_07.html>`_

`For Loops - Bash Guide for Beginners <http://tldp.org/LDP/Bash-Beginners-Guide/html/chap_09.html>`_
