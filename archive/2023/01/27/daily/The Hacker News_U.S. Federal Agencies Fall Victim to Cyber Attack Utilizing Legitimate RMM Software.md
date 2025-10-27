---
title: U.S. Federal Agencies Fall Victim to Cyber Attack Utilizing Legitimate RMM Software
url: https://thehackernews.com/2023/01/us-federal-agencies-fall-victim-to.html
source: The Hacker News
date: 2023-01-27
fetch_date: 2025-10-04T05:01:09.401656
---

# U.S. Federal Agencies Fall Victim to Cyber Attack Utilizing Legitimate RMM Software

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

# [U.S. Federal Agencies Fall Victim to Cyber Attack Utilizing Legitimate RMM Software](https://thehackernews.com/2023/01/us-federal-agencies-fall-victim-to.html)

**Jan 26, 2023**Ravie LakshmananCyber Threat / Phishing

[![Hackers using RMM Software](data:image/png;base64... "Hackers using RMM Software")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWOCl1OSvpVHqIIlbLUZkPv_Ymt8BgGGFmw_UHL3FQBZJ7HSAsPKj_sS8Em3IjU2p7ZPJIu6jiw2tXeKzweUG4OzcUOZy4hU5u-FmSFLTdtouV5FXEf2wuKlqGWrprQenjZnj4A72FH5S39Nflm26igmrnuRAk7KCNHz2TSyYz6Ddef9lND6X8FJ9e/s790-rw-e365/cybercrime.jpg)

At least two federal agencies in the U.S. fell victim to a "widespread cyber campaign" that involved the use of legitimate remote monitoring and management (RMM) software to perpetuate a phishing scam.

"Specifically, cyber criminal actors sent phishing emails that led to the download of legitimate RMM software – ScreenConnect (now ConnectWise Control) and AnyDesk – which the actors used in a refund scam to steal money from victim bank accounts," U.S. cybersecurity authorities [said](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a).

The joint advisory comes from the Cybersecurity and Infrastructure Security Agency (CISA), National Security Agency (NSA), and Multi-State Information Sharing and Analysis Center (MS-ISAC).

The attacks, which took place in mid-June and mid-September 2022, have financial motivations, although threat actors could weaponize the unauthorized access for conducting a wide range of activities, including selling that access to other hacking crews.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Usage of remote software by criminal groups has long been a concern as it offers an [effective](https://thehackernews.com/2022/01/new-zloader-banking-malware-campaign.html) [pathway](https://thehackernews.com/2022/12/telcom-and-bpo-companies-under-attack.html) to establish local user access on a host without the need for elevating privileges or obtaining a foothold by other means.

In one instance, the threat actors sent a phishing email containing a phone number to an employee's government email address, prompting the individual to a malicious domain. The emails, CISA said, are part of help desk-themed social engineering attacks orchestrated by the threat actors since at least June 2022 targeting federal employees.

The subscription-related missives either embed a link to a "first-stage" rogue domain or engage in a tactic known as [callback phishing](https://thehackernews.com/2022/10/bazarcall-callback-phishing-attacks.html) to entice the recipients into calling the actor-controlled phone number to visit the same domain.

Irrespective of the approach used, the malicious domain triggers the download of a binary that then connects to a second-stage domain to retrieve the RMM software in the form of portable executables.

The end goal is to leverage the RMM software to initiate a refund scam. This is achieved by instructing the victims to login to their bank accounts, after which the actors modify the bank account summary to make it appear as though the individual was mistakenly refunded an excess amount of money.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In the final step, the scam operators urge the email recipients to refund the additional amount, effectively defrauding them of their funds.

CISA attributed the activity to a "large trojan operation" [disclosed](https://www.silentpush.com/blog/silent-push-uncovers-a-large-phishing-operation-featuring-amazon-geek-squad-mcafee-microsoft-norton-and-paypal-domains) by cybersecurity firm Silent Push in October 2022. That said, similar telephone-oriented attack delivery methods have been adopted by other actors, including [Luna Moth](https://thehackernews.com/2022/11/luna-moth-gang-invests-in-call-centers.html) (aka Silent Ransom).

Patrick Beggs, chief information security officer at ConnectWise, said in an email statement that "software products intended for good use, including remote control tools, can be frequently used by bad actors for malicious purposes," and that "when alerted of this behavior, ConnectWise regularly issues take-down requests to remove malicious sites and domains."

"This campaign highlights the threat of malicious cyber activity associated with legitimate RMM software: after gaining access to the target network via phishing or other techniques, malicious cyber actors — from cybercriminals to nation-state sponsored APTs — are known to use legitimate RMM software as a backdoor for persistence and/or command and control (C2)," the agencies warned.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[RMM Software](https://thehackernews.com/search/label/RMM%20Software)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Ex...