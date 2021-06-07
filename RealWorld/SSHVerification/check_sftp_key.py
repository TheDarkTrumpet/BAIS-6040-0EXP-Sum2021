import subprocess
import re

server = "<YOUR_SSH_SERVER_HERE>"
expected = "<YOUR_RSA_PUB_KEY_HERE>"

keycheck_run = subprocess.run(["ssh-keyscan", server], capture_output=True)
key_match = re.match(r'.*?ssh-rsa (.*?)\\n.*', str(keycheck_run.stdout))

if len(keycheck_run.stderr) > 0 and key_match is None:
    print(f'[-] There was an error in the process, details: {keycheck_run.stderr}')
elif key_match is not None:
    key_to_check = key_match.group(1)
    if key_to_check == expected:
        print("[+] Server is up, fingerprint matches!")
    else:
        print("[-] Server fingerprint mismatch, host is up.  Man in the middle attack?")
else:
    print("[-] There was an unexpected error that wasn't properly handled.")