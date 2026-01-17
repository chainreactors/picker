---
title: LOTUSLITE Backdoor Targets U.S. Policy Entities Using Venezuela-Themed Spear Phishing
url: https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html
source: The Hacker News
date: 2026-01-16
fetch_date: 2026-01-17T03:28:20.537083
---

# LOTUSLITE Backdoor Targets U.S. Policy Entities Using Venezuela-Themed Spear Phishing

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

# [LOTUSLITE Backdoor Targets U.S. Policy Entities Using Venezuela-Themed Spear Phishing](https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html)

**Jan 16, 2026**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVK3A2yZNeTmDZQnzYo5bTA8R87lnRUIqYSSxOoyKUkAqFH97mjhNJ2LiAT64bsC9ExwqhQnDHhAfs5RJUIUbPGPp5E7h-L3efaT-216BWjYgGsZfZbe46N3BaIR7pxOusAcaJV7a9HHm6RyV3ZAvuz9ECIJPnBnrCuXimEH___3cbJkTefgy8dtfPx9mE/s790-rw-e365/policy-malware.jpg)

Security experts have disclosed details of a new campaign that has targeted U.S. government and policy entities using politically themed lures to deliver a backdoor known as **LOTUSLITE**.

The targeted malware campaign leverages decoys related to the [recent geopolitical developments](https://en.wikipedia.org/wiki/2026_United_States_intervention_in_Venezuela) between the U.S. and Venezuela to distribute a ZIP archive ("US now deciding what's next for Venezuela.zip") containing a malicious DLL that's launched using DLL side-loading techniques. It's not known if the campaign managed to successfully compromise any of the targets.

The activity has been attributed with moderate confidence to a Chinese state-sponsored group known as [Mustang Panda](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html) (aka Earth Pret, HoneyMyte, and Twill Typhoon), citing tactical and infrastructure patterns. It's worth noting that the threat actor is known for extensively relying on DLL side-loading to launch its backdoors, including TONESHELL.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

"This campaign reflects a continued trend of targeted spear phishing using geopolitical lures, favoring reliable execution techniques such as DLL side-loading over exploit-based initial access," Acronis researchers Ilia Dafchev and Subhajeet Singha [said](https://www.acronis.com/en/tru/posts/lotuslite-targeted-espionage-leveraging-geopolitical-themes/) in an analysis.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr9b8nYUTYZUsUwMOlL6I33hshEW0X-HRV4A9Up7LIAT2oNOK2ADd_a5g3to2K5103Ephu_ygD1S8Avmgd3G8ZtQqtTpfep7AslaGSZ70HvS5h13LSPfTDUhefz8JATSYoEe5-qmRZtcfrz47aF2IQDXsAdS6FepY4OpLPDfVonWgswg40QLh7wqQvMzAe/s790-rw-e365/c2.jpg)

The backdoor ("kugou.dll") employed in the attack, LOTUSLITE, is a bespoke C++ implant that's designed to communicate with a hard-coded command-and-control (C2) server using Windows WinHTTP APIs to enable beaconing activity, remote tasking using "cmd.exe," and data exfiltration. The complete list of supported commands is as follows -

* 0x0A, to initiate a remote CMD shell
* 0x0B, to terminate the remote shell
* 0x01, to send commands via the remote shell
* 0x06, to reset beacon state
* 0x03, to enumerate files in a folder
* 0x0D, to create an empty file
* 0x0E, to append data to a file
* 0x0F, to get beacon status

LOTUSLITE is also capable of establishing persistence by making Windows Registry modifications to ensure that it's automatically executed each time the user logs in to the system.

Acronis said the backdoor "mimics the behavioral shenanigans of Claimloader by embedding provocative messages." Claimloader is the name assigned to a DLL that's launched using DLL side-loading and is used to deploy PUBLOAD, another Mustang Panda tool. The malware was [first documented](https://thehackernews.com/2025/06/pubload-and-pubshell-malware-used-in.html) by IBM X-Force in June 2025 in connection with a cyber espionage campaign aimed at the Tibetan community.

"This campaign demonstrates how simple and well-tested techniques can still be effective when paired with targeted delivery and relevant geopolitical lures," the Singaporean cybersecurity company concluded. "Although the LOTUSLITE backdoor lacks advanced evasion features, its use of DLL sideloading, reliable execution flow, and basic command-and-control functionality reflects a focus on operational dependability rather than sophistication."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The disclosure comes as The New York Times [published](https://www.nytimes.com/2026/01/15/us/politics/cyberattack-venezuela-military.html) details about a purported cyber attack undertaken by the U.S. to disrupt electricity for most residents in the capital city of Caracas for a few minutes, before the January 3, 2026, military operation that captured Venezuelan President Nicolás Maduro. The mission

"Turning off the power in Caracas and interfering with radar allowed US military helicopters to move into the country undetected on their mission to capture Nicolás Maduro, the Venezuelan president who has now been brought to the United States to face drug charges," the Times reported.

"The attack caused most of Caracas's residents to lose their power for a few minutes, though some neighborhoods near the military base where Mr. Maduro was captured were left without electricity for up to 36 hours."

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

[Backdoor](https://thehackernews.com/search/label/Backdoor)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Spear Phishing](https://thehackernews.com/search/label/Spear%20Phishing)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worl...