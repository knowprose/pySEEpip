# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:12:51 2019

@author: Taran

Gets a snapshot of modules in the Software Engineering Environment. 
"""

import pkg_resources
import datetime 

#setup filename
now = datetime.datetime.now()
#filename = now.year() + now.month() + now.(day)
filename = "SEEpip"+ now.strftime("%Y-%m-%d")+".txt"

print (filename)

dists = [d for d in pkg_resources.working_set]
#print (dists)
local_pip_list = sorted(["%s==%s" % (ii.key, ii.version) for ii in dists])

with open(filename,"w+") as f:
    for item in local_pip_list:
        f.write("%s\n" % item)
        print(item)

f.close()