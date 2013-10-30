def sendalert(subject, body):

	import smtplib
	import datetime

	sender = 'info@dangerous-playground.com'
	passwordfile = open('password', 'r')
	password = passwordfile.readline()
	password = password.rstrip()	
	recipient = 'tdkwon@gmail.com'
	headers = ["From: " + sender,
	"Subject: " + subject,
	"To: " + recipient,
	"MIME-Version: 1.0",
	"Content-Type: text/html"]
	headers = "\r\n".join(headers)
	    
	try:
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.ehlo()
		session.starttls()
		session.ehlo()
		session.login(sender, password)
		session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
		session.quit()
		print "successful"
	except smtplib.SMTPException:
		todaydate = datetime.date.today()
		todaydate = str(todaydate)
		error_msg = todaydate + " Error: unable to send\n"
		ofp = open('sendalert.log', 'a')
		ofp.write(error_msg)
		ofp.close()

