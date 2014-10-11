import pickle
import socket
from struct import *
import time
import random
import sys
from time import strftime, localtime
import shared

def createDefaultKnownNodes(appdata):
    ############## Stream 1 ################
    stream1 = {}

    #stream1[shared.Peer('2604:2000:1380:9f:82e:148b:2746:d0c7', 8080)] = int(time.time())
    stream1[shared.Peer('68.33.0.104', 8444)] = int(time.time())
    stream1[shared.Peer('97.77.34.35', 8444)] = int(time.time())
    stream1[shared.Peer('71.232.195.131', 8444)] = int(time.time())
    stream1[shared.Peer('192.241.231.39', 8444)] = int(time.time())
    stream1[shared.Peer('75.66.0.116', 8444)] = int(time.time())
    stream1[shared.Peer('182.169.23.102', 8444)] = int(time.time())
    stream1[shared.Peer('75.95.134.9', 8444)] = int(time.time())
    stream1[shared.Peer('46.236.100.108', 48444)] = int(time.time())
    stream1[shared.Peer('66.108.53.42', 8080)] = int(time.time())
    
    ############# Stream 2 #################
    stream2 = {}
    # None yet

    ############# Stream 3 #################
    stream3 = {}
    # None yet

    allKnownNodes = {}
    allKnownNodes[1] = stream1
    allKnownNodes[2] = stream2
    allKnownNodes[3] = stream3

    #print stream1
    #print allKnownNodes

    with open(appdata + 'knownnodes.dat', 'wb') as output:
        # Pickle dictionary using protocol 0.
        pickle.dump(allKnownNodes, output)

    return allKnownNodes

def readDefaultKnownNodes(appdata):
    pickleFile = open(appdata + 'knownnodes.dat', 'rb')
    knownNodes = pickle.load(pickleFile)
    pickleFile.close()
    for stream, storedValue in knownNodes.items():
        for host,value in storedValue.items():
            try:
                # Old knownNodes format.
                port, storedtime = value
            except:
                # New knownNodes format.
                host, port = host
                storedtime = value
            print host, '\t', port, '\t', unicode(strftime('%a, %d %b %Y  %I:%M %p',localtime(storedtime)),'utf-8')

if __name__ == "__main__":

    APPNAME = "PyBitmessage"
    from os import path, environ
    if sys.platform == 'darwin':
        from AppKit import NSSearchPathForDirectoriesInDomains  # @UnresolvedImport
        # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
        # NSApplicationSupportDirectory = 14
        # NSUserDomainMask = 1
        # True for expanding the tilde into a fully qualified path
        appdata = path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], APPNAME) + '/'
    elif 'win' in sys.platform:
        appdata = path.join(environ['APPDATA'], APPNAME) + '\\'
    else:
        appdata = path.expanduser(path.join("~", "." + APPNAME + "/"))


    print 'New list of all known nodes:', createDefaultKnownNodes(appdata)
    readDefaultKnownNodes(appdata)

