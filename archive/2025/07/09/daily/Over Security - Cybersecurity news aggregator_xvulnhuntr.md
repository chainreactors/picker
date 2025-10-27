---
title: xvulnhuntr
url: https://blog.compass-security.com/2025/07/xvulnhuntr/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-09
fetch_date: 2025-10-06T23:54:54.462751
---

# xvulnhuntr

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [xvulnhuntr](https://blog.compass-security.com/2025/07/xvulnhuntr/ "xvulnhuntr")

[July 8, 2025](https://blog.compass-security.com/2025/07/xvulnhuntr/ "xvulnhuntr")
 /
[Nicolo Fornari](https://blog.compass-security.com/author/nfornari/ "Posts by Nicolo Fornari")
 /
[2 Comments](https://blog.compass-security.com/2025/07/xvulnhuntr/#comments)

In 2024 we looked at the possibility of leveraging open weights LLMs for source code analysis.

The answer was clearly negative, as a small code base could easily take 200K tokens, more than any context window offered by open weights models.

The table below summarizes the top LLMs by context window as of today. Context windows significantly increased, compared to an average of 32.000 tokens last year. However, we are still a few orders of magnitude away from being able to feed entire code bases to LLMs.

|  |  |  |
| --- | --- | --- |
| **Model** | **Tokens** | **Open Weight** |
| Gemini 1.5 Pro (Google) | 2.000.000 | No |
| GPT 4.1 | 1.000.000 | No |
| Claude (Anthropic) | 200.000 | No |
| DeepSeek | 128.000 | Yes |
| LLAMA 3.1 | 128.000 | Yes |

Last updated: 23.04.2025

Later in the year a tool named vulnhuntr was published (<https://github.com/protectai/vulnhuntr>). The tool approached limited context windows by performing [source code analysis](https://www.compass-security.com/en/services/security-reviews) from source to sink and providing code blocks of the call chains iteratively in a multi-step process. Initially the LLM is fed code blocks for a set of files (e.g. sources where API entry points are defined). Then it literally asks for code blocks of functions and classes which are required for the analysis.

In addition to the clever approach, a track record of discovered vulnerabilities was published, making the tool even more appealing.

There is one relevant limitation though: only python code bases are supported. It is in fact very difficult to statically determine the call chain from source to sink for non-typed languages.

We decided that it was worth extending the tool to support additional languages. Therefore we created xvulnhuntr (<https://github.com/CompassSecurity/xvulnhuntr>), a fork of the original project where the ‘x’ stands for extended.

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/xvulnhuntr.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/xvulnhuntr.png)

Xvulnuhntr also supports C#, Java and Go. For each language, there is a dedicated tool developed in the corresponding language. Given a repository path and a class or function name in input, the tool returns a json with the file name for the match and the source code of the code block matching the function/class name. This modular approach allows to easily extend support to other typed languages.

In addition, we intentionally put additional effort into making xvulnhuntr easier for developers to contribute to. Compared to the original project, it is possible to run xvulnhuntr against a local test suite, mocking API responses. This provides multiple advantages:

* reproducibility: while LLMs are not deterministic (even with temperature set to zero), mocked responses allow easier debugging
* speed: mocked responses avoid latency from the LLM provider
* cost reduction: no need to waste tokens during development

## Next Steps

We primarily focused on the development of the tool. We expect refinements and bugs to come up as the tool is used against a variety of code bases. We are also interested in evaluating how analysis from different LLM providers compare to each other. Finally, we welcome and encourage contributions. Until then, happy LLM-powered hacking!

[Tools](https://blog.compass-security.com/category/tools/)

[Analysis](https://blog.compass-security.com/tag/analysis/)[LLM](https://blog.compass-security.com/tag/llm/)

[##### Previous post

Pwn2Own Ireland 2024 – Ubiquiti AI Bullet](https://blog.compass-security.com/2025/06/pwn2own-ireland-2024-ubiquiti-ai-bullet/ "Previous post: Pwn2Own Ireland 2024 – Ubiquiti AI Bullet")
[##### Next post

Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/ "Next post: Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases")

## 2 Comments

1. Fabio Zuber

   July 8, 2025 at 16:22

   Cool stuff! Did you also think of / try upstreaming the enhancements instead of creating a fork?

   [Reply](https://blog.compass-security.com/2025/07/xvulnhuntr/?replytocom=390011#respond)

   * Nicolo Fornari  (Post author)

     July 9, 2025 at 08:35

     Hi Fabio,
     I thought about it but if you look at the original repo there are quite some pending open issues and PRs with no activity/comments from the authors. This is not meant to be a critique, I just doubt the authors have time/interest in reviewing and accepting so many changes.

     [Reply](https://blog.compass-security.com/2025/07/xvulnhuntr/?replytocom=390042#respond)

### Leave a Reply [Cancel reply](/2025/07/xvulnhuntr/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

### Recent Posts

* [Ensuring NIS2 Compliance: The Importance of Penetration Testing](https://blog.compass-security.com/2025/09/ensuring-nis2-compliance-the-importance-of-penetration-testing/)
* [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/)
* [Taming The Three-Headed Dog -Kerberos Deep Dive Series](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/)
* [Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/)
* [xvulnhuntr](https://blog.compass-security.com/2025/07/xvulnhuntr/)

### Categories

Categories
Select Category
APT  (8)
Authentication  (18)
Bug Bounty  (6)
Entra ID  (3)
Evasion  (3)
Event  (34)
Exploiting  (18)
Forensic  (25)
Hacking-Lab  (18)
Hardening  (33)
Incident Response  (14)
Industrial Control Systems  (14)
Information Leakage  (7)
Internet of Things  (15)
Job  (2)
Linux  (8)
Log Management  (6)
Machine Learning  (3)
Malware Detection  (6)
Mobile  (10)
Networking  (17)
OS X  (1)
Patch  (6)
Penetration Test  (61)
Red Teaming  (15)
Research  (75)
Reversing  (13)
Risk Assessment  (10)
Scam  (1)
Social Engineering  (1)
Standards  (11)
SuisseID  (1)
Talk  (22)
Tools  (28)
Training  (19)
Uncategorized  (19)
Vulnerability  (46)
Web Application  (51)
Web Server  (13)
Windows  (31)
Wireless  (6)
Write-up  (26)
Youtube  (1)

### Tags

[Active Directory](https://blog.compass-security.com/tag/active-directory/)
[Advanced Metering Infrastructure](https://blog.compass-security.com/tag/advanced-metering-infrastructure/)
[Advisory](https://blog.compass-security.com/tag/advisory/)
[Application Security](https://blog.compass-security.com/tag/application-security/)
[ASFWS](https://blog.compass-security.com/tag/asfws/)
[ASP.NET](https://blog.compass-security.com/tag/asp-net/)
[Black Hat](https://blog.compass-security.com/tag/black-hat/)
[bloodhound](https://blog.compass-security.com/tag/bloodhound/)
[Burp](https://blog.compass-security.com/tag/burp/)
[Burp Extension](https://blog.compass-security.com/tag/burp-extension/)
[Bypa...