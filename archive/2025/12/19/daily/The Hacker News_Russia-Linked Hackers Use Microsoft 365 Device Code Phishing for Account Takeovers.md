---
title: Russia-Linked Hackers Use Microsoft 365 Device Code Phishing for Account Takeovers
url: https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html
source: The Hacker News
date: 2025-12-19
fetch_date: 2025-12-20T03:15:36.795136
---

# Russia-Linked Hackers Use Microsoft 365 Device Code Phishing for Account Takeovers

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Russia-Linked Hackers Use Microsoft 365 Device Code Phishing for Account Takeovers](https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html)

**Dec 19, 2025**Ravie LakshmananCybersecurity / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6rG0It4YgDaraGdYMUeGqu11YGd_aORJs3sbrIhK3Xe1FaMag0ELM5dA_B5eSsPxFKWOd0HKBV1GzjQBUlS6sEundoKDqXUawbWkJgEg8GHlpSxDa2XE96vxccNI6Zi3OqxCKZL33azUFgZXsL3mHyORT0fd-BS0hnpsg9xNvJCCrvb9gUHEVKnzmiKej/s790-rw-e365/ms.jpg)

A suspected Russia-aligned group has been attributed to a phishing campaign that employs device code authentication workflows to steal victims' Microsoft 365 credentials and conduct account takeover attacks.

The activity, ongoing since September 2025, is being tracked by Proofpoint under the moniker **UNK\_AcademicFlare**.

The attacks involve using compromised email addresses belonging to government and military organizations to strike entities within government, think tanks, higher education, and transportation sectors in the U.S. and Europe.

"Typically, these compromised email addresses are used to conduct benign outreach and rapport building related to the targets' area of expertise to ultimately arrange a fictitious meeting or interview," the enterprise security company [said](https://www.proofpoint.com/us/blog/threat-insight/access-granted-phishing-device-code-authorization-account-takeover).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/windows-stealer-alert-d)

As part of these efforts, the adversary claims to share a link to a document that includes questions or topics for the email recipient to review before the meeting. The URL points to a Cloudflare Worker URL that mimics the compromised sender's Microsoft OneDrive account and instructs the victim to copy the provided code and click "Next" to access the supposed document.

However, doing so redirects the user to the legitimate Microsoft device code login URL, where, once the previously provided code is entered, it causes the service to generate an access token that can then be recovered by the three actors to take control of the victim account.

Device code phishing was [documented](https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html) in detail by both Microsoft and Volexity in February 2025, attributing the use of the attack method to Russia-aligned clusters such as Storm-2372, APT29, UTA0304, and UTA0307. Over the past couple of months, [Amazon Threat Intelligence](https://thehackernews.com/2025/08/amazon-disrupts-apt29-watering-hole.html) and [Volexity](https://thehackernews.com/2025/12/weekly-recap-usb-malware-react2shell.html#:~:text=Russian%20Hackers%20Spoof%20European%20Security%20Events%20in%20Phishing%20Wave) have warned of continued attacks mounted by Russian threat actors by abusing the device code authentication flow.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3ksFzCclpNXE7TC1hecey1H_ROtICx_GB4rEGzty4Jp5XuD_k7YyHJVB-6XBHJJuLCRsBzseDOjR6-EJzmr18yH2SF1wO1BgiA_1c4w_AMxkhSQUQZpgh9AqRGbPiqqgBtxaCHimzAw6Y7bg329-QilXsZhBwlQXcDrqsx35aoabqB1O-xAHRZKpUA0ld/s2600/corp.png)

Proofpoint said UNK\_AcademicFlare is likely a Russia-aligned threat actor given its targeting of Russia-focused specialists at multiple think tanks and Ukrainian government and energy sector organizations.

Data from the company shows that multiple threat actors, both state-aligned and financially-motivated, have latched onto the phishing tactic to deceive users into giving them access to Microsoft 365 accounts. This includes an e-crime group named TA2723 that has used salary-related lures in phishing emails to direct users to fake landing pages and trigger device code authorization.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The October 2025 campaign is assessed to have been fueled by the ready availability of crimeware offerings like the Graphish phishing kit and red-team tools such as [SquarePhish](https://github.com/secureworks/SquarePhish).

"Similar to SquarePhish, the tool is designed to be user-friendly and does not require advanced technical expertise, lowering the barrier for entry and enabling even low-skilled threat actors to conduct sophisticated phishing campaigns," Proofpoint said. "The ultimate objective is unauthorized access to sensitive personal or organizational data, which can be exploited for credential theft, account takeover, and further compromise."

To counter the risk posed by device code phishing, the best option is to create a Conditional Access policy using the Authentication Flows condition to block device code flow for all users. If that's not feasible, it's advised to use a policy that uses an allow-list approach to allow device code authentication for approved users, operating systems, or IP ranges.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[email security](https://thehackernews.com/search/label/email%20security)[Identity Security](https://thehackernews.com/search/...