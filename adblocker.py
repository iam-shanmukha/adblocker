#!/usr/bin/python
import os,sys, platform
import datetime
hosts = ["https://adaway.org/hosts.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
"https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt"]
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
	if os.geteuid() != 0:
		print("Please run as root \nsudo python adblocker.py")
		sys.exit()
	basename = "hosts_"
	suffix = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
	filename = "_".join([basename, suffix])
	os.system(r"sudo cp /etc/hosts /etc/{}".format(filename))
	print("Backup success \nBackup file --> /etc/{}".format(filename))
	open('/etc/hosts', 'w').close()
	for i in hosts:
		cmd = "sudo curl -s {} >> /etc/hosts".format(i)
		#print(cmd)
		os.system(cmd)
		print("completed {}/{}".format(count,len(hosts)))
		count = count+1
	print("Successfully Blocked Ad's")
	sys.exit()

elif platform.system() == 'Windows':
        print("starting Script on Windows")
        try:
                os.popen(r"copy c:\Windows\System32\Drivers\etc\hosts c:\Windows\System32\Drivers\etc\hosts_backup /y")
                print("Backup old file Success")
                open(r'c:\Windows\System32\Drivers\etc\hosts','w').close()
                for i in hosts:
                        cmd = r"curl -s {} >> c:\Windows\System32\Drivers\etc\hosts".format(i)
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
