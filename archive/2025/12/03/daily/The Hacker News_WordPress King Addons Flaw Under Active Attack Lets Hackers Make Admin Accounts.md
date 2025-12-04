---
title: WordPress King Addons Flaw Under Active Attack Lets Hackers Make Admin Accounts
url: https://thehackernews.com/2025/12/wordpress-king-addons-flaw-under-active.html
source: The Hacker News
date: 2025-12-03
fetch_date: 2025-12-04T03:19:40.414601
---

# WordPress King Addons Flaw Under Active Attack Lets Hackers Make Admin Accounts

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [WordPress King Addons Flaw Under Active Attack Lets Hackers Make Admin Accounts](https://thehackernews.com/2025/12/wordpress-king-addons-flaw-under-active.html)

**Dec 03, 2025**Ravie LakshmananVulnerability / Website Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOEUBRBU7yOr4ksYNRA4-5equs6h7KyW_qETUsEQn6G_YqC_Qf7XlkyQ4kr4Ycwj5N97XeMxAppRT_JDyz7IETPajE9USD0YGONtpR0cMK-Zkd8BvJmoTFZ14U-5nj7WScTRyJLngRoOpf72yLTRFxXKST20oeimcv4ktQ0990pcmrOqS4pgWitQMGl66W/s790-rw-e365/wordpress.jpg)

A critical security flaw impacting a WordPress plugin known as King Addons for Elementor has come under active exploitation in the wild.

The vulnerability, **[CVE-2025-8489](https://www.cve.org/CVERecord?id=CVE-2025-8489)** (CVSS score: 9.8), is a case of privilege escalation that allows unauthenticated attackers to grant themselves administrative privileges by simply specifying the administrator user role during registration.

It affects versions from 24.12.92 through 51.1.14. It was patched by the maintainers in version 51.1.35 released on September 25, 2025. Security researcher Peter Thaleikis has been credited with discovering and reporting the flaw. The plugin has over 10,000 active installs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

"This is due to the plugin not properly restricting the roles that users can register with," Wordfence [said](https://www.wordfence.com/blog/2025/12/attackers-actively-exploiting-critical-vulnerability-in-king-addons-for-elementor-plugin/) in an alert. "This makes it possible for unauthenticated attackers to register with administrator-level user accounts."

Specifically, the issue is rooted in the "handle\_register\_ajax()" function that's invoked during user registration. But an insecure implementation of the function meant that unauthenticated attackers can specify their role as "administrator" in a crafted HTTP request to the "/wp-admin/admin-ajax.php" endpoint, allowing them to obtain elevated privileges.

Successful exploitation of the vulnerability could enable a bad actor to seize control of a susceptible site that has installed the plugin, and weaponize the access to upload malicious code that can deliver malware, redirect site visitors to sketchy sites, or inject spam.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-wjqAzsEVFHf0Wn3mNbOhCWDA5FA3WgLbpbCkiGheYXhPmlMwptmiWZpNVADwFgOZyMDYuxsz37fdPVttC_dOPPynRZxLC80TYn2SGwJKx3XJp2JH3J8dKx9cQagSF9F1Kx5oHaslQt-HtH95spaibAJXsTi271vKAU6v93KMOtlm-WmGfAyQz9PLtqGg/s2600/flaw.png)

Wordfence said it has blocked over 48,400 exploit attempts since the flaw was publicly disclosed in late October 2025, with 75 attempts thwarted in the last 24 hours alone. The attacks have originated from the following IP addresses -

* 45.61.157.120
* 182.8.226.228
* 138.199.21.230
* 206.238.221.25
* 2602:fa59:3:424::1

"Attackers may have started actively targeting this vulnerability as early as October 31, 2025, with mass exploitation starting on November 9, 2025," the WordPress security company said.

Site administrators are advised to ensure that they are running the latest version of the plugin, audit their environments for any suspicious admin users, and monitor for any signs of abnormal activity.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[website security](https://thehackernews.com/search/label/website%20security)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/sentinelone-protect)

Trending News

[![⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More")

⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html)

[![ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access](data:image/svg+xml;base64... "ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access")

ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access](https://thehackernews.com/2025/11/shadowpad-malware-actively-exploits.html)

[![China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](data:image/svg+xml;base64... "China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services")

China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html)

[![Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft](data:image/svg+xml;base64... "Second Sha1-Hulud Wave Affects 25,000+ Repositories via...