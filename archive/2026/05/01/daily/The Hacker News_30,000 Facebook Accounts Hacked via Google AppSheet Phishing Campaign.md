---
title: 30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign
url: https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html
source: The Hacker News
date: 2026-05-01
fetch_date: 2026-05-02T05:00:27.610156
---

# 30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html)

**Ravie Lakshmanan**May 01, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilUS_xmTpvaJtwhFTnxsBtKSx2hWroMJKWUCKeB_CNx_9-5T85bdpqGfTZ0__XITi-i6ZnndaiiiFggf3Cgf-35KK-G6sEwvnlqom2DK6U-oH_o9GhEGNyd9kiSti-QC_dpl3v7b7IniC9kAUzV265yVbVsWAnLnH1RfQxrftUHj5MFAm03MOBw3Z6UEVb/s1700-e365/phish.jpg)

A newly discovered Vietnamese-linked operation has been observed using a Google AppSheet as a "phishing relay" to distribute phishing emails with an aim to compromise Facebook accounts.

The activity has been codenamed **AccountDumpling** by Guardio, with the scheme selling the stolen accounts back through an illicit storefront run by the threat actors. In all, roughly 30,000 Facebook accounts are estimated to have been hacked as part of the campaign.

"What we found wasn't a single phishing kit," security researcher Shaked Chen [wrote](https://guard.io/labs/accountdumpling---hunting-down-the-google-sent-phishing-wave-compromising-30-000-facebook-accounts) in a report shared with The Hacker News. "It was a living operation with real-time operator panels, advanced evasion, continuous evolution and a criminal-commercial loop that quietly feeds on the same accounts it helps steal back."

The findings are just the latest example of how [Vietnamese threat actors](https://thehackernews.com/2025/05/fake-kling-ai-facebook-ads-deliver-rat.html) continue to [embrace various tactics](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html) to gain unauthorized access to victims' Facebook accounts, which are then sold on underground ecosystems for monetary gain.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The starting point of the latest attacks is a phishing email targeting Facebook Business account owners, claiming to be from Meta Support and urging them to submit an appeal, or risk getting their account permanently deleted. The emails are sent from a Google AppSheet address ("noreply@appsheet.com"), allowing them to bypass spam filters.

This false sense of urgency is used to direct users to a fake web page designed to harvest their credentials. It's worth noting that a [similar campaign](https://thehackernews.com/2025/05/cybercriminals-clone-antivirus-site-to_4.html) was reported by KnowBe4 in May 2025.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXlG7ak9Xg9LnGZSFyN7pVQlOnvheYwL-HaPupZ2tf8_2c05HAz5GAy2dqkCt_x8X7ZuR39kc23-A-9QT4cMggVM9iEka1g8WXpZstOvNdukI0RlCU9HD62VO4kMcju6d60jSHKX8f0BvxMaGU8BwUCY_9L7WFfqWbNM1l7cJWiSwjGP101LCKnIBKQPW4/s1700-e365/appsheet.png)

Over the past few weeks, these campaigns have adopted various kinds of lures designed to induce a "Meta-related panic." These range from account disablement and copyright complaints to verification review, executive recruitment, and Facebook login alerts. The four main clusters identified by Guardio are listed below -

* Netlify-hosted Facebook help center pages that enable account takeover attacks, in addition to collecting dates of birth, phone numbers, and government-issued ID photos. The data is ultimately forwarded to an attacker-controlled Telegram channel.
* Blue badge evaluation lures that guide victims to Vercel-hosted "Security Check" or "Meta | Privacy Center" pages that are gated by a bogus CAPTCHA check before directing users to the phishing landing page to collect contact details, business information, credentials (after a forced retry), and two-factor authentication (2FA) codes and exfiltrate them to a Telegram channel.
* Google Drive-hosted PDFs masquerading as instructions to complete account verification to direct users to collect passwords, 2FA codes, government ID photos, and browser screenshots through html2canvas. The PDF documents are generated using a free Canva account.
* Fake job offers that impersonate companies like WhatsApp, Meta, Adobe, Pinterest, Apple, and Coca-Cola to build rapport with the recipients and ask them to join a call or continue the discussion on attacker-controlled sites.

Cumulatively, the Telegram channels associated with the first three clusters have been found to hold about 30,000 victim records, most of whom are located in the U.S., Italy, Canada, the Philippines, India, Spain, Australia, the U.K., Brazil, and Mexico, and have been locked out of their own accounts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

As for who is behind the operation, the smoking gun evidence has come from the PDFs generated as part of the third cluster using the free Canva account, with metadata listing a Vietnamese name "PHẠM TÀI TÂN" as the files' author. Further open-source intelligence has led to the discovery of a website ("phamtaitan[.]vn"), where they offer digital marketing services.

In a post shared on X in February 2023, the website's handle [said](https://x.com/phamtaitanvn/status/1623563864456720384) it "specializes in providing digital marketing services, marketing resources, and consulting on effective digital marketing strategies."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeR52KyZ-mtBJe1c8lFdjIe3BLKL_BYr42ksQ-hOoHWhDVgbu_MPRnmpSC97YLC702a_LSzKrWd-Q3eLnClm2D4i8GL7g3UI-LTvdxFT5OMNEhH4Mac0G9v07Swjj-W6Wy9QNxE-8wJQa-4gPtSKrvXOkPVCvRGJktP7g43RYOy0Swbfe-GeDe7jT3Bbfv/s1700-e365/telegram.png)

"Taken together, they form a consistent picture of a large, Vietnamese-based, mega operation," Chen said. "This campaign is bigger than a single AppSheet abuse. It's a window into the dark market around stolen Facebook assets, where access, business identity, ad reputation, and even account recovery have all become tradable commodities. Another entry in the pattern we keep surfacing: trusted platforms ...