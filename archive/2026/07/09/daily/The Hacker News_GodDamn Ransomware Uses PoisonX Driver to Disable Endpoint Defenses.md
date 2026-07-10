---
title: GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses
url: https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:13.639259
---

# GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses](https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html)

**Ravie Lakshmanan**Jul 09, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge_nKJNwSt3ZRkzfZ2qH61_1WFg5hyphenhyphenMSrC3-JM4AOXRKO-IVsJXFNiM926QnG25eTply3DRF57t61wi5Ucy4yxald1RpH1TRbItw83RqQ-K6UM670vpR76-kBl2xcntaDE7lxxNwurseG5iRM4sMhYK8Npb9COGNM_XjbwBLthnJjBfwqV7m96VKOnWb3Q/s1700-e365/endpoint-ransomware.jpg)

Cybersecurity researchers have flagged a new ransomware family called **GodDamn** that employs the PoisonX kernel driver to neutralize security software as part of its defense evasion strategy.

According to a [new report](https://www.security.com/threat-intelligence/goddamn-ransomware-beast-rebrand) published by the Threat Hunter Team from Symantec, the ransomware was first publicly spotted in the wild on May 21, 2026. It's assessed to be a rebrand of the [Beast](https://securelist.com/ransomware-updates-1-day-exploits/107291/) ransomware, which, in turn, was an enhanced version of [Monster](https://cyberint.com/blog/research/the-nature-of-the-beast-ransomware/), a Delphi-based ransomware that surfaced in March 2022. Broadcom's cybersecurity arm is tracing the developer behind these ransomware families under the moniker Hyadina.

In one attack orchestrated by the ransomware operation in early June 2026, the threat actors are said to have leveraged AnyDesk for remote access and used a [NirSoft-based credential harvesting toolkit](https://knowledge.broadcom.com/external/article/445443/detection-and-blocking-of-nirsoft-tool-a.html) before deploying the ransomware. The exact initial access vector is unknown. The credential harvester is designed to extract sensitive data from common web browsers, Windows Credential Manager, cached domain credentials, VNC sessions, email clients, Wi-Fi profiles, and live network traffic.

Also put to use in the attack is a user-mode defense evasion tool that's dressed as a Symantec product ("symantec.exe") and the PoisonX kernel driver ("g11.sys") to disable endpoint defenses in what's called a bring your own vulnerable driver (BYOVD) attack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"However, the PoisonX driver seems to be slightly more unusual, in that it appears to be a malicious driver that its developers succeeded in getting signed by Microsoft, and it is now being used by ransomware attackers," the Symantec Threat Hunter Team said in a report shared with The Hacker News.

It's worth noting that PoisonX is one of the eight drivers adopted by the operators of The Gentlemen ransomware-as-a-service (RaaS) scheme in its custom [GentleKiller](https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html) tool that it hands out to affiliates for impairing system defenses prior to executing the encryptor.

"Vulnerable drivers are the attacker's most reliable route in," Broadcom [noted](https://www.security.com/threat-intelligence/byovd-vulnerable-drivers) last month. "The attacker, having gained administrator privileges, can drop a flawed but validly signed driver onto the target machine. Because the driver is signed, Windows loads it automatically."

"The most common action is to kill the processes belonging to antivirus (AV) or endpoint detection and response (EDR) products, stripping the machine of its defenses. Some variants are more subtle. Attackers may strip the security agent of the rights it needs to function correctly, leaving it running but unable to act. Others tamper directly with the kernel's internal records so that the security product no longer receives notifications about what is happening on the machine, effectively making it blind."

The attack is also characterized by the use of PsExec to facilitate lateral movement, followed by setting up AnyDesk on each of those reachable hosts and registering it as an auto-start Windows service to survive reboots. On some machines, the entire AnyDesk setup is handled by a PowerShell script pre-staged on the system drive, suggesting the use of a reusable installer to streamline the process.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

"After completing the AnyDesk setup on each host, the attackers terminated the running AnyDesk process, waited briefly, then rebooted the machine," Symantec said. "By the end of June 2, this deployment sequence had been repeated across at least 10 hosts within the targeted organization."

The cybersecurity company said GodDamn ransomware was first detected on June 3 on a separate network segment associated with a distinct organizational unit, causing the files to be renamed with the victim's name as the extension instead of the ".God8Damn" extension used in other attacks carried out by Hyadina.

According to a report [released](https://www.cyfirma.com/news/weekly-intelligence-report-19-jun-2026/) by CYFIRMA, the ransom note dropped at the end of the intrusion urges victims to contact them either via email or the qTox encrypted messaging app.

"GodDamn's use of the relatively newly discovered PoisonX malicious driver component represents an escalation in defensive evasion capability by this group, indicating that Hyadina is continuing to actively develop its ransomware and its capabilities," the cybersecurity company concluded.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehack...