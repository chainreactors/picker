---
title: WordPress Quick Restaurant 2.0.2 XSS / CSRF / IDOR / Missing Authorization
url: https://cxsecurity.com/issue/WLB-2023020006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-03
fetch_date: 2025-10-04T05:33:08.531825
---

# WordPress Quick Restaurant 2.0.2 XSS / CSRF / IDOR / Missing Authorization

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
|  |  | |  | | --- | | **WordPress Quick Restaurant 2.0.2 XSS / CSRF / IDOR / Missing Authorization** **2023.02.02**  Credit:  **[Marco Wotschka](https://cxsecurity.com/author/Marco%2BWotschka/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0555](https://cxsecurity.com/cveshow/CVE-2023-0555/ "Click to see CVE-2023-0555")** | **[CVE-2023-0550](https://cxsecurity.com/cveshow/CVE-2023-0550/ "Click to see CVE-2023-0550")** | **[CVE-2023-0554](https://cxsecurity.com/cveshow/CVE-2023-0554/ "Click to see CVE-2023-0554")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

On January 16, 2023, the Wordfence Threat Intelligence team responsibly disclosed several vulnerabilities in Quick Restaurant Menu, a WordPress plugin that allows users to set up restaurant menus on their sites. This plugin is vulnerable to Missing Authorization, Insecure Direct Object Reference, Cross-Site Request Forgery as well as Cross-Site Scripting in versions up to, and including 2.0.2.
We found that contact information was not readily available for the vendor, so we reached out to the WordPress Plugin Security Team team directly on January 16, 2023 to report the security issues. The team acknowledged receipt of our email on January 18, 2023. All issues were addressed in version 2.1.0, which was released on January 20, 2023. Unfortunately, the plugin is still closed for downloads at this point, so we recommend manually downloading the patched version, or uninstalling the plugin completely until the plugin has been reinstated.
We released a firewall rule addressing the lack of authorization checks on January 16, 2023. Premium, Care, and Response customers received that protection the same day, while sites still running the free version of Wordfence will receive the same protection 30 days later on February 15, 2023.
Due to the nature of Cross-Site Request Forgery vulnerabilities, which involve tricking administrators into performing actions they are allowed to perform, it is not possible to provide full protection without blocking legitimate requests. As such, we recommend updating as soon as possible to ensure that your site is fully protected against any exploits that may target the Cross-Site Request Forgery vulnerability.
This email content has also been published on our blog and you're welcome to post a comment there if you'd like to join the conversation. Or you can read the full post in this email.
Vulnerability Summaries
Description: Missing Authorization to Arbitrary Post Deletion
Affected Plugin: Quick Restaurant Menu
Plugin Slug: quick-restaurant-menu
Affected Versions: <= 2.0.2
CVE ID: CVE-2023-0555
CVSS Score: 8.1 (High)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H
Researcher/s: Marco Wotschka, Ivan Kuzymchak
Fully Patched Version: 2.1.0
The Quick Restaurant Menu plugin for WordPress is vulnerable to authorization bypass due to a missing capability check on its AJAX actions in versions up to, and including, 2.0.2. This makes it possible for authenticated attackers, with subscriber-level permissions and above, to invoke those actions intended for administrator use. Actions include menu item creation, update and deletion and other menu management functions. Since the plugin does not verify that a post ID passed to one of its AJAX actions belongs to a menu item, this can lead to arbitrary post deletion/alteration.
Description: Insecure Direct Object Reference
Affected Plugin: Quick Restaurant Menu
Plugin Slug: quick-restaurant-menu
Affected Versions: <= 2.0.2
CVE ID: CVE-2023-0550
CVSS Score: 8.1 (High)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H
Researcher/s: Marco Wotschka
Fully Patched Version: 2.1.0
The Quick Restaurant Menu plugin for WordPress is vulnerable to Insecure Direct Object Reference in versions up to, and including, 2.0.2. This is due to the fact that during menu item deletion/modification, the plugin does not verify that the post ID provided to the AJAX action is indeed a menu item. This makes it possible for authenticated attackers, with subscriber-level access or higher, to modify or delete arbitrary posts.
Description: Cross-Site Request Forgery
Affected Plugin: Quick Restaurant Menu
Plugin Slug: quick-restaurant-menu
Affected Versions: <= 2.0.2
CVE ID: CVE-2023-0554
CVSS Score: 8.1 (High)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:H
Researcher/s: Marco Wotschka
Fully Patched Version: 2.1.0
The Quick Restaurant Menu plugin for WordPress is vulnerable to Cross-Site Request Forgery in versions up to, and including, 2.0.2. This is due to missing or incorrect nonce validation on its AJAX actions. This makes it possible for unauthenticated attackers to update menu items, via forged request granted they can trick a site administrator into performing an action such as clicking on a link.
Vulnerability Analysis
Quick Restaurant Menu is a plugin offered by ThingsForRestaurants that provides site owners with the ability to create menus for different occasions such as lunch and dinner along with the option to price items differently per menu.
As part of the plugin’s functionality, menu items can be created, deleted and moved around on menus. Dividers can be added to menus to visually separate different menu sections from one another. Menu items are stored as posts with type erm\_menu\_item.
More specifically, the plugin allows users to arrange menu items for menus via a drag-and-drop method and utilizes AJAX actions to accomplish this. Below is one of those functions in more detail:
Code Before Fix
We can see that this short function checks for the existence of a post\_id parameter in the POST request, casts this provided parameter to an integer and then deletes the menu item with this id. This function can be invoked by sending a POST request to /wp-admin/admin-ajax.php that contains the action name as well as a post id.
POST /wordpress/wp-admin/admin-ajax.php HTTP/1.1
Host: 127.0.0.1
action=erm\_delete\_menu\_item&post\_id=49
A Teaching Moment: Import...