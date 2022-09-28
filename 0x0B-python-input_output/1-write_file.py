#!/usr/bin/python3
"""Function that Defines a file-writing."""


def write_file(filename="", text=""):
    """Write a string to a UTF"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
