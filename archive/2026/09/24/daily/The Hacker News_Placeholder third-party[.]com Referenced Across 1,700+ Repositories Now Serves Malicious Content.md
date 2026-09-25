---
title: Placeholder third-party[.]com Referenced Across 1,700+ Repositories Now Serves Malicious Content
url: https://thehackernews.com/2026/09/placeholder-third-partycom-referenced.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:33.763888
---

# Placeholder third-party[.]com Referenced Across 1,700+ Repositories Now Serves Malicious Content

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Placeholder third-party[.]com Referenced Across 1,700+ Repositories Now Serves Malicious Content](https://thehackernews.com/2026/09/placeholder-third-partycom-referenced.html)

**Ravie Lakshmanan**Sep 24, 2026Phishing / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhy4aXDWSC5cKzOZO8lRbk8o5I1fHPlCGbfxxYL6tyJxauEL-8EVj7-AypDhYt_Wg6bDLqlj0UK4LrGJdeI4ChsksaB6tTZxo8ikCLdwC0wjRfJPE_Z1qM_CVUg7s1ORdmWW2XTDtlPPDcI8JvelrbmJhcjVthnqYWQrZ7ySnIMMPRZfa_VzgaBCWyWc_JJ/s1700-nu-rw-lo-l85-e365/third.jpg)

The "third-party[.]com" domain, commonly used as a documentation placeholder, has been observed serving a ClickFix lure to Windows browsers while displaying a harmless decoy to other users.

"third-party[.]com has been a generic documentation placeholder for years, the same role example.com plays," Manifold Security's Head of Research, Ax Sharma, [said](https://www.manifold.security/blog/third-party-com-placeholder-clickfix). "Unlike 'example[.]com,' third-party[.]com is not [IANA-reserved](https://www.iana.org/domains/reserved). Anyone could register it, and someone did. Every doc, test, and skill that hard-coded it now points readers at attacker infrastructure."

As of writing, the domain has been marked as malicious and unsafe on both [VirusTotal](https://www.virustotal.com/gui/domain/third-party.com) and Google's [Safe Browsing list](https://transparencyreport.google.com/safe-browsing/search?url=third-party.com&hl=en).

ClickFix is a [social engineering attack](https://www.group-ib.com/blog/clickfix-the-social-engineering-technique-hackers-use-to-manipulate-victims/) technique in which either malicious or legitimate-but-compromised websites display error messages, browser alerts, or CAPTCHA verification prompts, tricking users into [copying and executing hidden commands](https://www.halcyon.ai/ransomware-research-reports/clipboard-to-encryption-the-critical-role-of-clickfix-in-ransomware-campaigns) via the Windows Run dialog or Terminal to "fix" the issue.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Often, web pages using ClickFix rely on clipboard hijacking to automatically inject malicious script or commands into the victim's clipboard for subsequent pasting on Windows Run dialog or macOS Terminal. This approach is also sometimes referred to as pastejacking.

According to Manifold Security, the domain has been serving the ClickFix lure since at least June 2026. Windows users visiting the page are shown a Cloudflare check that poisons the victim's clipboard and instructs them to paste and run the command via the Windows Run dialog. The pasted command is designed to extract and run a remote PowerShell payload.

When a macOS user visits the same page, the fake security verification prompt shows an error: "macOS is not supported. This website requires a Windows PC to access. Please try again from a Windows device."

A search on GitHub shows that the domain is [referenced](https://github.com/search?q=third-party.com&type=code) in over 1,700 public repositories, including those related to AI agent skills and MCP-server docs that cite "third-party[.]com" as an example endpoint.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6FqmwDHOsb9pXyzBWm8SaBshhBvE3r8M92yyLgbKD2dxbXKl_uqwPhab2oBIViZWRKPqBWi6JNfJcjhop_8AHbN3paxONeY_7LulW3huATNeCkrLGWiHjZe0Wz9_esPCfAhT30cZC0egKtEntiavR1gI-E_YIwBPp82dTBO6JCANdz55TS2K6ioYW1j1y/s1700-nu-rw-lo-l85-e365/1000110911.jpg)

"In every one of those places it is exactly what it looks like: a placeholder, an example, a stand-in, and entirely reasonable use by the teams involved," Sharma noted. "It is also, now, a live pointer to a ClickFix server."

This weaponization of a blindly trusted domain, in turn, [can open up avenues](https://www.manifold.security/blog/curl-bash-ai-agents) for prompt injection and other unintended behaviors.

To counter the threat, it's advised to audit their documentation and treat non-reserved placeholder domains (e.g., yourcompany[.]com, mycompany[.]com, your-api[.]com, and their lookalikes) as squattable and open to abuse by threat actors, who can register them and serve malicious content.

Developers working on skills, documentation, or test cases are recommended to use reserved placeholders like "example[.]com" (or "example[.]org," "example[.]net") only and avoid using plausible-sounding domains that are not under their control.

"You can scan the skill, read the file, resolve the domain from your analysis box, and conclude it is fine, and be completely wrong about what a Windows user's agent receives when it follows the same link," Manifold Security pointed out. "A file scan cannot see what a website decides to send. The tell only appears at request time, from the caller that matters."

The disclosure comes as Manifold said it has since identified 13 more placeholder domains that are not IANA-reserved, with two of them – yoursite[.]com and your-domain[.]com – serving scams and scareware to macOS visitors and an ordinary parking page to other users.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

"On a macOS browser, your-domain[.]com showed a fake 'MacOS Security Center' claiming four viruses and selling a counterfeit McAfee renewal at 55% off," security researcher Cody Nash [said](https://www.manifold.security/blog/placeholder-domains-ads-serve-scams). "On another macOS render, yoursite[.]com showed a counterfeit ZDF news article advertising an investment scheme."

The complete list of domains, each of which pass standard static checks, is as follows -

* your-domain[.]com
* yourdomain[.]com
* your-site[.]com
* yoursite[.]com
* your-app[.]com
* yourapp[.]com
* myapp[.]com
* mysite[.]com
* acme[.]com
* company[.]com
* mycompany[.]com
* vendor[.]com
* foo[.]com

To make matters worse, the two scam-scarware-serving sites are present in hundreds of thous...