---
title: Changing the tide: Reflections on threat data from 2024
url: https://blog.talosintelligence.com/changing-the-tide-reflections-on-threat-data-from-2024/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-07
fetch_date: 2025-10-06T20:38:27.883212
---

# Changing the tide: Reflections on threat data from 2024

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Changing the tide: Reflections on threat data from 2024

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, February 6, 2025 14:03

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

> “Enough Ripples, And You Change The Tide. For The Future Is Never Truly Set.” X-Men: Days of Future Past

In January, I dedicated some time to examine threat data from 2024, comparing it with the previous years to identify anomalies, spikes, and changes.

As anticipated, the number of Common Vulnerabilities and Exposures (CVEs) rose significantly, from 29,166 in 2023 to 40,289 in 2024, marking a substantial 38% increase. Interestingly, the severity levels of the CVEs remained centered around 7-8 for both years.

When taking a closer look at the known exploited vulnerabilities reported by the Cybersecurity and Infrastructure Security Agency (CISA), I observed that the numbers remained relatively stable, with 186 in 2024 compared to 187 in 2023. However, there was a noteworthy 36% increase for the critical vulnerabilities scored (9-10).

There is more to uncover from this data, and the analysis is still ongoing.

![](https://blog.talosintelligence.com/content/images/2025/02/Top-Initial-Access-Vectors-2024_blog.jpg)

It was also time to “stack” the data of our [Quarterly Incident Response Reports.](https://blog.talosintelligence.com/talos-ir-trends-q4-2024/) The standout aspects are the initial access vectors to me. "Exploiting Public Facing Applications" and "Valid Accounts" were dominant, outperforming other methods. This serves as a timely reminder to implement (proper) MFA and other identity and access control solutions as well as patch regularly and replace end-of-life assets.

Reflecting on CVEs, patching, initial access vectors and also lateral movement, it's important to remember that the "free" support for Windows 10 will end on October 14, 2025.

Mark.your.calendars. Please. And plan accordingly to ensure your systems remain secure.

## Newsletter reader survey

**We want your feedback! Tell us your thoughts and five lucky readers will receive Talos Swag boxes.**

[Launch survey](https://forms.office.com/r/PhJ1FFRfHe)

### The one big thing

Cisco Talos’ Vulnerability Research team recently [disclosed](https://blog.talosintelligence.com/whatsup-gold-observium-offis-vulnerabilities/) three vulnerabilities in Observium, three vulnerabilities in Offis, and four vulnerabilities in Whatsup Gold.

### Why do I care?

Observium and WhatsUp Gold can be categorized as Network Monitoring Systems (NMS). A NMS as such holds a lot of valuable information such as Network Topology, Device Inventory, Log Files, Configuration Data and more, making them an attractive for the bad guys.

### So now what?

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, make sure your installation is up to date.

### Top security headlines of the week

The Cybersecurity and Infrastructure Security Agency analyzed a patient monitor used by the Healthcare and Public Health sector and discovered an embedded backdoor. ([CISA](https://www.cisa.gov/resources-tools/resources/contec-cms8000-contains-backdoor))

Apple has released software updates to address several security flaws across its portfolio, including a zero-day vulnerability that it said has been exploited in the wild. ([Hacker News](https://thehackernews.com/2025/01/apple-patches-actively-exploited-zero.html))

Nearly 100 journalists and other members of civil society using WhatsApp were targeted by a “zero-click” attack ([Guardian](https://www.theguardian.com/technology/2025/jan/31/whatsapp-israel-spyware))

DeepSeek AI tools impersonated by infostealer malware on PyPI ([Bleeping Computer](https://www.bleepingcomputer.com/news/security/deepseek-ai-tools-impersonated-by-infostealer-malware-on-pypi/))

### Can't get enough Talos?

* [Web shell frenzies, the first appearance of Interlock, and why hackers have the worst cybersecurity: IR Trends Q4 2024](https://talostakes.talosintelligence.com/2018149/episodes/16538703-web-shell-frenzies-the-first-appearance-of-interlock-and-why-hackers-have-the-worst-cybersecurity-ir-trends-q4-2024)
* [New TorNet backdoor seen in widespread campaign](https://blog.talosintelligence.com/new-tornet-backdoor-campaign/)

### Upcoming events where you can find Talos

Talos team members: Martin LEE, Thorsten ROSENDAHL, Yuri KRAMARZ, Giannis TZIAKOURIS, and Vanja SVAJCER will be speaking at [Cisco Live EMEA](https://www.ciscolive.com/emea.html). Amsterdam, Netherlands, 9-14 February.

[S4x25](http://s4xevents.com/agenda/) (February 10-12, 2025)
Tampa, FL

[RSA](https://www.rsaconference.com/usa) (April 28-May 1, 2025)
San Francisco, CA

[TIPS 2025](https://www.cyberthreatalliance.org/tips-conference/) (May 14-15, 2025)
Arlington, VA

### Most prevalent malware files from the week

SHA 256: 9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507

MD5: 2915b3f8b703eb744fc54c81f4a9c67f

VirusTotal: <https://www.virustotal.com/gui/file/9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507>

Typical Filename: VID001.exe

Claimed Product: N/A

Detection Name: Win.Worm.Coinminer::1201

SHA256: 47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca

MD5: 71fea034b422e4a17ebb06022532fdde

VirusTotal: <https://www.virustotal.com/gui/file/47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca>

Typical Filename: VID001.exe

Claimed Product: n/a

Detection Name: Coinminer:MBT.26mw.in14.Talos

SHA256:873ee789a177e59e7f82d3030896b1efdebe468c2dfa02e41ef94978aadf006f

MD5: d86808f6e519b5ce79b83b99dfb9294d

VirusTotal:

<https://www.virustotal.com/gui/file/873ee789a177e59e7f82d3030896b1efdebe468c2dfa02e41ef94978aadf006f>

Typical Filename: n/a

Claimed ...