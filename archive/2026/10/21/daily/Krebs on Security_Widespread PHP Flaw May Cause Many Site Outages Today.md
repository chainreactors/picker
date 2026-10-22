---
title: Widespread PHP Flaw May Cause Many Site Outages Today
url: https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/
source: Krebs on Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:59.429123
---

# Widespread PHP Flaw May Cause Many Site Outages Today

Advertisement

[![](/b-doppel/17.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

[![](/b-doppel/18.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Widespread PHP Flaw May Cause Many Site Outages Today

October 21, 2026

[0 Comments](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/#respond)

Expect to see quite a few websites serving error pages today: Nearly 70 percent of websites need to update their core software to fix a pair of vulnerabilities that allow an attacker to seize full control over affected servers. Experts say there are working exploits for the flaws, and that these critical bugs are already being exploited in the wild.

![](https://krebsonsecurity.com/wp-content/uploads/2026/10/shutterstock-codeonscreenphp.png)

Image: Shutterstock.com, Sashkin.

The flaws at issue are present in **PHP**, the programming language that powers sites running on a large number of web publishing systems, including **Drupal**, **Magento**, **Joomla** and **WordPress**. Earlier today, PHP released [an emergency security update](https://www.php.net/index.php) to fix two critical bugs that can allow an attacker to execute code of their choosing on a vulnerable server.

**Reuters** [reports](https://www.reuters.com/world/asia-pacific/eu-agency-warns-websites-may-need-be-taken-offline-php-prepares-patches-2026-10-21/) that government websites in Europe and elsewhere went offline today after the PHP vulnerabilities were disclosed. Cloudflare [said](https://blog.cloudflare.com/php-vulnerabilities-waf-protection) it has already detected some exploitation of the flaw, and that at 3:02 am (UTC) it implemented web application firewall rules to protect websites from attack traffic seeking to exploit the bugs, which could cause a denial of service condition, remote code execution, and data exposure.

**OpenAI**, which was involved in the vulnerability research and outreach, [said](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) “given the severity of these flaws and PHP’s widespread use, we consider this one of the most impactful security issues in recent memory.”

**Censys**, a company that tracks the technology used by Internet hosts, [said](https://censys.com/advisory/cve-2026-109618-cve-2026-109619/) a recent scan identified approximately 2.58 million Internet facing hosts and 54.9 million web properties running PHP.

Security experts at **Wiz** said every PHP version released in the last decade is affected by at least one of these vulnerabilities [full disclosure: Wiz is an advertiser on this blog].

“These findings rank among the most severe vulnerabilities discovered in PHP, and arguably in software history,” reads [a blog post](https://www.wiz.io/blog/php2shell-php-rce) published today by a team of researchers at Wiz, which was one of several organizations credited with discovering the vulnerabilities. “The underlying flaws had been present for decades, but demonstrating their exploitability required an exceptionally complex chain of steps, at the edge of what human researchers could practically achieve. Frontier AI models substantially reduced that barrier, turning a longstanding flaw into an exploit.”

The Wiz researchers say it is likely the PHP vulnerabilities will be mass-exploited to install web-based backdoors or “web shells,” which give attackers a web-based panel that allows them to remotely control infected sites. Wiz said that prior to the PHP bugs being publicly disclosed, the company worked with the PHP team, Calif and OpenAI to measure the size of the problem and coordinate patch verification and disclosure.

The PHP zero-day vulnerabilities are being tracked by their CVE numbers, [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/cve-2026-109618) and [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/cve-2026-109619), and they affect all web servers running PHP 5.4 or later. The bugs are fixed in PHP **8.5.12**, **8.4.27**, **8.3.36**, and **8.2.35**.

According to Wiz, PHP is so deeply embedded in many web applications that we are likely to see organizations struggling to patch these vulnerabilities for some time to come, comparing this PHP vulnerability pair with [the Log4Shell weakness](https://en.wikipedia.org/wiki/Log4Shell) that emerged in 2021 — a widespread, severe-as-it-gets security flaw in Log4j, a popular Java logging framework.

“A vulnerability in core PHP reaches far beyond a single application,” the Wiz researchers wrote. “PHP runs across clouds, hosting providers, content-delivery networks and millions of independently managed servers. Reducing exposure before the technical details became public required coordinated work across that entire ecosystem.”

The **SANS Internet Storm Center** is [keeping an eye on](https://isc.sans.edu/diary/Critical%20PHP%20Vulnerability%20%28CVE-2026-109618%2C%20CVE-2026-109619%29%20%5Binfocon%20yellow%5D/33440) major software platforms that are shipping updates to deal with these PHP flaws. For example, Ubuntu just released updated PHP packages. For a technical deep-dive on these vulnerabilities that tells the timeline of the discovery of these bugs in a comic book style, check out [this post](https://calif.io/php2shell/) from **Calif**, another technology company credited with finding the PHP flaws.

*This is a fast-moving story. Updates will be noted here with timestamps.*

**Update, 2:30 pm ET:** Add figures from Censys and a link to Calif’s writeup.

*This entry was posted on Wednesday 21st of October 2026 11:26 AM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2026-109618](https://krebsonsecurity.com/tag/cve-2026-109618/) [CVE-2026-109619](https://krebsonsecurity.com/tag/cve-2026-109619/) [Drupal](https://krebsonsecurity.com/tag/drupal/) [Joomla](https://krebsonsecurity.com/tag/joomla/) [Magento](https://krebsonsecurity.com/tag/magento/) [OpenAI](https://krebsonsecurity.com/tag/openai/) [PHP vulnerability](https://krebsonsecurity.com/tag/php-vulnerability/) [Wiz](https://krebsonsecurity.com/tag/wiz/) [wordpress](https://krebsonsecurity.com/tag/wordpress/)

Post navigation

[← Feds Suspect Ransom Negotiator Ran ShinyHunters Extortion Site](https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/)

### Leave a Reply [Cancel reply](/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Δ

Advertisement

[![](/b-flashpoint/7.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

Advertisement

Mailing List

[Subscribe here](/subscribe/)

Search KrebsOnSecurity

Search for:

Recent Posts

* [Widespread PHP Flaw May Cause Many Site Outages Today](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)
* [Feds Suspect Ransom Negotiator Ran ShinyHunters Extortion Site](https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/)
* [U.K. Sanctions Cryptomus for RU Money Laundering](https://krebsonsecurity.com/2026/10/u-k-sanctions-cryptomus-for-...