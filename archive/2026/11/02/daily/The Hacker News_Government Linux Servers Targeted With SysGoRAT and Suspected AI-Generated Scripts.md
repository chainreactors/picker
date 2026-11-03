---
title: Government Linux Servers Targeted With SysGoRAT and Suspected AI-Generated Scripts
url: https://thehackernews.com/2026/11/government-linux-servers-targeted-with.html
source: The Hacker News
date: 2026-11-02
fetch_date: 2026-11-03T08:51:45.416814
---

# Government Linux Servers Targeted With SysGoRAT and Suspected AI-Generated Scripts

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Government Linux Servers Targeted With SysGoRAT and Suspected AI-Generated Scripts](https://thehackernews.com/2026/11/government-linux-servers-targeted-with.html)

**Ravie Lakshmanan**Nov 02, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYHKbP_7yOsvpwAldBMCL3QkCJ9SbUVrJz1Tr_RB6m3O99Gj73H0fX20hIbzKujRWB-1qkBCWv1UEJEbrTe1NFYpPkTm0OoNqJe7OdJoZa1HcZDT2On3mUT0igQeCOsMnWw_ZfT-HsLx6B8R84XYHHg4mUI2hPzM15ggddQCFAAmzChzC5Of90LInW8RB8/s1700-nu-rw-lo-l85-e365/artex.jpg)

Cybersecurity researchers have disclosed details of a cyber espionage campaign specifically targeting Linux infrastructure associated with government entities and state-affiliated infrastructure.

The activity, observed by Palo Alto Networks Unit 42 between October 2025 and April 2026, has been tracked under the moniker **CL-UNK-1211**, where "CL" refers to cluster and "UNK" stands for unknown motivation.

A notable aspect of the campaign concerns the use of large language models (LLMs) and/or automated artificial intelligence (AI) agents to generate payloads and execute malicious code.

"The attackers behind this cluster of activity focused on Linux environments to conduct extensive reconnaissance and maintain persistent network access to support intelligence-gathering," researchers Roey Porat and Tom Fakterman [said](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/). "The attackers attempted to dump sensitive databases and exfiltrate government mailboxes to access social media accounts."

The campaign employs a "versatile operational playbook," leveraging a combination of open-source tools, custom cross-platform backdoors, and web shells to maintain access. Another hallmark involves attempts to disable endpoint protections, wipe system logs, and plant deceptive red-team markers so as to disguise the activity as a legitimate security assessment.

The threat actor has also been observed using malicious PHP and shell scripts, likely generated using AI, to maintain persistence, perform reconnaissance, and exfiltrate data.

"Rather than standard developer documentation, multiple scripts contained conversational, step-by-step reasoning notes. These notes explained the code's logic to the operator who provided the initial instructions," the cybersecurity company said. "Their presence suggests that the code was either copied directly from an AI prompt output or deployed by an automated AI agent."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

A mix of open-source and bespoke PHP web shells is used as a way to maintain a persistent backdoor into the host networks. The access is then abused to gather credentials from the targeted environment using three different methods -

* Replacing the .bashrc file with a malicious version containing a command to steal passwords.
* Injecting code into PHP login pages to harvest admin credentials.
* Scanning for cleartext email, SMTP, and database passwords within configuration files and command history files.

Also deployed as part of the attacks is a custom, multi-platform remote access trojan written in Go that supports various persistence methods to maintain long-term access on Windows and Linux systems. Called SysGoRAT, it establishes a command-and-control (C2) connection over WebSocket to a hard-coded IP address ("104.194.158[.]65:443") and fetches seven types of commands -

* command, to execute arbitrary commands via /bin/sh -c (Linux) or cmd /C (Windows)
* control, to spawn via sub-commands an interactive shell (shell\_start), screenshots (screenshot), exfiltrate files to the C2 server (download), and install persistence (persist)
* list\_dir, to list directory content
* shell\_input, to create an interactive shell session
* proxy\_connect, to establish a TCP connection to an arbitrary target
* proxy\_data, to relay data bidirectionally to an established proxy connection
* proxy\_close, to terminate and remove a proxy session

Furthermore, the attacks make use of in-memory reverse shells to avoid leaving forensic artifacts on disk, as well as enumerate "/var/qmail/mailnames/" directories to count the number of emails stored in specific folders.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVwd3OEDFdT2yctOl3M0PGYmx-5S4GMt4qExxNkP5k2Yq-qn9VijOfBeOTnSqjvgtD1FJ2mQEPsWbk0urshqSBtbzqJZpNcyvuwejrqXMeiieIF5K2HlE53CgJ4INPq6Gh2sFE03CcIEhK5fHp2j2GFQsEp-YQVuASIzlopFr5B9EsgqyF9V0eYaaTq_37/s1700-nu-rw-lo-l85-e365/cat.png)

"Next, the attackers searched for social media-related emails," Unit 42 explained. "They deployed a PHP script, named search\_social.php, that searched for specific keywords in email headers and displayed the results in a user-friendly format."

"The script then parsed the response and displayed the exact file path, social media account email sender, recipient and subject."

The attackers have also been found attempting to generate a bash script named "zip\_mails.sh" in a bid to compress emails of interest into ZIP archives and exfiltrate the information. However, syntax errors present in the script meant that the program failed upon execution.

"This campaign demonstrates how attackers are combining traditional post-exploitation techniques with AI-accelerated workflows to target governmental Linux server infrastructure," Unit 42 said. "By leveraging AI to rapidly generate, adapt and deploy operational scripts, the attackers behind CL-UNK-1211 maintained a fast pace of operation while minimizing manual developer overhead."

The development comes as Google Threat Intelligence Group (GTIG) and Mandiant, along with Microsoft, documented threat actors' abuse of open-source agentic penetration testing frameworks like [ARTEX](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html), [PentAGI](https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html), [Hexstrike](...