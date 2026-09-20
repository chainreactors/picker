---
title: CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories
url: https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html
source: The Hacker News
date: 2026-09-19
fetch_date: 2026-09-20T07:17:02.501052
---

# CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories

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

# [CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories](https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html)

**Swati Khandelwal**Sep 19, 2026Data Breach / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1oastBaXn1Z-Cqbx-BPWZb2oSsgDseV8bReFs787OUvmfsQxJppvU6Fq_uUY_yrCdz1Z4xuevbNRdG88X9lnejn0NUF2RILOB8VxTm8lGXQ6VpZ1hPPqfmC4U86Ci2iYpIqpjy_3H3rCxJe6_9AKm0U9vgO6GHGrDHaKSdzCcFfgpUolbZvSB6VPbCC8/s1700-nu-rw-lo-l85-e365/crowdsec.jpg)

An attacker copied about 170 of CrowdSec's private GitHub repositories on May 22 using the account of an employee who had just left, CrowdSec said on September 18.

The French security company had kept his GitHub access open. CrowdSec says his laptop was compromised in May's [supply chain attack on TanStack](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html), in which malicious versions of TanStack's npm packages stole credentials from developers' machines.

The code appeared on an online forum on September 16. Along with the source code, it contained the email addresses of 83 CrowdSec users and the names, email addresses, and investment context of 51 potential investors from 2020, the company said.

[CrowdSec says](https://www.crowdsec.net/blog/tanstack-supply-chain-attack-analysis) the account was used only to copy code, that its infrastructure and databases were not accessed, and that no code was changed.

### How the Code Was Taken

On May 11, 84 malicious versions of 42 TanStack npm packages were published. The compromise is tracked as **CVE-2026-45321**. Installing one of those versions ran code that stole credentials from the machine, including GitHub tokens, SSH keys, and cloud credentials, according to [TanStack's advisory](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx).

The company says the copy was made 11 days later with a GitHub OAuth token from the former employee's account. The company had kept his access so he could finish some work.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

CrowdSec removed his account from its GitHub organization on May 25, three days after the copy and months before it learned of the leak. His other access had already been removed, which the company says explains why it saw no suspicious activity in its AWS systems.

The token left no trace in the GitHub logs it could check and no longer existed when it learned of the leak. It says GitHub support then traced the token's history and confirmed its suspicion that TanStack was the source.

CrowdSec did not say which malicious package reached the former employee's laptop or when, and its report does not include GitHub's own findings. It says its developers' machines were checked and came back clean.

The same attack also reached other companies. [Mistral AI](https://docs.mistral.ai/resources/security-advisories/MAI-2026-002) said a developer device was involved in its case, and [OpenAI](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/) said two employee devices were affected, with unauthorized access to a limited set of its internal code repositories.

### What the Archive Held

CrowdSec's open-source Security Engine detects attacks on servers, and users who share their detections receive a shared blocklist of malicious IP addresses. The leaked code comes from the company's private repositories, not this public engine.

According to the company, the code includes its web console, data science scripts and models, automation scripts, and the consensus algorithm that determines which IP addresses are added to the blocklists.

It says the code is almost four months old and has changed a lot since.

CrowdSec says the leak also revealed the thresholds the consensus algorithm uses, such as how many detections it requires before adding an IP address to the blocklist. These had not been public before.

As far as it knows, the blocklist still cannot be poisoned, meaning tricked into blocking a harmless IP address. It says an attacker would need tens of detections from tens of trusted engines across tens of separate networks, at great cost. CrowdSec also says it can change the thresholds, as it often does.

According to the company, the only usable credential in the leak was for AWS's SNS notification service, and it could only publish messages to one topic. Someone tried to use it on August 17, a month before the code was posted, but got no further. Other tokens in the code had already been rotated or could not be used from the internet, as far as the company knows.

CrowdSec says it has about 150,000 users. Its data science team kept the 83 exposed email addresses to study how people used the product, and the company says it will contact those users.

The investors' details came from a 2020 system that CrowdSec says was never meant to be public. The company says it will report the leak to the investors and to the authorities. CEO Philippe Humeau wrote to the investors in the report that "for this I personally apologize."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

The affected company rotated the exposed credentials on September 16 and 17. It did not require endpoint protection software on developers' machines at the time, but it now runs such software on the laptops of staff who work with its code or systems.

Neither CrowdSec's report nor its first statement asks users to take any action.

### How CrowdSec's Account Changed

CrowdSec's September 18 report differs from its [first statement](https://www.crowdsec.net/blog/crowdsec-statement-source-code-exposure), published a day earlier. In that statement, CrowdSec said "No client data, login/password, name, organization, or anything else was leaked," and that the impact was limited to the company.

The first statement also named the TanStack...