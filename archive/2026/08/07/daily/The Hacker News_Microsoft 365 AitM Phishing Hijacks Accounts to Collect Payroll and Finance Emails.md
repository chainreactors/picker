---
title: Microsoft 365 AitM Phishing Hijacks Accounts to Collect Payroll and Finance Emails
url: https://thehackernews.com/2026/08/microsoft-365-aitm-phishing-hijacks.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:01.531425
---

# Microsoft 365 AitM Phishing Hijacks Accounts to Collect Payroll and Finance Emails

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

![cybersecurity](data:image/svg+xml;base64...)

# [Microsoft 365 AitM Phishing Hijacks Accounts to Collect Payroll and Finance Emails](https://thehackernews.com/2026/08/microsoft-365-aitm-phishing-hijacks.html)

**Ravie Lakshmanan**Aug 07, 2026Phishing / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgH78NjDW1Q_sIk9dwQ1scYlCkNCMutfjGx_9flqrKbE42fEXqvHT8s5EeHTnWjbBGvzCuHPEWStR5r6wjwtIuuHF1hyphenhyphenot22E_Q98xedC1zXVhIhwglw6hLWQs45oSrPKPflK6Tt1BlHTj9iokMPpVaTehuemHGHDLL02cn2sqZJ5iIVstxiVf5IZ5Khodp/s1700-e365/ms-phish.jpg)

Cybersecurity researchers have called attention to an active "widespread email-driven phishing campaign" that employs adversary-in-the-middle (AitM) techniques to take control of Microsoft 365 accounts with an aim to identify key personnel involved in financial workflows and gather related email.

"The campaign uses residential proxies to disguise malicious sign-ins as ordinary consumer traffic," Arctic Wolf Labs [said](https://arcticwolf.com/resources/blog/payroll-pirates-strange-new-tides-in-business-email-compromise/). "Automated activity maintains compromised sessions at approximately eight-hour intervals."

The activity is assessed to impact organizations across healthcare, education, manufacturing, government, and professional services sectors located in the U.S., Canada, and Europe. It shares tactical overlaps with Payroll Pirate attacks tracked by Microsoft under the moniker [Storm-2755](https://thehackernews.com/2026/04/weekly-recap-fiber-optic-spying-windows.html#:~:text=Storm%2D2755%20Conducts%20Payroll%20Pirate%20Attacks).

Payroll Pirates is the designation assigned to a broader [financially motivated threat cluster](https://thehackernews.com/2025/10/microsoft-warns-of-payroll-pirates.html) that involves [hijacking](https://sra.io/blog/payroll-pirate-campaign-aitm-session-hijacking-and-microsoft-graph-reconnaissance-across-multiple-client-environments/) the accounts of employees to reroute salary payments to attacker-controlled accounts. Some aspects of these campaigns have been documented since early 2025, with Microsoft tracking a related threat as Storm-2657.

Arctic Wolf said it observed hundreds of organizations being targeted by email as part of the latest phishing campaign last month, resulting in successful intrusions spanning a broad range of victim environments.

Attack chains involve the use of voicemail-themed phishing emails to lead victims to AitM decoy pages that act as a proxy for the legitimate Microsoft account authentication flow, while stealthily capturing their credentials and multi-factor authentication (MFA) codes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

This is accomplished by means of a six-stage redirection chain that employs legitimate and trusted services like Google, Google Meet, Google Ads, and Amazon S3 to sidestep reputation-driven filters.

"The chain begins with a Google Meet linkredirect URL, and continues through Google's outbound-link infrastructure before reaching a Campaign Manager /ddm/clk dynamic click tracker," Arctic Wolf said. "In the activity we observed, the destination embedded in the tracker URL pointed to an HTML object hosted in an Amazon AWS S3 bucket. The S3-hosted page then redirected the victim to the campaign's AitM phishing infrastructure."

The phishing pages also employ JavaScript to fingerprint the visiting host, gathering information about the web browser, operating system, screen and window dimensions, browser language, time zone offset, cookie capabilities, WebDriver status, WebGL vendor, and browser API availability. All this information is packaged and sent to a PHP endpoint through an HTTP POST request. The script then redirects the browser to the proxied Microsoft OAuth authorization endpoint.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjawHPyzxcVaMFSCmvbKM9yj9CC5Re7tuR9hmz7QM7RDyQNe7175m4rYm9V37zVoHB6DODZAuutuR0-P7Yg2ep_DYYT1a45Vdj1KiemkDkfLmaSnvJf_s-1AsR6rc_iZ4QqDdDzeIbLPb2LOLaepIUg57Er8vU7_675bs_OhY-zUGunuoVf4YUoor1YNnF/s1700-e365/redirect.png)

It also queries a geolocation API ("api.country[.]is") for the requester's country code, and stores the result in a "rcfh\_country" cookie with a seven-day expiration. Once initial access is obtained, the threat actor abuses the compromised sessions to collect emails from payroll and HR personnel who are involved in financial matters at the enterprise.

What's more, controlled testing reveals that the malicious sign-in activity originates within minutes from a residential proxy exit node in the victim's country, indicating that the threat actors are possibly leveraging the geolocation data to select geographically matched proxy infrastructure for subsequent logins and evade security controls that otherwise prevent access from unusual IP addresses.

Some of these sign-in events report "implausible browser and operating-system combinations," such as mobile versions of Apple Safari or Google Chrome on Windows 10.

"Typically, 11 to 24 hours after the initial anomalous activity, malicious sign-ins began recurring at eight-hour intervals from rotating residential proxy addresses," Arctic Wolf added. "These events reported Microsoft Outlook as the client application but used Firefox 131.0, Firefox 151.0, or occasionally Python Requests user agents rather than the expected Edge user agent."

"The recurring sign-ins retained the same SessionID while the source IP address, ASN, and geographic location changed, providing further evidence that centralized automation was refreshing each compromised session independently."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Like in the case of Storm-2755, the threat actors have been found relying on the Microsoft Graph API to enumerate tenant users associated with payroll, HR, finance, and administrative functions, and then accessing messages related to payroll, invoices, payments, banking, benefits, and internal documents..

In most intrusions investigated by the security vendor, the attackers are said to have restricted their post-compromise actions to session maintenance, reconnaissance, and mailbox collection. No other activity, including MFA-method changes, device ...