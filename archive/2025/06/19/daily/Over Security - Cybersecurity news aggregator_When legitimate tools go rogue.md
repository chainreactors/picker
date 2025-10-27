---
title: When legitimate tools go rogue
url: https://blog.talosintelligence.com/when-legitimate-tools-go-rogue/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-19
fetch_date: 2025-10-06T22:55:43.834961
---

# When legitimate tools go rogue

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

# When legitimate tools go rogue

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Wednesday, June 18, 2025 06:09

[The Need to Know](https://blog.talosintelligence.com/category/the-need-to-know/)

Late one Tuesday night, Elena’s phone buzzed with an alert from her company’s SIEM. Her team had set up a rule to flag when certain system tools — `whoami`, `nltest` and `nslookup`—were run one after another in quick succession. That exact pattern had just triggered on a computer in the Finance Department. The time? 2:13 a.m.

Concerned, Elena logged in from home to investigate. Almost immediately, two more alerts appeared. One signaled that Mimikatz (a tool popular with threat actors to steal credentials) had been used on the same Finance machine. The other reported a PsExec download (a command line tool used to execute processes) on a domain controller.

Elena and her team began isolating systems and tracing the activity, determined to stop it before it spread any further. What first looked like routine system commands now clearly pointed to something more serious.

This story is a compartmentalized version of something we’re seeing more and more often in [Cisco Talos Incident Response engagements](https://blog.talosintelligence.com/ir-trends-q1-2025/): Rather than inventing their own tools, attackers are making use of familiar, legitimate software - just with a very different purpose.

## What exactly are LOLBins?

A big part of this trend revolves around “living off the land binaries,” or LOLBins. LOLBins are tools built into an operating system that attackers can use to carry out malicious actions without having to download or install any new software or utilities.

They’re especially concerning because they’re already installed, trusted, and frequently used for normal IT tasks, making them difficult to detect or block without disrupting operations.

Defenders can reference the “Living Off The Land Binaries, Scripts and Libraries” or LOLBAS project, which maintains a list of known LOLBins on [GitHub](https://lolbas-project.github.io/).

## But it’s not just LOLBins…

LOLBins were used often across [Talos IR engagements in 2024](https://blog.talosintelligence.com/year-in-review-exploring-vulnerabilities-email-threats-and-adversary-tooling/), but we actually saw a wider variety of commercial and open-source tools used as well. Threat actors likely gravitate towards these because they can choose which tools best suit their needs best (or which commercial tools will blend into the victim environment).

![](https://blog.talosintelligence.com/content/images/2025/06/UsedTools_fig10.jpg)

Take DonPAPI, for example. This is an open-source tool observed in several recent Talos IR engagements that automates credential dumping remotely on multiple Windows computers. It locates and retrieves Windows Data Protection API (DPAPI) protected credentials, a process also known as “DPAPI dumping.” DonPAPI searches for certain files, including Wi-Fi keys, RDP passwords and credentials saved in web browsers, to help authenticate and move laterally to identify other assets in the environment.

From an identity perspective, open-source tools like DonPAPI pose a significant risk to organizations based on their wide availability on code repositories like GitHub and their ease of installation.

## Legit tool, suspicious intent

Here’s how this plays out in the field, using the top three examples of most used tools as observed in Cisco Talos’ [2024 Year in Review](https://blog.talosintelligence.com/year-in-review-exploring-vulnerabilities-email-threats-and-adversary-tooling/):

![](https://blog.talosintelligence.com/content/images/2025/06/UsedTools_table.jpg)

These tools weren’t built for attackers, but they’ve become some of the most common ingredients in ransomware and advanced persistent threat (APT) campaigns.

In a recent episode of [The Talos Threat Perspective](https://www.youtube.com/watch?v=p1s_-AajB-w), one of our senior Talos IR consultants spoke about tools that were created for legitimate purposes (e.g., HRSword, REMCOS RAT and Cobalt Strike), but played a large part in the ransomware engagements investigated by Talos IR in 2025.

## Remote Access Management tools

Lately, Talos has seen an increase in the use of remote monitoring and management (RMM) tools during attacks - the same kind of software IT teams and managed service providers rely on to access systems remotely. These tools are designed for legitimate use, but in the wrong hands, they become a stealthy way to maintain persistence on compromised systems without raising alarms.

One colleague shared a story that stuck with me: In some incidents, the attackers showed up with an entire toolkit of RMM software, testing each one to see which would slip through unnoticed (or not get blocked). Often, they’d use exactly the same tools already trusted by the target or their service provider, such as ScreenConnect or AnyDesk.

It’s like they arrived at the front door with a ring full of keys, trying each one until something clicked. And when the tool they use is something the environment already knows and trusts the question becomes: how do you spot the intruder when they’re using your own keys?

## How do you detect something that looks normal?

Let’s go back to Elena. Her team stopped the attack not just because of the alert, but because they knew what should be running on that workstation. They had clear asset inventories and network behavior baselines, and they conducted continuous anomaly monitoring.

That’s really the heart of what works best when it comes to detecting these types of attacks:

* Asset management: Know what’s installed and where. Know who owns what assets and what high-privileged accounts are for.
* Behavioral baselining: Understand what “normal” looks ...