---
title: Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Attack Campaign
url: https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html
source: The Hacker News
date: 2026-11-25
fetch_date: 2026-11-26T10:15:12.711168
---

# Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Attack Campaign

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Attack Campaign](https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html)

**Ravie Lakshmanan**Nov 25, 2026Cyber Attacks / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzxhgIKTt8K5ep8a4qHW9dDpkSYcBC5D1CWgkvvh9Ee5DRlNRSg-2UcZZVNoXrHXVTeIcdzj47FFcSz6gAssLknSDf6f0JDyQCoH51D4GYLSju_wh4smA6-2yE3Z7I30SPeuY8LOKA__Y9xPiU66t1aPsHTzuRnX0QUq2iadcKXFfv7ZhAhcXti_BDnrmu/s1700-nu-rw-lo-l85-e365/code.jpg)

An unknown threat actor has been using artificial intelligence (AI)-driven offensive tooling in a campaign targeting Check Point Security Management servers, impacting 22 distinct organizations across the world.

The intrusion activity, [tracked](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) by GreyNoise under the moniker **GreyNoise Threat 13** (GT13), is assessed to have targeted organizations in the financial services, energy, government, transportation, mining, engineering, and manufacturing sectors across the U.K., Ireland, France, Netherlands, Greece, Germany, Austria, Bulgaria, Poland, India, Thailand, Vietnam, South Korea, Hong Kong, China, Australia, and the U.S.

Confirmed attack activity has been recorded between October 17 and November 2, 2026, with the threat actor using 99 IP addresses to conduct scanning, exploitation, and control. Most of these IP addresses are associated with disposable network infrastructure.

The campaign has not been attributed to any known threat actor or group. It's suspected that the attackers are relying on agentic harnesses and systems for vulnerability scanning, exploitation, and automatic interaction with compromised assets.

The threat actor has also been observed using tools like Nmap, Chisel, Impacket, Paramiko, and other Python scripts to carry out internal reconnaissance, privilege escalation, and lateral movement on victim environments.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"We witnessed the GT13 actor use 99 IP addresses, all of which were either egresses through ExpressVPN or compromised victim Check Point devices, including activity over 1400+ network sessions, 800+ command line artifacts, and 1200+ files downloaded, uploaded, or created," GreyNoise said.

In one case, the attackers have been found using an automated scanning and exploitation pipeline to compromise an HFS server using [CVE-2026-61500](https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html), a critical flaw in Rejetto HFS, in early October 2026 to obtain control of the server and issue commands, including adding an SSH key to the "/root/.ssh/authorized\_keys" file.

Subsequently, GT13 is said to have used the compromised server as a relay for follow-on operations centered around saving command results and exfiltrating data from 24 previously compromised Check Point Security Management servers. The attackers also unsuccessfully attempted to deploy a Linux implant named ZULT to the compromised Rejetto HFS server.

"The GT13 adversary had access to the victim Check Point Security Management Servers before they compromised the HFS server," the cybersecurity company said. "We could not determine when or how the attacker gained access to those Check Point assets."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihNbatGxoIHWBR7BGp9bPGYRXHOnqExm-SLL39fXEhv2cr_0eseZ-aQFP_eIhJ-lYSwkV0EwjjVDZVZEMiiAc07IqYuj7qmSOUpZGwXBu66LIVfermvV87jXSGpkA8YEonIO4Zy2tv3s8D6zQhnnfsC3Uk0ykWxRAgXw2OKmQ2RQul2iAQSrL4UoqV2cGX/s1700-nu-rw-lo-l85-e365/browser.png)

The attackers also moved to burrow deeper into one of the victim networks, using a script for a now-patched Check Point flaw ([CVE-2026-16232](https://thehackernews.com/2026/07/check-point-patches-exploited.html)) to launch over 100 management tasks on multiple Check Point Management Servers to -

* Steal firewall databases and internal certificate authority files
* Mint a new certificate
* Unload security policies, effectively disabling firewall protections
* Conduct internal network reconnaissance and attempt lateral movement

The post-compromise activity also involved attempts to target other enterprise systems, such as Citrix NetScaler ([CVE-2023-4966](https://nvd.nist.gov/vuln/detail/cve-2023-4966)), Ivanti Connect Secure ([CVE-2024-21893](https://nvd.nist.gov/vuln/detail/cve-2024-21893)), VMware vCenter ([CVE-2021-21972](https://nvd.nist.gov/vuln/detail/cve-2021-21972) and [CVE-2023-34048](https://nvd.nist.gov/vuln/detail/cve-2023-34048)), Microsoft Exchange ([CVE-2021-26855](https://nvd.nist.gov/vuln/detail/cve-2021-26855) and [CVE-2021-34473](https://nvd.nist.gov/vuln/detail/cve-2021-34473)), and Microsoft Netlogon ([CVE-2020-1472](https://nvd.nist.gov/vuln/detail/cve-2020-1472)).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

In tandem, the threat actor has attempted to exploit various other security flaws, including, but not limited to -

* [CVE-2024-21893](https://nvd.nist.gov/vuln/detail/cve-2024-21893) (Ivanti Connect Secure)
* [CVE-2025-5777](https://nvd.nist.gov/vuln/detail/cve-2025-5777) (Citrix NetScaler)
* [CVE-2026-41089](https://nvd.nist.gov/vuln/detail/cve-2026-41089) (Windows Netlogon)
* [CVE-2026-98432](https://nvd.nist.gov/vuln/detail/cve-2026-98432) (Linux IPv4 UAF)

GreyNoise has theorized that GT13 has in its possession a "mature AI-enabled offensive apparatus" that it uses to weaponize vulnerabilities, scan for susceptible assets, and exploit them to gain access to systems that can be later used as operational relays or true targets.

"The activity reported by the GreyNoise article involves CVE-2026-16232, a previously disclosed vulnerability with patches already available, and does not represent a new vulnerability or exploitation technique," Sergey Shykevich, Director, Threat ...