---
title: LockBit 3.0 Ransomware Builder Leak Gives Rise to Hundreds of New Variants
url: https://thehackernews.com/2023/08/lockbit-30-ransomware-builder-leak.html
source: The Hacker News
date: 2023-08-27
fetch_date: 2025-10-04T12:00:27.568521
---

# LockBit 3.0 Ransomware Builder Leak Gives Rise to Hundreds of New Variants

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [LockBit 3.0 Ransomware Builder Leak Gives Rise to Hundreds of New Variants](https://thehackernews.com/2023/08/lockbit-30-ransomware-builder-leak.html)

**Aug 26, 2023**Ravie LakshmananEndpoint Security / Cyber Threat

[![LockBit 3.0 Ransomware Builder](data:image/png;base64... "LockBit 3.0 Ransomware Builder")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxUonlMxMgT7OQkZZfEPCf019hT-EW2sn8RyBw_EhyXLcWUtft3I-sEvlrJuUeY07Ig0WDxRLT37GYtoYjkRGApjxkiEwTamxt8jSmfJL2knlCmATBOu4HjfwD-vYn9taFQ-2uca1x6UhDg68rBLR0jAf4hFZ-1MkEVmwH6Q6QUBEyKnAqLzcNWrxQAS83/s790-rw-e365/lockbit.jpg)

The leak of the [LockBit 3.0 ransomware](https://thehackernews.com/2023/06/lockbit-ransomware-extorts-91-million.html) builder last year has led to threat actors abusing the tool to spawn new variants.

Russian cybersecurity company Kaspersky said it detected a ransomware intrusion that deployed a version of LockBit but with a markedly different ransom demand procedure.

"The attacker behind this incident decided to use a different ransom note with a headline related to a previously unknown group, called NATIONAL HAZARD AGENCY," security researchers Eduardo Ovalle and Francesco Figurelli [said](https://securelist.com/lockbit-ransomware-builder-analysis/110370/).

The revamped ransom note directly specified the amount to be paid to obtain the decryption keys, and directed communications to a Tox service and email, unlike the LockBit group, which doesn't mention the amount and uses its own communication and negotiation platform.

NATIONAL HAZARD AGENCY is far from the only cybercrime gang to use the leaked LockBit 3.0 builder. Some of the other threat actors known to leverage it include [Bl00dy and Buhti](https://thehackernews.com/2023/05/buhti-ransomware-gang-switches-tactics.html).

Kaspersky noted it detected a total of 396 distinct LockBit samples in its telemetry, of which 312 artifacts were created using the leaked builders. As many as 77 samples make no reference to "LockBit" in the ransom note.

"Many of the detected parameters correspond to the default configuration of the builder, only some contain minor changes," the researchers said. "This indicates the samples were likely developed for urgent needs or possibly by lazy actors."

The disclosure comes as Netenrich delved into a ransomware strain called ADHUBLLKA that has rebranded several times since 2019 (BIT, LOLKEK, OBZ, U2K, and TZW), while targeting individuals and small businesses in exchange for meager payouts in the range of $800 to $1,600 from each victim.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Although each of these iterations come with slight modifications to encryption schemes, ransom notes, and communication methods, a closer inspection has tied them all back to ADHUBLLKA owing to source code and infrastructure similarities.

"When a ransomware is successful out in the wild, it is common to see cybercriminals use the same ransomware samples — slightly tweaking their codebase — to pilot other projects," security researcher [Rakesh Krishnan](https://twitter.com/RakeshKrish12) [said](https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family).

"For example, they may change the encryption scheme, ransom notes, or command-and-control (C2) communication channels and then rebrand themselves as a 'new' ransomware."

Ransomware remains an [actively evolving ecosystem](https://www.sentinelone.com/blog/from-conti-to-akira-decoding-the-latest-linux-esxi-ransomware-families/), witnessing frequent shifts in tactics and targeting to increasingly focus on Linux environments using families such as [Trigona](https://thehackernews.com/2023/06/8base-ransomware-spikes-in-activity.html), [Monti](https://thehackernews.com/2023/08/monti-ransomware-returns-with-new-linux.html), and [Akira](https://thehackernews.com/2023/07/blackcat-operators-distributing.html), the latter of which [shares links](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/) to Conti-affiliated threat actors.

[![LockBit 3.0 Ransomware Builder](data:image/png;base64... "LockBit 3.0 Ransomware Builder")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzs7o0EK3uZhUHY44-itGAJXr5DsZ9NwtVga2iwdAFiU5EWD18fss8scu7U_hQE7k9ILeKGgUStxS33Ll4g4IQqvVwygqxB8rYScyOSSptXqXv3LHJt7lWA7a-Qjsx9IL4K3vkphhV8ZLXBMLb2tPna2M8JZ5Guv_Ksw7Cya8AV_Ak3gIKCkM_RKO16jA5/s790-rw-e365/agency.jpg)

Akira has also been linked to attacks weaponizing Cisco VPN products as an attack vector to gain unauthorized access to enterprise networks. Cisco has since acknowledged that the threat actors are targeting Cisco VPNs that are not configured for multi-factor authentication.

"The attackers often focus on the absence of or known vulnerabilities in multi-factor authentication (MFA) and known vulnerabilities in VPN software," the networking equipment major [said](https://blogs.cisco.com/security/akira-ransomware-targeting-vpns-without-multi-factor-authentication).

"Once the attackers have obtained a foothold into a target network, they try to extract credentials through LSASS (Local Security Authority Subsystem Service) dumps to facilitate further movement within the network and elevate privileges if needed."

The development also comes amid a [record surge in ransomware attacks](https://www.nccgroup.com/us/resource-hub/cyber-threat-intelligence-reports/), with the Cl0p ransomware group having [breached 1,000 known organizations](https://www.emsisoft.com/en/blog/44123/unpacking-the-moveit-breach-statistics-and-analysis/) by exploiting [flaws in MOVEit Transfer app](https://thehackernews.com/2023/06/third-flaw-uncovered-in-moveit-transfer.html) to gain initial access and encrypt targeted networks.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

U.S.-based entities account for 83.9% of the corporate victims, followed by Germany (3.6%), Canada (2.6%), and the U.K. (2.1%). More than 60 million individuals are said to have been im...