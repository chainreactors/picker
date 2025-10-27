---
title: Watch Out! These Android Keyboard Apps With 2 Million Installs Can be Hacked Remotely
url: https://thehackernews.com/2022/12/watch-out-these-android-keyboard-apps.html
source: The Hacker News
date: 2022-12-03
fetch_date: 2025-10-04T00:26:40.578791
---

# Watch Out! These Android Keyboard Apps With 2 Million Installs Can be Hacked Remotely

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Watch Out! These Android Keyboard Apps With 2 Million Installs Can be Hacked Remotely](https://thehackernews.com/2022/12/watch-out-these-android-keyboard-apps.html)

**Dec 02, 2022**Ravie LakshmananMobile Security / Vulnerability

[![Android Remote Keyboard App](data:image/png;base64... "Android Remote Keyboard App")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQrGQZnw71xbHna91_XFGhMxRYuui5j1sbAmGTkQTph4ohlJeVpMn-iP0tbxXCE4tk29iTpgc0LT9ZcRswHblSlG9Eug9EUgQcsFDv0VBtBx_wZTjjjStjh7X7XcvuHX-9V4j9HI8AS9zJlU6d5kW2qKmqscEFMvfAFs_o6EG1zFM5JQBIDr-AA7W-/s790-rw-e365/apps.png)

Multiple unpatched vulnerabilities have been discovered in three Android apps that allow a smartphone to be used as a remote keyboard and mouse.

The apps in question are **Lazy Mouse**, **PC Keyboard**, and **Telepad**, which have been cumulatively downloaded over two million times from the Google Play Store. Telepad is no longer available through the app marketplace but can be downloaded from its website.

* Lazy Mouse (com.ahmedaay.lazymouse2 and com.ahmedaay.lazymousepro)
* PC Keyboard (com.beapps.pckeyboard)
* Telepad (com.pinchtools.telepad)

While these apps function by connecting to a server on a desktop and transmitting to it the mouse and keyboard events, the Synopsys Cybersecurity Research Center (CyRC) [found](https://www.synopsys.com/blogs/software-security/cyrc-advisory-remote-code-execution-vulnerabilities-mouse-keyboard-apps/) as many as seven flaws related to weak or missing authentication, missing authorization, and insecure communication.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The issues (from CVE-2022-45477 through CVE-2022-45483), in a nutshell, could be exploited by a malicious actor to execute arbitrary commands sans authentication or harvest sensitive information by exposing users' keystrokes in cleartext.

The Lazy Mouse server further suffers from a weak password policy and doesn't implement rate limiting, enabling remote unauthenticated attackers to trivially brute-force the PIN and execute rogue commands.

It's worth noting that none of the apps have received any updates for over two years, making it imperative that users remove the apps with immediate effect.

"These three applications are widely used but they are neither maintained nor supported, and evidently, security was not a factor when these applications were developed," Synopsys security researcher Mohammed Alshehri said.

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

[Android](https://thehackernews.com/search/label/Android)[hacking news](https://thehackernews.com/search/label/hacking%20news)[mobile hacking](https://thehackernews.com/search/label/mobile%20hacking)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Remote Keyboard App](https://thehackernews.com/search/label/Remote%20Keyboard%20App)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware")

Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](https://thehackernews.com/2025/09/cisco-asa-firewall-zero-day-exploits.htm...