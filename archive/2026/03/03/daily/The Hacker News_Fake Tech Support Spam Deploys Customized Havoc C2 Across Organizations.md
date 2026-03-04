---
title: Fake Tech Support Spam Deploys Customized Havoc C2 Across Organizations
url: https://thehackernews.com/2026/03/fake-tech-support-spam-deploys.html
source: The Hacker News
date: 2026-03-03
fetch_date: 2026-03-04T04:04:34.444187
---

# Fake Tech Support Spam Deploys Customized Havoc C2 Across Organizations

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

# [Fake Tech Support Spam Deploys Customized Havoc C2 Across Organizations](https://thehackernews.com/2026/03/fake-tech-support-spam-deploys.html)

**Ravie Lakshmanan**Mar 03, 2026Endpoint Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMxXTslXwVQy4UDmwQOi39oPLz0gBjk3E_mUL0hONp_uAbe2mkCooBcTU3zE6nArVycOldRPm5jMHfzTAI_plrX1jvn5o8zmSGKTH794N2tpztPyTLW-TBZqfHaa4nbHLMY2LHhW0l1J4wzmg8lCRXOFWdAQSSn1Qb4iR8PIeRUE9K1NvpCtluT69-y7By/s1700-e365/outlook.jpg)

Threat hunters have called attention to a new campaign as part of which bad actors masqueraded as fake IT support to deliver the [Havoc](https://github.com/HavocFramework/Havoc) command-and-control (C2) framework as a precursor to data exfiltration or ransomware attack.

The intrusions, [identified](https://www.huntress.com/blog/fake-tech-support-havoc-command-control) by Huntress last month across five partner organizations, involved the threat actors using email spam as lures, followed by a phone call from an IT desk that activates a layered malware delivery pipeline.

"In one organization, the adversary moved from initial access to nine additional endpoints over the course of eleven hours, deploying a mix of custom [Havoc Demon](https://attack.mitre.org/software/S1229/) payloads and legitimate RMM tools for persistence, with the speed of lateral movement strongly suggesting the end goal was data exfiltration, ransomware, or both," researchers Michael Tigges, Anna Pham, and Bryan Masters said.

It's worth noting that the modus operandi is consistent with email bombing and Microsoft Teams phishing attacks [orchestrated](https://thehackernews.com/2025/01/qakbot-linked-bc-malware-adds-enhanced.html) by [threat actors](https://thehackernews.com/2025/06/former-black-basta-members-use.html) associated with the Black Basta ransomware operation in the past. While the cybercrime group appears to have gone silent following a public leak of its internal chat logs last year, the continued presence of the group's playbook suggests two possible scenarios.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

One possibility is that former Black Basta affiliates have moved on to other ransomware operations and are using them to mount fresh attacks, or two, rival threat actors have adopted the same strategy to conduct social engineering and obtain initial access.

The attack chain begins with a spam campaign aiming to overwhelm a target's inboxes with junk emails. In the next step, the threat actors, masquerading as IT support, contact the recipients and trick them into granting remote access to their machines either via a Quick Assist session or by installing tools like AnyDesk to help remediate the problem.

With the access in place, the adversary wastes no time launching the web browser and navigating to a fake landing page hosted on Amazon Web Services (AWS) that impersonates Microsoft and instructs the victim to enter their email address to access Outlook's anti-spam rules update system and update the spam rules.

Clicking a button to "Update rules configuration" on the counterfeit page triggers the execution of a script that displays an overlay asking the user to enter their password.

"This mechanism serves two purposes: it allows the threat actor (TA) to harvest credentials, which, when combined with the required email address, provides access to the control panel; concurrently, it adds a layer of authenticity to the interaction, convincing the user the process is genuine," Huntress said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEii4Lib-wKbh4pAovQsn5oiBbzv2fPcZbMECZ03FDMU0cFMzd5BNvg-qFAmq8OrTFYJ8f3_khRg9aqLAcM5zOqiA8xzrmUTzvFrjnfcJQ_-NfgYvZCJl146UiHI4FONhE2zrMfOtmEm-8P3P1VRbh-pcegdvLp3LtXjhODwoNBeOq4A_4WS_RhQ0Cv2APDN/s1700-e365/anti.jpg)

The attack also hinges on downloading the supposed anti-spam patch, which, in turn, leads to the execution of a legitimate binary named "ADNotificationManager.exe" (or "DLPUserAgent.exe" and "Werfault.exe") to sideload a malicious DLL. The DLL payload implements defense evasion and executes the Havoc shellcode payload by spawning a thread containing the Demon agent.

At least one of the identified DLLs ("vcruntime140\_1.dll") incorporates additional tricks to sidestep detection by security software using control flow obfuscation, timing-based delay loops, and techniques like [Hell's Gate](https://thehackernews.com/2025/04/lazarus-hits-6-south-korean-firms-via.html) and [Halo's Gate](https://blog.sektor7.net/#!res/2021/halosgate.md) to [hook](https://malwaretech.com/2023/12/an-introduction-to-bypassing-user-mode-edr-hooks.html) [ntdll.dll functions](https://0xmaz.me/posts/HookChain-A-Deep-Dive-into-Advanced-EDR-Bypass-Techniques/) and bypass endpoint detection and response (EDR) solutions.

"Following the successful deployment of the Havoc Demon on the beachhead host, the threat actors began lateral movement across the victim environment," the researchers said. "While the initial social engineering and malware delivery demonstrated some interesting techniques, the hands-on-keyboard activity that followed was comparatively straightforward."

This includes creating scheduled tasks to launch the Havoc Demon payload every time the infected endpoints are rebooted, providing the threat actors with persistent remote access. That said, the threat actor has been found to deploy legitimate remote monitoring and management (RMM) tools like Level RMM and XEOX on some compromised hosts instead of Havoc, thus diversifying their persistence mechanisms.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

Some important takeaways from these attacks are that threat actors are more than happy to impersonate IT staff and call personal phone numbers if it improves the success rate, techniques like defense evasion that were once lim...