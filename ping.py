import subprocess
import socket
import time
import os

ipDict = {socket.gethostbyname("instance-w.web-server-1.com"): "instance-w.web-server-1.com", socket.gethostbyname("instance-x.web-server-1.com"): "instance-x.web-server-1.com", socket$
ipList = list(ipDict.keys())
#[socket.gethostbyname("instance-w.web-server-1.com"), socket.gethostbyname("instance-x.web-server-1.com"), socket.gethostbyname("instance-y.web-server-1.com"), socket.gethostbyname("i$
localhost = socket.gethostbyname(socket.gethostname())
if localhost in ipList:
        ipList.remove(localhost)

while True:
	return_text = ""
        for ip in ipList:
            res = subprocess.Popen(['ping', '-w', '1', '-c', '1', ip],stdout=subprocess.PIPE)
            stdout, stderr = res.communicate()
            if res.returncode == 0:
                    #return_text += '<div>' + ipDict[ip].split(".")[0].upper() + " .....<span style='color:green'> Connected</span></div><br />"
                    return_text += "  " + ipDict[ip].split(".")[0].upper() + " ...... Connected\n"
            elif res.returncode == 2:
                    return_text += "  " + ipDict[ip].split(".")[0].upper() + " ...... Unreachable\n"
            else:
                    return_text += "  " + ipDict[ip].split(".")[0].upper() + " ...... Unreachable\n"
        #return_text += "</body></html>"
        # res.kill()
        os.system('cls||clear')
        print("\n\n\n")
        print("Connection Status (Updates every second)")
        print(return_text)
        time.sleep(1)


