---
title: OX App Suite 7.10.6 Cross Site Scripting / SSRF / Resource Consumption
url: https://cxsecurity.com/issue/WLB-2022120001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-02
fetch_date: 2025-10-04T00:16:03.662470
---

# OX App Suite 7.10.6 Cross Site Scripting / SSRF / Resource Consumption

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
|  |  | |  | | --- | | **OX App Suite 7.10.6 Cross Site Scripting / SSRF / Resource Consumption** **2022.12.01**  Credit:  **[Martin Heiland](https://cxsecurity.com/author/Martin%2BHeiland/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-31469](https://cxsecurity.com/cveshow/CVE-2022-31469/ "Click to see CVE-2022-31469")** | **[CVE-2022-37307](https://cxsecurity.com/cveshow/CVE-2022-37307/ "Click to see CVE-2022-37307")** | **[CVE-2022-37308](https://cxsecurity.com/cveshow/CVE-2022-37308/ "Click to see CVE-2022-37308")** | **[CVE-2022-37309](https://cxsecurity.com/cveshow/CVE-2022-37309/ "Click to see CVE-2022-37309")** | **[CVE-2022-37310](https://cxsecurity.com/cveshow/CVE-2022-37310/ "Click to see CVE-2022-37310")** | **[CVE-2022-37313](https://cxsecurity.com/cveshow/CVE-2022-37313/ "Click to see CVE-2022-37313")** | **[CVE-2022-37312](https://cxsecurity.com/cveshow/CVE-2022-37312/ "Click to see CVE-2022-37312")** | **[CVE-2022-37311](https://cxsecurity.com/cveshow/CVE-2022-37311/ "Click to see CVE-2022-37311")**  CWE: **[CWE-80](https://cxsecurity.com/cwe/CWE-80 "Click to see CWE-80")  [CWE-918](https://cxsecurity.com/cwe/CWE-918 "Click to see CWE-918")  [CWE-400](https://cxsecurity.com/cwe/CWE-400 "Click to see CWE-400")  [CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Product: OX App Suite
Vendor: OX Software GmbH
Internal reference: OXUIB-1654
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16
Vendor notification: 2022-05-23
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-31469
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)
Vulnerability Details:
The detection mechanism for "deep links" in E-Mail (e.g. pointing to OX Drive) allows to inject references to arbitrary fake applications. This can be used to request unexpected content, potentially including script code, when those links are used.
Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would require the victim to follow a hyperlink.
PoC:
<a class="deep-link-app" href="https://test/#!!&app=%2e./%2e./%2e./%2e./%2e./%2e./appsuite/apps/themes/default/logo.png?cut=&id=123">
Solution:
We improved deep-link validation to avoid malicious use.
---
Internal reference: OXUIB-1678
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.3
Vendor notification: 2022-05-30
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37307
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)
Vulnerability Details:
Certain content like E-Mail signatures are stored using the "snippets" mechanism. This mechanism contains a weakness that allows to inject seemingly benign HTML content, like XHTML CDATA constructs, that will be sanitized to malicious code. Once such code is in place it can be used for persistent access to the users account.
Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would require access to the same OX App Suite instance or temporary access to the users account.
PoC:
<![CDATA[
<bo<script></script>dy>AA<img src onerror="alert('XSS')">BB</body>
]]>
Solution:
We improved the sanitizing algorithm to deal with disguised code.
---
Internal reference: OXUIB-1731
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.3
Vendor notification: 2022-06-22
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37308
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)
Vulnerability Details:
Plain-text mail that contains HTML code can be used to inject script code when printing E-Mail.
Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would need to make the victim print a malicious E-Mail.
PoC:
...
Content-Type: text/plain
<img src onerror="alert('XSS')">
Solution:
We removed plain-text specific code and use existing sanitization mechanisms for HTML content.
---
Internal reference: OXUIB-1732
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.4
Vendor notification: 2022-06-22
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37309
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)
Vulnerability Details:
Contacts that do not contain a name but only a e-mail address can be used to inject script code to the "contact picker" component, commonly used to select contacts as recipients or participants.
Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would require access to the same OX App Suite instance or make the victim import malicious contact data.
Solution:
We now apply proper HTML escaping to all relevant data sets.
---
Affected product: OX App Suite
Internal reference: OXUIB-1785
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: fron...