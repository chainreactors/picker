---
title: ThreatsDay Bulletin: Codespaces RCE, AsyncRAT C2, BYOVD Abuse, AI Cloud Intrusions & 15+ Stories
url: https://thehackernews.com/2026/02/threatsday-bulletin-codespaces-rce.html
source: The Hacker News
date: 2026-02-05
fetch_date: 2026-02-06T04:10:22.976697
---

# ThreatsDay Bulletin: Codespaces RCE, AsyncRAT C2, BYOVD Abuse, AI Cloud Intrusions & 15+ Stories

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [ThreatsDay Bulletin: Codespaces RCE, AsyncRAT C2, BYOVD Abuse, AI Cloud Intrusions & 15+ Stories](https://thehackernews.com/2026/02/threatsday-bulletin-codespaces-rce.html)

**Ravie Lakshmanan**Feb 05, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYa_2XB7ryXippAp9zUFVo52pAx1ApwoiVUwGxURxVTNIji0VO33VdciwulLXVslQ90-eSYknrIr8KSJMDEjC2uHK92e1Iin45YEI3IN5LvHAp5AJif7FqHJ-hsZ_WlmiOlXemsLpQWZ5KBSvKKZGoQ6AqePah4TWVcwbu2aFAKgugkK6SA8YglMDW5kUx/s1700-e365/threatsday-main.jpg)

This week didn’t produce one big headline. It produced many small signals — the kind that quietly shape what attacks will look like next.

Researchers tracked intrusions that start in ordinary places: developer workflows, remote tools, cloud access, identity paths, and even routine user actions. Nothing looked dramatic on the surface. That’s the point. Entry is becoming less visible while impact scales later.

Several findings also show how attackers are industrializing their work — shared infrastructure, repeatable playbooks, rented access, and affiliate-style ecosystems. Operations are no longer isolated campaigns. They run more like services.

This edition pulls those fragments together — short, precise updates that show where techniques are maturing, where exposure is widening, and what patterns are forming behind the noise.

1. Startup espionage expansion

   [Operation Nomad Leopard Targets Afghanistan](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)

   In a sign that the threat actor has moved beyond government targets, the Pakistan-aligned [APT36](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html) threat actor has been observed targeting India's startup ecosystem, using ISO files and malicious LNK shortcuts using sensitive, startup-themed lures to deliver [Crimson RAT](https://thehackernews.com/2022/03/new-hacking-campaign-by-transparent.html), enabling comprehensive surveillance, data exfiltration, and system reconnaissance. The initial access vector is a spear-phishing email carrying an ISO image. Once executed, the ISO contains a malicious shortcut file and a folder holding three files: a decoy document, a batch script that acts as the persistence mechanism, and the final Crimson RAT payload, disguised as an executable named Excel. "Despite this expansion, the campaign remains closely aligned with Transparent Tribe's historical focus on Indian government and defense-adjacent intelligence collection, with overlap suggesting that startup-linked individuals may be targeted for their proximity to government, law enforcement, or security operations," Acronis [said](https://www.acronis.com/en/tru/posts/new-year-new-sector-transparent-tribe-targets-indias-startup-ecosystem/).
2. Shared cybercrime infrastructure

   [ShadowSyndicate Levels Up with New Tactics](https://www.group-ib.com/blog/new-shadowsyndicate-infrastructure/)

   The [threat activity cluster](https://thehackernews.com/2025/08/weekly-recap-vpn-0-day-encryption.html#:~:text=ShadowSyndicate%20Infrastructure%20Analyzed) known as [ShadowSyndicate](https://thehackernews.com/2023/09/shadowsyndicate-new-cybercrime-group.html) has been linked to two additional SSH markers that connect dozens of servers to the same cybercrime operator. These hosts are then used for a wide range of malicious activities by various threat clusters linked to Cl0p, BlackCat, Ryuk, Malsmoke, and Black Basta. A notable finding is that the threat actor tends to transfer servers between their SSH clusters. ShadowSyndicate continues to be associated with toolkits including Cobalt Strike, Metasploit, Havoc, Mythic, Sliver, AsyncRAT, MeshAgent, and Brute Ratel. "The threat actor tends to reuse previously employed infrastructure, sometimes rotating various SSH keys across their servers," Group-IB [said](https://www.group-ib.com/blog/new-shadowsyndicate-infrastructure/). "If such a technique is performed correctly, the infrastructure is transferred subsequently, much like in a legitimate scenario, when a server goes to a new user."
3. Ransomware KEV expansion

   [CISA Marks 59 CVEs as Exploited in Ransomware Attacks](https://www.greynoise.io/blog/unmasking-cisas-hidden-kev-ransomware-updates)

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has tweaked 59 actively exploited vulnerability notices in 2025 to reflect their use by ransomware groups. That list includes 16 entries for Microsoft, six for Ivanti, five for Fortinet, three for Palo Alto Networks, and three for Zimbra. "When it flips from 'Unknown' to 'Known,' reassess, especially if you've been deprioritizing that patch because 'it's not ransomware-related yet," GreyNoise's Glenn Thorpe [said](https://www.greynoise.io/blog/unmasking-cisas-hidden-kev-ransomware-updates).

   [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiznYhUpd7H-rwS5sLB5CXsJ2r0MRDXHZwA-0kPk4xO6h9R7nSd-ACDmA1EGRMpJ1A4mgCVKzFmSJwIBnuBID1jGs_xbnQNyLUcO5_y5yaULPGiddE778Ka2drnLtoCLDMOdf5BcfaOAYBw4RSIcST4I_fI96u0kAge7Zef4daSwHvcxM7JZUrybTd0X3Sy/s1700-e365/kev.png)
4. Espionage and DDoS arrests

   [Polish Authorities Detain Two People](https://www.polskieradio.pl/399/7977/Artykul/3642849%2Czatrzymano-pracownika-mon-podejrzewanego-o-wspolprace-z-rosyjskim-i-bialoruskim-wywiadem)

   Polish authorities have [detained](https://www.polskieradio.pl/399/7977/Artykul/3642849%2Czatrzymano-pracownika-mon-podejrzewanego-o-wspolprace-z-rosyjskim-i-bialoruskim-wywiadem) a 60-year-old employee of the country's defense ministry on [suspicion](https://www.gov.pl/web/obrona-narodowa/komunikat-mon32) of spying for a foreign intelligence agency. The suspect worked in the Ministry of National Defense’s strategy and planning department, including on military modernization projects, officials said. While the name of the country was not revealed, Polish state officials told local media that the suspect had worked with Russian and Belarusian intelligence...