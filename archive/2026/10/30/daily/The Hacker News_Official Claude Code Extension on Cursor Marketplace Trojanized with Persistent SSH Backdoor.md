---
title: Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor
url: https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html
source: The Hacker News
date: 2026-10-30
fetch_date: 2026-10-31T07:49:07.166714
---

# Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)

**Ravie Lakshmanan**Oct 30, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMAV00lkxu7R724ItLdgrRsnEYHR_d2eUSdcen_KymGeBY1tCo8SRVz6w_XiNzzYgwpcl0Me3JCJz8DeieRM_0jb8aL4VkHAAIeXrqNf8oQkmzKahqMHOGvhkFK32HOasHZht8BwtI1NxEZ-_nIwmQY_8fxpGbbl3csC6oZKCVnIRk3iYTRhH975dyxsWS/s1700-nu-rw-lo-l85-e365/cursor-vscode.jpg)

Cybersecurity researchers have [disclosed](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor) that a trojanized version of Anthropic's official Claude Code extension was distributed through the Cursor Marketplace as a legitimate update, attempting to install a persistent SSH backdoor on affected systems.

The malicious update, version 2.1.313, was distributed under the extension's legitimate publisher identity, prompting Cursor to temporarily shut down its marketplace to remove the compromised package. The exact method attackers used to introduce the unauthorized update remains unclear.

"We identified a security incident affecting a modified Claude Code VS Code extension accessed through our Cursor IDE extension marketplace, impacting at most 5,000 users," Cursor [said](https://x.com/cursor_ai/status/2116074289053175808). "This malicious version of the extension was not developed by Anthropic. It does not impact other extensions downloaded from the cursor[.]com/marketplace, Grok Bot, Grok, or our other SpaceXSI product.

However, Cursor's statement that the malicious version "was not developed by Anthropic" misses the point. The attackers distributed it as version 2.1.313 under Anthropic's legitimate Claude Code extension ID (anthropic.claude-code), rather than as a separate fake extension.

"The package identifies itself as anthropic.claude-code version 2.1.313, but its main JavaScript bundle contains a malicious 66-line loader inserted before the legitimate extension code," Jenn Gile, co-founder of OpenSourceMalware, said in a statement shared with The Hacker News.

The malicious update was distributed only through Cursor's marketplace, with no evidence that it reached Open VSX or Microsoft's official VS Code Marketplace. Users who installed Claude Code through either of those marketplaces are not known to be affected by this incident.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

As of October 30, 2026, the malicious version has been removed, and Anthropic has [published version 2.1.314](https://github.com/anthropics/claude-code/releases) to both Open VSX and Microsoft VS Code Marketplace.

The extension is designed to activate after VS Code startup and when its webview opens, then proceeds to add an attacker-controlled key to the user's "~/.ssh/authorized\_keys" file. The key is labeled "svc-telemetry" in an attempt to make it appear harmless.

Subsequently, it attempts to make the victim reachable through SSH across Windows, Linux, and macOS, establishes a reverse tunnel to "[134.209.82[.]225](https://www.virustotal.com/gui/ip-address/134.209.82.225/detection)," installs platform-specific persistence in the form of a scheduled task, crontab, and LaunchAgent, and transmits host reconnaissance data to "134.209.82[.]225:8099/beacon" on port 8099 over an unencrypted HTTP request.

"Turning on the local SSH service requires admin rights, which the malicious extension does not have on most macOS and Windows hosts," the SpaceXAI-owned company [said](https://cursor.com/blog/claude-code-extension-security-notice) in its own analysis of the incident.

"On those hosts the step fails and the attacker could not have logged in through the tunnel. The extension still adds the attacker's SSH key, installs persistence, and sends host details to the attacker. Follow the remediation steps below regardless."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4Ew0Bj3BoXpUeH6TD2jNswGM1qWxJ956j4_sI9otnOjW_hHhyrbfmuhd-kovwe07nO3rsiuAjjOAq1kZXc4x5Gk_g8uqiYAyrm-RCnaGabGsNC-D1W_92UaKoUZ56AGraAszeX_pkW5hMAq1lFGu7VBicGP1jbBqNsd9BhTkjqWJT6CYNE0YcyF-u3mih/s1700-nu-rw-lo-l85-e365/aa.png)

The collected data includes -

* Public IP address from api.ipify[.]org
* Hostname and local username
* Operating system and CPU architecture
* Home directory and current working directory
* Global Git email from git config --global user.email
* Names of up to 40 environment variables containing KEY, TOKEN, SECRET, PASS, AWS, or GCP

"Environment-variable values are not placed directly in the initial beacon," security researcher Paul McCarty said. "Their names can still reveal which cloud providers, CI systems, and credential types are configured. More importantly, successful SSH access would allow the operator to inspect the account directly."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

No other follow-on payloads have been observed. That said, the establishment of a reverse tunnel provides a pathway to the victim's SSH service, allowing the operator to issue commands or transfer files.

"It was pulled very quickly, but anyone who has their Claude Code instance set to auto-update could have consumed the malware," Gile said.

Cursor has revealed that the incident has affected at most 5,000 users who installed the malicious version between about 2:27 a.m. and 1:35 p.m. PT on October 29, 2026. The company also said that it will be reaching out to impacted users directly.

Users who have installed the compromised extension during the window are advised to isolate the hosts, remove the unauthorized SSH key and persistence mechanisms, and rotate credentials and sessions.

The disclosure comes a little over a week after an unknown attacker [replaced](https://thehackernews.com/2026/10/hackers-hi...