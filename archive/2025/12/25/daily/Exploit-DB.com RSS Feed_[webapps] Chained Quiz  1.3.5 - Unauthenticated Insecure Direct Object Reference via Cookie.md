---
title: [webapps] Chained Quiz  1.3.5 - Unauthenticated Insecure Direct Object Reference via Cookie
url: https://www.exploit-db.com/exploits/52464
source: Exploit-DB.com RSS Feed
date: 2025-12-25
fetch_date: 2025-12-26T03:22:52.120623
---

# [webapps] Chained Quiz  1.3.5 - Unauthenticated Insecure Direct Object Reference via Cookie

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

# Chained Quiz 1.3.5 - Unauthenticated Insecure Direct Object Reference via Cookie

#### EDB-ID:

###### 52464

#### CVE:

###### [2025-10493](https://nvd.nist.gov/vuln/detail/CVE-2025-10493)

---

**EDB Verified:**

#### Author:

###### [0xsabre](/?author=12322)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-12-25

---

**Vulnerable App:**

```
# Exploit Title: Chained Quiz  1.3.5 - Unauthenticated Insecure Direct Object Reference via Cookie
# Date: 19-12-2025
# Exploit Author: Karuppiah Sabari Kumar(0xsabre)
# Vendor Homepage: https://wordpress.org/plugins/chained-quiz/
# Software Link: https://downloads.wordpress.org/plugin/chained-quiz.1.3.3.zip
# Version: <= 1.3.3
# Tested on: WordPress / Linux
# CVE: CVE-2025-10493

------------------------------------------------------------

## Vulnerability Type
Insecure Direct Object Reference (IDOR) / Improper Authorization

------------------------------------------------------------

## Description
The Chained Quiz plugin stores each quiz attempt using a predictable,
auto-incrementing database ID (completion_id) and exposes this value
directly in a client-side cookie named:

    chained_completion_id<quiz_id>

When submitting or re-submitting quiz answers via admin-ajax.php, the
server updates the quiz attempt record based solely on this cookie value,
without verifying that the attempt belongs to the currently authenticated
user.

No authentication is required to exploit this vulnerability when the
plugin is used with default settings.

The server retrieves the quiz attempt directly using the completion_id
from the cookie and performs an UPDATE query without verifying ownership.

As a result, an attacker can hijack or tamper with other users’ quiz
attempts by guessing or enumerating valid completion_id values and
replaying answer submissions.

------------------------------------------------------------

## Affected Component
Quiz submission and results handling functionality via admin-ajax.php

------------------------------------------------------------

## Proof of Concept (PoC)

### Step 1: Victim user submission
A user completes a quiz. The submission is stored using a completion ID
and associated with the user’s session via a cookie, for example:

    chained_completion_id1=2

------------------------------------------------------------

### Step 2: Attacker interception
The attacker completes the same quiz and intercepts their own submission
request using a proxy or browser developer tools.

Example request:

POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost
Cookie: chained_completion_id1=1
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded

answer=0&question_id=1&quiz_id=1&post_id=117&question_type=radio&points=0&action=chainedquiz_ajax&chainedquiz_action=answer&total_questions=1

------------------------------------------------------------

### Step 3: Tampering
The attacker modifies the cookie value to match another user’s quiz
attempt, for example:

    chained_completion_id1=2

The attacker may also modify parameters such as "answer" or "points" to
manipulate quiz responses or scores.

The modified request is then sent to the server.

------------------------------------------------------------

### Step 4: Result
The server overwrites the victim user’s quiz submission, including answers
and points, without validating ownership of the completion ID.

------------------------------------------------------------

## Impact
An attacker can arbitrarily modify quiz answers, scores, or results
belonging to other users. This results in an integrity violation of quiz
data and allows unauthorized manipulation of finalized quiz attempts.
In environments where quiz results are used for assessments, leaderboards,
or certificates, this can undermine trust in the platform and affect any
downstream integrations that rely on quiz completion data.

------------------------------------------------------------

## CWE
- CWE-639: Authorization Bypass Through User-Controlled Key
- CWE-285: Improper Authorization

------------------------------------------------------------
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
compliant](http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html) archive of public exploits and corresponding vulnerable sof...