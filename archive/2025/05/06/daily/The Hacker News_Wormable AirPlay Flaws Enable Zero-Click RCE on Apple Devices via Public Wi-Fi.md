---
title: Wormable AirPlay Flaws Enable Zero-Click RCE on Apple Devices via Public Wi-Fi
url: https://thehackernews.com/2025/05/wormable-airplay-flaws-enable-zero.html
source: The Hacker News
date: 2025-05-06
fetch_date: 2025-10-06T22:34:41.577456
---

# Wormable AirPlay Flaws Enable Zero-Click RCE on Apple Devices via Public Wi-Fi

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

# [Wormable AirPlay Flaws Enable Zero-Click RCE on Apple Devices via Public Wi-Fi](https://thehackernews.com/2025/05/wormable-airplay-flaws-enable-zero.html)

**May 05, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![Wormable AirPlay Flaws](data:image/png;base64... "Wormable AirPlay Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjilfYxt9qS9GS2OvMO9uwYEcv0kEQUpJlMRJeZ7jbRr-5CCegKl3ANonBsspiigbOyGmB3BLsd_ujTQrVcnhPK78Mq8faqJ6FhQWa-KoNJ70mhtIdkd51j0hJew3u17Jqddr_nW3THa8Nprn_zPg7TuGPh7FXEJwl4BIyYTfZi1YN5hgnlCog0aqBQDkwo/s790-rw-e365/apple.jpg)

Cybersecurity researchers have disclosed a series of now-patched security vulnerabilities in Apple's AirPlay protocol that, if successfully exploited, could enable an attacker to take over susceptible devices supporting the proprietary wireless technology.

The shortcomings have been collectively codenamed **AirBorne** by Israeli cybersecurity company Oligo.

"These vulnerabilities can be chained by attackers to potentially take control of devices that support AirPlay – including both Apple devices and third-party devices that leverage the AirPlay SDK," security researchers Uri Katz, Avi Lumelsky, and Gal Elbaz [said](https://www.oligo.security/blog/airborne).

Some of the vulnerabilities, like CVE-2025-24252 and CVE-2025-24132, can be strung together to fashion a wormable zero-click RCE exploit, enabling bad actors to deploy malware that propagates to devices on any local network the infected device connects to.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This could then pave the way for sophisticated attacks that can lead to the deployment of backdoors and ransomware, posing a serious security risk.

The vulnerabilities, in a nutshell, could enable zero- or one-click remote code execution (RCE), access control list (ACL) and user interaction bypass, local arbitrary file read, information disclosure, adversary-in-the-middle (AitM) attacks, and denial-of-service (DoS).

This includes chaining CVE-2025-24252 and CVE-2025-24206 to achieve a zero-click RCE on macOS devices that are connected to the same network as an attacker. However, for this exploit to succeed, the AirPlay receiver needs to be on and set to the "Anyone on the same network" or "Everyone" configuration.

In a hypothetical attack scenario, a victim's device could get compromised when connected to a public Wi-Fi network. Should the device be connected later to an enterprise network, it could provide an attacker with a way to breach other devices that are connected to the same network.

Some of the other notable flaws are listed below -

* **CVE-2025-24271** - An ACL vulnerability that can enable an attacker on the same network as a signed-in Mac to send AirPlay commands to it without pairing
* **CVE-2025-24137** - A vulnerability that could cause arbitrary code execution or an application to terminate
* **CVE-2025-24132** - A stack-based buffer overflow vulnerability that could result in a zero-click RCE on speakers and receivers that leverage the AirPlay SDK
* **CVE-2025-24206** - An authentication vulnerability that could allow an attacker on the local network to bypass authentication policy
* **CVE-2025-24270** - A vulnerability that could allow an attacker on the local network to leak sensitive user information
* **CVE-2025-24251** - A vulnerability that could allow an attacker on the local network to cause an unexpected app termination
* **CVE-2025-31197** - A vulnerability that could allow an attacker on the local network to cause an unexpected app termination
* **CVE-2025-30445** - A type confusion vulnerability that could could allow an attacker on the local network to cause an unexpected app termination
* **CVE-2025-31203** - An integer overflow vulnerability that could allow an attacker on the local network to cause a DoS condition

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Following a responsible disclosure process, the identified vulnerabilities have been patched in the below versions -

* iOS 18.4 and iPadOS 18.4
* iPadOS 17.7.6
* macOS Sequoia 15.4
* macOS Sonoma 14.7.5
* macOS Ventura 13.7.5
* tvOS 18.4, and
* visionOS 2.4

Some of the weaknesses (CVE-2025-24132 and CVE-2025-30422) have also been patched in AirPlay audio SDK 2.7.1, AirPlay video SDK 3.6.0.126, and CarPlay Communication Plug-in R18.1.

"For organizations, it is imperative that any corporate Apple devices and other machines that support AirPlay are updated immediately to the latest software versions," Oligo said.

"Security leaders also need to provide clear communication to their employees that all of their personal devices that support AirPlay need to also be updated immediately."

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

[AirPlay](https://thehackernews.com/search/label/AirPlay)[Apple](https://thehackernews.com/search/label/Apple)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[MacOS](https://thehackernews.com/search/label/MacOS)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[remote code execution](https:...