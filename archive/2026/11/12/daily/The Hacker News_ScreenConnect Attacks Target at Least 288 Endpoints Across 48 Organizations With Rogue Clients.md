---
title: ScreenConnect Attacks Target at Least 288 Endpoints Across 48 Organizations With Rogue Clients
url: https://thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:46.458138
---

# ScreenConnect Attacks Target at Least 288 Endpoints Across 48 Organizations With Rogue Clients

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [ScreenConnect Attacks Target at Least 288 Endpoints Across 48 Organizations With Rogue Clients](https://thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html)

**Ravie Lakshmanan**Nov 12, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEfz7InYm8UO-p35K6B4j009BxA-MO7DdZ2x1d-xhyphenhyphenPxNnVs848IlgAGelmuW-sPbEZbE8-L9_KWEYNH_M5HaTMy14MFd87A7YkqHAzDKaamKOdpZKR9owL3nK3gbqAngvWa6A4NC1KK1l0ie9FK731LfKPI0lguiGQ1b71sHIZj2kR2H3I-GJjSPY4kJU/s1700-nu-rw-lo-l85-e365/screenconnect-hack.jpg)

ConnectWise has taken the precautionary step of disabling five third-party extensions in partner environments [following reports of unauthorized access](https://www.reddit.com/r/msp/comments/1xts3f2/active_malware_campaign_abusing_screenconnect/).

In an advisory posted on its site, the company said there is no evidence that the incident involves a compromise of its infrastructure or a vulnerability in the ScreenConnect software.

"Our initial assessment suggests the activity may involve a threat actor's abuse of independent third-party extensions installed in partner environments," it [said](https://www.connectwise.com/company/trust/advisories). "We are continuing to validate this assessment. The initial access method and full scope remain under investigation."

ConnectWise has identified about 400 partner environments with at least one of the third-party extensions installed. It also emphasized that the presence of the extensions alone does not indicate or establish compromise.

While these extensions provide an API capable of executing remote commands, access to that API is secured by a passphrase configured by the partner during setup, it added. The list of extensions identified for precautionary disabling is below -

* Labtech Plus
* RMM Plus
* RMM+
* RMM Plus Password Link
* RMM+ Password Link

ConnectWise also said it has urged on-premises partners to disable the extensions, and is recommending all partners to ensure security controls are running, preserve suspicious activity logs, and stay vigilant for -

* Unusual sign-ins, unfamiliar locations, repeated login failures, and unexpected multi-factor authentication (MFA) prompts
* New administrator accounts or changes to user permissions
* Unexpected extension installations, remote commands, and Toolbox activity
* Unapproved remote-access software on customer devices and technician workstations
* Unexpected support requests, password-reset messages, and software downloads through a trusted channel

The company has shared the following indicators of compromise (IoCs) -

* IP addresses:
  + 185.99.255[.]28
  + 155.94.150[.]39
* Domains and URLs:
  + ns[.]mo7sen[.]dev
  + ns[.]mo7sen[.]dev/EadF.php?p=4
  + sc[.]payproofkit[.]com
  + cdn007-digitaldownloads[.]com
  + newnewnew[.]gotdns[.]org
  + Soxnewwork[.]homedns[.]org
* Artifacts:
  + sckit-run.bat
  + sckit-decoder.ps1
  + TrapWatch.ps1
  + Panel-Lateral.ps1
  + Run-Lateral-Full.bat
  + runnew.cmd
  + ToolboxRelayUploader.exe
  + Sqlite3.exe

Cybersecurity company Huntress, which is also [tracking](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect) the activity, said it has observed attackers using access to cloud-hosted ScreenConnect panels to push Run commands with an aim to install rogue ScreenConnect clients on at least 288 managed endpoints across 48 organizations. The activity was first detected on November 11, 2026, at around 5:47 p.m. UTC.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Huntress told The Hacker News that it has not seen evidence of a new vulnerability, but noted the exact method through which the attacker got panel access remains unclear. Current telemetry points to compromised credentials or hijacked operator sessions to gain initial access, it said.

The overall attack unfolds in a worm-like fashion using a two-step process -

* **Initial access:** Attackers use a compromised ScreenConnect panel's Run Command feature to deploy a rogue ScreenClient client across endpoints, creating a persistent backdoor that no longer depends on the original panel.
* **Lateral movement:** When a technician connects to an infected endpoint through ScreenConnect, the malware can spread back to their workstation, steal saved browser sessions and authentication tokens, and pivot to other ScreenConnect panels the technician has access to.

"The rogue clients deliver SCKit, a custom malicious toolkit that establishes persistent remote access and creates a relay trap for intercepting session cookies," Huntress researchers Ben Nahorney and Susannah Matt said.

"The infection path works in two stages: from an infected endpoint to a technician who connects to it, and from a technician's workstation to every endpoint their panel can connect to. However, not all functionality has been observed during observed incidents; some functionality has been discovered through analysing the payloads."

SCKit is delivered as an encrypted payload and via a Base64-encoded dropper ("sckit-run.bat"), which then contacts a remote server to fetch a PowerShell payload ("sckit-decoder.ps1") that's responsible for launching the toolkit.

Other components of the malware are designed to add Microsoft Defender exclusions, install a second attacker-controlled ScreenConnect client, create a scheduled task named "TrapWatch," and replace the legitimate ScreenConnect installation with an attacker-controlled copy.

There are signs that at least one of the scripts is generated by a large language model (LLM) based on the detailed source code references and comments that explain its functionality.

"Going beyond what we've observed, we've reconstructed an additional functionality intended to spread from a technician's workstation to the ScreenConnect panel," Huntress said. "This has been discovered from analysis of its scripts, configuration, and tools. To date we have not observed a successful jump from...