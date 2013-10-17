#!/usr/bin/python
#Threaded Python Program for spew(1)
import os
import sys
import time
import subprocess
import threading    #python Thread inheritance 
import logging

__author__ = "ryan.wallner@emc.com"
__version__ = "$Revision: 1.1 $"
__date__ = "2012/07/12 "

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

class SpewClient(threading.Thread):
    
    def __init__(self,cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
        return
    
    def run(self):
        """ Run a *spew command in a separate thread and process.

        """
        try:
            logging.debug("running %s" % self.cmd)
            starttime = time.time()
            p = subprocess.Popen(self.cmd, shell=True)
            print "parent ppid: %s and this process pid: %s" % (os.getppid(),p.pid)
            p.wait()
	    #print threading.enumerate() #Debug Current Threads
	    # Subtract 1 because of the MainThread
	    print "%d threads still alive" % (len(threading.enumerate())-1)
            logging.debug("total time for %s was %s " % (self.cmd,(time.time()-starttime)))
        except ValueError as e:
            print e
        return
            
