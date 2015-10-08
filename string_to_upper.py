
import re

def repl_func(m):
    """process regular expression match groups for word upper-casing problem"""
    return m.group(1) + m.group(2).upper()

def string_to_upper(string):
	return re.sub("(^|\s)(\S)", repl_func, string)
