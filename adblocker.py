#!/usr/bin/python
import os,sys, platform
hosts = ["https://adaway.org/hosts.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"]
count = 1
print(r'''

           _ _     _            _                               
  __ _  __| | |__ | | ___   ___| | _____ _ __       _ __  _   _ 
 / _` |/ _` | '_ \| |/ _ \ / __| |/ / _ \ '__|     | '_ \| | | |
| (_| | (_| | |_) | | (_) | (__|   <  __/ |     _  | |_) | |_| |
 \__,_|\__,_|_.__/|_|\___/ \___|_|\_\___|_|    (_) | .__/ \__, |
                                                   |_|    |___/ 

                                        @gitub.com/iam-shanmukha
	''')

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

elif platform.system() == 'Windows':
        print("starting Script on Windows")
        try:
                os.popen(r"copy c:\Windows\System32\Drivers\etc\hosts c:\Windows\System32\Drivers\etc\hosts_backup /y")
                open(r'c:\Windows\System32\Drivers\etc\hosts','w').close()
                print("Backup old file Success")
                for i in hosts:
                        cmd = r"curl -s {} -o c:\Windows\System32\Drivers\etc\hosts".format(i)
                        os.system(cmd)
                        print("completed {}/{}".format(count,len(hosts)))
                        count = count+1
                print("Successfully Blocked AD's")
                sys.exit()
        except PermissionError:
                print("Abort! Please run as Administrator")
                sys.exit()
                        
else:
        print("Sorry! Platform Not Supported")
        
