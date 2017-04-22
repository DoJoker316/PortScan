#coding=utf-8
#By DoJoker 2017-04-22
#Python 2.x
#Use: xxx.py -H xxx.xxx.xxx.xxx -p xx xx

import optparse
import socket
from socket import *
def connScan(tgtHost,tgtPort):
	try:
		connSkt =socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		connSkt.send('ViolentPython\r\n')
		results =connSkt.recv(100)
		print '[+]%d/tcp open'% tgtPort
		print '[+] '+str(results)
		connSkt.close()
	except:
		print '[-]%d/tcp closed'% tgtPort
def portScan(tgtHost,tgtPorts):
	try:
		tgtIP =gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s' : Unknown host"% tgtHost
		return
	try:
		tgtName =gethostbyaddr(tgtIP)
		print '\n[+] Scan Results For : ' + tgtName[0]
	except:
		print '\n[+]Scan Results For : ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print 'Scanning port '+tgtPort
		connScan(tgtHost,int(tgtPort))
def main():
	# Writing parameter on script ,inlcuding host and ports 
	parser = optparse.OptionParser("usage%prog "+\
		"-H <target host> -p <target port>")
	parser.add_option('-H',dest = 'tgtHost',type = 'string',\
		help='specify target host')
	parser.add_option('-p',dest = 'tgtPort',type = 'string',\
		help ='specify target port[s] separated by comma')
	# Make port entered to list named ports 
	(options, args) =parser.parse_args()
	tgtHost =options.tgtHost
	tgtPorts =str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print '[-] You must specify a target host and port[s].'
		exit(0)
	# Scanning
	portScan(tgtHost, tgtPorts)
if __name__ == "__main__":
	main()
