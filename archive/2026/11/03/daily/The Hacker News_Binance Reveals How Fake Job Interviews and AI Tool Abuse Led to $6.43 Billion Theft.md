---
title: Binance Reveals How Fake Job Interviews and AI Tool Abuse Led to $6.43 Billion Theft
url: https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html
source: The Hacker News
date: 2026-11-03
fetch_date: 2026-11-04T08:19:20.058860
---

# Binance Reveals How Fake Job Interviews and AI Tool Abuse Led to $6.43 Billion Theft

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Binance Reveals How Fake Job Interviews and AI Tool Abuse Led to $6.43 Billion Theft](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html)

**Ravie Lakshmanan**Nov 03, 2026Cryptocurrency / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZCMCR8h3YCPcfY8Fbe54ckYKh_YUt_Yd7v82dAHobZtMNlQl_JVKWUX4OUPwR0dEmYsLNfeKsW6rUthk8pYRVhIddbPXx86sHCcNBRL9E-9LJTPrYSYwJ_V66EwGJNFeoWgDPbjcGfeJ4w2qn_gfTjXBoNAnfWq4GZ8rq7VOhnqt4QlItYEBr3Zar7XL1/s1700-nu-rw-lo-l85-e365/bin.jpg)

Binance on Tuesday said the [record-setting theft of $6.43 billion in assets](https://thehackernews.com/2026/11/fbi-links-north-koreas-tradertraitor-to.html) from the world's largest cryptocurrency exchange was the culmination of a "sophisticated, multi-stage campaign" that involved the use of a tampered Homebrew installation and recruitment-themed social engineering attack targeting two of its engineers.

"It was not a single isolated breach or a simple phishing incident," the company [said](https://x.com/binance/status/2117626126214504729). "The attackers combined a range of techniques, including social engineering by fake recruitment interviews, malicious software downloads, compromised internal AI tooling, endpoint compromise, and an advanced transaction-authorisation method."

The starting point has been traced back to a supply chain attack targeting one of its engineers from the Wallet DevOps team (named "Engineer A"), who [downloaded](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) a [trojanized Homebrew installer](https://isc.sans.edu/diary/32942) to install a popular artificial intelligence (AI) tool after searching for it on a search engine. The incident occurred in June 2026.

Although Binance said it detected the attack and rotated all related credentials as a precautionary step, the company said information about "Engineer A's role and his related colleagues on our wallet infrastructure team was exposed to the hacker."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The second part of the attack occurred in September 2026, with the threat actor contacting another engineer (named "Engineer B") via a legitimate job-hunting platform by disguising themselves as a Project Director.

The Project Director persona arranged a first-round interview with a human resources (HR) representative, which was then followed by a second-round interview with an individual claiming to be the CEO of a non-existent company. Binance did not disclose details of the fake company.

Over the course of the first-round video interview, the HR representative shared a social media account, including personal photos and videos posted on the platform, in an attempt to build credibility and establish trust. The second round, on the other hand, took place on a popular social chat app.

"Near the end of the interview, Engineer B was instructed to download an 'assignment' containing a malicious code repository onto his work computer," Binance said. "The repository contained malicious code that executed during the setup process, initiating a series of unauthorized activities."

The undetected malware utilized advanced obfuscation and evasion techniques, including substituting a legitimate development tool component with a poisoned version to execute commands and establish communication with an attacker-controlled external server. In addition, the threat actor took steps to cover up tracks by removing forensic artifacts related to the compromise.

The intrusion moved to the next stage on October 20, 2026, when the adversary leveraged Engineer B's compromised computer and abused an internal AI tool to gain control over Engineer A and another Wallet Software Engineer C.

"The attacker soon discovered Wallet DevOps Engineer A had a container deployment permission token on his computer," Binance explained. "On 29 October between 17:15 and 19:56, the attacker logged onto Software Engineer C's computer, used the credentials stolen from Wallet DevOps Engineer A, deployed a container, and triggered a malicious script to launch the attack."

The attack ultimately exploited its unauthorized access to an internal wallet signing service to initiate transactions outside the normal withdrawal process.

In response to the incident, Binance has reconstructed the affected wallet system in a new environment, as well as rebuilt the internal AI tool and access controls. Other steps taken as of November 3 are listed below -

* Replaced affected devices.
* Decommissioned credentials and tokens related to affected engineers.
* Completed enhanced security scans across all employee devices.
* Enhanced AI-based behavioural anomaly detection.
* Strengthened wallet-service risk controls.
* Worked with law enforcement, blockchain intelligence firms, and industry partners to trace and freeze affected assets.

"The entry points identified as having been used in the attack have been closed. Systems touched in the attack path have been rebuilt or replaced," Binance said. "We have also implemented tighter device controls, enhanced wallet-service risk controls and expanded AI-based behavioural anomaly detection."

"We are increasing investment in AI-enabled detection, endpoint protection, developer-environment security and behavioural anomaly monitoring."

Since the start of the year, Binance is estimated to have foiled 57 suspected North Korea-linked cyber threat cases, underscoring the persistent nature of the attacks targeting the cryptocurrency industry.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"The techniques include fraudulent job interviews, malicious software disguised as popular developer tools, compromised software packages and browser extensions, fake video conferencing applications, and social engineering campaigns designed to steal credentials or deploy remote access malware," Bina...