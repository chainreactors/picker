---
title: Operation BlueDash Deploys Level RMM and ScreenConnect via Fake Teams Update
url: https://thehackernews.com/2026/07/operation-bluedash-deploys-level-rmm.html
source: The Hacker News
date: 2026-07-27
fetch_date: 2026-07-28T05:00:16.717947
---

# Operation BlueDash Deploys Level RMM and ScreenConnect via Fake Teams Update

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Operation BlueDash Deploys Level RMM and ScreenConnect via Fake Teams Update](https://thehackernews.com/2026/07/operation-bluedash-deploys-level-rmm.html)

**Ravie Lakshmanan**Jul 27, 2026Malware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQ69OB4Ww_Yj5rfCn7WOwEue0i4sxEuvzaqGj1v71E-W52Q6DDfFRKpesydsd2bD9_QQVghes677fGD0S-PJpJQOz10JYs_NV6wv5peadJtT-dbxFzl7eMqaavlrBl0OfePVtGIm9WvI-rEAAUcDqdFdYcBF6ByDv4iPSCzLZgbuzg0Nb-ASL0uzTb90Ag/s1700-e365/teams-malware.jpg)

Cybersecurity researchers have flagged a Microsoft Teams-themed phishing campaign that employs "secure document" lures to deliver legitimate remote monitoring and management ([RMM](https://redcanary.com/threat-detection-report/trends/rmm-tools/)) tools.

"The victim was directed through compromised web infrastructure to a counterfeit Microsoft Store page claiming that Microsoft Teams had to be updated before the shared document could be opened," ZeroBEC [said](https://zerobec.com/blog/operation-bluedash-multi-rmm-workplace-phishing) in a report published last week. The bogus Teams page in question is "teamvem[.]com."

The active download is used to deliver "supportdev.exe," an Inno Setup-based loader that launches PowerShell in a hidden window, fetches an official Level RMM installer, and registers the endpoint using an attacker-controlled enrollment secret ("LEVEL\_API\_KEY=GxSCHE8EZwfyYN3iPQHPai8D").

The same PowerShell command has been found to download and deploy ConnectWise ScreenConnect in parallel, indicating an attempt to drop multiple RMM tools with an intent to establish persistent remote access.

This is [not the first time](https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html) threat actors have abused RMM tools to their advantage. Earlier this year, Microsoft [warned](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html#signed-phishing-malware) of multiple phishing campaigns that used workplace meeting lures and PDF attachments to distribute signed malware dubbed TrustConnect, which then acted as a conduit for ScreenConnect, along with other RMM programs like Tactical RMM and MeshAgent.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Another campaign [documented](https://zerobec.com/blog/screenconnect-phishing-dkim-spf-dmarc-passed) by ZeroBEC in May 2026 involved the use of phishing emails that purported to share secure documents in order to kick off an attack chain that stealthily dropped RMM backdoors.

The latest set of phishing attacks has been codenamed **Operation BlueDash**, with the email security company attributing it with moderate-to-high confidence to a threat actor group operating from Nigeria based on an analysis of infrastructure, code history, and a GitHub environment used to operate the campaigns.

The deployment of multiple RMM tools on the same host is seen as an attempt to set up redundant access and improve resilience in the event one of the programs is detected and removed from the environment.

Subsequently, the threat actors have been observed attempting to explore the infected host, running commands to determine if it's pending a reboot or whether the system volume was protected, measure active firewall profiles, enumerate members of the local Administrators group, and identify the local Administrators group name.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMGA1s07KKQvuzs60C5fAftQ0B9FWcU5FvDt9JjfjNozVRw2reIYx9phFW-yMIgeD-YH9-sMXd8nzpLnT__lVNbUEb_UPBrelVju0sje-n4X0e-PEE_855xELtDgrtWee1jNpS8lUltFP0AkoFsW1XAaFLJO5_Zm-5hNMl0uygCQLcAYaF05CCaHdg_041/s1700-e365/teams.png)

"This sequence suggests a practical operator checklist: determine system state, understand encryption and firewall posture, and identify privileged local users before deciding how to continue," ZeroBEC said. "It also provides defenders with a behavioral detection opportunity because the commands originate through an unauthorized RMM context rather than an approved IT workflow."

Further analysis of the threat actor infrastructure ("support[.]berrydev[.]xyz") has uncovered a GitHub Pages domain ("berry4603.github[.]io") and a repository named "Bluedashltd" that contains the phishing source, CNAME configuration, and SupportDev payload. The commit history indicates that the campaign has been active since at least February 2026, when the repository was created with the fake Microsoft Store page featuring an "update" for Teams.

What's more, a second repository ("rustovni") tied to the same GitHub account has been found to host a Zoom meeting lure along with its payload-delivery components. The end goal, in this case, is to download the Tactical RMM agent from its official GitHub release, install it in the Windows temporary directory, and register the compromised host with the attacker using an embedded authentication token.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

The Zoom-themed operation also suggests that the threat actors are running a multi-brand scheme that keeps the core intact, while altering the workplace application lure, payload host, and the remote management platform.

The disclosure comes as ZeroBEC detailed JIVS PhishKit, a coordinated mailbox credential-harvesting campaign targeting multiple users within the same organization to deliver a provider-agnostic phishing page that can target Microsoft 365, Google Workspace, cPanel, Roundcube, Zimbra, and other email identities. The earliest artifact related to the effort dates back to August 21, 2025.

"The messages used an authenticated but unrelated external sender, warned that each recipient mailbox...