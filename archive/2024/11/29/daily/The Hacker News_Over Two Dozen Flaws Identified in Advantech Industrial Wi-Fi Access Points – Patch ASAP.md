---
title: Over Two Dozen Flaws Identified in Advantech Industrial Wi-Fi Access Points – Patch ASAP
url: https://thehackernews.com/2024/11/over-two-dozen-flaws-identified-in.html
source: The Hacker News
date: 2024-11-29
fetch_date: 2025-10-06T19:19:52.422775
---

# Over Two Dozen Flaws Identified in Advantech Industrial Wi-Fi Access Points – Patch ASAP

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

# [Over Two Dozen Flaws Identified in Advantech Industrial Wi-Fi Access Points – Patch ASAP](https://thehackernews.com/2024/11/over-two-dozen-flaws-identified-in.html)

**Nov 28, 2024**Ravie LakshmananIoT Security / Vulnerability

[![Industrial Wi-Fi Access Points](data:image/png;base64... "Industrial Wi-Fi Access Points")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5JpLpZSTuw5BOTZ3_pJZvZp2Pa_UhHUIFiPPnxNKAdktmY6cZAY2gm81rNzLwgPL3C8NmYQXzq8JDVrl8HvpqrNDEmdIna1O3YB9v_217aJU75aneIY1qAvl2m9QHVE7c-T7a3iptqCS7bf98P95JFDbuLtHwcKvt4nFjKlMC2FeHrseCYYUHQ5KtWMkK/s790-rw-e365/wifi.png)

Nearly two dozen security vulnerabilities have been disclosed in Advantech EKI industrial-grade wireless access point devices, some of which could be weaponized to bypass authentication and execute code with elevated privileges.

"These vulnerabilities pose significant risks, allowing unauthenticated remote code execution with root privileges, thereby fully compromising the confidentiality, integrity, and availability of the affected devices," cybersecurity company Nozomi Networks [said](https://www.nozominetworks.com/blog/over-the-air-vulnerabilities-discovered-in-advantech-eki-access-points) in a Wednesday analysis.

Following responsible disclosure, the weaknesses have been addressed in the following firmware versions -

* 1.6.5 (for EKI-6333AC-2G and EKI-6333AC-2GD)
* 1.2.2 (for EKI-6333AC-1GPO)

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Six of the identified 20 vulnerabilities have been deemed critical, allowing an attacker to obtain persistent access to internal resources by implanting a backdoor, trigger a denial-of-service (DoS) condition, and even repurpose infected endpoints as Linux workstations to enable lateral movement and further network penetration.

Of the six critical flaws, five (from CVE-2024-50370 through CVE-2024-50374, CVSS scores: 9.8) relate to improper neutralization of special elements used in an operating system (OS) command, while CVE-2024-50375 (CVSS score: 9.8) concerns a case of missing authentication for a critical function.

Also of note is CVE-2024-50376 (CVSS score: 7.3), a cross-site scripting flaw that could be chained with CVE-2024-50359 (CVSS score: 7.2), another instance of OS command injection that would otherwise require authentication, to achieve arbitrary code execution over-the-air.

That said, in order for this attack to be successful, it requires the external malicious user to be in physical proximity to the Advantech access point and broadcast specially crafted data from a rogue access point.

[![Industrial Wi-Fi Access Points](data:image/png;base64... "Industrial Wi-Fi Access Points")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAm63Cf5f2dP-jiX7_CthcJ5MFkPOEDOXgnXG_6Qaon6iDJbJ4B3LQbSMU8BpyOfMlGRfx0R-SOlGuQLZoWSZmh0W1Hy-WrCwGQCpCPOIRtVmeAhJWgTy6TUtny587J9FfSgD3nu9oMnDQRfY-W0X7xNfOWZVkqcrZmFhkOrF-vLXeqpdn2aJUlxelHB0R/s790-rw-e365/WIFIHACK.png)

The attack gets activated when an administrator visits the "Wi-Fi Analyzer" section in the web application, causing the page to automatically embed information received through beacon frames broadcasted by the attacker without any sanitization checks.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"One such piece of information an attacker could broadcast through its rogue access point is the SSID (commonly referred to as the 'Wi-Fi network name')," Nozomi Networks said. "The attacker could therefore insert a JavaScript payload as SSID for its rogue access point and exploit CVE-2024-50376 to trigger a cross-site scripting (XSS) vulnerability inside the web application."

The result is the execution of arbitrary JavaScript code in the context of the victim's web browser, which could then be combined with CVE-2024-50359 to achieve command injection at the OS level with root privileges. This could take the form of a reverse shell that provides persistent remote access to the threat actor.

"This would enable attackers to gain remote control over the compromised device, execute commands, and further infiltrate the network, extracting data or deploying additional malicious scripts," the company said.

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

[Cross-site Scripting](https://thehackernews.com/search/label/Cross-site%20Scripting)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firmware Security](https://thehackernews.com/search/label/Firmware%20Security)[iot security](https://thehackernews.com/search/label/iot%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[wireless security](https://thehackernews.com/search/label/wireless%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-...