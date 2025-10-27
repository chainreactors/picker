---
title: WordPress Core 6.2 XSS / CSRF / Directory Traversal
url: https://cxsecurity.com/issue/WLB-2023050040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-18
fetch_date: 2025-10-04T11:37:06.400685
---

# WordPress Core 6.2 XSS / CSRF / Directory Traversal

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
|  |  | |  | | --- | | **WordPress Core 6.2 XSS / CSRF / Directory Traversal** **2023.05.17**  **![pl](https://cert.cx/cxstatic/images/flags/pl.png) [Jakub Zoczek](https://cxsecurity.com/author/Jakub%2BZoczek/1/) **(PL)** ![pl](https://cert.cx/cxstatic/images/flags/pl.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-2745](https://cxsecurity.com/cveshow/CVE-2023-2745/ "Click to see CVE-2023-2745")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")  [CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

On May 16, 2023, the WordPress core team released WordPress 6.2.1, which contains patches for 5 vulnerabilities, including a Medium Severity Directory Traversal vulnerability, a Medium-Severity Cross-Site Scripting vulnerability, and several lower-severity vulnerabilities.
These patches have been backported to every version of WordPress since 4.1. WordPress has supported automatic core updates for security releases since WordPress 3.7, and the vast majority of WordPress sites should receive a patch for their major version of WordPress automatically over the next 24 hours. We recommend verifying that your site has been automatically updated to one of the patched versions. Patched versions are available for every major version of WordPress since 4.1, so you can update without risking compatibility issues.
If your site has not been updated automatically we strongly recommend updating manually as soon as possible, as one of the vulnerabilities patched in this release can be used by an attacker with a low-privileged contributor-level account to take over a site.
This email content has also been published on our blog and you're welcome to post a comment there if you'd like to join the conversation. Or you can read the full post in this email.
Vulnerability Analysis
As with every WordPress core release containing security fixes, the Wordfence Threat Intelligence team analyzed the code changes in detail to evaluate the impact of these vulnerabilities on our customers, and to ensure our customers remain protected.
Description: WordPress Core <= 6.2 - Directory Traversal via wp\_lang
Affected Versions: WordPress Core < 6.2.1
Researcher: Matt Rusnak, reported by Ramuel Gall as well as an undisclosed third party auditor
CVE ID: CVE-2023-2745
CVSS Score: 5.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L/A:N
Fully Patched Version: 6.2.1
WordPress Core is vulnerable to Directory Traversal in versions up to, and including, 6.2, via the ‘wp\_lang’ parameter. This allows unauthenticated attackers to access and load arbitrary translation files. In cases where an attacker is able to upload a crafted translation file onto the site, such as via an upload form, this could be also used to perform a Cross-Site Scripting attack. This vulnerability would not be easy to exploit in an impactful manner on most configurations.
Description: WordPress Core <= 6.2 - Cross-Site Request Forgery via wp\_ajax\_set\_attachment\_thumbnail
Affected Versions: WordPress Core < 6.2.1
Researcher: John Blackbourn of the WordPress security team
CVE ID: Pending
CVSS Score: 4.3 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N
Fully Patched Version: 6.2.1
WordPress Core is vulnerable to Cross-Site Request Forgery due to missing nonce validation on the ‘wp\_ajax\_set\_attachment\_thumbnail’ AJAX function in versions up to, and including, 6.2. This allows unauthenticated users to update the thumbnail image associated with existing attachments, granted they can trick an authenticated user with appropriate permissions into performing an action, such as clicking a link. The impact of this vulnerability is incredibly minimal and we do not expect to see any exploitation of this weakness.
Description: WordPress Core <= 6.2 - Authenticated (Contributor+) Stored Cross-Site Scripting via Embed Discovery Functionality
Affected Versions: WordPress Core < 6.2.1
Researcher: Jakub Żoczek of Securitum and undisclosed third-party auditor
CVE ID: Pending
CVSS Score: 6.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N
Fully Patched Version: 6.2.1
WordPress Core is vulnerable to stored Cross-Site Scripting in versions up to, and including, 6.2, due to insufficient validation of the protocol in the response when processing oEmbed discovery. This makes it possible for authenticated attackers with contributor-level and above permissions to use a crafted oEmbed payload at a remote URL to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.
Description: WordPress Core <= 6.2 - Insufficient Sanitization of Block Attributes
Affected Versions: WordPress Core < 6.2.1
Researcher: Undisclosed third-party auditor
CVE ID: Pending
CVSS Score: 6.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N
Fully Patched Version: 6.2.1
WordPress Core fails to sufficiently sanitize block attributes in versions up to, and including, 6.2. This makes it possible for authenticated attackers with contributor-level and above permissions to embed arbitrary content in HTML comments on the page, though Cross-Site scripting may be possible when combined with an additional vulnerability. Please note that this would only affect sites utilizing a block editor compatible theme.
Description: WordPress Core <= 6.2 - Shortcode Execution in User Generated Content
Affected Versions: WordPress Core < 6.2.1
Researcher: Liam Gladdy of WP Engine
CVE ID: Pending
CVSS Score: 6.5 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
Fully Patched Version: 6.2.1
WordPress Core processes shortcodes in user-generated content on block themes in versions up to, and including, 6.2. This could allow unauthenticated attackers to execute shortcodes via submitting comments or other content, allowing them to exploit vulnerabilities that typically require Subscriber or Contributor-level permissions. While this is likely to have minimal impact on its own, it can significantl...