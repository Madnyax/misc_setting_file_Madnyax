import datetime
import subprocess
import os

now_str = datetime.datetime.now()
string = str(now_str.year) + '_' + str(now_str.month) + '_' + str(now_str.day)  + '_' + str(now_str.hour) + '_' + str(now_str.minute)  + '_' + str(now_str.second)

shell_str = 'sudo tcpdump -I -Q in -i wlan1 -w ./a_rssi/wifi_rssi_' + string +  '.pcap subtype probereq'

#os.system('sudo ./c_mode_change.sh')
#os.system('sudo ./c_hopper.sh &')
os.system(shell_str)
