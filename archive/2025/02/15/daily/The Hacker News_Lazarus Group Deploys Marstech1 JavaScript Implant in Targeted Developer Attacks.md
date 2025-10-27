---
title: Lazarus Group Deploys Marstech1 JavaScript Implant in Targeted Developer Attacks
url: https://thehackernews.com/2025/02/lazarus-group-deploys-marstech1.html
source: The Hacker News
date: 2025-02-15
fetch_date: 2025-10-06T20:57:41.989957
---

# Lazarus Group Deploys Marstech1 JavaScript Implant in Targeted Developer Attacks

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

# [Lazarus Group Deploys Marstech1 JavaScript Implant in Targeted Developer Attacks](https://thehackernews.com/2025/02/lazarus-group-deploys-marstech1.html)

**Feb 14, 2025**Ravie LakshmananBrowser Security / Cryptocurrency

[![JavaScript Implant](data:image/png;base64... "JavaScript Implant")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMV_7QDoHZosCoqKrd-ZpwL-uuHBvtNaNRyayal8neUbOqPGjmJ-ir41EfosP81EsF9S1PPUJSbfX5y1VjoQTZbhefTYAInoGRP2aA_hD7AAoLq2LvBqVU-r28KMju3U93Xv9IudpWFWMem6HZbdMK_ivX0ZWWwFBZj9LxInorWMGwmPRVRbP3R7F7eHGI/s790-rw-e365/dev-hacking.png)

The North Korean threat actor known as the [Lazarus Group](https://thehackernews.com/2025/01/lazarus-group-targets-web3-developers.html) has been linked to a previously undocumented JavaScript implant named Marstech1 as part of limited targeted attacks against developers.

The active operation has been dubbed Marstech Mayhem by SecurityScorecard, with the malware delivered by means of an open-source repository hosted on GitHub that's associated with a profile named "SuccessFriend." The profile, active since July 2024, is no longer accessible on the code hosting platform.

The implant is designed to collect system information, and can be embedded within websites and NPM packages, posing a supply chain risk. Evidence shows that the malware first emerged in late December 2024. The attack has amassed 233 confirmed victims across the U.S., Europe, and Asia.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The profile mentioned web dev skills and learning blockchain which is in alignment to the interests of Lazarus," SecurityScorecard [said](https://securityscorecard.com/wp-content/uploads/2025/02/Operation-Marstech-Mayhem-Report_021025_03.pdf). "The threat actor was committing both pre-obfuscated and obfuscated payloads to various GitHub repositories."

In an interesting twist, the implant present in the GitHub repository has been found to be different from the version served directly from the command-and-control (C2) server at 74.119.194[.]129:3000/j/marstech1, indicating that it may be under active development.

Its chief responsibility is to search across Chromium-based browser directories in various operating systems and alter extension-related settings, particularly those related to the MetaMask cryptocurrency wallet. It's also capable of downloading additional payloads from the same server on port 3001.

Some of the other wallets targeted by the malware include Exodus and Atomic on Windows, Linux, and macOS. The captured data is then exfiltrated to the C2 endpoint "74.119.194[.]129:3000/uploads."

Ryan Sherstobitoff, senior vice president of Threat Research and Intelligence at SecurityScorecard, told The Hacker News that the malicious JavaScript file was also implanted in select NPM packages that were part of cryptocurrency projects.

"The introduction of the Marstech1 implant, with its layered obfuscation techniques — from control flow flattening and dynamic variable renaming in JavaScript to multi-stage XOR decryption in Python — underscores the threat actor's sophisticated approach to evading both static and dynamic analysis," the company said.

The disclosure comes as Recorded Future revealed that at least three organizations in the broader cryptocurrency space, a market-making company, an online casino, and a software development company, were targeted as part of the [Contagious Interview](https://thehackernews.com/2025/02/north-korean-hackers-deploy-ferret.html) campaign between October and November 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The cybersecurity firm is tracking the cluster under the name PurpleBravo, stating the [North Korean IT workers](https://cloud.google.com/blog/topics/threat-intelligence/cybercrime-multifaceted-national-security-threat) behind the [fraudulent employment scheme](https://thehackernews.com/2025/02/north-korean-hackers-exploit-powershell.html) are also behind the cyber espionage threat. The threat activity is also referred to as CL-STA-0240, Famous Chollima, and Tenacious Pungsan.

"Organizations that unknowingly hire North Korean IT workers may be in violation of international sanctions, exposing themselves to legal and financial repercussions," the company [said](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat). "More critically, these workers almost certainly act as insider threats, stealing proprietary information, introducing backdoors, or facilitating larger cyber operations."

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

[browser security](https://thehackernews.com/search/label/browser%20security)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub](https://thehackernews.com/search/label/GitHub)[JavaScript](https://thehackernews.com/search/label/JavaScript)[lazarus group](https://thehackernews.com/search/label/lazarus%20group)[Malware](https://thehackernews.com/search/label/Malware)[North Korea](https://thehackernews.com/search/label/North%20Korea)[supply chain attack](https://theh...