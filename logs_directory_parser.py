# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:06:04 2015

@author: saqibullah
"""

from lxml import html
import urllib2
import getpass

def get_Username():
    return getpass.getuser()

#Open logs directory using urlopen method
response = urllib2.urlopen("http://hopebuild.org/logs/")

#read http response into data variable
data = response.read()
tree = html.fromstring(data)

#using xpath get all <a href /> tags from response data
filenames = tree.xpath('//a/@href')

prefix = "access_"
for filename in filenames:
    # if file name start from access_ prefix
    if prefix in filename:       # 
        response = urllib2.urlopen("http://hopebuild.org/logs/"+filename)
        data = response.read() 
        print "download {} file".format(filename)        
        local_filename = "/home/{}/Downloads/weblogs/{}".format(get_Username(),filename)        
        # Write web log data to file
        with open(local_filename, 'w') as code:
            code.write(data)