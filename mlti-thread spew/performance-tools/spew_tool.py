#!/usr/bin/python
#
#This script takes a "spew" I/O testing string of commands
#and runs the commands in a given number of threads passed in by the user
#

import sys
import os
import re
import threadedspew
import time
import subprocess


__author__ = "ryan.wallner@emc.com"
__version__ = "$Revision: 1.1 $"
__date__ = "2012/07/12 "

if __name__ == "__main__":

    dnull = open(os.devnull, 'w')
    val = subprocess.call(['dpkg','-s','spew']
	,stdout=dnull,stderr=subprocess.STDOUT)
    dnull.close()
    if val != 0:
	print "Please install spew, 'sudo apt-get install spew'"    
        exit(1)

    def usage():
        print '''
	    usage %s <#ofthreads> "spew-string"
	      ''' % sys.argv[0]
        print '''
	    Supportsed OPTIONS
		Type: "spew --help" for options
	       '''
               
    if len(sys.argv) == 2:
        if sys.argv[1] == "-?":
            usage()
        elif sys.argv[1] == "--help":
            usage()
    if len(sys.argv) <= 2:
        usage()
    if len(sys.argv) > 3:
	usage()
	
    if len(sys.argv) > 2:
        cmd = sys.argv[0]
	threads = sys.argv[1] 
    
	#get spew string
	spew_str = sys.argv[2]
	print spew_str
	    
        
	#call threaded spew class to pass in the queue
	t = 0
	print "threading %s in %d threads " % (cmd,int(threads))
	while t < int(threads):
	    # t count is for /bigfile1 /bigfile2 etc...
	    cmd = "%s%s" % (spew_str.rstrip(),t)
	    thread = threadedspew.SpewClient(cmd)
	    thread.start()
	    thread.is_alive()
	    t = t + 1
        
	        #TIMING??!!***
    else:
        print '''
		Type %s -? or --help for usage
	      ''' % sys.argv[0]
    
