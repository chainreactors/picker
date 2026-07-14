---
title: Attacker Uses Suspected AI-Generated PowerShell Script to Map Active Directory
url: https://thehackernews.com/2026/07/attacker-uses-suspected-ai-generated.html
source: The Hacker News
date: 2026-07-13
fetch_date: 2026-07-14T04:48:21.537503
---

# Attacker Uses Suspected AI-Generated PowerShell Script to Map Active Directory

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

# [Attacker Uses Suspected AI-Generated PowerShell Script to Map Active Directory](https://thehackernews.com/2026/07/attacker-uses-suspected-ai-generated.html)

**Ravie Lakshmanan**Jul 13, 2026Artificial Intelligence / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh43TJKqVkJoN7Q3donw2FnXp1IrJEr6vvDteFOBCSR-PptAc8fMXXCq07kvKWoDacCHo6gi5-eUoX9mIBHggv-KXsoH31yBi0-_MZBjxYbiYNlhvAu8V_xhjuKHgnQj43x5S2pORBIGONxE_yLZdZOnDCmcjMegQjhwZtHDThg_4nlhZqwSizsMRCfZFQW/s1700-e365/ps-ai.jpg)

Cybersecurity researchers have flagged an intrusion in which an unknown threat actor leveraged a vibe-coded PowerShell script for Active Directory (AD) enumeration.

"The script looked for the Domain Controller (DC) and mapped users, computers, and domains, before creating a directory and exporting out a number of files, and finally creating AD\_Report.html to measure the success of the enumeration attempt," Huntress researchers Jevon Ang and Dray Agha [said](https://www.huntress.com/blog/ai-coded-malware-vibe-coding-active-directory).

The attack chain involved the threat actor establishing Remote Desktop Protocol (RDP) access onto a domain-joined Windows Server with a set of pre-compromised credentials, followed by staging the tools in the "C:\ProgramData\" folder. The incident took place in early June 2026.

This included an artificial intelligence (AI)-generated payload to map the Active Directory environment. The assessment is based on various telltale signs, such as the prompt iteration title, placeholder strings, over-engineered code that features multiple methods to find a Domain Controller, and beautified console output using cyan, green, red, and yellow.

Huntress described the bespoke PowerShell script as "highly aggressive" and "noisy," making use of a "five-step cascading fallback mechanism" to enable reconnaissance and discovery. It's titled "100% Working AD Information Gathering Script - FULLY FIXED," suggesting a back-and-forth with a large language model (LLM).

Once the primary Domain Controller is located, it initiates a data collection routine to systematically harvest AD users, computers, groups, organizational units (OUs), and trusts, and store the details in a staging directory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

About 30 minutes later, the attacker moved to deploy a [s5cmd](https://github.com/peak/s5cmd), a legitimate tool used for bulk file operations, along with [SharpShares](https://github.com/mitchmoser/SharpShares), a C#-based network shares enumeration utility, to look for user-accessible data repositories.

In the final stage, the data is said into CSV files, archived, and exfiltrated to a remote server, but not before creating an HTML file summarizing the data theft in the form of an Active Directory Inventory Report.

"It's likely a 'helpful' inject from the LLM that the attacker simply went along with, rather than being intentionally authored into the script," the researchers explained.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBmmFR1cuGuh0l2g9YSpbvcSNDqY3yfiiJLGWxonWr4HWu8dk-SifDjpa1O1UK48CmgAd99kTH_XfSIk0jwL9sUHAhLxjwo9rwq2hy84klI01jDimB46YblHNf9JS1eLMOVE2cbBd1PUtRNWiDYoYWvrPC7joJCaTYP8ln2Qm6lFIUlSEr1r17LK2eG8r_/s1700-e365/ad.png)

The development is yet another sign that threat actors are augmenting their arsenal with vibe-coded malware generated with assistance from AI models, even if the technology isn't being abused in ways not seen before. What it does change is that it lowers the barrier to entry for cybercrime, permitting less-skilled actors to come up with highly capable, evasive tooling with minimal effort.

"The underlying attack chain still resembles the tried-and-tested smash-and-grab playbook we've seen for years," Huntress said. "This core methodology has remained consistent, but it is now being selectively augmented by AI. This hybrid approach prioritises aggression and speed over stealth, allowing threat actors to execute highly damaging campaigns faster than ever."

### AI as a Force Multiplier

In a report published last week, Sygnia revealed that AI-enabled attackers do not necessarily need novel malware or zero-days, but that the real shift lies in the fact that cyber intrusions can be orchestrated at a speed and scale faster and bigger than defenders can contain them.

The incident response company said it observed an AI-assisted cloud attack that progressed from initial access to broad compromise within a span of about 72 hours against a large Amazon Web Services (AWS)-based environment. The end goal of the activity is assessed to be financially motivated, with the attacker using the access to the victim's cloud infrastructure for use as leverage for extortion.

"The threat actor repeatedly leveraged newly acquired credentials to restart discovery, secrets harvesting, persistence, and impact activities," it [said](https://www.sygnia.co/blog/inside-an-ai-assisted-cloud-attack/). "The attack relied on familiar cloud techniques rather than novel malware or zero-days."

"The threat actor was not exploiting a single misconfiguration; they were chaining weaknesses across application services, AWS resources, source-control repositories, CI/CD workflows, runtime components, and data stores, while rapidly executing credential discovery, secrets harvesting, cloud enumeration, deployment-pipeline abuse, runtime modification, database access, and operational disruption."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The attacker, per Sygnia, entailed repeated attempts to establish persistence on the compromised hosts, o...