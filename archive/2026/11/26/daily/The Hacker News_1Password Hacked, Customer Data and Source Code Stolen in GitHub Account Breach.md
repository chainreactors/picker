---
title: 1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach
url: https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html
source: The Hacker News
date: 2026-11-26
fetch_date: 2026-11-27T10:17:34.750585
---

# 1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach

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

# [1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach](https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html)

**Ravie Lakshmanan**Nov 26, 2026Data Breach / Password Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbu9vulg5_P2PLmwCbF5nNRu8UujJDFNLLCGackgRWjz4lmkQcAom8TerCouyPh1pF8sgBAiJTwO7qAQN3kLVd-_0e7czxqhyphenhyphenUQuSG6WyCJvoNsI92X7tl1ukE6h8QDLmQBUBJaKBCyTYXjaGMUeaczy-sTIjMvDHdQjphWmWyCsUyIG4Y7WD4J2FoQfgY/s1700-nu-rw-lo-l85-e365/1password.jpg)

Popular password management software 1Password on Wednesday [disclosed](https://1password.com/blog/update-on-nov-2026-security-incident) a security incident involving its backend systems that led to the unauthorized access of some customer information, but emphasized that customer password vaults and other secrets were not accessed.

"While we took immediate steps to contain the incident, the attacker gained access to some of our backend systems and accessed a limited amount of customer account information from a subset of our customers, including names and email addresses," the Toronto-based company said.

It noted that no customer vault content, including secrets, passwords, and other vault items, account recovery keys, or the keys that secure them, was accessed or compromised as a result of the breach. It also stated that customers do not need to take any action, but cautioned them to stay vigilant against unexpected phishing attempts.

As part of its efforts to remediate the incident, 1Password has disabled the affected GitHub account, revoked the stolen token, hardened GitHub, CI/CD, and endpoint controls, restored clean versions of the affected service, and rotated internal credentials. It has also lengthened the codes used in invitation and recovery emails from six digits to ten characters as a precautionary measure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

According to the company, the incident dates back to November 19, 2026, when it began investigating suspicious activity after an unknown threat actor gained access to an employee's corporate GitHub account.

The attacker is said to have weaponized the account to access source code and push malicious code to its backend services, resulting in the download of administrative data related to its customers, including -

* Names
* Email addresses
* Account and user identifiers, such as account creation and last sign-in times
* Public keys
* [Secure Remote Password](https://1password.com/blog/developers-how-we-use-srp-and-you-can-too) protocol parameters
* Tokens present in certain emailed links for invitations, [provisioning](https://support.1password.com/provisioning/), and account recovery
* Non-secret internal metadata about the account, such as version numeric identifiers, file numeric identifiers

1Password also noted that the tokens embedded in the links cannot be used on their own to gain access to customer accounts, as doing so requires either single sign-on (SSO) authentication or a six-digit verification code sent to the user's registered email address. However, it noted that a small number of users were affected and have been individually notified.

"The attacker also copied source code from private repositories and gained access to our CI/CD system," 1Password said. "Our source code is not customer data, and contains no user secrets. There is no impact to 1Password’s services, availability, or product security."

"Your vault secrets are encrypted with keys that only you hold, so we can’t access them, and neither can an attacker who gets into our servers."

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

[CI/CD Security](https://thehackernews.com/search/label/CI/CD%20Security), [data breach](https://thehackernews.com/search/label/data%20breach), [GitHub](https://thehackernews.com/search/label/GitHub), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [Password Managers](https://thehackernews.com/search/label/Password%20Managers), [Software Security](https://thehackernews.com/search/label/Software%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: GPT-6.2 Jailbreak Flaws, BubbleLoader PNG Malware, $500M Ransom Demands ...