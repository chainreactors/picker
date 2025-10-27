---
title: WordPress Blog2Social 6.9.11 Missing Authorization
url: https://cxsecurity.com/issue/WLB-2022110010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-11
fetch_date: 2025-10-03T22:20:09.480341
---

# WordPress Blog2Social 6.9.11 Missing Authorization

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
|  |  | |  | | --- | | **WordPress Blog2Social 6.9.11 Missing Authorization** **2022.11.10**  Credit:  **[Marco Wotschka](https://cxsecurity.com/author/Marco%2BWotschka/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-3622](https://cxsecurity.com/cveshow/CVE-2022-3622/ "Click to see CVE-2022-3622")**  CWE: **N/A** | |

Description: Missing Authorization to Authenticated (Subscriber+) Settings Update
Affected Plugin: Blog2Social
Plugin Slug: blog2social
Affected Versions: <= 6.9.11
CVE ID: CVE-2022-3622
CVSS Score: 4.7 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:L/A:N
Researcher/s: Marco Wotschka
Fully Patched Version: 6.9.12
Blog2Social: Social Media Auto Post & Scheduler is a plugin offered by Blog2Social/Adenion that provides content-creators with the ability to quickly share site content to their social media accounts. It offers automatic post sharing as well as optimized scheduling and also extends some of its features to subscribers, enabling them to share posts to their own social media accounts.
As part of the plugin’s functionality, there are some more advanced settings that can be managed. Unfortunately, this was implemented insecurely making it possible for authenticated attackers to update these settings even without the authorization to do so.
More specifically, the plugin provides administrators with the ability to enable legacy mode, which is intended to reduce server load. In legacy mode, the plugin will load content one item at a time instead of loading all content in bulk in an attempt to reduce the likelihood of dashboard freeze-ups. In order to reduce the number of concurrent outgoing connections, legacy mode will also load connections to social media accounts in sequential order as opposed to doing so simultaneously. While functionality should not be significantly affected by this for most use cases, this legacy option setting is reserved for administrators only. Unfortunately, due to a lack of capability checking on the function and in the user interface, site subscribers had access to this setting via the dashboard:
/wp-admin/admin.php?page=blog2social-settings
Furthermore, the same URL offers access to a Social Meta Data tab, which contains forms that are disabled for non-administrative users. However, browsers offer inspector tools, which can be used to modify html on the fly in order to change properties of such forms and their elements. For instance, a save button with the following properties can be modified to become functional by removing the disabled attribute from the button:
<button class="btn btn-primary pull-right" disabled="disabled" type="submit">save</button> – as a result, such a form can be submitted by a subscriber. This indicates the developer used client-side validation, which can easily be bypassed by modifying the request sent to the server.
A request could be submitted using a third party tool similar to this one:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: 127.0.0.1
Cookie:
b2s\_og\_default\_title=SiteTitle&b2s\_og\_default\_desc=Just%20another%20WordPress%20site&b2s\_og\_default\_image=&b2s\_og\_imagedata\_active=1&b2s\_og\_objecttype\_active=1&b2s\_og\_locale\_active=1&b2s\_og\_locale=en\_US&b2s\_card\_default\_type=Summary&b2s\_card\_default\_title=SiteTitle&b2s\_card\_default\_desc=Just%20another%20WordPress%20site&b2s\_card\_default\_image=&is\_admin=1&version=0&action=b2s\_save\_social\_meta\_tags&b2s\_security\_nonce=<nonce>
This had consequences such as allowing subscribers to change social meta tags which could potentially be used to impact brand reputation.
A third issue that we discovered surrounded the plugin’s general authorization mechanism.
[Please view this code snippet on our blog here.] (https://email.wordfence.com/e3t/Ctc/GC+113/cwG7R04/VWydX-1ZpVtDW5m3pbH5yxlc9W2C4PM94S6TLRN1sYgXV5mNXrV3Zsc37CgPpPW1\_8BsQ650vs3W86NLQQ1Cb22gW8qlQJx717QmtN2Cx03MLNfRLW2-JNJb7nLtJDW6WM7R34PtmhMW1Q6y\_X7lS\_zWVjVDs36QWQxhVzcJwS8zW-6JW8R8sdQ5n8VyMW3xQZRx311bNnW52MK5T99M-WqN2bB3jwTbxZzW1VZPJL4W2QZ5W1sVXxZ2kr-JTTbvjx4xd9hxN1FlKQT1fwwDW7k9F6p6vRy5QVbh2jM4ll2JJW999K9x38XkPRW6ZTcyY2C85K-W5CC1TG1747mhW7gFskm1Y2Zy8W1f8khN7hdTbPVNS67c54W0xjW19nHJ55SGL4QW4BD90m6r6kRYW90HD6J3JT--YW9cg9wz21JSczW3tFWZp50-1qtW8wjp8m8gL9xyW7JNDB-5x1VB83f5z1 )
The first if-statement is intended to prevent unauthorized use of this function and similar functions using the same protection. The following parts need to evaluate to true in order for the if-statement to do the same:
- current\_user\_can('read') – This gives access to the administration screens and user profiles. This permission is generally available to all authenticated users such as subscribers.
- isset($\_POST['b2s\_security\_nonce']) – this nonce is set by the plugin and can be obtained by searching the code of /wp-admin/profile.php for the string ‘b2s\_security\_nonce’. This nonce is generated for subscribers and higher.
- (int) wp\_verify\_nonce(sanitize\_text\_field(wp\_unslash($\_POST['b2s\_security\_nonce'])), 'b2s\_security\_nonce') > 0 – this verifies the nonce after some sanitization.
As long as a userId is provided, we are able to lock B2S\_LOCK\_AUTO\_POST\_IMPORT\_ for any user, resulting in that user being unable to automatically import posts. We found that many other functions lacked proper capability checks as well.
The Importance of Capability Checks
Capability checks are an important part of securing AJAX actions since those are available to any logged in users, including subscribers. The following is an example of an AJAX action from the Blog2Social plugin.
add\_action('wp\_ajax\_b2s\_lock\_auto\_post\_import', array($this, 'lockAutoPostImport'));
While nonce checks ensure that the user initiating the request intended to do so, they don’t provide authorization. As mentioned above, the check current\_user\_can('read') does ensure that the user initiating the request has that specific capability, but it does not suffice to protect actions intended for administrators only. A proper way to secure such actions would be to utilize a check such as
current\_user\_can('manage\...