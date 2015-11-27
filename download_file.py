# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:29:54 2015

@author: saqibullah
@email: saqibullah@gmail.com
"""

import urllib2
import getpass
from datetime import date, timedelta


def get_Username():
    return getpass.getuser()

def get_Previousdate():
    previous = date.today() - timedelta(1)
    return previous.strftime('%y%m%d')


weblogfile = "access_{}.log".format(get_Previousdate())
print weblogfile
response = urllib2.urlopen("http://hopebuild.org/logs/"+weblogfile)
data = response.read()
 
filename = "/home/{}/Downloads/{}".format(get_Username(),weblogfile)    
# Write web log data to file
with open(filename, 'w') as code:
    code.write(data)