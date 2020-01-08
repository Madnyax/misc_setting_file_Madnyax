import datetime
import subprocess
import os

now_str = datetime.datetime.now()
string = str(now_str.year) + '_' + str(now_str.month) + '_' + str(now_str.day)  + '_' + str(now_str.hour) + '_' + str(now_str.minute)  + '_' + str(now_str.second)

#cmd = 'sudo tcpdump -I -Q in -i wlan1 -w ./a_rssi/wifi_rssi_.pcap subtype probereq ' 
#process = (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
#result = subprocess.check_output(["sudo tcpdump","-I", "-Q in", "-i wlan1", "-w ./a_rssi/wifi_rssi_.pcap", "subtype probereq"])
#print(result)

shell_str = 'sudo tcpdump -I -Q in -i wlan1 -w ./a_rssi/wifi_rssi_' + string +  '.pcap'
#os.system('sudo tcpdump -I -Q in -i wlan1 -w ./a_rssi/wifi_rssi_%s.pcap subtype probereq',string )

os.system(shell_str)
