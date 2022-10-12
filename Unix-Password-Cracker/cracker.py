
# Unix Password Cracker
# Musa Akyüz

# The crypt module is not supported on Windows
import crypt
import os
import re


'''
 	testPass function
 	-----------------
 	parameter -- password -- which taking hashed passwords

	Find your unix hashed password on this file;
 	/etc/shadow (needed root previlege)
'''
def testPass(password, dictFilePath):

	# CHECKING ON DICTIONARY
	dictFile = open(dictFilePath, "r")
	for word in dictFile.readlines():
		word = word.strip("\n")
		cryptWord = crypt.crypt(word, crypt.METHOD_SHA256)
		print("word : " + word + "cryptWord : " + cryptWord)
		if cryptWord == password:
			return "[+] Found password : " + word + "\n"
	return "[-] Not in dictionary file !!!"

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
	else:
		salt = None
		
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
	
def main():
	testPass("$5$EU9QNNm6Tpk3oizd$o6r.l4RtEN8JFKmVmr3EHqsd2ZERkBJVGTWrDekHGg7", "dict.txt")
			
if __name__ == "__main__":
	main()



	

	
	

