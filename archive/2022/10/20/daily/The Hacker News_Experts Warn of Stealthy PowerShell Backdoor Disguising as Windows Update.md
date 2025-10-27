---
title: Experts Warn of Stealthy PowerShell Backdoor Disguising as Windows Update
url: https://thehackernews.com/2022/10/experts-warn-of-stealthy-powershell.html
source: The Hacker News
date: 2022-10-20
fetch_date: 2025-10-03T20:26:23.339198
---

# Experts Warn of Stealthy PowerShell Backdoor Disguising as Windows Update

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

# [Experts Warn of Stealthy PowerShell Backdoor Disguising as Windows Update](https://thehackernews.com/2022/10/experts-warn-of-stealthy-powershell.html)

**Oct 19, 2022**Ravie Lakshmanan

[![PowerShell Backdoor](data:image/png;base64... "PowerShell Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqYrJmZDKh1r7FdG8H9inTS6c0P7Mp_gPIp_ewfD_PlwKkigkv3JsTu5X3JXFFRmN-20DrXmw89c0rRF04hr6gnIRVqqBl-KzH-5onQAOaMXEnL2MZY3D61sf7vuR8DpNfoT-D3XfKeHvB03SoWI7xrNefZucL0B4a8V5qx7F5gjdZNv7Kf6En4UbL/s790-rw-e365/malware.jpg)

Details have emerged about a previously undocumented and fully undetectable (FUD) PowerShell backdoor that gains its stealth by disguising itself as part of a Windows update process.

"The covert self-developed tool and the associated C2 commands seem to be the work of a sophisticated, unknown threat actor who has targeted approximately 100 victims," Tomer Bar, director of security research at SafeBreach, [said](https://www.safebreach.com/resources/blog/safebreach-labs-researchers-uncover-new-fully-undetectable-powershell-backdoor/) in a new report.

Attributed to an [unnamed threat actor](https://securelist.com/top-10-unattributed-apt-mysteries/107676/), attack chains involving the malware commence with a weaponized [Microsoft Word document](https://www.virustotal.com/gui/file/45f293b1b5a4aaec48ac943696302bac9c893867f1fc282e85ed8341dd2f0f50) that, per the company, was uploaded from Jordan on August 25, 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Metadata associated with the lure document indicates that the initial intrusion vector is a LinkedIn-based spear-phishing attack, which ultimately leads to the execution of a PowerShell script via a piece of embedded macro code.

"The Macro drops 'updater.vbs,' creates a scheduled task pretending to be part of a Windows update, which will execute the updater.vbs script from a fake update folder under '%appdata%\local\Microsoft\Windows,'" Tomar said.

[![PowerShell Backdoor](data:image/png;base64... "PowerShell Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6nJrDmnqPFEzv4URTHO3wLr6X09GI6nV5svxewdF6tzhBL9dxIvsWgCVc7PJTD_ko7TiuBtHnNl_d6sNWdvG7QnilMstfDwsukF2qgtfNfwnHyi-hLoyfoYZC2bNvEw-p6Hf_L1sHKqCIv739KFp5PUXt8Cr8vXClIpD7GBPcWwNEXvtsC1NpE2qe/s790-rw-e365/hack.jpg)

The PowerShell script ([Script1.ps1](https://www.virustotal.com/gui/file/bda4484bb6325dfccaa464c2007a8f20130f0cf359a7f79e14feeab3faa62332)) is designed to connect to a remote command-and-control (C2) server and retrieve a command to be launched on the compromised machine by means of a second PowerShell script ([temp.ps1](https://www.virustotal.com/gui/file/16007ea6ae7ce797451baec2132e30564a29ee0bf8a8f05828ad2289b3690f55)).

But an operational security error made by the actor by using a trivial incremental identifier to uniquely identify each victim (i.e., 0, 1, 2, etc.) allowed for reconstructing the commands issued by the C2 server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Some of the notable instructions transmitted consist of exfiltrating the list of running processes, enumerating files in specific folders, launching whoami, and deleting files under the public user folders.

As of writing, 32 security vendors and 18 anti-malware engines flag the decoy document and the PowerShell scripts as malicious, respectively.

The findings come as Microsoft has [taken steps](https://thehackernews.com/2022/07/microsoft-resumes-blocking-office-vba.html) to block Excel 4.0 (XLM or XL4) and Visual Basic for Applications (VBA) macros by default across Office apps, prompting threat actors to pivot to [alternative delivery methods](https://thehackernews.com/2022/07/hackers-opting-new-attack-methods-after.html).

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

[powershell](https://thehackernews.com/search/label/powershell)[SafeBreach](https://thehackernews.com/search/label/SafeBreach)[Windows](https://thehackernews.com/search/label/Windows)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews....