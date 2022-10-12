'''
	Not complex hash identifier
	Looking for salts only
	hashType -- first 3 charachter in password text
	Chack this website to understand unix how password hashing works on linux
	website -- https://www.networkworld.com/article/3629440/how-password-hashing-works-on-your-linux-system.html

	hashTypes 
	---------
	$1$ means MD5
	$2a$ means Blowfish
	$2y$ means Blowfish
	$5$ means SHA-256
	$6$ means SHA-512
'''
def hashIdentifier(password):
	if password[0] == "$":
		salt = re.search(r'\$(.*)\$', password).group(1)
	
	salt = str(salt)

	if salt == "1":
		return ["MD5", password[3:]]
	elif salt == "2a" or salt == "2y":
		return ["Blowfish", password[4:]]
	elif salt == "5":
		return ["SHA-256", password[3:]]
	elif salt == "6":
		return ["SHA-512", password[3:]]
	else:
		return ["Didnt found", password]