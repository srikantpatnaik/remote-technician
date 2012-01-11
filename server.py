#!/usr/bin/python
# file: server.py
# desc: will sync both jpeg files and compiled binary

# import time
import sys
import os

# blackHole
blackHole = '/dev/null'
rsync_command = 'rsync -rvth ' + sourceDir + ' ' + destDir + '&>' + blackHole

# sync jpeg image
def syncImage():
    # source
    sourceDir = '/home/linus/temp/github/remote-technician/src/'
    # destination
    destDir = '/home/linus/temp/github/remote-technician/dest'

    if os.system(rsync_command) == 0:
        print 'Successfully synced all jpeg images to ', destDir
    else:
        print 'ERROR: Sync for jpeg FAILED'

# sync binary
def syncBinary():
    # source
    sourceDir = '/home/linus/temp/github/remote-technician/src-bin/'
    # destination
    destDir = '/home/linus/temp/github/remote-technician/dest-bin'

    if os.system(rsync_command) == 0:
        print 'Successfully synced binary ', destDir
    else:
        print 'ERROR: Sync for binary FAILED'


syncImage()
syncBinary()









