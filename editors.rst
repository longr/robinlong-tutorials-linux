****************
Editors
****************

At some point we are going to want to create files on the command line and fill them with text.  To do this we will need a text editor. There are many editors on linux, and many `arguments <https://xkcd.com/378/>`_. If you use linux with a GUI there are many graphical editors that you can use (Kate and gEdit for example), however the command line editors are generally more powerful, and are very useful when working remotely.  The main editors used are emacs and vim, whilst I might add tutorials for these later for now I will focus on nano as it is easier to use than either (for simple editting).

Overview
========

In this chapter you will learn:

* what nano is.
* what a text editor is.
* basic commands for nano.


Nano, a command line editor
===========================

``nano`` is a text editor. This means it will display only text files, no font formatting, font sizes, styles or images.  It also means there is no mouse, everything is plain and has to be done with the keyboard.  Whilst this seems like a step back, it is very useful for editing and has some benefits when it comes to writing as style is separated from content.

To start **nano** we issue a single command, with an optional file name. If the file exists, it is opened for editing, if not it will be created when we save later.

.. code-block:: none
		
   nano <file>

One advantage of **nano** when learning an editor is that it displays the main commands that you need along the bottom of the screen.

.. code-block:: none

     GNU nano 2.5.3                New Buffer                                      
  
  
  
  
    
  
  
  
   ^G Get Help  ^O Write Out   ^W Where Is  ^K Cut Text    ^J Justify   ^C Cur Pos
   ^X Exit      ^R Read File   ^\ Replace   ^U Uncut Text  ^T To Spell  ^_ Go To Line


Saving and Exiting
==================

The key combination for exiting **nano** is ``^X`` - to do this press and hold ``Ctrl`` and then tap ``x`` (the case of the letter is not important).

.. tip::

   Many interactive programs in linux make use of the modifier keys: The Control key, ``Ctrl``; The alt or meta key, ``Alt``; and the super or *windows* key ``Super``.  These are sometimes shortened and represented as:
   * ``Ctrl``: ``C-`` or ``^``
   * ``Alt``/Meta: ``M-``
   * Super/Windows, ``Super``: ``S-``

   These can be stacked as either:
   * ``C-M-x``, which means press and hold ``Ctrl`` and ``Alt``, and then tap x;
   or
   * ``C-c M-x``, which means press and hold ``Ctrl`` and tap ``c``, and then press and hold ``Alt`` and tap ```x``.

Whilst **nano** will prompt us to save the file if we have not done already, we can do this manually.  To *Write Out*, or save the file press ``^O``. Nano will prompt for a file name; if the file already has a name, this will be pre-filled, but can be changed. Press ``Enter`` to confirm.
     
* ``^X`` - eXit nano. Nano prompts you to save if you have not already.
* ``^O`` - write Out. This saves the file, with its current name

If you started a command and want to cancel it, or just got stuck in a menu, press ``^C`` to cancel.

Navigating files
================

To navigate through text in **nano** we use the same keys as on the command line.

* Left and Right ``Arrow keys`` - move the cursor along the line.
* Up and Down ``Arrow keys`` - move cursor up and down one line at a time.
* ``PgUp`` and ``PgDn`` - move up and down one page at a time.
* ``Home`` and ``End`` - move to beginning and end of line.

Deleting, Cutting and Pasting text
==================================

To delete text in ``nano`` we use the ``del`` (delete) key and the ``backspace`` key.  They work slightly differently to each other.  The ``del`` key will delete one character at a time to the right of the cursor. The ``backspace`` key will delete one character at a time to the left of the cursor.

To delete more than one character at a time, we use the cut commands.

Cutting and pasting text
--------------------------

``^K`` will cut text, but only whole lines at a time.  ``^U`` will then paste the text at the cursors current position.

To cut only specific sections of text, press ``^^`` (that is, hold ``Ctrl`` and ``Shift``, and then press ``6``).  This will mark the start of the text to cut, we can then move the cursor with with arrow keys to the end of the text we wish to cut and press ``^K`` to cut it.


Undoing actions
===============

If we make a mistake, we can undo this by press ``M-U``.  To undo an undo, that is, to redo something we press ``M-E``.

------------------------------

Summary
=======

Concepts
--------

* Many text editors exits in linux.
* Command line text editors use the keyboard and do not use the mouse.
* Many linux programs make use of key combinations and modifier keys.
* ``^`` or ``C-`` means press and hold the ``Ctrl`` key, and then tap the next key shown.
* ``M-`` means press and hold the ``Alt`` or ``Meta`` key, and then tap the next key shown.
* ``S-`` means press and hold the ``Super`` or windows key, and then tap the next key shown.

Commands
--------

* ``nano <filename>`` - open file.
* ``^X`` - Exit nano
* ``^O`` - Save file.
* ``^K`` - Cut the whole line of text.
* ``^U`` - Paste or *uncut* text.
* ``^^`` (``C-^``) - mark the beginning of text to cut, mark the end with ``^K``.
* ``M-U`` - undo a change.
* ``M-U`` - redo a change.

Exercises
=========
* Use nano to create a files with a few lines of text.
* Using find and replace, make sure every sentance ends with the word *penguin*.
* Save the file.
* Move the first line to the bottom of the file.
* Exit ``nano``.
  
Further Reading
===============

`Nano Manual <https://www.nano-editor.org/dist/v2.6/nano.html>`_
