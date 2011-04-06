#!/usr/bin/python
import os, re, string, sys, traceback
from pxletters import pxletters
print "Content-Type: text/html; charset=ISO-8859-1\n"

test = pxletters('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz^Hey^no^1234567890^,./?!@\'"')

print '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Example</title>
<link rel="stylesheet" type="text/css" href="pxletters.css" />
</head>

<body>
'''
test.write()
print '''
</body>

</html>
'''
