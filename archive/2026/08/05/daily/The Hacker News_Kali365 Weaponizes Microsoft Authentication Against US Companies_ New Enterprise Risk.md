---
title: Kali365 Weaponizes Microsoft Authentication Against US Companies: New Enterprise Risk
url: https://thehackernews.com/2026/08/kali365-weaponizes-microsoft.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:52.228195
---

# Kali365 Weaponizes Microsoft Authentication Against US Companies: New Enterprise Risk

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

# [Kali365 Weaponizes Microsoft Authentication Against US Companies: New Enterprise Risk](https://thehackernews.com/2026/08/kali365-weaponizes-microsoft.html)

**The Hacker News**Aug 05, 2026Phishing / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW4SMtq8o2R4j-NiqM2jQTNNSKABhkghGsH1AkUpqHf7sms7KTAr63IKabEzV2vAfAFO3XxYjh6YH8rDNtNVuu41JePoUdB_WQB-WWtJt4A-FWfmT6rwyzKAL_scAorwzVMt5R_7LZp2qzmUAAKfAodH__3_HLwa-nFV6b6TEng-5Cjviybn07c-ZNKUoU/s1700-e365/main-anyrun.jpg)

Kali365 is turning a legitimate Microsoft login into a gateway to corporate data.

The phishing kit targets US organizations with attacker-controlled device codes that victims approve on Microsoft's real authentication page. Once access and refresh tokens are issued, attackers may retain access to email, documents, and cloud resources, creating a direct path to data exposure, financial fraud, operational disruption, and costly incident response.

## How Kali365 Targets US Organizations

Kali365 is a device code phishing kit built to abuse legitimate Microsoft authentication. ANY.RUN telemetry records more than 80 public sessions linked to the campaign each week, with the United States emerging as its main geographic target.

One of these sandbox sessions shows a SharePoint-themed lure used to draw the victim into the authentication flow.

**[View the analysis session and gather IOCs](https://app.any.run/tasks/d078f430-c3cc-44e8-a809-5506205049c3?utm_source=thehackernews&utm_medium=article&utm_campaign=kali365&utm_content=task&utm_term=050826)**

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBeE0RgIVZOEsXZ2V3RYJ5g66W-vRx41-5lTp6wIofMvV87pbckFAT29b9ZoVYYyYZcMRRv4jGmFSlqrrcogeMumLr3wFBRXRFD1Fn5BcWE4v5We5yHwAzWd87R3nGjY_dxXGgFV8M-jW09WN2BEeZGOrrfOQfz8QizQ16aPDrEoRLPHcZOFpTbEV_VsJf/s1700-e365/11.jpg) |
| SharePoint-themed Kali365 lure analyzed inside ANY.RUN’s Interactive Sandbox |

Based on the research, the attack unfolds in three main stages:

**Lure:** The victim is presented with a page impersonating a trusted business service such as SharePoint, OneDrive, or DocuSign.

**Microsoft authentication:** The page redirects the victim to Microsoft's legitimate device login portal and asks them to enter an attacker-provided code.

**OAuth access:** Once the victim completes authentication, attackers may obtain access and refresh tokens that provide continued access to Microsoft 365 email, documents, and cloud resources.

Reveal the full phishing chain in as little as 60 seconds to reduce response delays and prevent a single compromised account from becoming a wider business incident.

**[Reduce Incident Risk](https://any.run/enterprise/?utm_source=thehackernews&utm_medium=article&utm_campaign=kali365&utm_content=enterprise&utm_term=050826#contact-sales)**

## What Kali365 Can Cost the Business

A single approved device-code request can expand into a wider Microsoft 365 compromise. For US companies, the consequences may include:

* **Financial fraud:** Compromised email accounts can support invoice manipulation, payment fraud, and business email compromise.
* **Sensitive data exposure:** Attackers may access corporate email, internal files, customer information, and confidential documents.
* **Operational disruption:** Unauthorized access to cloud services can interfere with daily communications and business processes.
* **Higher response costs:** Fewer obvious phishing indicators can delay detection and make containment more complex.
* **Compliance and reputational risk:** Exposure of regulated or customer data can trigger reporting obligations and damage trust.

As the victim authenticates on Microsoft's legitimate page, the activity may appear routine at first, giving attackers more time to misuse trusted access before the incident is confirmed.

## Three Priorities for Reducing Kali365 Risk

Kali365 cannot be addressed through email filtering alone. Security leaders need current campaign intelligence, faster validation of suspicious activity, and better preparation for how the threat may evolve.

### 1. Expand Detection with Actionable Phishing Intelligence

Kali365 operators can rotate domains, URLs, and hosting infrastructure as campaigns evolve. Indicators from one confirmed case may quickly become outdated, leaving gaps across the rest of the environment.

Fresh phishing IOCs should reach SIEM, SOAR, TIP, firewalls, and other security controls where they can support alert enrichment, retrospective searches, and blocking decisions. ANY.RUN's [Threat Intelligence Feeds](https://any.run/threat-intelligence-feeds/?utm_source=thehackernews&utm_medium=article&utm_campaign=kali365&utm_content=feeds&utm_term=050826) deliver newly observed indicators through STIX/TAXII, API, and SDK.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrNqFR-DzDdlFcE1Z_wRQ3kU8gpZsrdBwvne0c3RCMcYB_EIC0KqySE07YfECxYN3M1xdWuYNOdmPy9_xFbsAOgQRDGGCaHpj4JgXx1OKaUEtMGWE95byKGW4cqkw8KVl7vzbPkpVJuN8uvJIreo9XTVlVaW_AYi_2wvRTe8k-tQXTHENa4WY2D58y8Eyd/s1700-e365/2.jpg) |
| Get fresh and trustworthy IOCs on emerging threats for deeper investigations |

The intelligence is drawn from sandbox investigations submitted by more than 15,000 organizations and 600,000 security professionals worldwide. Each IOC links back to the session where it appeared, giving defenders the full context needed to verify the threat and identify related Kali365 infrastructure.

### 2. Give Tier 1 the Evidence Needed to Act on Kali365

As victims authenticate on Microsoft's legitimate device login page, Kali365 may look like normal activity at first. The real warning signs often appear earlier, in the lure, redirects, browser behavior, scripts, and attacker-controlled infrastructure.

ANY.RUN's Interactive Sandbox combines hands-on interaction with automated analysis to reveal the full attack chain faster, from the phishing page and redirect paths to network activity and the transition into Microsoft's authentication flow.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb6IC2-HlawFAT6hDkMUdFOHTSnYaTD57nPB056_iYVtkRzGfr5MuN33Rue4MVMU0ftNzKc9he3eB9r9NqtMvwcKoX...