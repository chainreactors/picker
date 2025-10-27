---
title: WordPress Royal Elementor 1.3.59 XSS / CSRF / Insufficient Access Controls
url: https://cxsecurity.com/issue/WLB-2023010013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-12
fetch_date: 2025-10-04T03:36:15.914220
---

# WordPress Royal Elementor 1.3.59 XSS / CSRF / Insufficient Access Controls

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
|  |  | |  | | --- | | **WordPress Royal Elementor 1.3.59 XSS / CSRF / Insufficient Access Controls** **2023.01.11**  Credit:  **[Ramuel Gall](https://cxsecurity.com/author/Ramuel%2BGall/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-4700](https://cxsecurity.com/cveshow/CVE-2022-4700/ "Click to see CVE-2022-4700")** | **[CVE-2022-4702](https://cxsecurity.com/cveshow/CVE-2022-4702/ "Click to see CVE-2022-4702")** | **[CVE-2022-4704](https://cxsecurity.com/cveshow/CVE-2022-4704/ "Click to see CVE-2022-4704")** | **[CVE-2022-4701](https://cxsecurity.com/cveshow/CVE-2022-4701/ "Click to see CVE-2022-4701")** | **[CVE-2022-4703](https://cxsecurity.com/cveshow/CVE-2022-4703/ "Click to see CVE-2022-4703")** | **[CVE-2022-4705](https://cxsecurity.com/cveshow/CVE-2022-4705/ "Click to see CVE-2022-4705")** | **[CVE-2022-4711](https://cxsecurity.com/cveshow/CVE-2022-4711/ "Click to see CVE-2022-4711")** | **[CVE-2022-4708](https://cxsecurity.com/cveshow/CVE-2022-4708/ "Click to see CVE-2022-4708")** | **[CVE-2022-4709](https://cxsecurity.com/cveshow/CVE-2022-4709/ "Click to see CVE-2022-4709")** | **[CVE-2022-4707](https://cxsecurity.com/cveshow/CVE-2022-4707/ "Click to see CVE-2022-4707")** | **[CVE-2022-4710](https://cxsecurity.com/cveshow/CVE-2022-4710/ "Click to see CVE-2022-4710")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

On December 23, 2022, the Wordfence Threat Intelligence team initiated the responsible disclosure process for a set of 11 vulnerabilities in Royal Elementor Addons, a WordPress plugin with over 100,000 installations. The plugin developers responded on December 26, and we sent over the full disclosure that day.
We released a firewall rule protecting against these vulnerabilities to Wordfence Premium, Care, and Response customers on December 23, 2022. Sites still running the free version of Wordfence will receive the same protection 30 days later, on January 22, 2023.
While none of the vulnerabilities were critical, several of them could have been used by any authenticated user to modify content, disable plugins, or even temporarily take down the site in some circumstances. Additionally one of the patched vulnerabilities was a Reflected Cross-Site Scripting vulnerability which could have been used to take over the site if an attacker was able to trick an administrator into performing an action, such as clicking a link.
This email content has also been published on our blog and you're welcome to post a comment there if you'd like to join the conversation. Or you can read the full post in this email.
Vulnerability Details
The primary set of issues we found with Royal Elementor Addons was due to a lack of access control and nonce checks on various AJAX actions in the plugin.
Description: Insufficient Access Control to Theme Activation
Affected Plugin: Royal Elementor Addons
Plugin Slug: royal-elementor-addons
Affected Versions: <= 1.3.59
CVE ID: CVE-2022-4700
CVSS Score: 5.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L
Researcher/s: Ramuel Gall
Fully Patched Version: 1.3.60
Royal Elementor Addons has an option to quickly activate the recommended Royal Elementor Kit theme. Unfortunately, this is performed via an AJAX function, wpr\_activate\_required\_theme, which did not perform capability or nonce checks, or even check if the theme was installed on the site. This meant that any logged-in user, such as a subscriber, could change a vulnerable site’s theme. If the Royal Elementor Kit theme was not installed on the site, this would result in a loss of availability as the site would fail to load and instead display an error message.
Description: Insufficient Access Control to Plugin Deactivation
Affected Plugin: Royal Elementor Addons
Plugin Slug: royal-elementor-addons
Affected Versions: <= 1.3.59
CVE ID: CVE-2022-4702
CVSS Score: 5.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L
Researcher/s: Ramuel Gall
Fully Patched Version: 1.3.60
Royal Elementor Addons has an option to revert the site to a “compatible” state for imported templates via the wpr\_fix\_royal\_compatibility AJAX function. This involves deactivating all but a short list of hard-coded plugins. As the function did not use capability or nonce checks, this means that any authenticated user could deactivate plugins necessary for site functionality as well as any security plugins that do not specifically block this action. This could cause the site to become unavailable or vulnerable to additional exploits.
Description: Insufficient Access Control to Template Import
Affected Plugin: Royal Elementor Addons
Plugin Slug: royal-elementor-addons
Affected Versions: <= 1.3.59
CVE ID: CVE-2022-4704
CVSS Score: 5.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L
Researcher/s: Ramuel Gall
Fully Patched Version: 1.3.60
Royal Elementor Addons allows importing preset templates via the wpr\_import\_templates\_kit AJAX function. Vulnerable versions of the plugin do not include capability or nonce check for this function, so any authenticated user could import templates, potentially overwriting any existing templates.
Description: Insufficient Access Control to Plugin Activation
Affected Plugin: Royal Elementor Addons
Plugin Slug: royal-elementor-addons
Affected Versions: <= 1.3.59
CVE ID: CVE-2022-4701
CVSS Score: 4.3 (Low)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
Researcher/s: Ramuel Gall
Fully Patched Version: 1.3.60
Royal Elementor Addons has an option to activate the 'contact-form-7', 'media-library-assistant', or 'woocommerce' plugins if they are installed on the site via the wpr\_activate\_required\_plugins AJAX action, and this functionality was available to any logged-in user. Fortunately the impact of this vulnerability is quite minimal as it would only allow an attacker to activate three select plugins.
Description: Insufficient Access Control to Import Deletion
Affected Plugin: Royal Elementor Addons
Plugin Slug: royal-elementor-a...