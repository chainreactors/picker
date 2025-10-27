---
title: Roundcube Webmail Flaws Allow Hackers to Steal Emails and Passwords
url: https://thehackernews.com/2024/08/roundcube-webmail-flaws-allow-hackers.html
source: The Hacker News
date: 2024-08-08
fetch_date: 2025-10-06T18:08:38.628806
---

# Roundcube Webmail Flaws Allow Hackers to Steal Emails and Passwords

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

# [Roundcube Webmail Flaws Allow Hackers to Steal Emails and Passwords](https://thehackernews.com/2024/08/roundcube-webmail-flaws-allow-hackers.html)

**Aug 07, 2024**Ravie LakshmananEmail Security / Vulnerability

[![Roundcube Webmail](data:image/png;base64... "Roundcube Webmail")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX5YB3bwk3OIyl0ZqBULKUWDGb2Gn3XnAD8Jfl5qBUs1xnAhZbxOKJOVyE4eB5DXQI-XjbyCRbwRxhiByayenxBRBMuw9wgS8KFgnWleSHGoElMGmc9LsoADNYzY9KkG5LHYOIAilfrttbrReBAEg6yDJe0VOn-6fmCtUb0aYUZXfzI5XfMSyZ85kT1TT-/s790-rw-e365/roundcube.png)

Cybersecurity researchers have disclosed details of security flaws in the Roundcube webmail software that could be exploited to execute malicious JavaScript in a victim's web browser and steal sensitive information from their account under specific circumstances.

"When a victim views a malicious email in Roundcube sent by an attacker, the attacker can execute arbitrary JavaScript in the victim's browser," cybersecurity company Sonar [said](https://www.sonarsource.com/blog/government-emails-at-risk-critical-cross-site-scripting-vulnerability-in-roundcube-webmail/) in an analysis published this week.

"Attackers can abuse the vulnerability to steal emails, contacts, and the victim's email password as well as send emails from the victim's account."

Following responsible disclosure on June 18, 2024, the three vulnerabilities have been [addressed](https://github.com/roundcube/roundcubemail/releases) in Roundcube versions 1.6.8 and 1.5.8 released on August 4, 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The list of vulnerabilities is as follows -

* **[CVE-2024-42008](https://github.com/advisories/GHSA-78jf-j6qx-c7j3)** - A cross-site scripting flaw via a malicious email attachment served with a dangerous Content-Type header
* **[CVE-2024-42009](https://github.com/advisories/GHSA-j43g-prf4-578j)** - A cross-site scripting flaw that arises from post-processing of sanitized HTML content
* **[CVE-2024-42010](https://github.com/advisories/GHSA-853r-xr2f-r2x6)** - An information disclosure flaw that stems from insufficient CSS filtering

Successful exploitation of the aforementioned flaws could allow unauthenticated attackers to steal emails and contacts, as well as send emails from a victim's account, but after viewing a specially crafted email in Roundcube.

"Attackers can gain a persistent foothold in the victim's browser across restarts, allowing them to exfiltrate emails continuously or steal the victim's password the next time it is entered," security researcher Oskar Zeino-Mahmalat said.

"For a successful attack, no user interaction beyond viewing the attacker's email is required to exploit the critical XSS vulnerability (CVE-2024-42009). For CVE-2024-42008, a single click by the victim is needed for the exploit to work, but the attacker can make this interaction unobvious for the user."

Additional technical details about the issues have been withheld to give time for users to update to the latest version, and in light of the fact that flaws in the webmail software have been [repeatedly exploited](https://thehackernews.com/2024/02/alert-cisa-warns-of-active-roundcube.html) by nation-state actors like [APT28, Winter Vivern](https://thehackernews.com/2023/10/nation-state-hackers-exploiting-zero.html), and [TAG-70](https://thehackernews.com/2024/02/russian-linked-hackers-breach-80.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings come as details have emerged about a maximum-severity local privilege escalation flaw in the [RaspAP](https://github.com/RaspAP/raspap-webgui) open-source project ([CVE-2024-41637](https://github.com/advisories/GHSA-q623-2j2j-23jj), CVSS score: 10.0) that allows an attacker to elevate to root and execute several critical commands. The vulnerability has been addressed in version 3.1.5.

"The www-data user has write access to the restapi.service file and also possesses sudo privileges to execute several critical commands without a password," a security researcher who goes by the online alias 0xZon1 [said](https://blog.0xzon.dev/2024-07-27-CVE-2024-41637/). "This combination of permissions allows an attacker to modify the service to execute arbitrary code with root privileges, escalating their access from www-data to root."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[email security](https://thehackernews.com/search/label/email%20security)[hacking](https://thehackernews.com/search/label/hacking)[Information security](https://thehackernews.com/search/label/Information%20security)[Malware](https://thehackernews.com/search/label/Malware)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Web Application Security](https://thehackernews.com/search/label/Web%20Application%20Security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Cont...