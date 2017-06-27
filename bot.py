#import os
#import ConfigParser

mFile = open(mPath, `r`)
lines = mFile.readlines()
for line in lines:
    print line.split(`=`)[0],
mFile.close()

c = ConfigParser.ConfigParser()
c.read(`dd.ini`)
print c.get(`setting`, `valuse`)
