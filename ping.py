import subprocess
import socket
import time


ipDict = {socket.gethostbyname("instance-w.web-server-1.com"): "instance-w.web-server-1.com", socket.gethostbyname("instance-x.web-server-1.com"): "instance-x.web-server-1.com", socket.gethostbyname("instance-y.web-server-1.com"):  "instance-y.web-server-1.com", socket.gethostbyname("instance-z.web-server-1.com"):  "instance-z.web-server-1.com"}
ipList = list(ipDict.keys())
#[socket.gethostbyname("instance-w.web-server-1.com"), socket.gethostbyname("instance-x.web-server-1.com"), socket.gethostbyname("instance-y.web-server-1.com"), socket.gethostbyname("instance-z.web-server-1.com")]
localhost = socket.gethostbyname(socket.gethostname())
if localhost in ipList:
	ipList.remove(localhost)

while True:
	return_text = ""
	for ip in ipList:
	    res = subprocess.Popen(['ping', '-c', '3', ip],stdout=subprocess.PIPE)
	    stdout, stderr = res.communicate()
	    if res.returncode == 0:
	            #return_text += '<div>' + ipDict[ip].split(".")[0].upper() + " .....<span style='color:green'> Connected</span></div><br />"
	            return_text += ipDict[ip].split(".")[0].upper() + " ...... Connected\n"
	    elif res.returncode == 2:
	            return_text += ipDict[ip].split(".")[0].upper() + " ...... Unreachable\n"
	    else:
	            return_text += ipDict[ip].split(".")[0].upper() + " ...... Unreachable\n"
	#return_text += "</body></html>"
	print(return_text)




