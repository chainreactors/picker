---
title: ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories
url: https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html
source: The Hacker News
date: 2026-06-11
fetch_date: 2026-06-12T06:28:10.542759
---

# ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories](https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html)

**Ravie Lakshmanan**Jun 11, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwRILGY9KcqTFlus6q7_YKlkzrx_LNXb7KS96PijLOM63YqrZIcvxXaf9j0i-sJhst_yL59b7pq32rwcHSSByX7dzVRXSv_dRnrAYqn0Hpps_G7odqCYu8BEonGPMlUkCAz-d0q2No-ojqaZou-b06UwZxzq0oV5CthkgjmTdTBU1JEkWRLV28PwRR5UW7/s1700-e365/tt.png)

It's been one of those weeks. You expect the usual noise: recycled malware, sloppy attacks, another easy target getting hit. Instead, there's a supply chain attack kit in a public repo, a $5,000-a-month RAT that clones browsers, and research showing AI agents can be tricked into leaking real credentials.

The bigger problem is how polished this all looks now. Mule networks run like SaaS. Deepfake KYC bypass is sold as a feature. Endpoint tools can be quietly weakened using built-in OS settings, with no exploit needed.

Here's the full list of threats, tools, flaws, and updates worth knowing.

1. 3.3B identity records exposed

   [How Infostealers Fuel Identity-Based Attacks](https://flashpoint.io/blog/proactive-defender-guide-infostealers/)

   A new analysis from Flashpoint has [revealed](https://flashpoint.io/blog/proactive-defender-guide-infostealers/) that "more than 11.1 million devices were infected with infostealers last year, fueling a supply of over 3.3 billion stolen credentials, session cookies, cloud tokens, and other forms of identity data now circulating across illicit markets." There are over 30 unique infostealer strains actively listed for sale across illicit marketplaces, forums, and underground communities, indicating the "scale and accessibility of the modern malware-as-a-service ecosystem." Lumma, Acreed, Rhadamanthys, Vidar, and StealC were the most prolific stealers in 2025. India, Brazil, Indonesia, Vietnam, the Philippines, and the U.S. were the top six countries affected by stealer malware during the same period.
2. MaaS RAT targets credentials

   [New SilabRAT Spotted](https://www.group-ib.com/blog/silabrat-hijackloader-trojan-malware/)

   A threat actor named "o1oo1" has advertised an advanced remote access trojan (RAT) named SilabRAT that's sold under a malware-as-a-service (MaaS) model for $5,000 a month on darknet forums since September 2025. "SilabRAT is heavily focused on financial gain through credential theft," Group-IB [said](https://www.group-ib.com/blog/silabrat-hijackloader-trojan-malware/). "It offers stability and is capable of bypassing existing security measures." Delivered via [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html) campaigns using [Hijack Loader](https://thehackernews.com/2024/05/hijack-loader-malware-employs-process.html), the malware uses Hidden Virtual Network Computing (HVNC) to facilitate remote control capabilities, employs techniques like Browser Profile Cloning to replicate a user's browser profile (user agent, extensions, storage, and other fingerprinting attributes) to the attacker's system, and can identify wallet addresses or extract cryptocurrency-related artifacts. The Russian-speaking malware developer and vendor, "o1oo1," has been active since late 2020, previously launching a service called [AsmCrypt](https://thehackernews.com/2023/09/cybercriminals-using-new-asmcrypt.html).
3. 47% of tech intrusions

   [North Korean Hackers Behind Nearly 50% of Tech Industry Hacks](https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-technology-threat-landscape-report/)

   CrowdStrike has revealed that a North Korean threat actor known as [Famous Chollima](https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html), which is behind the long-running IT worker and Contagious Interview campaign, accounted for 47% of all state-sponsored hands-on-keyboard operations against the tech sector between April 2025 and March 2026. Hands-on intrusions refer to cyber attacks in which a human operator controls and interacts with a system rather than relying solely on malware. "In their IT worker infiltration campaigns, they sought fraudulent employment at tech companies across North America, Europe, and Asia," the cybersecurity company [said](https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-technology-threat-landscape-report/).
4. 13 domains seized

   [U.S. Takes Down 13 Domains Linked to Alleged Chinese Intelligence Collection](https://www.justice.gov/opa/pr/justice-department-fbi-disable-13-websites-backed-suspected-chinese-agents-sought-sensitive)

   The U.S. Department of Justice has announced the seizure of 13 internet domains masquerading as consulting companies used to target U.S. persons, including current and former security clearance holders with access to classified and sensitive U.S. government information. "These domain seizures offer a glimpse at how foreign actors can use promises of easy money to lure Americans into revealing sensitive or classified information that they are duty-bound to protect," [said](https://www.justice.gov/opa/pr/justice-department-fbi-disable-13-websites-backed-suspected-chinese-agents-sought-sensitive) Assistant Attorney General for National Security John A. Eisenberg. "Anyone approached online with offers of easy income for vague 'consulting' work should treat those overtures with extreme caution and remain vigilant for warning signs of malicious targeting." These sham companies advertised generic consulting or analyst jobs on platforms like Upwork, Expertia AI, Hubstaff Talent, Wellfound, and Post Job Free that sought to recruit current or former U.S. government and U.S. military employees to lend their expertise to unspecified clients. The recruiters then pressured candidates to part with confidential information and reports from "insider" sources in exchange for cryptocurrency payments. The operation is assessed t...