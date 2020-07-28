#!/usr/bin/python
import os,sys, platform
hosts = ["https://adaway.org/hosts.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"]
count = 1
if platform.system() == 'Linux':
	print("Starting Script on Linux")
	try:
		open('/etc/hosts', 'w').close()
		for i in hosts:
			cmd = "sudo curl -s {} >> /etc/hosts".format(i)
			#print(cmd)
			os.system(cmd)
			print("completed {}/{}".format(count,len(hosts)))
			count = count+1
		print("Successfully Applied")
		sys.exit()
	except PermissionError:
		print("Please run as root \nsudo python adblocker.py")
		sys.exit()