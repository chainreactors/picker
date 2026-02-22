---
title: AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries
url: https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html
source: The Hacker News
date: 2026-02-21
fetch_date: 2026-02-22T04:10:33.381398
---

# AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries](https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html)

**Ravie Lakshmanan**Feb 21, 2026Threat Intelligence / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJJ0OGjlNTnrjpx23D3iKXHFeEEDiGO2GRCI-o4SmtGRuXcl5S4rAcjOqOBrfuI1g8E_pj6UQjQP-R2qfAsV08Oukshw6Inq8fUK83I9sLd3LwnPyWazzaQ3yUghSA3UL0j-BNz0tn2dCEQsG3MpACZKSXoKnM6nhyphenhyphenf727_4S_f3L8EU3fxDc332_6Swkm/s1700-e365/FortiGate.jpg)

A Russian-speaking, financially motivated threat actor has been observed taking advantage of commercial generative artificial intelligence (AI) services to compromise over 600 FortiGate devices located in 55 countries.

That's according to new findings from Amazon Threat Intelligence, which said it observed the activity between January 11 and February 18, 2026.

"No exploitation of FortiGate vulnerabilities was observed—instead, this campaign succeeded by exploiting exposed management ports and weak credentials with single-factor authentication, fundamental security gaps that AI helped an unsophisticated actor exploit at scale," CJ Moses, Chief Information Security Officer (CISO) of Amazon Integrated Security, [said](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/) in a report.

The tech giant described the threat actor as having limited technical capabilities, a constraint they overcame by relying on multiple commercial generative AI tools to implement various phases of the attack cycle, such as tool development, attack planning, and command generation.

While one AI tool served as the primary backbone of the operation, the attackers also relied on a second AI tool as a fallback to assist with pivoting within a specific compromised network. The names of the AI tools were not disclosed.

The threat actor is assessed to be driven by financial gain and not associated with any advanced persistent threat (APT) with state-sponsored resources. As recently [highlighted](https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html) by Google, generative AI tools are being increasingly adopted by threat actors to scale and accelerate their operations, even if they don't equip them with novel uses of the technology.

If anything, the emergence of AI tools illustrates how capabilities that were once off-limits to novice or technically challenged threat actors are becoming increasingly feasible, further lowering the barrier to entry for cybercrime and enabling them to come up with attack methodologies.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"They are likely a financially motivated individual or small group who, through AI augmentation, achieved an operational scale that would have previously required a significantly larger and more skilled team," Moses said.

Amazon's investigation into the threat actor's activity has revealed that they have successfully compromised multiple organizations’ Active Directory environments, extracted complete credential databases, and even targeted backup infrastructure, likely in a lead-up to ransomware deployment.

What's interesting here is that rather than devising ways to persist within hardened environments or those that had employed sophisticated security controls, the threat actor chose to drop the target altogether and move to a relatively softer victim. This indicates the use of AI as a way to bridge their skill gap for easy pickings.

Amazon said it identified publicly accessible infrastructure managed by the attackers that hosted various artifacts pertinent to the campaign. This included AI-generated attack plans, victim configurations, and source code for custom tooling. The entire modus operandi is akin to an "AI-powered assembly line for cybercrime," the company added.

At its core, the attacks enabled the threat actor to breach FortiGate appliances, allowing it to extract full device configurations that, in turn, made it possible to glean credentials, network topology information, and device configuration information.

This involved systematic scanning of FortiGate management interfaces exposed to the internet across ports 443, 8443, 10443, and 4443, followed by attempts to authenticate using commonly reused credentials. The activity was sector-agnostic, indicating automated mass scanning for vulnerable appliances. The scans originated from the IP address [212.11.64[.]250](https://www.virustotal.com/gui/ip-address/212.11.64.250/detection).

The stolen data was then used to burrow deeper into targeted networks and conduct post-exploitation activities, including reconnaissance for vulnerability scanning using Nuclei, Active Directory compromise, credential harvesting, and efforts to access backup infrastructure that align with typical ransomware operations.

Data gathered by Amazon shows that the scanning activity resulted in organizational-level compromise, causing multiple FortiGate devices belonging to the same entity to be accessed. The compromised clusters have been detected across South Asia, Latin America, the Caribbean, West Africa, Northern Europe, and Southeast Asia.

"Following VPN access to victim networks, the threat actor deploys a custom reconnaissance tool, with different versions written in both Go and Python," the company said.

"Analysis of the source code reveals clear indicators of AI-assisted development: redundant comments that merely restate function names, simplistic architecture with disproportionate investment in formatting over functionality, naive JSON parsing via string matching rather than proper deserialization, and compatibility shims for language built-ins with empty documentation stubs."

Some of the other steps undertaken by the threat actor following the reconnaissance phase are listed below -

* Achieve domain compromise via [DCSync att...