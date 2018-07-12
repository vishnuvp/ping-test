from flask import Flask
import subprocess
import socket
import time

app = Flask(__name__)
ipList = [socket.gethostbyname("instance-x.web-server-1.com"), socket.gethostbyname("instance-y.web-server-1.com")	]
#[socket.gethostbyname("instance-w.web-server-1.com"), socket.gethostbyname("instance-x.web-server-1.com"), socket.gethostbyname("instance-y.web-server-1.com"), socket.gethostbyname("instance-z.web-server-1.com")]
localhost = socket.gethostbyname(socket.gethostname())
ipList.remove(localhost)

@app.route('/')
def hello_world():
	return_text ="<html><head><title>Connection Status</title></head><body style='text-align:center'>"
	for ip in ipList:
	    res = subprocess.Popen(['ping', '-c', '3', ip],stdout=subprocess.PIPE)
	    stdout, stderr = res.communicate()
	    if res.returncode == 0:
	            return_text += '<div>' + ip.split('.')[0] + " ..... Connected</div>"
	    elif res.returncode == 2:
	            return_text += '<div>' + ip.split('.')[0] + " ..... Unreachable</div>"
	    else:
	            return_text += '<div>' + ip.split('.')[0] + " ..... Unreachable</div>"
	return_text += "</body></html>"
	return return_text

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)




#print localhost
# try:
#         while True:
#                 for ip in ipList:
#                         if (ip !=localhost):
#                                 res = subprocess.Popen(['ping', '-c', '3', ip],stdout=subprocess.PIPE)
#                                 stdout, stderr = res.communicate()
#                                 if res.returncode == 0:
#                                         print "ping to", ip, "is successful"
#                                 elif res.returncode == 2:
#                                         print "no response from", ip
#                                 else:
#                                         print "ping to", ip, "failed!"

#                 time.sleep(2)
#                 continue
# except KeyboardInterrupt:
#         print "Ping stopped by user"