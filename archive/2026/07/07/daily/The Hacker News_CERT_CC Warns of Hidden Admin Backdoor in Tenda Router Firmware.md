---
title: CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware
url: https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:53.468426
---

# CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware](https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html)

**Ravie Lakshmanan**Jul 07, 2026

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibED37Q9WinxGoPYaXltP_givD-Q30FneMyezHB4uftr5E4hy4fMm97v_UH34sQWEvlp688bYvMR6zDzy_C93ddbqNDfIVSX7swJgdTD38hOmKgu6ZLGjBW068gXHpsT4soRscJ1vWDxTz2z8xBDSb2QD2UWrR68nVytui4mo6Q0cXVh_GjK5FC6P4imvK/s1700-e365/backdoor-admin.jpg)

Several versions of firmware released by Chinese network device manufacturer Tenda have been found to embed an undocumented authentication backdoor that enables administrative access to the devices' web management interfaces, the CERT Coordination Center (CERT/CC) warned Monday.

"An attacker can exploit this vulnerability, tracked as **[CVE-2026-11405](https://www.cve.org/CVERecord?id=CVE-2026-11405)**, to bypass the password verification process and obtain full administrative control without valid credentials," the CERT/CC [said](https://kb.cert.org/vuls/id/213560) in an alert.

The vulnerability impacts multiple versions of the firmware -

* US\_FH1201V1.0BR\_V1.2.0.14(408)\_EN\_TD
* US\_W15EV1.0br\_V15.11.0.5(1068\_1567\_841)\_EN\_TDE
* US\_AC10V1.0re\_V15.03.06.46\_multi\_TDE01
* US\_AC5V1.0RTL\_V15.03.06.48\_multi\_TDE01
* US\_AC6V2.0RTL\_V15.03.06.51\_multi\_T

The backdoor functionality is present within the "login()" function of the "/bin/httpd" web server binary. While the method initially follows a normal authentication path using MD5-based password verification, it activates an alternate code path if the authentication fails.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Specifically, this involves calling "GetValue("sys.rzadmin.password")" to fetch an alternate password value from the device configuration, and performing a direct plaintext comparison between the user-supplied password and the configuration-stored value. Should these values match, the application grants admin-level access (role=2) and creates a valid session with elevated privileges.

"The associated ["rzadmin"] username is not validated, so any provided username will succeed when paired with the backdoor password," the CERT/CC said. "This backdoor authentication mechanism is not documented or visible through any administrative interface."

Successful exploitation of this standard username validation override allows full administrative access to the device's web interface regardless of the administrator account credentials. It can permit an attacker to make unauthorized remote modification of settings, disable security features, or reconfigure the device, potentially leading to a complete device takeover.

The vulnerability, reported by an anonymous researcher, remains unpatched as of writing. The Hacker News has contacted Tenda for comment, and we will update the story if we hear back.

In the interim, users are advised to disable remote management on the device and change the default LAN IP address to prevent bad actors from reaching it and reduce opportunistic discovery by automated scanners that target known default IP ranges.

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

[Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [device security](https://thehackernews.com/search/label/device%20security), [Firmware Security](https://thehackernews.com/search/label/Firmware%20Security), [iot security](https://thehackernews.com/search/label/iot%20security), [network security](https://thehackernews.com/search/label/network%20security), [router security](https://thehackernews.com/search/label/router%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](data:image/svg+xml;base64... "ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories")

ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html)

[![Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](data:image/svg+xml;base64... "Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability")

Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)

[![New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets](data:image/svg+xml;base64... "New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets")

New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets](https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html)

[![Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs](data:image/svg+xml;base64... "Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs")

Amazon Q Develope...