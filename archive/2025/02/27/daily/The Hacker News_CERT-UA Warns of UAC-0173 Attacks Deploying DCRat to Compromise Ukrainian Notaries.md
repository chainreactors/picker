---
title: CERT-UA Warns of UAC-0173 Attacks Deploying DCRat to Compromise Ukrainian Notaries
url: https://thehackernews.com/2025/02/cert-ua-warns-of-uac-0173-attacks.html
source: The Hacker News
date: 2025-02-27
fetch_date: 2025-10-06T21:55:35.480078
---

# CERT-UA Warns of UAC-0173 Attacks Deploying DCRat to Compromise Ukrainian Notaries

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

# [CERT-UA Warns of UAC-0173 Attacks Deploying DCRat to Compromise Ukrainian Notaries](https://thehackernews.com/2025/02/cert-ua-warns-of-uac-0173-attacks.html)

**Feb 26, 2025**Ravie LakshmananNetwork Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhY0324h3uo5bz417HGRaeXwvocbEwwHLaylpICIGZfQzC8szBZOLjgdwq_t11_Yiihar1RIg1aso3JVgcd8cAbbxmrvPCBJeSH2Q4z5z3w95DKHesWvE1W4tCTF79aR4Glo__XpponIRB4BAWzad8VZoHlQQ6D_FNPWI7i26BFeF_PvYIOMTvImH1zvIcS/s790-rw-e365/cyberattack.jpg)

The Computer Emergency Response Team of Ukraine (CERT-UA) on Tuesday warned of renewed activity from an organized criminal group it tracks as UAC-0173 that involves infecting computers with a remote access trojan named [DCRat](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html) (aka DarkCrystal RAT).

The Ukrainian cybersecurity authority said it observed the latest attack wave starting in mid-January 2025. The activity is designed to target the Notary of Ukraine.

The infection chain leverages phishing emails that claim to be sent on behalf of the Ministry of Justice of Ukraine, urging recipients to download an executable, which, when launched, leads to the deployment of the DCRat malware. The binary is hosted in [Cloudflare's R2](https://thehackernews.com/2023/08/cybercriminals-abusing-cloudflare-r2.html) cloud storage service.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Having thus provided primary access to the notary's automated workplace, the attackers take measures to install additional tools, in particular, RDPWRAPPER, which implements the functionality of parallel RDP sessions, which, in combination with the use of the BORE utility, allows you to establish RDP connections from the Internet directly to the computer," CERT-UA [said](https://cert.gov.ua/article/6282536).

The attacks are also characterized by the use of other tools and malware families like FIDDLER for intercepting authentication data entered in the web interface of state registers, NMAP for network scanning, and XWorm for stealing sensitive data, such as credentials and clipboard content.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjSsKVsOsUaBv_0vO1EH8UpCGfJZnymCGYevuM02SpikON2l4wQuxvCKPt3hqo9CjVIf8HQIPWk24pdBTd_JP_umWZ6XyXPddYAhgsoWx-UncMMgnXYhsaqlyKJw_g6-G4fpqqXAXHtVREeYDlF1c7bCQuwpUnMs-f-D7iwXBSPrpgsfLHeBM9cF_DRILI/s790-rw-e365/script.png)

Furthermore, the compromised systems are used as a conduit to draft and send malicious emails using the SENDMAIL console utility in order to further propagate the attacks.

The development comes days after CERT-UA attributed a sub-cluster within the Sandworm hacking group (aka APT44, Seashell Blizzard, and UAC-0002) to the exploitation of a now-patched security flaw in Microsoft Windows ([CVE-2024-38213](https://thehackernews.com/2024/08/microsoft-issues-patches-for-90-flaws.html), CVSS score: 6.5) in the second half of 2024 via booby-trapped documents.

The attack chains have been found to execute PowerShell commands responsible for displaying a decoy file, while simultaneously launching additional payloads in the background, including SECONDBEST (aka EMPIREPAST), SPARK, and a Golang loader named CROOKBAG.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The activity, [attributed](https://cert.gov.ua/article/6282517) to UAC-0212, targeted supplier companies from Serbia, the Czech Republic, and Ukraine between July 2024 and February 2025, with some of them recorded against more than two dozen Ukrainian enterprises specializing in development of automated process control systems (ACST), electrical works, and freight transportation.

Some of these attacks have been documented by [StrikeReady Labs](https://strikeready.com/blog/ru-apt-targeting-energy-infrastructure-unknown-unknowns-part-3/) and Microsoft, the latter of which is tracking the threat group under the moniker [BadPilot](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html).

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Phishing](https://thehackernews.com/search/label/Phishing)[ransomware](https://thehackernews.com/search/label/ransomware)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident R...