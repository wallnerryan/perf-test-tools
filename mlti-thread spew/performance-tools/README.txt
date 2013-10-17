*Tested on Ubuntu 12.04, Python 2.7.5*

Spawn multiple "spew" commands into multiple threads.

Used for scale-out testing. 

Example: 
(This will spawn three separate threads which will write to file0-2 on device /dev/sdx mounted on /mnt)

	1.  mount /dev/sdx /mnt

	2. ./spew_tool.py 3 "spew --write -u m -b 8k 6860m /mnt/file"


