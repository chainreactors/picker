---
title: Microsoft Reveals ClickFix Campaign Using Windows Terminal to Deploy Lumma Stealer
url: https://thehackernews.com/2026/03/microsoft-reveals-clickfix-campaign.html
source: The Hacker News
date: 2026-03-06
fetch_date: 2026-03-07T03:57:09.340704
---

# Microsoft Reveals ClickFix Campaign Using Windows Terminal to Deploy Lumma Stealer

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Microsoft Reveals ClickFix Campaign Using Windows Terminal to Deploy Lumma Stealer](https://thehackernews.com/2026/03/microsoft-reveals-clickfix-campaign.html)

**Ravie Lakshmanan**Mar 06, 2026Endpoint Security / Browser Security

[![ClickFix Campaign](data:image/png;base64... "ClickFix Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8H7sofZNyrZMv3vcKOeRa7Rw948uDto8VgAXNO8ZKLjUdzhpZW-ub4M_fxuM631fZplWm8BkPK8OifkblZnbNgFKXUB4PoFXXSeg1D0_olC5lAxQ0KtidSFQHlUvxVn1subQyQtI2qbzhChm0Sm3ADLs9C120EfhvLoBtNLbbtrSiyl3AKcss7u-WT-lS/s1700-e365/clickfix.jpg)

Microsoft on Thursday disclosed details of a new widespread [ClickFix](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html) social engineering campaign that has leveraged the [Windows Terminal app](https://en.wikipedia.org/wiki/Windows_Terminal) as a way to activate a sophisticated attack chain and deploy the [Lumma Stealer](https://thehackernews.com/2024/06/beware-fake-browser-updates-deliver.html) malware.

The activity, observed in February 2026, makes use of the terminal emulator program instead of instructing users to launch the Windows Run dialog and paste a command into it.

"This campaign instructs targets to use the Windows + X → I shortcut to launch Windows Terminal (wt.exe) directly, guiding users into a privileged command execution environment that blends into legitimate administrative workflows and appears more trustworthy to users," the Microsoft Threat Intelligence team [said](https://x.com/MsftSecIntel/status/2029692925118992473) in a series of posts on X.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

What makes the latest variant notable is that it bypasses detections specifically designed to flag Run dialog abuse, not to mention take advantage of the legitimacy of Windows Terminal to trick unsuspecting users into running malicious commands delivered via bogus CAPTCHA pages, troubleshooting prompts, or other verification-style lures.

The post-compromise attack chain is also unique: when the user pastes a hex-encoded, XOR-compressed command copied from the ClickFix lure page into a Windows Terminal session, it spans additional Terminal/PowerShell instances to ultimately invoke a PowerShell process responsible for decoding the script.

This, in turn, leads to the download of a ZIP payload and a legitimate but renamed 7-Zip binary, the latter of which is saved to disk with a randomized file name. The utility then proceeds to extract the contents of the ZIP file, triggering a multi-stage attack chain that involves the following steps -

* Retrieving more payloads
* Setting up persistence via scheduled tasks
* Configuring Microsoft Defender exclusions
* Exfiltrating machine and network data
* Deploying Lumma Stealer using a technique called [QueueUserAPC()](https://nyameeeain.medium.com/queueuserapc-process-injection-6f31fcb89410) by injecting the malware into "chrome.exe" and "msedge.exe" processes

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

"The stealer targets high-value browser artifacts, including Web Data and Login Data, harvesting stored credentials and exfiltrating them to attacker-controlled infrastructure," Microsoft said.

The Windows maker said it also detected a second attack pathway, as part of which, when the compressed command is pasted into Windows Terminal, it downloads a randomly named batch script to the "AppData\Local" folder by means of "cmd.exe" in order to write a Visual Basic Script to the Temp folder (aka %TEMP%).

"The batch script is then executed via cmd.exe with the /launched command-line argument. The same batch script is then executed through MSBuild.exe, resulting in LOLBin abuse," it added. "The script connects to Crypto Blockchain RPC endpoints, indicating an etherhiding technique. It also performs QueueUserAPC()-based code injection into chrome.exe and msedge.exe processes to harvest Web Data and Login Data."

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

[browser security](https://thehackernews.com/search/label/browser%20security), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft](https://thehackernews.com/search/label/Microsoft), [powershell](https://thehackernews.com/search/label/powershell), [social engineering](https://thehackernews.com/search/label/social%20engineering), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [windows security](https://thehackernews.com/search/label/windows%20security)

Trending News

[![Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](data:image/svg+xml;base64... "Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies")

Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](https://thehackernews.com/2026/02/researchers-show-copilot-and-grok-can.html)

[![⚡ Weekly Recap: Double-Tap Skimm...