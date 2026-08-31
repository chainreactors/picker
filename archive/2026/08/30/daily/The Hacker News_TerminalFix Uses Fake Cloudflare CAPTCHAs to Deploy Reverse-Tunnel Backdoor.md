---
title: TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor
url: https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html
source: The Hacker News
date: 2026-08-30
fetch_date: 2026-08-31T07:53:52.152175
---

# TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor](https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html)

**Ravie Lakshmanan**Aug 30, 2026Social Engineering / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpxriybAzLw0daA0mtL3sZd04fy8Sal4s0mrBAz2-ksjwfP2V08YK_KbCJY57hKG28Kt6gn2mKq4HFSpkG2MNvA3Oz6MhNUe77_1Nvpahn2nnCFHPpxIlp5Ix4DvAZw08qXtxt1M-4zCtSENbBkODQyP_WDp9j3PXACc0XKYk1BK1K-2Xabho1cBPqerW9/s1700-nu-rw-lo-l85-e365/cf-clickfix.jpg)

Microsoft has disclosed details of a new ClickFix variant, dubbed **TerminalFix**, that aims to trick users into running a malicious command in Windows Terminal or PowerShell.

"While traditional [ClickFix campaigns](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) direct victims to the Windows Run dialog, TerminalFix campaigns apply the same technique but direct users to Windows Terminal or PowerShell instead, increasing the likelihood that complex, multi-line scripts execute successfully," Microsoft security researchers Sagar Patil, Suriyaraj Natarajan, and Parasharan Raghavan [said](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/) in an analysis published this week.

The campaign, targeting organizations across multiple sectors, leverages compromised websites as a starting point to serve fake Cloudflare CAPTCHA verifications that prompt unsuspecting site visitors to copy and execute a malicious PowerShell command.

The attack chain, per the Windows maker, is a sophisticated multi-stage process that leverages DLL sideloading, steganographic payload extraction, extensive Active Directory reconnaissance, and a bespoke custom reverse-tunnel implant that grants the attacker persistent, network-level proxy access through the infected machine.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Specifically, the PowerShell command is designed to download a ZIP archive containing a legitimate binary ("LockScreenContentServer.exe") and a rogue DLL ("dui70.dll") in order to initiate a DLL sideloading attack.

The sideloaded DLL is responsible for retrieving next-stage payloads hidden within PNG images from external domains ("bestsocialmedianewspapper[.]com" or "offlineupdater[.]com"), establishes persistence via both Registry Run keys and scheduled tasks, carries out domain reconnaissance, and then deploys a Python-based reverse-tunnel command-and-control (C2) implant.

The backdoor ("client.py") is equipped to tunnel arbitrary TCP traffic back to attacker-controlled infrastructure ("gitnow[.]dev:443") through an encrypted WebSocket channel, as well as enable the C2 server to reach any host visible from the victim's network.

The reconnaissance phase involves the following steps -

* Collect system metadata
* Perform domain trust discovery, domain admin enumeration, and Active Directory user and computer searches
* Ping named servers to map the internal network topology

The attack also delivers a persistent PowerShell file-watch loop that monitors a text file for new commands, executes them via Invoke-Expression, and writes results to an output file.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"This type of intrusion is particularly dangerous because it provides attackers with direct access to an organization's internal network through the reverse tunnel," Microsoft said. "The observed reconnaissance and reverse-tunnel capability could enable an attacker to identify and reach additional systems from a compromised host."

The tech giant has warned that such access can be abused further to escalate privileges, disarm security controls, exfiltrate sensitive data, and deploy ransomware, making TerminalFix a serious threat to enterprise environments.

To mitigate the threat, it's advised to restrict PowerShell and Run dialog execution for standard users through AppLocker, Application Control for Windows, or Group Policy; consider blocking or auditing the Windows Run dialog ("Win+R") if it's not required; monitor for DLL sideloading indicators; train employees to keep an eye out for ClickFix attacks; and enable PowerShell script block logging to detect and analyze obfuscated or encoded commands.

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

[Active Directory](https://thehackernews.com/search/label/Active%20Directory), [Malware](https://thehackernews.com/search/label/Malware), [network security](https://thehackernews.com/search/label/network%20security), [Social Engineering](https://thehackernews.com/search/label/Social%20Engineering), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account](https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leak...