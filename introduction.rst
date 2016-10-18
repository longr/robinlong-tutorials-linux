*************
Introduction
*************

This tutorial is about using the command line in linux.  The aim is to ensure you have the require skills to succesfully navigate through linux, get to your files and begin automating your research.

At first the command line looks archaic, something from a by-gone age of computing. However it allows researchers to work faster, to automate their analyses, and more it is a more powerful and flexible way of using the tools we have. To borrow a quote:  *"This is the tool of a Researcher. Not as clumsy or as random as a GUI. An elegant tool... for a more civilized age."*

With GUI (Graphical User Interface) the power of the underlying program is limitted by what has been put into the GUI, and the designers idea of how to chain commands together.  Accessing the command line directly allows us to chain commands in the way that allows us to complete the tasks at hand.

Reproducability is another requirement of research; we can take notes as we click on buttons, but what if we accidentally click on somethign else, or type the wrong input? Do we know for sure how we got here? With the command line we can review what we have done and be sure that we are running the same things each time.

To access this power and control, we need to start at the beginning. Learn how to navigate through the filesystem using the command line, how to invoke the commands we need, find help to use them, learn how to chain them together, and how to script them so we can automate and repeat.

This chapter introduces the command line, the shell and the terminal.  The following chapters will build on what we learn here.

Overview
========

In this chapter you will learn

* How to open a terminal.
* What the shell is.
* How to use the shell.


Opening a terminal
==================

The first thing we will need to do is open a terminal. If you are using Linux or OSX, this should be simple.  If you are using windows, you will need to access a remote linux machine using a program called PuTTY.  All three methods are described in their relevant subsections:

Linux
-----

This varies from system to system, but a good bet is to try **Applications -> System** or **Activities -> Show Applications**, and type terminal into the search box.

Mac OS
------

You should find the **terminal** under **Applications -> Utilities**.  

Windows
-------

On windows you will need two programs, **PuTTY** and **Xming**.  You can find instructions on how to set these up `here <http://www.geo.mtu.edu/geoschem/docs/putty_install.html>`_

  
The Shell
=========

The shell is a program that sits between the user (and keyboard) and the operating system.  Users type commands into the shell and run them by pressing the return key.  The shell takes text input from the keyboard and outputs information as text to the screen.  Using this we can interact with the computer and run any programs we wish to.


Sometimes the word terminal is used interchangeably with shell.  Terminals were originally hardware that was used to enter and display information from computers, these days when people talk about terminals they usually are referring to terminal emulators that run on GUIs and give you access to the shell.  Each terminal can run many different kinds of shells, most these days run a single shell called BASH (Bourne Again SHell).  This tutorial will assume that BASH is the shell being used.

The shell allows us to run any of the programs on the computer by typing there name. Many of these programs have strange short names such as \command{ls}, which runs the listings program that lists the contents of a directory. We shall learn more about these commands in the next chapter, but first a little look at the command line.

The shell takes input from the keyboard.  You can type in commands, and they are not ran until you press the return key.  You can use the left and right cursor keys to navigate the cursor forwards and backward along the line, delete text or insert new text.

The shell contains a history of all the commands you have run in it.  You can navigate this using the up and down cursor keys.

  .. tip::
     To search back through the history, press ``Ctrl + r``, and then type part of the previous command. Pressing ``Ctrl + r`` again cycles through options.
     
Summary
=======

Concepts
--------

The shell is how you interact with the computer and give it commands to run.  You can edit anything you type on the command line using the left and right cursor keys.  Using the up and down cursor keys allows you to access the history of previous commands.

Commands
--------

* Left and right arrow keys - navigate along text on the command line.
* Up and down arrow keys - browse through previously entered commands.
* `Ctrl + r` - Search back through previous commands.
   
Further Reading
===============

* Linux in a nutshell, O'Reilly - Chapter 3, The UNIX Shell.
* Linux in a nutshell, O'Reilly - Chapter 4, bash.
* `Linux Documentation Project - Chapter 2, Section 2, Absolute Basics <http://www.tldp.org/LDP/intro-linux/html/sect_02_02.html>`_

* `Introduction to the command line <https://en.flossmanuals.net/command-line/>`_
