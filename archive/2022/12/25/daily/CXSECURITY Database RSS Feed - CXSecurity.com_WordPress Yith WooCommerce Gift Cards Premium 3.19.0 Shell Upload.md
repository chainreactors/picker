---
title: WordPress Yith WooCommerce Gift Cards Premium 3.19.0 Shell Upload
url: https://cxsecurity.com/issue/WLB-2022120043
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-25
fetch_date: 2025-10-04T02:28:31.023098
---

# WordPress Yith WooCommerce Gift Cards Premium 3.19.0 Shell Upload

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
|  |  | |  | | --- | | **WordPress Yith WooCommerce Gift Cards Premium 3.19.0 Shell Upload** **2022.12.24**  Credit:  **[Dave Jong](https://cxsecurity.com/author/Dave%2BJong/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45359](https://cxsecurity.com/cveshow/CVE-2022-45359/ "Click to see CVE-2022-45359")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

Description: Unauthenticated Arbitrary File Upload
Affected Plugin: Yith WooCommerce Gift Cards Premium
Plugin Slug: yith-woocommerce-gift-cards-premium
Affected Versions: <= 3.19.0
CVE ID: CVE-2022-45359
CVSS Score: 9.8 (Critical)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:L/A:N
Researcher/s: Dave Jong
Fully Patched Version: 3.20.0
We were able to reverse engineer the exploit based on attack traffic and a copy of the vulnerable plugin and are providing information on its functionality as this vulnerability is already being exploited in the wild and a patch has been available for some time.
The issue lies in the import\_actions\_from\_settings\_panel function which runs on the admin\_init hook.
Since admin\_init runs for any page in the /wp-admin/ directory, it is possible to trigger functions that run on admin\_init as an unauthenticated attacker by sending a request to /wp-admin/admin-post.php.
Since the import\_actions\_from\_settings\_panel function also lacks a capability check and a CSRF check, it is trivial for an attacker to simply send a request containing a page parameter set to yith\_woocommerce\_gift\_cards\_panel, a ywgc\_safe\_submit\_field parameter set to importing\_gift\_cards, and a payload in the file\_import\_csv file parameter.
Since the function also does not perform any file type checks, any file type including executable PHP files can be uploaded.
Cyber Observables
These attacks may appear in your logs as unexpected POST requests to wp-admin/admin-post.php from unknown IP addresses. Additionally, we have observed the following payloads which may be useful in determining whether your site has been compromised. Note that we are providing normalized hashes (hashes of the file with all extraneous whitespace removed):
kon.php/1tes.php – this file loads a copy of the “marijuana shell” file manager in memory from a remote location at shell[.]prinsh[.]com and has a normalized sha256 hash of 1a3babb9ac0a199289262b6acf680fb3185d432ed1e6b71f339074047078b28c
b.php – this file is a simple uploader with a normalized sha256 hash of 3c2c9d07da5f40a22de1c32bc8088e941cea7215cbcd6e1e901c6a3f7a6f9f19
admin.php – this file is a password-protected backdoor and has a normalized sha256 hash of 8cc74f5fa8847ba70c8691eb5fdf8b6879593459cfd2d4773251388618cac90d
Although we’ve seen attacks from more than a hundred IPs, the vast majority of attacks were from just two IP addresses:
103.138.108.15, which sent out 19604 attacks against 10936 different sites
and
188.66.0.135, which sent 1220 attacks against 928 sites.
The majority of attacks occurred the day after the vulnerability was disclosed, but have been ongoing, with another peak on December 14, 2022. As this vulnerability is trivial to exploit and provides full access to a vulnerable website we expect attacks to continue well into the future.
Recommendations
If you are running a vulnerable version of YITH WooCommerce Gift Cards Premium, that is, any version up to and including 3.19.0, we strongly recommend updating to the latest version available. While the Wordfence firewall does provide protection against malicious file uploads even for free users, attackers may still be able to cause nuisance issues by abusing the vulnerable functionality in less critical ways.
If you believe your site has been compromised as a result of this vulnerability or any other vulnerability, we offer Incident Response services via Wordfence Care. If you need your site cleaned immediately, Wordfence Response offers the same service with 24/7/365 availability and a 1-hour response time. Both of these products include hands-on support in case you need further assistance.
If you have any friends or colleagues who are using this plugin, please share this announcement with them and encourage them to update to the latest patched version of YITH WooCommerce Gift Cards Premium as soon as possible.
If you are a security researcher, you can responsibly disclose your finds to us and obtain a CVE ID and get your name on the Wordfence Intelligence Community Edition leaderboard.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120043)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
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