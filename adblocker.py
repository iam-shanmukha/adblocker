

#!/usr/bin/python
import os,sys, platform
import datetime
hosts = ["https://adaway.org/hosts.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"]

WINDOWS_ETC = "c:\\Windows\\System32\\Drivers\\etc\\"
WINDOWS_HOSTS = "c:\\Windows\\System32\\Drivers\\etc\\hosts"
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

basename = "hosts_"
suffix = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
filename = "_".join([basename, suffix])

def execute():
    global count
    os.system(cmd)
    print(f'completed {count}/{len(hosts)}')
    count = count+1

if platform.system() == 'Linux':
        print("Starting Script on Linux")
        try:
                if os.geteuid() !=0:
                    raise PermissionError
                os.system(r"sudo cp /etc/hosts /etc/{}".format(filename))
                print("Backup success \nBackup file --> /etc/{}".format(filename))
                open('/etc/hosts', 'w').close()
                for i in hosts:
                    cmd = f'sudo curl -s {i} >> /etc/hosts'
                    execute()
                print("Successfully Blocked Ad's")
                sys.exit()
        except PermissionError:
                print("Please run as root \nsudo python adblocker.py")
                sys.exit()
elif platform.system() == 'Windows':
        print("starting Script on Windows")
        try:    
                os.system(f'copy {WINDOWS_HOSTS} {WINDOWS_ETC}{filename} /y')
                print(f'Backup success \nBackup file --> {WINDOWS_ETC}{filename}')
                open(f'{WINDOWS_HOSTS}','w').close()
                for i in hosts:
                        cmd = f'curl -s {i} >> {WINDOWS_HOSTS}'
                        execute()
                print("Successfully Blocked AD's")
                sys.exit()
        except PermissionError:
                print("Abort! Please run as Administrator")
                sys.exit()
else:
        print("Sorry! Platform Not Supported")

