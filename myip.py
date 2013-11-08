import sendalert
import urllib2
import re
import os
import datetime

my_url = 'http://www.whatismyip.com/ip-tools/ip-address-lookup/'
response = urllib2.urlopen(my_url)

if response.getcode() == 200:
	# Get all data
	html = response.read()
	match = re.search(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', html)
	new_ip = match.group()
else:
	print "not 200"
	
try:	
	ifp = open('/home/pi/django/myip/ipfile.txt','r')
	old_ip = ifp.read()
	ifp.close()
except IOError:
	old_ip = "0.0.0.0"

try:
	logfile = open('/home/pi/django/myip/myip.log', 'a')
except IOError:
	print "Failed to open myip.log"	

todaysdate = str(datetime.date.today())

if old_ip == new_ip:
	print "no change"
	logfile.write(todaysdate + " no change\n")
else:
	ofp = open('/home/pi/django/myip/ipfile.txt', 'w')
	ofp.write(new_ip)
	print old_ip, ' changed to ', new_ip
	subject = "Your IP has been changed to: " + new_ip
	body = old_ip + " has been changed to " + new_ip
	sendalert.sendalert(subject, body)
	
