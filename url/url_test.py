#!/usr/bin/env python

import urllib

response = urllib.urlopen ("http://www.asahi.com")
print 'RESPONSE' :, response
print 'URL'      :, response.geturl()

