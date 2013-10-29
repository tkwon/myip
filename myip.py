import urllib2
import re

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
	ifp = open('ipfile.txt','r')
	old_ip = ifp.read()
	ifp.close()
except IOError:
	old_ip = "0.0.0.0"


if old_ip == new_ip:
	print "no change"
else:
	ofp = open('ipfile.txt', 'w')
	ofp.write(new_ip)
	print old_ip, ' changed to ', new_ip