#!/usr/bin/python
# file: server.py
# desc: will sync both jpeg files and compiled binary across client and server
# One should change the paths of clienDir & serverDir in both functions

# import time
import sys
import os


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

    makeDir(serverDir)
    
    rsync_command = 'rsync -rvth ' + clientDir + ' ' + serverDir + '&>' + blackHole

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

    rsync_command = 'rsync -rvth ' + serverDir + ' ' + clientDir + '&>' + blackHole

    if os.system(rsync_command) == 0:
        print 'Successfully synced binary to ', clientDir
    else:
        print 'ERROR: Sync for binary FAILED'

def makeDir(destDir):
    # check if the destination path already exist, if not, create it.
    if not os.path.exists(destDir):
        os.mkdir(destDir)             # make directory
        print 'Successfully created directory', destDir
        
if __name__ == "__main__":
    syncImage()
    syncBinary()


