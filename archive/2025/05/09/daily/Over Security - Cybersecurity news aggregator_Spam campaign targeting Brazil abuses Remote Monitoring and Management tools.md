---
title: Spam campaign targeting Brazil abuses Remote Monitoring and Management tools
url: https://blog.talosintelligence.com/spam-campaign-targeting-brazil-abuses-rmm-tools/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-09
fetch_date: 2025-10-06T22:29:56.707529
---

# Spam campaign targeting Brazil abuses Remote Monitoring and Management tools

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

# Spam campaign targeting Brazil abuses Remote Monitoring and Management tools

By
[Guilherme Venere](https://blog.talosintelligence.com/author/guilherme/)

Thursday, May 8, 2025 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[initial access broker](https://blog.talosintelligence.com/category/initial-access-broker/)

* Cisco Talos identified a spam campaign targeting Brazilian users with commercial [remote monitoring and management](https://lolrmm.io/) (RMM) tools since at least January 2025. Talos observed the use of PDQ Connect and N-able remote access tools in this campaign.
* The spam message uses the Brazilian electronic invoice system, [NF-e](https://docs.oracle.com/en/applications/jd-edwards/localizations/9.2/eoabz/understanding-nota-fiscal-and-nfe-generation.html), as a lure to entice users into clicking hyperlinks and accessing malicious content hosted in Dropbox.
* Talos has observed the threat actor abusing RMM tools in order to create and distribute malicious agents to victims. They then use the remote capabilities of these agents to download and install Screen Connect after the initial compromise.
* Talos assesses with high confidence that the threat actor is an initial access broker (IAB) abusing the free trial periods of these RMM tools.

---

Talos recently observed a spam campaign targeting Portuguese-speaking users in Brazil with the intention of installing commercial remote monitoring and management (RMM) tools. The initial infection occurs via [specially crafted spam messages](https://blog.talosintelligence.com/ir-trends-q1-2025/) purporting to be from financial institutions or cell phone carriers with an overdue bill or electronic receipt of payment issued as an NF-e (see Figures 1 and 2).

![Picture](https://blog.talosintelligence.com/content/images/2025/05/data-src-image-843fa8f9-561b-4fa2-94e5-a133746471ac.png)

Figure 1. Spam message purporting to be from a cell phone provider.

![Picture](https://blog.talosintelligence.com/content/images/2025/05/data-src-image-9f63a517-f4b0-4d3f-a7c7-5195c4d7ad61.png)

Figure 2. Spam message masquerading as a bill from a financial institution.

Both messages link to a Dropbox file, which contains the malicious binary installer for the RMM tool. The file names also contain references to NF-e in their names:

* AGENT\_NFe\_<random>.exe
* Boleto\_NFe\_<random>.exe
* Eletronica\_NFe\_<random>.exe
* Nf-e<random>.exe
* NFE\_<random>.exe
* NOTA\_FISCAL\_NFe\_<random>.exe

*Note: <random> means the filename uses a random sequence of letters and numbers in that position.*

The victims targeted in this campaign are mostly C-level executives and financial and human resources accounts across several industries, including some educational and government institutions. This assessment is based on the most common recipients found in the messages Talos observed during this campaign.

![Picture](https://blog.talosintelligence.com/content/images/2025/05/data-src-image-5ca62d69-b812-4471-b7b5-2db93ebe6465.jpeg)

Figure 3. Targeted recipients.

## Abusing RMM tools for profit

This campaign's objective is to lure the victims into installing an RMM tool, which allows the threat actor to take complete control of the target machine. [N-able RMM Remote Access](https://www.n-able.com/products/n-sight-rmm/remote-access) is the most common tool distributed in this campaign and is developed by N-able, Inc., previously known as SolarWinds. N-able is aware of this abuse and took action to disable the affected trial accounts. Another tool Talos observed in some cases is [PDQ Connect](https://www.pdq.com/landing/pdq-connect/), a similar RMM application. Both provide a 15-day free trial period.

To assess whether these actors were using a trial version rather than stolen credentials to create these accounts, Talos checked samples older than 15 days and confirmed all of them returned errors that the accounts were disabled, while newer samples found in the last 15 days were all active.

Talos also examined the email accounts used to register for the service. They all use free email services such as Gmail or Proton Mail, as well as usernames following the theme of the spam campaign, with few exceptions where the threat actors used personal accounts. These exceptions are potentially compromised accounts which are being abused by the threat actors to create additional trial accounts. Talos did not find any samples in which the registered account was issued by a private company, so we can assess with high confidence these agents were created using trial accounts instead of stolen credentials.

*N-able is aware of this abuse and took action to disable the affected trial accounts.*

Talos found no evidence of a common post-infection behavior for the affected machines, with most machines staying infected for days before any other malicious activity was executed by the tool. However, in some cases, we observed the threat actor installing an additional RMM tool and removing all security tools from the machine a few days after the initial compromise. This is consistent with actions of initial access broker (IAB) groups.

An IAB's main objective is to rapidly create a network of compromised machines and then sell access to the network to third parties. Threat actors commonly use IABs when looking for specific target companies to deploy ransomware on. However, IABs have varied priorities and may sell their services to any threat actors, including state-sponsored actors.

Adversaries’ abuse of commercial RMM tools has steadily increased in recent years. These tools are of interest to threat actors because they are usually digitally signed by recognized entities and are a fully featured backdoor. They also have little to no cost in software or infrastructure, as all of this is general...