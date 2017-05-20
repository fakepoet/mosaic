#!/usr/bin/env python
# coding=utf-8


class InlineElement(object):
    """The abstract inline element."""

    def __init__(self):
        self.subs = []       # The sub elements.


class TextElement(InlineElement):
    """The text element."""

    def __init__(self):
        super(TextElement, self).__init__()


class SoftLineBreakElement(InlineElement):
    """The soft line break element."""

    def __init__(self):
        super(SoftLineBreakElement, self).__init__()
