---
title: Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide
url: https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html
source: The Hacker News
date: 2026-10-30
fetch_date: 2026-10-31T07:49:06.436933
---

# Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)

**Ravie Lakshmanan**Oct 30, 2026Cyber Espionage / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP1M46Z4Xs0qNHz9xzhTea14XsqTHvNhAfnGb4Ni9goHQR2ypz3BLKRgu-WxWD8VSUNMB3YAP7UhcCAK1AweCc3lC-7VlJ-OqNniD4FvZdE_R-XJkkRadhl2tp3-PqbKPWmQTeJ3a3gvd1kHH_zaW06tCf9cH-7k5feNqHrqbChMAsc5K3hruiX9BDROAe/s1700-nu-rw-lo-l85-e365/CS.jpg)

Chinese state-sponsored threat actors have been observed using a Go-based artificial intelligence (AI)-powered penetration testing framework called **ARTEX** in attacks aimed at high-value targets simultaneously.

The activity has been attributed by CrowdStrike to a China-based "targeted intrusion adversary" it tracks under the moniker **Vapor Panda** (previously VexatiousTemper). First identified in February 2021, the hacking group overlaps with a threat cluster detailed by Trend Micro as [Earth Estries](https://thehackernews.com/2024/11/chinese-hackers-use-ghostspider-malware.html).

"Agentic tooling like ARTEX enables this scale of expansion at speed, allowing a small team to pursue a wider target set than manual operations would support, rather than a wholesale shift away from the adversary's established access-development mission," CrowdStrike [said](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/) in a Thursday analysis.

Starting October 17, 2026, Vapor Panda is said to have used the AI tool against more than 200 distinct organizations across the world, including foreign ministries in Latin America, Europe, Asia, and the Middle East; semiconductor, defense, and think tank organizations in the U.S.; and telecommunications providers in multiple regions.

Some of the notable targets listed by CrowdStrike are listed below -

* Foreign ministries of two Latin America-based countries, Central America, and Asia
* A Middle East-based interior ministry
* A European country's foreign ministry, presidency, and prime minister's office, along with defense, justice, finance, and intelligence entities
* 19 U.S.-based organizations in the pharmaceutical, semiconductor, defense, nuclear, and financial sectors
* Telecommunications providers in the U.S., Belgium, and the Philippines

Post-exploitation activity has been confirmed at nine organizations, allowing the attacker to deploy [BLOODALCHEMY](https://thehackernews.com/2026/08/silkparasite-espionage-campaign-targets.html), a derivative of ShadowPad, followed by credential spraying, network scanning, and reconnaissance.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Vapor Panda is also said to have conducted password-spraying and credential-scanning activity against at least 12 additional organizations, including U.S.-based think tanks and government entities in Europe.

Central to the operation is the use of ARTEX with DeepSeek and an as-yet-unknown, subscription-based commercial large language model (LLM) to conduct the intrusions at scale, leveraging an army of planner and worker agents that coordinate with each other in pursuit of a common goal to move from initial access to host reconnaissance and lateral movement.

A human operator in the loop oversees the operation, directing the agents to write web shells, extract domain administrator passwords, and enumerate endpoint sensor coverage.

"In a single intrusion, Vapor Panda's planning agents consumed on the order of 1.4 billion input tokens, indicating the scale of the automated activity and implying far higher consumption across the operation as a whole," CrowdStrike said.

Unlike some campaigns that used to assist with individual digital break-ins, the use of ARTEX is at a much higher level to run multiple engagements concurrently, with the human operator only stepping in to steer the agents to accomplish their objective, while taking steps to bypass endpoint defenses.

Analysis of the recovered transcripts highlights the use of ARTEX in combination with tried-and-tested approaches -

* Chaining an unsigned Security Assertion Markup Language (SAML) assertion and an XML external entity (XXE) flaw to query the cloud Instance Metadata Service. This is followed by obtaining a role that can issue administration commands to thousands of instances before escalating access to recover an enterprise administrator account.
* Deploying web shells, abusing an unauthenticated orchestration service to obtain root access in a production container environment, reading Local Administrator Password Solution (LAPS) passwords, and leveraging resource-based constrained delegation to impersonate a privileged account.
* Supplying the agent with a set of authentication keys that had not been rotated since 2022, which then uses those keys to forge an administrator token and read mailboxes. In the next phase, the agent uses VPN configurations recovered from a user's sent mail, along with a VPN client key originating from a purported May 2024 email leak, to reach the internal network.

"Across these engagements, the agents pursued multiple attack paths in parallel, spanning web applications, cloud services, container environments, Active Directory, and mail and VPN infrastructure," CrowdStrike explained. "They shifted to alternative approaches when a path failed. This breadth likely enables a single operator to apply a wider range of techniques against more targets at once than would be feasible through manual operations."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHNmLL4bv5hxRdn8rpu-lQO0wAWjJPsSfra5wgZgKahZU9IceBRFKKMpcS6jJSrDiVFZDIeFlXlbdKzJ9jHTyzXXykNNPFFhen_44r6czo75d4BWCd4TkjTPnowj7c783kVOXS84ZbvlHN9DIZycE-WFwxTR37wFLPOhnmcIz_oGwijmVi4PYRwfmOIjrL/s1700-nu-rw-lo-l85-e365/zz.jpg)

The development comes as ARTEX has [witnessed](https://thehac...