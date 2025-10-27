---
title: WordPress Shield Security 17.0.17 Cross Site Scripting / Missing Authorization
url: https://cxsecurity.com/issue/WLB-2023040081
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-26
fetch_date: 2025-10-04T11:32:32.955988
---

# WordPress Shield Security 17.0.17 Cross Site Scripting / Missing Authorization

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
|  |  | |  | | --- | | **WordPress Shield Security 17.0.17 Cross Site Scripting / Missing Authorization** **2023.04.25**  Credit:  **[Ramuel Gall](https://cxsecurity.com/author/Ramuel%2BGall/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0992](https://cxsecurity.com/cveshow/CVE-2023-0992/ "Click to see CVE-2023-0992")** | **[CVE-2023-0993](https://cxsecurity.com/cveshow/CVE-2023-0993/ "Click to see CVE-2023-0993")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Affected Plugin: Shield Security – Smart Bot Blocking & Intrusion Prevention
Plugin Slug: wp-simple-firewall
Affected Versions: <= 17.0.17
CVE ID: CVE-2023-0992
CVSS Score: 7.2 (High)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N
Researcher/s: Ramuel Gall
Fully Patched Version: 17.0.18
The Shield Security plugin for WordPress is vulnerable to stored Cross-Site Scripting in versions up to, and including, 17.0.17 via the 'User-Agent' header. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.
Description: Shield Security <= 17.0.17 - Missing Authorization
Affected Plugin: Shield Security – Smart Bot Blocking & Intrusion Prevention
Plugin Slug: wp-simple-firewall
Affected Versions: <= 17.0.17
CVE ID: CVE-2023-0993
CVSS Score: 4.3 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
Researcher/s: Ramuel Gall
Fully Patched Version: 17.0.18
The Shield Security plugin for WordPress is vulnerable to Missing Authorization on the 'theme-plugin-file' AJAX action in versions up to, and including, 17.0.17. This allows authenticated attackers to add arbitrary audit log entries indicating that a theme or plugin has been edited, and is also a vector for Cross-Site Scripting via CVE-2023-0992.
Vulnerability Analysis
The Shield Security plugin includes a number of features, including an audit log that records certain types of suspicious activity, such as plugin and theme installation, modification, post deletion, and other types of activity that might impact the site. While most of these events require authentication or higher privileges in order to trigger, we found that certain events could be triggered by unauthenticated users. In particular, failed attempts to authenticate using application passwords, new user registrations, and spam activity are among the actions recorded for unauthenticated users.
The audit log records metadata about the client that performed the logged activity, including the client’s User-Agent, which can be accessed by clicking the “Meta” tag icon on an audit log entry. Unfortunately, the metadata was not escaped when it was output. While most of the metadata collected about a request has a very strict format and can only be spoofed to a limited extent, User-Agent strings are alphanumeric, and we were able to inject a script in an iframe in the User-Agent header that fired when an administrator viewed an event entry:
shieldalert-1024x454
While this exploit does technically require user interaction, it can be considered “Passive” user interaction, that is, it does not require tricking the administrator into performing any actions they might not have performed otherwise. Depending on the payload used, an attacker could use the script executing in the administrator’s browser to create a new administrator account under their control. Additionally, this exploit can be automated, and can be exploited by unauthenticated attackers via a variety of vectors, at least one of which is likely to be present in most common site configurations. As such it earns its High severity rating.
The second vulnerability was much lower in severity and consisted of a missing authorization check on the ‘edit-theme-plugin-file’ AJAX action, which is used to record edits to plugin or theme files. The primary consequence of this is that an authenticated attacker can spoof an audit log entry indicating that any file belonging to any plugin or theme on the site was edited. While this is primarily a nuisance, since it can be used to create audit log entries it is yet another vector to exploit the aforementioned Cross-Site Scripting vulnerability.
Disclosure Timeline
March 20, 2023 – Wordfence Premium, Care, and Response users receive a firewall rule to provide protection against any exploits that may target this vulnerability. We responsibly disclose the plugin to the developer, who responds quickly and releases a patch in version 17.0.18.
April 19, 2023 – The firewall rule becomes available to all Wordfence users.
Conclusion
In today’s post, we detailed a High Severity Cross-Site Scripting vulnerability in Shield Security. We also detailed a lower-severity issue allowing authenticated attackers to spoof audit log entries indicating that plugin and theme files had been edited. These vulnerabilities have been fully patched in version 17.0.18.
Wordfence Premium, Care, and Response users received a firewall rule to protect against any exploits targeting this vulnerability on March 20, 2023. Sites still using the free version of Wordfence received the same protection on April 19, 2023.
If you know a friend or colleague who is using the Shield Security plugin on their site, we highly recommend forwarding this advisory to them as the Cross-Site Scripting vulnerability can allow Unauthenticated attackers to execute malicious JavaScript in an administrator’s browser, which can lead to site takeover.
If you are a security researcher, you can responsibly disclose your finds to us and obtain a CVE ID and get your name on the Wordfence Intelligence leaderboard. Thanks to Paul Goodchild from Shield Security for patching the issue quickly.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040081)

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

|  |  |...