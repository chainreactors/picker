---
title: WordPress Metform Elementor Contact Form Builder 3.1.2 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023020018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-09
fetch_date: 2025-10-04T06:06:32.514488
---

# WordPress Metform Elementor Contact Form Builder 3.1.2 Cross Site Scripting

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
|  |  | |  | | --- | | **WordPress Metform Elementor Contact Form Builder 3.1.2 Cross Site Scripting** **2023-02-08 / 2023-02-09**  Credit:  **[Mohammed El Amin](https://cxsecurity.com/author/Mohammed%2BEl%2BAmin/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0084](https://cxsecurity.com/cveshow/CVE-2023-0084/ "Click to see CVE-2023-0084")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Affected Plugin: Metform Elementor Contact Form Builder
Plugin Slug: metform
Affected Versions: <= 3.1.2
CVE ID: CVE-2023-0084
CVSS Score: 7.2 (High)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N
Researcher/s: Mohammed El Amin, Chemouri
Fully Patched Version: 3.2.0
The Metform Elementor Contact Form Builder plugin allows site builders to create highly functional contact forms. Unfortunately, vulnerable versions of the Metform plugin fail to escape submitted form entries when displaying them in the admin panel.
This meant that any site visitor could fill out a contact form with malicious JavaScript, and that the script would execute in the browser of any administrator viewing that form entry.
While sanitizing input may also have helped, escaping output is much more important for preventing Cross-Site Scripting as bypasses are far less common.
The patched version updated the format\_form\_data function to escape the output form data in order to address this issue.
An attacker able to execute JavaScript in the browser of an administrator can use it to take over a website via several methods, including by adding a new malicious administrator or injecting a backdoor into a plugin or theme on the site.
Unauthenticated Stored Cross-Site Scripting vulnerabilities are the most dangerous variant of Cross-Site Scripting for WordPress sites as they are much easier for attackers to automatically exploit en masse without needing an existing user account.
Timeline
January 4, 2023 - Mohammed Chemouri responsibly discloses the vulnerability to the plugin vendor and our Vulnerability Disclosure program.
January 8, 2023 - A patched version of the Metform plugin, 3.2.0, is made available.
February 3, 2023 - The Wordfence Threat Intelligence team discovers a potential bypass of the existing Cross-Site Scripting rule and releases an additional firewall rule to Wordfence Premium, Care, and Response sites.
March 5, 2023 - The firewall rule becomes available to Wordfence free users.
Conclusion
In today’s post we detailed an unauthenticated stored Cross-Site Scripting vulnerability in the Metform plugin discovered and responsibly disclosed by independent security researcher Mohammed Chemouri. The Wordfence firewall’s built-in Cross-Site Scripting protection should provide coverage for all Wordfence users including those using Wordfence free.
While we did find a potential bypass and deploy an additional rule to coverit, we have not seen this vulnerability exploited at a large scale in the wild, and have not seen any instances of the bypass being exploited. Nonetheless, we strongly recommend updating to the latest version of the Metform Elementor Contact Form Builder plugin, which is 3.2.1 at the time of this writing.
If you believe your site has been compromised as a result of this vulnerability or any other vulnerability, we offer Incident Response services via Wordfence Care. If you need your site cleaned immediately, Wordfence Response offers the same service with 24/7/365 availability and a 1-hour response time. Both of these products include hands-on support in case you need further assistance.
If you have any friends or colleagues who are using this plugin, please share this announcement with them and encourage them to update to the latest patched version of Metform Elementor Contact Form Builder as soon as possible.
If you are a security researcher, you can responsibly disclose your finds to us and obtain a CVE ID and get your name on the Wordfence Intelligence Community Edition leaderboard.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020018)

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