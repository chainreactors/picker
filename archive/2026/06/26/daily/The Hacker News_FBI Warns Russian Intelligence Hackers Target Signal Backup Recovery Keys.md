---
title: FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys
url: https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html
source: The Hacker News
date: 2026-06-26
fetch_date: 2026-06-27T05:52:30.252152
---

# FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys](https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html)

**Swati Khandelwal**Jun 26, 2026Secure Messaging / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjt2-y25_EiB31BmVQQpt9ne8mH9iPOJpYJmItVSIKGexUBmKRwzNSvDYzbVyRm9xxR6H0rE880CTv3QTblUdJgkRh2EoXqYGJ9wwOq-cOktE6iIvI0fZdeuxf8gTmdEpStuzq5CywuWYEjb32JqfwIznRc6YtDK_V5dFH1bcx2EoqvQ1Koieo4g7QDKA/s1700-e365/signal-phishing.jpg)

The FBI and CISA have updated [their March warning](https://thehackernews.com/2026/03/fbi-warns-russian-hackers-target-signal.html) about Russian intelligence phishing Signal accounts, and the operators have added a step: they now coax targets into handing over their Signal Backup Recovery Key.

Hand it over once, and the attacker can restore the account's backup, read the private and group message history, and take over the account. Worse, the key keeps working. Make a new account on the same phone number, and the old key can still be used against it, the advisory warns.

The fix is blunt: generate a new key in Settings, which kills the old one for future backup downloads, and accept that anything the attacker already pulled is gone.

The updated advisory, [PSA I-062626-PSA](https://www.ic3.gov/PSA/2026/PSA260626), adds two public tracking names the [March notice](https://www.ic3.gov/PSA/2026/PSA260320) lacked: UNC5792 and UNC4221. The FBI ties the activity to multiple Russian Intelligence Services (RIS) groups, including FSB officers embedded with the FSB Border Guards and others working for the Russian military services. The campaign hits Signal and WhatsApp accounts; the new recovery-key tactic the advisory describes is specific to Signal.

The targets are individuals of high intelligence value: current and former U.S. and international government officials, military personnel, political figures, journalists, and officials in Ukraine. The March notice said the broader campaign had already compromised thousands of accounts worldwide.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The phishing message poses as Signal support. Earlier waves asked for SMS verification codes and account PINs, or used doctored "group invite" links that silently [linked an attacker's device](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html) to the account.

The updated version walks the target through turning on Signal backups, opening the Recovery Key, and pasting it into the chat. The advisory prints two sample messages: one dressed up as a mandatory two-factor rollout, the other as an urgent "data recovery" fix for messages supposedly at risk of loss.

As in March, the agencies are clear that none of these breaks Signal's encryption or the app itself. The actors compromise individual accounts through social engineering, then walk in through a legitimate feature.

Alongside the update, the State Department's [Rewards for Justice](https://rewardsforjustice.net/rewards/unc5792/) program is offering up to $10 million for information on UNC5792.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUdTUbUhtHeDSpxPbDadxuhu_ioOHZ6D9yC9MJ7QbkdOBmwkPQ7znYyJzGwiO2qb9Jn1syftuWfAEXtwR_y4bthmtdYKKFytJ6WwukICUMJ5FJFtmAwX_TUyLKOAYjwxYhf9k21c2QTWdolpu0Jk62ZMGcBK3m9EEV3YEHr_V6B61XxaeMlJ-DzKx1qy8/s1700-e365/reward.jpg)

The activity overlaps with warnings from Dutch intelligence (AIVD and MIVD), [Germany's BfV and BSI](https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html), and France's ANSSI earlier this year. Google's Threat Intelligence Group [first documented](https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger/) UNC5792 abusing Signal's linked-device feature in early 2025, and saw the same tradecraft turn up against WhatsApp and Telegram.

## What to do now

* Treat any in-app message from "Signal support" as hostile. Real support does not message you inside the app to ask for codes, PINs, or your Recovery Key.
* Never paste your Backup Recovery Key, verification code, or PIN into a chat. Nothing legitimate asks for them that way.
* Open Settings, check Linked Devices, and remove anything you do not recognize.
* If you think you handed over your Recovery Key, generate a new one in Settings now, and assume any backup made before that is already in someone else's hands.

The March notice warned the tactics would shift. They have, from chasing one-time codes to taking the key that opens the entire archive. The encryption holds. The account is the weak point, and the person holding it is the target.

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

[CISA](https://thehackernews.com/search/label/CISA), [FBI](https://thehackernews.com/search/label/FBI), [Phishing](https://thehackernews.com/search/label/Phishing), [Russian Intelligence](https://thehackernews.com/search/label/Russian%20Intelligence), [Secure Messaging](https://thehackernews.com/search/label/Secure%20Messaging), [Signal](https://thehackernews.com/search/label/Signal), [Social En...