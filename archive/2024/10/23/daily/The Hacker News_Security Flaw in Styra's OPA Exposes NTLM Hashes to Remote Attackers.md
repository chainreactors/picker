---
title: Security Flaw in Styra's OPA Exposes NTLM Hashes to Remote Attackers
url: https://thehackernews.com/2024/10/security-flaw-in-styras-opa-exposes.html
source: The Hacker News
date: 2024-10-23
fetch_date: 2025-10-06T18:56:21.135288
---

# Security Flaw in Styra's OPA Exposes NTLM Hashes to Remote Attackers

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

# [Security Flaw in Styra's OPA Exposes NTLM Hashes to Remote Attackers](https://thehackernews.com/2024/10/security-flaw-in-styras-opa-exposes.html)

**Oct 22, 2024**Ravie LakshmananVulnerability / Software Security

[![NTLM Hashes to Remote Attackers](data:image/png;base64... "NTLM Hashes to Remote Attackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkAJrS6a_Xi7ugYUNVu-hBUj8frLR-hpz2yZ9Ltb5_MmKpKEdNTExazRruofPjwwHZL8bCYcBd-52h8oPjtPBA76IUKkHxY7r38b3aFYSBH_LehbTPcPeHXPFUm2UjTIg14eV9yINEEruDTi9hAFp08QWgFnMkfg0YpwxYL-Sv_8tZfYt8p8ghCskUAiv3/s790-rw-e365/passw3rod.png)

Details have emerged about a now-patched security flaw in Styra's Open Policy Agent ([OPA](https://www.openpolicyagent.org)) that, if successfully exploited, could have led to leakage of New Technology LAN Manager ([NTLM](https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview)) hashes.

"The vulnerability could have allowed an attacker to leak the NTLM credentials of the OPA server's local user account to a remote server, potentially allowing the attacker to relay the authentication or crack the password," cybersecurity firm Tenable [said](https://www.tenable.com/blog/cve-2024-8260-smb-force-authentication-vulnerability-in-opa-could-lead-to-credential-leakage) in a report shared with The Hacker News.

The security flaw, described as a Server Message Block (SMB) force-authentication vulnerability and tracked as [CVE-2024-8260](https://nvd.nist.gov/vuln/detail/CVE-2024-8260) (CVSS score: 6.1/7.3), impacts both the CLI and Go software development kit (SDK) for Windows.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

At its core, the issue stems from an [improper input validation](https://www.tenable.com/security/research/tra-2024-36) that can lead to unauthorized access by leaking the Net-NTLMv2 hash of the user who is currently logged into the Windows device running the OPA application.

However, for this to work, the victim must be in a position to initiate outbound Server Message Block (SMB) traffic over port 445. Some of the other prerequisites that contribute to the medium severity are listed below -

* An initial foothold in the environment, or social engineering of a user, that paves the way for the execution of the OPA CLI
* Passing a Universal Naming Convention (UNC) path instead of a Rego rule file as an argument to OPA CLI or the OPA Go library's functions

The credential captured in this manner could then be weaponized to stage a relay attack in order to bypass authentication, or perform offline cracking to extract the password.

"When a user or application attempts to access a remote share on Windows, it forces the local machine to authenticate to the remote server via NTLM," Tenable security researcher Shelly Raban said.

"During this process, the NTLM hash of the local user is sent to the remote server. An attacker can leverage this mechanism to capture the credentials, allowing them to relay the authentication or crack the hashes offline."

Following responsible disclosure on June 19, 2024, the vulnerability was addressed in [version 0.68.0](https://github.com/open-policy-agent/opa/releases/tag/v0.68.0) released on August 29, 2024.

"As open-source projects become integrated into widespread solutions, it is crucial to ensure they are secure and do not expose vendors and their customers to an increased attack surface," the company noted. "Additionally, organizations must minimize the public exposure of services unless absolutely necessary to protect their systems."

The disclosure comes as Akamai shed light on a [privilege escalation flaw](https://github.com/akamai/akamai-security-research/tree/main/PoCs/cve-2024-43532) in the Microsoft Remote Registry Service ([CVE-2024-43532](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-43532), CVSS score: 8.8) that could permit an attacker to gain SYSTEM privileges by means of an NTLM relay. It was patched by the tech giant earlier this month after it was reported on February 1, 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The vulnerability abuses a fallback mechanism in the WinReg [RPC] client implementation that uses obsolete transport protocols insecurely if the SMB transport is unavailable," Akamai researcher Stiv Kupchik [said](https://www.akamai.com/blog/security-research/2024/oct/winreg-relay-vulnerability).

"By exploiting this vulnerability, an attacker can relay the client's NTLM authentication details to the Active Directory Certificate Services (ADCS), and request a user certificate to leverage for further authentication in the domain."

The susceptibility of NTLM to relay attacks hasn't gone unnoticed by Microsoft, which, earlier this May, [reiterated](https://thehackernews.com/2024/05/windows-11-to-deprecate-ntlm-add-ai.html) its plans to retire NTLM in Windows 11 in favor of Kerberos as part of its efforts to strengthen user authentication.

"While most RPC servers and clients are secure nowadays, it is possible, from time to time, to uncover relics of insecure implementation to varying degrees," Kupchik said. "In this case, we managed to achieve NTLM relay, which is a class of attacks that better belongs to the past."

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
[![...