#import os
import ConfigParser
import subprocess

p = subprocess.Popen('git pull | find "Already"', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line)

#mFile = open(mPath,'r')
#lines = mFile.readlines()
#for line in lines:
#    print line.split('=')[0],
#mFile.close()

mConfig = ConfigParser.ConfigParser()
mConfig.read('config.ini')
print mConfig.get('settings', 'version')