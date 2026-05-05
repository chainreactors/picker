---
title: Phishing Campaign Hits 80+ Orgs Using SimpleHelp and ScreenConnect RMM Tools
url: https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html
source: The Hacker News
date: 2026-05-04
fetch_date: 2026-05-05T05:04:17.548604
---

# Phishing Campaign Hits 80+ Orgs Using SimpleHelp and ScreenConnect RMM Tools

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

# [Phishing Campaign Hits 80+ Orgs Using SimpleHelp and ScreenConnect RMM Tools](https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html)

**Ravie Lakshmanan**May 04, 2026Network Security / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqa_ifaDYXI_GirxdHpZgSiE6fjnNdCmviv3QO9JsRvy1ddAWCRfoNd032ANB7pNfFMS4hLEwkfNHPHC5MNwkhK6XRjbe_y8qzWGpXRsdqhMnnUMGguScuIYtcUNQqQlmZkY4BUXy-ue6fAlor8LOfvEZNZrOq0JrIbOc2jXXAUBarqlodfdsIshRq7dXi/s1700-e365/phishing-org.jpg)

An active phishing campaign has been observed targeting multiple vectors since at least April 2025, with legitimate Remote Monitoring and Management (RMM) software as a way to establish persistent remote access to compromised hosts.

The activity, codenamed **VENOMOUS#HELPER**, has impacted over 80 organizations, most of which are in the U.S., according to Securonix. It shares overlaps with clusters previously tracked by [Red Canary](https://redcanary.com/blog/threat-intelligence/phishing-rmm-tools/) and Sophos, the latter of which has given it the moniker [STAC6405](https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html#saas-platforms-abused-for-phishing-delivery). While it's not clear who is behind the campaign, the cybersecurity company said it aligns with a financially motivated Initial Access Broker (IAB) or a ransomware precursor operation.

"In this case, a customized SimpleHelp and ScreenConnect RMMs are used to bypass defenses as they are legitimately installed by the unsuspecting victim," researchers Akshay Gaikwad, Shikha Sangwan, and Aaron Beardslee [said](https://www.securonix.com/blog/venomous-helper-phishing-campaign) in a report shared with The Hacker News.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

Setting aside the fact that the use of legitimate RMM tools can evade detection, the deployment of both SimpleHelp and ScreenConnect indicates an attempt to create a "redundant dual-channel access architecture" that enables continued operations even when either of them is detected and blocked.

It all begins with a phishing email impersonating the U.S. Social Security Administration (SSA), where the recipient is instructed to verify their email address and download a purported SSA statement by clicking on a link embedded in the message. The link points to a legitimate-but-compromised Mexican business website ("gruta.com[.]mx"), indicating a deliberate strategy to evade email spam filters.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjblWm6GIEienA1OGWMJ5fYEXYlRs7Eu788Qc7z0o7Xd0fDR7p_9xQSL-1xlO-Wg3jO6dHad-7p0Pgjzd5VYWDfOJk_-r9BN76KgrD5b3QUiIC_enfWKttaNfYMlRXFCyx744nq-wUqixK7wuJ45tiarAB6rO_dilmBNyTy5fhLWZIDieozoYITLRpZjHYC/s1700-e365/remote.jpg)

The "SSA statement" is then downloaded from a second attacker-controlled domain ("server.cubatiendaalimentos.com[.]mx"), an executable that's responsible for delivering the SimpleHelp RMM tool. It's believed that the attacker gained access to a single cPanel user account on the legitimate hosting server to stage the binary.

As soon as the victim opens the JWrapper-packaged Windows executable, thinking it's a document, the malware installs itself as a Windows service with Safe Mode persistence, makes sure it's running by means of a "self-healing watchdog" that automatically restarts it when killed, and periodically enumerates registered security products using the root\SecurityCenter2 WMI namespace every 67 seconds, and polls user presence every 23 seconds.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

To facilitate fully interactive desktop access, the SimpleHelp remote access client acquires SeDebugPrivilege via [AdjustTokenPrivileges](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges), while "elev\_win.exe" – a legitimate executable file associated with the software – is used to gain SYSTEM-level privileges. This, in turn, allows the operator to read the screen, inject keystrokes, and access user-context resources.

This elevated remote access is then abused to download and install ConnectWise ScreenConnect, offering a fallback communication mechanism if the SimpleHelp channel is taken down.

"The deployed SimpleHelp version (5.0.1) provides a comprehensive remote administration capability set," the researchers said. "The victim organization is left in a state where the attacker can return at any time, execute commands silently in the user’s desktop session, transfer files bidirectionally, and pivot to adjacent systems, while standard antivirus and signature-based controls see nothing but legitimately signed software from a reputable U.K. vendor."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data breach](https://thehackernews.com/search/label/data%20breach), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Malware](https://thehackernews.com/search/label/Malware), [network security](https://thehacker...