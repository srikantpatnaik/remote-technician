#!/usr/bin/python
# file: server.py
# desc: will sync both jpeg files and compiled binary across client and server
# One should change the paths of clienDir & serverDir in both functions

# import time
import sys
import os

# blackHole
blackHole = '/dev/null'

# sync jpeg image
def syncImage():
    # source
    clientDir = '/home/linus/temp/github/remote-technician/src/'
    # destination
    serverDir = '/home/linus/temp/github/remote-technician/dest'

    rsync_command = 'rsync -rvth ' + clientDir + ' ' + serverDir + '&>' + blackHole

    if os.system(rsync_command) == 0:
        print 'Successfully synced all jpeg images to ', serverDir
    else:
        print 'ERROR: Sync for jpeg FAILED'

# sync binary
def syncBinary():
    # source
    serverDir = '/home/linus/temp/github/remote-technician/src-bin/'
    # destination
    clientDir = '/home/linus/temp/github/remote-technician/dest-bin'

    rsync_command = 'rsync -rvth ' + serverDir + ' ' + clientDir + '&>' + blackHole

    if os.system(rsync_command) == 0:
        print 'Successfully synced binary to ', clientDir
    else:
        print 'ERROR: Sync for binary FAILED'


if __name__ == "__main__":
    syncImage()
    syncBinary()

