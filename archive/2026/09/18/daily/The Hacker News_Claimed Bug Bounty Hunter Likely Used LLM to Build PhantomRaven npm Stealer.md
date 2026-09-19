---
title: Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer
url: https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.989681
---

# Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer

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

# [Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer](https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html)

**Ravie Lakshmanan**Sep 18, 2026Malware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyW8DcUYeyW1LOG-Gc3uqyV8_5rO4iwyEIM6FbRFwuvilvbfC7RSTjueJ4lEELpGvXX-22zzWuNCusN2qdODymiKNOQSz_8f1Q4u59bH7HCEZFT5PVsyBjj2NhWtlYiwvhXzXbwG_n3P_DCloZvMdajsc93hvqbJo6HCJy5wjNevUyN46ODFo7AlYsj499/s1700-nu-rw-lo-l85-e365/npm-cicd.jpg)

A financially motivated threat actor has been linked to the development and distribution of a JavaScript (JS)-based information stealer known as **PhantomRaven** via the npm package registry.

"The developer likely wrote the malware using a large language model (LLM), an assessment made with high confidence based on verbose comments, placeholder code, and statistical token-analysis patterns," CrowdStrike's Counter Adversary Operations [said](https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) in an analysis published this week.

PhantomRaven was [first flagged](https://thehackernews.com/2025/10/phantomraven-malware-found-in-126-npm.html) by Koi Security and DCODX in late October 2025, calling attention to a slopsquatting and typosquatted campaign in which more than 100 malicious packages were uploaded to npm to steal authentication tokens, CI/CD secrets, and GitHub credentials from developers' machines.

The software supply chain attack used these packages as a cover to retrieve a remote dynamic dependency (RDD) from an external server so that the libraries themselves are not flagged by security tools.

Once installed, the malware embedded in the remote dependency scans the developer environment for email addresses, gathers information about the CI/CD environment, collects a system fingerprint, including the public IP address, and transmits the results to an attacker-controlled server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

It's also equipped to collect runtime details, current date and time, username and email addresses from Git/npm configurations, as well as CI/CD environment variables for GitHub Actions, GitLab CI, Jenkins, and CircleCI.

The latest findings from CrowdStrike show that the threat actor has been active since November 2022 and claims to be a bug bounty hunter who has collected bounties from no less than nine entities across the technology, retail, and hospitality sectors.

The cybersecurity company said it has not observed information stolen from the malware appearing on stealer log shops, indicating "the operator likely uses the information stealer solely to identify bug bounty opportunities."

At least two different npm user accounts maintained by the operator have been observed pushing npm packages containing PhantomRaven. Both npm accounts are no longer accessible as of writing.

* jpdhellonpm1 - transform-jsbi-to-bigint
* jpd15 - sort-imports-es6-autofix

Some of the other online identities linked to the same operation include jpd12, jpd13, npmhell, npmpackagejpd, npmtestdharsh, jpdhackerone11, and packagedharsh.

"In August 2025, the threat actor claimed to have discovered a remote code execution (RCE) vulnerability via a malicious npm package they published," security researcher Maddie Stewart noted. "The threat actor explained that they had compromised the target machine and executed their preinstall script, which purportedly allowed them to achieve RCE."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

In addition, evidence has emerged that the threat actor attempted to push packages to the Python Package Index (PyPI) repository containing code for an information stealer that exhibits similarities with PhantomRaven.

The likely use of a large language model (LLM) to generate the malware once again highlights how threat actors are increasingly adopting the technology in their operations, compressing the time and effort it takes to pull off such campaigns.

"Most criminal actors [...] rent commodity tools or operate their own proprietary malware; however, this threat actor has likely developed their proprietary PhantomRaven to compromise company assets and then used these compromises as leverage to claim rewards from reputable disclosure programs," CrowdStrike said.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cybercrime](https://thehackernews.com/search/label/Cybercrime), [Malware](https://thehackernews.com/search/label/Malware), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

[![The Hacker News](data:image/svg+xml;base64...)

GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cv...