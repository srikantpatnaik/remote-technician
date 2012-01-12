#!/usr/bin/python
# file: server.py
# desc: will sync both jpeg files and compiled binary across client and server
# One should change the paths of clienDir & serverDir in both functions

import sys
import os

# user
frm_user='sachin'
to_user='sachin'

# enter hostname or IP address
frm_host='ver'
to_host='localhost'

# client='sachin@ver:'
# server='sachin@localhost:'

client=frm_user + '@' + frm_host + ':'
server=to_user + '@' + to_host + ':'

print client
print server

# comman-path to both server and client
commonPath='/tmp/remote-technician'

# blackHole, to store all the dump
blackHole = '/dev/null'

# sync jpeg image
def syncImage():
    # source
    clientDir = commonPath + '/src/'
    # destination
    serverDir = commonPath + '/dest'

    if not os.path.exists(client + clientDir):
        print 'ERROR: No src.'

    makeDir(serverDir)
    
    rsync_command = 'rsync -rvth ' + client + clientDir + ' ' + serverDir + ' &> ' + blackHole

    # print rsync_command

    if os.system(rsync_command) == 0:
        print 'Successfully synced all jpeg images to ', serverDir
    else:
        print 'ERROR: Sync for jpeg FAILED'

# sync binary
def syncBinary():
    # source
    serverDir = commonPath + '/src-bin/'
    # destination
    clientDir = commonPath + '/dest-bin'

    makeDir(clientDir)

    rsync_command = 'rsync -rvth ' + serverDir + ' ' + client + clientDir + '&>' + blackHole

    print rsync_command
    # if os.system(rsync_command) == 0:
    #     print 'Successfully synced binary to ', clientDir
    # else:
    #     print 'ERROR: Sync for binary FAILED'

# check if the destination path already exist, if not, create it.
def makeDir(destDir):
    if not os.path.exists(destDir):
        os.makedirs(destDir)             # make directories
        print 'Successfully created directory', destDir
        
if __name__ == "__main__":
    syncImage()
    # syncBinary()



'''
TODO:
=====

for JPEG file:
-------------
- Check for remote(client) path[client@hostname:/tmp/remote-technician/src/], if exist, then
check/create dir on server[/tmp/remote-technician/dest]. Finally sync *.jpg files on server.

for binary file:
----------------
- Check for server path[/tmp/remote-technician/src-bin/], if exist,then check/create dir on
client[client@hostname:/tmp/remote-technician/dest-bin] and finally sync binary file on client

some change for testing-branch

'''

