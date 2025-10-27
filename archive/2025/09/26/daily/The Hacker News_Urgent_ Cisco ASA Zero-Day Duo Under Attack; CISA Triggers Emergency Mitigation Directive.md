---
title: Urgent: Cisco ASA Zero-Day Duo Under Attack; CISA Triggers Emergency Mitigation Directive
url: https://thehackernews.com/2025/09/urgent-cisco-asa-zero-day-duo-under.html
source: The Hacker News
date: 2025-09-26
fetch_date: 2025-10-02T20:44:42.966007
---

# Urgent: Cisco ASA Zero-Day Duo Under Attack; CISA Triggers Emergency Mitigation Directive

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

# [Urgent: Cisco ASA Zero-Day Duo Under Attack; CISA Triggers Emergency Mitigation Directive](https://thehackernews.com/2025/09/urgent-cisco-asa-zero-day-duo-under.html)

**Sep 25, 2025**Ravie LakshmananZero-Day / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb62bTFQ5J-V9tH8fTA9NS07AsTjPNVMSznx_nisSoruMwRCXxwy-p9UzEqHwcGveaBix09mJL-kAgY0HUR3bJOQhEgR-fWgL2qwB1PM472WS_juPcOvBMpEPPPfVgpkfmuiMF-UY7OjMr-g1g0XuUy8H5o5DUGw62dxpN4mCU6nFz_0ZOyaUtamXRu7bA/s790-rw-e365/CISCO.jpg)

Cisco is urging customers to patch two security flaws impacting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software, which it said have been exploited in the wild.

The zero-day vulnerabilities in question are listed below -

* **[CVE-2025-20333](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-webvpn-z5xP8EUB)** (CVSS score: 9.9) - An improper validation of user-supplied input in HTTP(S) requests vulnerability that could allow an authenticated, remote attacker with valid VPN user credentials to execute arbitrary code as root on an affected device by sending crafted HTTP requests
* **[CVE-2025-20362](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-webvpn-YROOTUW)** (CVSS score: 6.5) - An improper validation of user-supplied input in HTTP(S) requests vulnerability that could allow an unauthenticated, remote attacker to access restricted URL endpoints without authentication by sending crafted HTTP requests

Cisco said it's aware of "attempted exploitation" of both vulnerabilities, but did not reveal who may be behind it, or how widespread the attacks are. It's suspected that the two vulnerabilities are being chained to bypass authentication and execute malicious code on susceptible appliances.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It also credited the Australian Signals Directorate, Australian Cyber Security Centre (ACSC), Canadian Centre for Cyber Security, U.K. National Cyber Security Centre (NCSC), and U.S. Cybersecurity and Infrastructure Security Agency (CISA) for supporting the investigation.

### CISA Issues Emergency Directive ED 25-03

In a separate alert, CISA [said](https://www.cisa.gov/news-events/alerts/2025/09/25/cisa-directs-federal-agencies-identify-and-mitigate-potential-compromise-cisco-devices) it's issuing an emergency directive urging federal agencies to identify, analyze, and mitigate potential compromises with immediate effect. In addition, both vulnerabilities have been [added](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) to the Known Exploited Vulnerabilities (KEV) catalog, giving the agencies 24 hours to apply the necessary mitigations.

"CISA is aware of an ongoing exploitation campaign by an advanced threat actor targeting Cisco Adaptive Security Appliances (ASA)," the agency [noted](https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices).

"The campaign is widespread and involves exploiting zero-day vulnerabilities to gain unauthenticated remote code execution on ASAs, as well as manipulating read-only memory (ROM) to persist through reboot and system upgrade. This activity presents a significant risk to victim networks."

The agency also noted that the activity is linked to a threat cluster dubbed [ArcaneDoor](https://thehackernews.com/2024/05/china-linked-hackers-suspected-in.html), which was previously identified as targeting perimeter network devices from several vendors, including Cisco, to deliver malware families like Line Runner and Line Dancer. The activity was attributed to a threat actor codenamed UAT4356 (aka Storm-1849).

"This threat actor has demonstrated a capability to successfully modify ASA ROM at least as early as 2024," CISA added. "These zero-day vulnerabilities in the Cisco ASA platform are also present in specific versions of Cisco Firepower. Firepower appliances' Secure Boot would detect the identified manipulation of the ROM."

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

[CISA](https://thehackernews.com/search/label/CISA)[cisco](https://thehackernews.com/search/label/cisco)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsof...