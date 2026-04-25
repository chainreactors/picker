---
title: FIRESTARTER Backdoor Hit Federal Cisco Firepower Device, Survives Security Patches
url: https://thehackernews.com/2026/04/firestarter-backdoor-hit-federal-cisco.html
source: The Hacker News
date: 2026-04-24
fetch_date: 2026-04-25T04:38:42.038954
---

# FIRESTARTER Backdoor Hit Federal Cisco Firepower Device, Survives Security Patches

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [FIRESTARTER Backdoor Hit Federal Cisco Firepower Device, Survives Security Patches](https://thehackernews.com/2026/04/firestarter-backdoor-hit-federal-cisco.html)

**Ravie Lakshmanan**Apr 24, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhL39ca_K84pnKcPSv77aXouF3t3HCOjjL1zFVEdeDE64LiUxQ2Het8xQeTeO0JZRHZE56SbG87psVmhYCbSyu5PE3FZiHrAIzm0zp8nfGKk7XwVTUUjpeZ7zDEZwuJaQkZp6Cl20WF7qkWDAuaOQW5-OtTQ1ZvjW4xhHB9HrC2O-C6pPPnE94gLqp1GZrI/s1700-e365/cisco.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has revealed that an unnamed federal civilian agency's Cisco Firepower device running Adaptive Security Appliance (ASA) software was compromised in September 2025 with malware called **FIRESTARTER**.

FIRESTARTER, per CISA and the U.K.'s National Cyber Security Centre (NCSC), is [assessed](https://www.cisa.gov/news-events/analysis-reports/ar26-113a) to be a backdoor designed for remote access and control. It's believed to be deployed as part of a "widespread" campaign orchestrated by an advanced persistent threat (APT) actor to obtain access to Cisco Adaptive Security Appliance (ASA) firmware by exploiting [now-patched security flaws](https://thehackernews.com/2025/11/cisco-warns-of-new-firewall-attack.html) such as -

* **CVE-2025-20333** (CVSS score: 9.9) - An improper validation of user-supplied input vulnerability that could allow an authenticated, remote attacker with valid VPN user credentials to execute arbitrary code as root on an affected device by sending crafted HTTP requests.
* **CVE-2025-20362** (CVSS score: 6.5) - An improper validation of user-supplied input vulnerability that could allow an unauthenticated, remote attacker to access restricted URL endpoints without authentication by sending crafted HTTP requests.

"FIRESTARTER can persist as an active threat on Cisco devices running ASA or Firepower Threat Defense (FTD) software, maintaining post-patching persistence and enabling threat actors to re-access compromised devices without re-exploiting vulnerabilities," the agencies said.

In the investigated incident, the threat actors have been found to deploy a post-exploitation toolkit called [LINE VIPER](https://thehackernews.com/2025/09/cisco-asa-firewall-zero-day-exploits.html) that can execute CLI commands, perform packet captures, bypass VPN Authentication, Authorization, and Accounting (AAA) for actor devices, suppress syslog messages, harvest user CLI commands, and force a delayed reboot.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

The elevated access afforded by LINE VIPER served as a conduit for FIRESTARTER, which was deployed on the Firepower device before September 25, 2025, allowing the threat actors to maintain continued access and return to the compromised appliance as recently as last month.

A Linux ELF binary, FIRESTARTER can set up persistence on the device, and survive firmware updates and device reboots unless a hard power cycle occurs. The malware lodges itself into the device's boot sequence by manipulating a startup mount list, ensuring it automatically reactivates every time the device reboots normally. The resilience aside, it also shares some level of overlap with a previously documented bootkit referred to as RayInitiator.

"FIRESTARTER attempts to install a hook – a way to intercept and modify normal operations – within LINA, the device’s core engine for network processing and security functions," according to the advisory. "This hook enables the execution of arbitrary shell code provided by the APT actors, including the deployment of LINE VIPER."

"Although Cisco's patches addressed CVE-2025-20333 and CVE-2025-20362, devices compromised prior to patching may remain vulnerable because FIRESTARTER is not removed by firmware updates."

Cisco, which is tracking the exploitation activity associated with the two vulnerabilities under the moniker [UAT4356](https://thehackernews.com/2024/04/state-sponsored-hackers-exploit-two.html) (aka Storm-1849), [described](https://blog.talosintelligence.com/uat-4356-firestarter/) FIRESTARTER as a backdoor that facilitates the execution of arbitrary shellcode received by the LINA process by parsing specially crafted WebVPN authentication requests containing a "magic packet."

The exact origins of the threat activity are not known, although an [analysis](https://thehackernews.com/2024/05/china-linked-hackers-suspected-in.html) from attack surface management platform Censys in May 2024 suggested links to China. UAT4356 was first attributed to a campaign called ArcaneDoor that exploited two zero-day flaws in Cisco networking gear to deliver bespoke malware capable of capturing network traffic and reconnaissance.

"To fully remove the persistence mechanism, Cisco strongly recommends reimaging and upgrading the device," Cisco [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-persist-CISAED25-03). "In cases of confirmed compromise on any Cisco Secure ASA or FTD platforms, all configuration elements of the device should be considered untrusted."

As mitigations until reimaging can be performed, the company is recommending that customers perform a cold restart to remove the FIRESTARTER implant. "The shutdown, reboot, and reload CLI commands will not clear the malicious persistent implant, the power cord must be pulled out and plugged back in the device," it added.

### Chinese Hackers Shift From Individually Procured Infrastructure to Covert Networks

The disclosure comes as the U.S., the U.K., and various international partners [released](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-113a) a joint advisory about large-scale networks of compromised SOHO routers and IoT devices commandeered by China-nexus threat actors to disguise their espionage attacks and complicate attribution efforts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

State-sponsored groups like [Volt Typhoon](https://thehackernews.com/2024/02/after-fbi-takedown-kv-botnet-operators.html) and [Flax Typhoon](https://thehackernews.com/2024/09/new-raptor-train-iot-botnet-compromises.html) have been using these botnets, consisting...