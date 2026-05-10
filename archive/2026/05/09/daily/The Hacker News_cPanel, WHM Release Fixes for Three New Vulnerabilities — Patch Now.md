---
title: cPanel, WHM Release Fixes for Three New Vulnerabilities — Patch Now
url: https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html
source: The Hacker News
date: 2026-05-09
fetch_date: 2026-05-10T05:38:45.315433
---

# cPanel, WHM Release Fixes for Three New Vulnerabilities — Patch Now

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [cPanel, WHM Release Fixes for Three New Vulnerabilities — Patch Now](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html)

**Ravie Lakshmanan**May 09, 2026Vulnerability / Web Hosting

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8HLwOMzo20kbZmflPvJJmY7su6wWOWgDLV-dJNx-k76m5ivbwVoCkFrnsLXkyO4PHAyLSkPXinjK71SDmWabyOcTlKb3juZgkXTzOVuMvZk6-LUFMhoJ-UGFvv0qEby7QmYcjTWn1m1L19VTKeB7CdmKvpvIP5ifniLO92ARSLjtf8rcXIbm8AFMZei-M/s1700-e365/cpanel-3.jpg)

cPanel has released updates to address three vulnerabilities in cPanel and Web Host Manager (WHM) that could be exploited to achieve privilege escalation, code execution, and denial-of-service.

The list of vulnerabilities is as follows -

* **[CVE-2026-29201](https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026)** (CVSS score: 4.3) - An insufficient input validation of the feature file name in the "feature::LOADFEATUREFILE" adminbin call that could result in an arbitrary file read.
* **[CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)** (CVSS score: 8.8) - An insufficient input validation of the "plugin" parameter in the "create\_user API" call that could result in arbitrary Perl code execution on behalf of the already authenticated account's system user.
* **[CVE-2026-29203](https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026)** (CVSS score: 8.8) - An unsafe symlink handling vulnerability that allows a user to modify access permissions of an arbitrary file using chmod, resulting in denial-of-service or possible privilege escalation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The shortcomings have been patched in the following versions -

* cPanel and WHM -
  + 11.136.0.9 and higher
  + 11.134.0.25 and higher
  + 11.132.0.31 and higher
  + 11.130.0.22 and higher
  + 11.126.0.58 and higher
  + 11.124.0.37 and higher
  + 11.118.0.66 and higher
  + 11.110.0.116 and higher
  + 11.110.0.117 and higher
  + 11.102.0.41 and higher
  + 11.94.0.30 and higher
  + 11.86.0.43 and higher
* WP Squared -
  + 11.136.1.10 and higher

cPanel has released 110.0.114 as a direct update for customers who are still on CentOS 6 or CloudLinux 6. Users are advised to update to the latest versions for optimal protection.

While there is no evidence that the vulnerabilities have been exploited in the wild, the disclosure comes days after another critical flaw in the product ([CVE-2026-41940](https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html)) has been weaponized by threat actors as a zero-day to deliver Mirai botnet variants and a ransomware strain called Sorry.

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

[Code Execution](https://thehackernews.com/search/label/Code%20Execution), [cPanel](https://thehackernews.com/search/label/cPanel), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [denial of service](https://thehackernews.com/search/label/denial%20of%20service), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [web hosting](https://thehackernews.com/search/label/web%20hosting), [WHM](https://thehackernews.com/search/label/WHM)

⚡ Top Stories This Week

[![30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](data:image/svg+xml;base64... "30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign")

30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html)

[![Trellix Confirms Source Code Breach With Unauthorized Repository Access](data:image/svg+xml;base64... "Trellix Confirms Source Code Breach With Unauthorized Repository Access")

Trellix Confirms Source Code Breach With Unauthorized Repository Access](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html)

[![⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE and More](data:image/svg+xml;base64... "⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE and More")

⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE and More](https://thehackernews.com/2026/05/weekly-recap-ai-powered-phishing.html)

[![Progress Patches Critical MOVEit Automation Bug Enabling Authentication Bypass](data:image/svg+xml;base64... "Progress Patches Critical MOVEit Automation Bug Enabling Authentication Bypass")

Progress Patches Critical MOVEit Automation Bug Enabling Authentication Bypass](https://thehackernews.com/2026/05/progress-patches-critical-moveit.html)

[![Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries](data:image/svg+xml;base64... "Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries")

Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries](h...