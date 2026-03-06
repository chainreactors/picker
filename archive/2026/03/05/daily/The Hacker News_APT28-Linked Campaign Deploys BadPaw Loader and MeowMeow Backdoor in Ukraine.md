---
title: APT28-Linked Campaign Deploys BadPaw Loader and MeowMeow Backdoor in Ukraine
url: https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html
source: The Hacker News
date: 2026-03-05
fetch_date: 2026-03-06T04:04:48.488851
---

# APT28-Linked Campaign Deploys BadPaw Loader and MeowMeow Backdoor in Ukraine

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

# [APT28-Linked Campaign Deploys BadPaw Loader and MeowMeow Backdoor in Ukraine](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html)

**Ravie Lakshmanan**Mar 05, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihW1ns0JTT2vYUjdQEqTcDwytBGmTnID9xQkCxuT-WURhd71xeh9UD80hZiRL3WWBOg5dCVZKY2huOuElbB-QjczQquCirdpgVRjWNM426jLNF-U_s8RGs9CjNC1Qr2DJhQ532z6bz2hdMkzUjJ-vSKpJmBdvyy5qgkAuwB2armvVyx4HNsn4glFMWmupC/s1700-e365/Ukraine.jpg)

Cybersecurity researchers have disclosed details of a new Russian cyber campaign that has targeted Ukrainian entities with two previously undocumented malware families named **BadPaw** and **MeowMeow**.

"The attack chain initiates with a phishing email containing a link to a ZIP archive. Once extracted, an initial HTA file displays a lure document written in Ukrainian concerning border crossing appeals to deceive the victim," ClearSky [said](https://www.clearskysec.com/russian-campaign-targeting-ukraine-badpaw-and-meowmeow/) in a report published this week.

In parallel, the attack chain leads to the deployment of a .NET-based loader called BadPaw, which then establishes communication with a remote server to fetch and deploy a sophisticated backdoor called MeowMeow.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The campaign has been attributed with moderate confidence to the Russian state-sponsored threat actor known as [APT28](https://thehackernews.com/2026/03/apt28-tied-to-cve-2026-21513-mshtml-0.html), based on the targeting footprint, the geopolitical nature of the lures used, and overlaps with techniques observed in previous Russian cyber operations.

The starting point of the attack sequence is a phishing email sent from ukr[.]net, likely in an attempt to establish credibility and secure the trust of targeted victims. Present in the message is a link to a purported ZIP file, causing the user to be redirected to a URL that loads an "exceptionally small image," effectively acting as a tracking pixel to signal the operators that the link was clicked.

Once this step is complete, the victim is redirected to a secondary URL from where the archive is downloaded. The ZIP file includes an HTML Application (HTA) that, once launched, drops a decoy document as a distraction mechanism, while it executes follow-on stages in the background.

"The dropped decoy document serves as a social engineering tactic, presenting a confirmation of receipt for a government appeal regarding a Ukrainian border crossing," ClearSky said. "This lure is intended to maintain the veneer of legitimacy."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-P9XUCcbV5wWzU9pKyasYZXvQYB-JEVsj59Sorl0S3rTKRo1aaI9qr9Y4zLAVlnpdmULwcArGhdcb-D4E_fSNKhPrs4JOs-STJytV-6Ls679-HiYfDAbXEmnQSAOztnwL9fgEcKaToUvK0-sxIYYeI-3x7uw-gfS2M5awzGI3RquJJ_VkEh1AaPcWNKFT/s1700-e365/clear.jpg)

The HTA file also carries out checks to avoid running within sandbox environments. It does this by querying the Windows Registry key "KLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\InstallDate" to estimate the "age" of the operating system. The malware is designed to abort execution if the system was installed less than ten days prior.

Should the system meet the environment criteria, the malware locates the downloaded ZIP archive and extracts two files from it – a Visual Basic Script (VBScript) and a PNG image – and saves them to disk under different names. It also creates a scheduled task to execute the VBScript as a way of ensuring persistence on the infected system.

The primary responsibility of the VBScript is to extract malicious code embedded within the PNG image, an obfuscated loader referred to as BadPaw that's capable of contacting a command-and-control (C2) server to download additional components, including an executable named MeowMeow.

"Consistent with the 'BadPaw' tradecraft, if this file is executed independently of the full attack chain, it initiates a dummy code sequence," the Israeli cybersecurity company explained. "This decoy execution displays a graphical user interface (GUI) featuring a picture of a cat, aligning with the visual theme of the initial image file from which the primary malware was extracted."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

"When the 'MeowMeow' button within the decoy GUI is clicked, the application simply displays a 'Meow Meow Meow' message, performing no further malicious actions. This serves as a secondary functional decoy to mislead manual analysis."

The backdoor's malicious code is activated only when it's executed with a certain parameter ("-v") that's provided by the initial infection chain, and after checking that it's running on an actual endpoint as opposed to a sandbox, and no forensic and monitoring tools like Wireshark, Procmon, Ollydbg, and Fiddler are running in the background.

At its core, MeowMeow is equipped to remotely execute PowerShell commands on the compromised host and support file system operations, such as the ability to read, write, and delete data. ClearSky said it identified Russian language strings in the source code, reinforcing the assessment that the activity is the work of a Russian-speaking threat actor.

"The presence of these Russian-language strings suggests two possibilities: the threat actor committed an operational security (OPSEC) error by failing to localize the code for the Ukrainian target environment, or they inadvertently left Russian development artifacts within the code during the malware's production phase," it said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to...