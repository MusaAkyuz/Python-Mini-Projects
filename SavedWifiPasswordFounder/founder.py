
# Learn saved wifi password
import subprocess

# bringing info from subprocess
metaData = subprocess.check_output(["netsh", "wlan", "show", "profiles"])
#print(metaData)

# converting to humanly understanding
data = metaData.decode("utf-8", errors="backslashreplace")
#print(data)

# splitting every line
# conveting list actually
data = data.split('\n')
#print(data)

profiles = []

for line in data:
    if "All User Profile" in line:
        # again splitting line with ":"
        # so we can read the value of all profiles
        line = line.split(":")

        # reading profile name
        line = line[1]

        # first charachter is spc char " "
        # last charachter is /r
        line = line[1:-1]
        profiles.append(line)

print(f"Wifi Names{'':<30}| Passwords")
for name in profiles:
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", name, "key=clear"])
        result = result.decode("utf-8", errors="backslashreplace")
        result = result.split("\n")
        
        for password in result:
            if "Key Content" in password:
                result = password.split(":")[1][1:-1]
                print(f"{name:<40}| {password:<}")
    except:
        print(f"{'Error':<40}|")
    
