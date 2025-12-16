---
title: FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws Enabling RCE
url: https://thehackernews.com/2025/12/freepbx-authentication-bypass-exposed.html
source: The Hacker News
date: 2025-12-15
fetch_date: 2025-12-16T03:24:40.117989
---

# FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws Enabling RCE

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

# [FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws Enabling RCE](https://thehackernews.com/2025/12/freepbx-authentication-bypass-exposed.html)

**Dec 15, 2025**Ravie LakshmananVulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgv01p712eomGjpG3imw4Fow3C_gFqZq2RwuHvosDk7WWN08kcB3sVc9ZCeOyic9zqqYml63fAppF-DF0gDBXnwMBbtFE7mr81Trn8IQVOmCn4Msnx5pL87XopJicEYXlyFchV5u0hToNbvtRYR0rhG0y5S0cK06UGK8_7HFAbNJylUxYV4BDG3ZupUNh7b/s790-rw-e365/zeroday.jpg)

Multiple security vulnerabilities have been [disclosed](https://horizon3.ai/attack-research/the-freepbx-rabbit-hole-cve-2025-66039-and-others/) in the open-source private branch exchange (PBX) platform FreePBX, including a critical flaw that could result in an authentication bypass under certain configurations.

The shortcomings, discovered by Horizon3.ai and reported to the project maintainers on September 15, 2025, are listed below -

* **[CVE-2025-61675](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-292p-rj6h-54cp)** (CVSS score: 8.6) - Numerous authenticated SQL injection vulnerabilities impacting four unique endpoints (basestation, model, firmware, and custom extension) and 11 affected parameters that enable read and write access to the underlying SQL database
* **[CVE-2025-61678](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-7p8x-8m3m-58j9)** (CVSS score: 8.6) - An authenticated arbitrary file upload vulnerability that allows an attacker to exploit the firmware upload endpoint to upload a PHP web shell after obtaining a valid PHPSESSID and run arbitrary commands to leak the contents of sensitive files (e.g., "/etc/passwd")
* **[CVE-2025-66039](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-9jvh-mv6x-w698)** (CVSS score: 9.3) - An authentication bypass vulnerability that occurs when the "Authorization Type" (aka AUTHTYPE) is set to "webserver," allowing an attacker to log in to the Administrator Control Panel via a forged Authorization header

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

It's worth mentioning here that the authentication bypass is not vulnerable in the default configuration of FreePBX, given that the "Authorization Type" option is only displayed when the three following values in the Advanced Settings Details are set to "Yes":

* Display Friendly Name
* Display Readonly Settings, and
* Override Readonly Settings

However, once the prerequisite is met, an attacker could send crafted HTTP requests to sidestep authentication and insert a malicious user into the "ampusers" database table, effectively accomplishing something similar to [CVE-2025-57819](https://thehackernews.com/2025/08/freepbx-servers-targeted-by-zero-day.html), another flaw in FreePBX that was disclosed as having been actively exploited in the wild in September 2025.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCKSGep-X285M1cJ2hIWOo-yxzr35tolP06gN3V7z6LZfO3hf9_uYbZhhDn0soUVwRfeQuJ4JEFYHOwJDWgqctyE6SGVaM6c8E-4zKNy8TIlhMytsGJsGIf5QpztI-XoJmt2OFS8A8dSMmfxOHnsTKo8fz06wRZ8KzN3C_kmgKcJO1rLTkQvzpbAekm-FI/s790-rw-e365/flaws.jpg)

"These vulnerabilities are easily exploitable and enable authenticated/unauthenticated remote attackers to achieve remote code execution on vulnerable FreePBX instances," Horizon3.ai security researcher Noah King said in a report published last week.

The issues have been addressed in the following versions -

* **CVE-2025-61675** and **CVE-2025-61678** - 16.0.92 and 17.0.6 (Fixed on October 14, 2025)
* **CVE-2025-66039** - 16.0.44 and 17.0.23 (Fixed on December 9, 2025)

In addition, the option to choose an authentication provider has now been removed from Advanced Settings and requires users to set it manually through the command-line using fwconsole. As temporary mitigations, FreePBX has recommended that users set "Authorization Type" to "usermanager," set "Override Readonly Settings" to "No," apply the new configuration, and reboot the system to disconnect any rogue sessions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

"If you did find that web server AUTHTYPE was enabled inadvertently, then you should fully analyze your system for signs of any potential compromise," it said.

Users are also displayed a warning on the dashboard, stating "webserver" may offer reduced security compared to "usermanager." For optimal protection, it's advised to avoid using this authentication type.

"It's important to note that the underlying vulnerable code is still present and relies on authentication layers in front to provide security and access to the FreePBX instance," King said. "It still requires passing an Authorization header with a basic Base64-encoded username:password."

"Depending on the endpoint, we noticed a valid username was required. In other cases, such as the file upload shared above, a valid username is not required, and you can achieve remote code execution with a few steps, as outlined. It is best practice not to use the authentication type webserver as it appears to be legacy code."

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
[**Share on T...