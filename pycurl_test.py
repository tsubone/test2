#!/usr/bin/env python

import pycurl
from StringIO import StringIO

buffer = StringIO ()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.sourceforge.net')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
print body
