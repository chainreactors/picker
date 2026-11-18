---
title: ConnectWise Warns ScreenConnect Attacks Continue as SCKit Targets Unpatched Systems
url: https://thehackernews.com/2026/11/connectwise-warns-screenconnect-attacks.html
source: The Hacker News
date: 2026-11-17
fetch_date: 2026-11-18T09:22:49.249383
---

# ConnectWise Warns ScreenConnect Attacks Continue as SCKit Targets Unpatched Systems

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [ConnectWise Warns ScreenConnect Attacks Continue as SCKit Targets Unpatched Systems](https://thehackernews.com/2026/11/connectwise-warns-screenconnect-attacks.html)

**Ravie Lakshmanan**Nov 17, 2026Endpoint Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjErwt0frcFKiESffCoP1OtYh0j23goqdMN0nz-RT02biCz30WlLG4PD5gTyGgbumOWB3Zh1PJfENQoRtOwQVm3Nbg8VsiRhvNk662qVFNGqO8DQ4bFrroSzWgsvfCYGLWFzD1A-f6fcTu_E_dm4o1iUJz96scWy7skw49vzD9hfIfVEILTVPKsvbsEpGca/s1700-nu-rw-lo-l85-e365/screenconnect-flaws.jpg)

ConnectWise on Monday said it completed its investigation into unauthorized access targeting partner ScreenConnect environments, and recommended customers to ensure that the technician client is running version 26.6.5 or later.

The company said additional activity targeting on-premises environments continues to be reported where the identified third-party extensions remain enabled and ScreenConnect has not been updated to the latest version.

"On-premises partners must immediately disable the identified extensions and update ScreenConnect to the latest supported version," the company [said](https://www.connectwise.com/company/trust/advisories).

It's worth noting that version 26.6.5 addresses a critical-severity flaw in ScreenConnect client tracked as [CVE-2026-84869](https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin) (CVSS score: 9.9) that could allow files to be transferred and executed through an active remote session without authorization or Host confirmation in certain circumstances.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

As highlighted by [Huntress](https://thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html) and [Blackpoint Cyber](https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html) last week, unknown threat actors are suspected to be exploiting an authentication flaw in RMM+ versions 1.0.31 and 1.0.32 to execute unauthorized commands while bypassing ScreenConnect's regular authentication controls.

The attacks have been found to deploy a multi-component toolkit dubbed SCKit that's capable of spreading from infected customer devices to MSP technicians' computers and compromising additional managed networks by means of a C# module called RelayTrap ("RelayTrap.cs").

Specifically, the malware employs a worm-like technique that exploits CVE-2026-84869 to execute malicious code on a technician's workstation when they connect to an infected device to investigate a problem. There is no evidence this worm-like behavior has succeeded in the latest campaign.

Huntress has since said it detected another spike in SCKit-related activity on November 13, 2026, impacting 205 hosts across 41 organizations.

"Across the incidents, we saw the new ScreenConnect client being hosted at [185.241.211[.]197](https://www.virustotal.com/gui/ip-address/185.241.211.197), which is associated with [1337 Services GmbH](https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html), a bulletproof hosting provider known for previously hosting malicious traffic," the company [said](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"In one of the incidents, we saw a rogue ScreenConnect client establish persistence via a service called Windows Update Agent, posing as a legitimate system component. The service executable (UpdateConnect.ClientService.exe) was placed in C:\ProgramData\Windows Update Agent (de362a425905bcc4)\ and configured to run under the LocalSystem account."

In response to the incident, ConnectWise has taken the step of disabling five third-party extensions, including Labtech Plus, RMM Plus, RMM+, RMM Plus Password Link, and RMM+ Password Link, across 400 partner environments. That said, the presence of these extensions alone does not imply those environments were impacted.

The company is also urging partners not to re-enable or reinstall the extensions until further guidance. "Disabling extensions and updating software do not remove unauthorized access or persistence already established on affected devices," it added.

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

[ConnectWise](https://thehackernews.com/search/label/ConnectWise), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Malware](https://thehackernews.com/search/label/Malware), [Remote Monitoring and Management](https://thehackernews.com/search/label/Remote%20Monitoring%20and%20Management), [ScreenConnect](https://thehackernews.com/search/label/ScreenConnect), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

[![The Hacker News](data:image/svg+xml;base64...)

PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](htt...