#Imports
import urllib2
import smtplib
from email.mime.text import MIMEText
from BeautifulSoup import BeautifulSoup

#Vars
#Page to fetch
url = "http://cablebel.be/pag/metalprices.php"

#File to read from / write to 
tmpfile = "/tmp/cokoers"

##### MAIL SETTINGS #####
#From address in email
from_address = 'noreply@xxxxxxx.be'

#Address to send the mail to
to_address = 'xxxxxxxxxxxxxxx'

#Mail subject
subject = 'Koperkoerswijziging'

#SMTP Server
smtp_server = 'localhost'

#Script
#Open file read-only
f = open(tmpfile,'r')
old_price = f.readline()
f.close()

#fetching current price
opener = urllib2.build_opener()
url_opener = opener.open(url)
page = url_opener.read()
html = BeautifulSoup(page)
priceString = html.find("span", {"class" : "title-text"}).string
price = priceString.split(" ")[6]

#checking
if (price != old_price):
    #price has changed.
    #Preparing email
    msg = MIMEText("\nAutomatisch bericht\n\nKoperkoerswijziging naar: "+price+"\n\n")
    msg['Subject'] = 'Koperkoerswijziging'
    msg['From'] = from_address
    msg['To'] = to_address
    s = smtplib.SMTP(smtp_server)
    s.sendmail(from_address,to_address,msg.as_string())
    s.quit()

    #Mail has been sent. Writing new value to file
    f = open(tmpfile,'w')
    f.write(price)
    f.close()
    #All done



