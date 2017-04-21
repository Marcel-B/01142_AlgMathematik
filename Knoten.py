# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.
Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

class Knoten:
    """Stellt einen Knoten aus einem Graphen dar"""
    def __init__(self):
        """ Eine Liste mit Vorgängern"""
        self.pred = []
        """ Eine Liste mit Nachfolgern """
        self.succ = []
        print("Node initialized")

    def add_knoten_pred(self, knoten):
        """ Fuegt der Adjazenzliste Knoten hinten hinzu"""
        self.pred.append(knoten)
        print("new knoten added")

    def add_knoten_succ(self, knoten):
        """ Fuegt der Adjazenzliste Konten vorne hinzu"""
        self.succ.append(knoten)

    def print_me(self):
        """ eine einfache alberne ausgabe """
        print("Hello")
