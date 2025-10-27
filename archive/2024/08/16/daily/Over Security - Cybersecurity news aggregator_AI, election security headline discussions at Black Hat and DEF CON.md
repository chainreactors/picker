---
title: AI, election security headline discussions at Black Hat and DEF CON
url: https://blog.talosintelligence.com/threat-source-newsletter-aug-15-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-16
fetch_date: 2025-10-06T18:05:04.332096
---

# AI, election security headline discussions at Black Hat and DEF CON

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

# AI, election security headline discussions at Black Hat and DEF CON

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, August 15, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

As promised, I’m back this week to recap some of the top stories coming out of Black Hat and DEF CON.

Also as promised, AI was the talk of Vegas during Hacker Summer Camp (or at least from what I’ve been reading and hearing, I wasn’t there in person).

Several exhibitions and talks at both conferences showed how easy it is to create deepfake videos and potentially use them to spread fake news and disinformation. Two security researchers [worked to deepfake themselves](https://www.theregister.com/2024/08/04/realtime_deepfakes_defcon/) and even managed to trick people into believing it really was them on one end of a video conference call.

Others on the show floor had the opportunity to try their hand at creating deepfakes with the help of the Defense Advanced Research Projects Agency (DARPA). One [standout example](https://www.axios.com/2024/08/12/def-con-darpa-deepfake-lab) was a fake video of former Royal Family member Meghan Markle being transposed onto the face of a reporter who could then speak in an approximation of Markle’s voice to say whatever she wanted to.

The good news is that, for now, these types of deepfakes are also incredibly easy for tools and humans alike to detect.

For example, [Adobe’s Content Authenticity Initiative](https://www.pcmag.com/articles/70-ai-adobe-talks-verifying-content-in-the-age-of-deepfakes) is working to place labels on images to indicate that they were originally human-made, and clicking on the image would allow the user to read more information about that image’s history and where and how it had been created.

And in the case of the Meghan Markle deepfake, the SemaFor tool on display at the DEF CON village appropriately detected the image as fake using its scoring system (it didn’t help that the deepfake creator couldn’t account for the fact that the “creator” was wearing glasses).

Security researchers also used DEF CON and Black Hat to show where potential security pitfalls lie with the rise of AI tools and software.

One talk centered around how Microsoft’s AI Copilot could essentially be turned into an [“automated phishing machine”](https://fortune.com/2024/08/13/microsoft-ai-copilot-hacking-prompt-injectoin-attack-black-hat/) by [leaking personal information](https://www.theregister.com/2024/08/08/copilot_black_hat_vulns/), and other researchers warned about an over-reliance on learned language models (LLMs) to write software code that [often includes vulnerabilities and errors](https://www.scmagazine.com/news/ai-will-create-a-tidal-wave-of-buggy-vulnerable-software).

Over in the DEF CON Voting Village, security researchers found their usual swath of vulnerabilities that could be used against popular voting machines and other hardware that will likely be used in the 2024 U.S. presidential election. While we don’t have many details on the specific vulnerabilities found, Voting Village co-founder [Harri Hursti told Politico](https://www.politico.com/news/2024/08/12/hackers-vulnerabilities-voting-machines-elections-00173668) the list of vulnerabilities ran “multiple pages.”

There are a few issues that came to light for me when I was reading about this research and bug hunting: One is that [there isn’t enough time to implement many of these fixes](https://www.nextgov.com/cybersecurity/2024/08/researchers-race-document-voting-machine-vulnerabilities-ahead-november/398768/) before the November election, and there are just so many different pieces of equipment and manufacturers that it’s impossible to properly inspect all these devices. I may feel compelled to write more about this later, but it’s interesting to me that we as a country have managed to decide on essentially two cell phone manufacturers that we’re willing to buy from: Apple and Google. Yet there is no standard for the types, age and vendors that we rely on for our elections, and when they’re not in use, they just sit in storage.

## The one big thing

This month’s [Microsoft Patch Tuesday](https://blog.talosintelligence.com/talos-discovers-11-vulnerabilities-between-microsoft-adobe-software-disclosed-on-patch-tuesday/) includes updates for security vulnerabilities in Office, Visual Studio, Azure, CoPilot, Teams and more. Of the six zero-day vulnerabilities Microsoft disclosed as part of its regular patching cadence, half are local privilege escalation vulnerabilities, meaning adversaries could combine them with other flaws to make their attack more serious or with higher-level privileges. Cisco Talos’ Vulnerability Research team discovered four of the vulnerabilities Microsoft patched this week: CVE-2024-38184, CVE-2024-38185, CVE-2024-38186 and CVE-2024-38187. These are elevation of privilege vulnerabilities in the Microsoft Windows kernel-mode driver that could allow an attacker to gain SYSTEM-level privileges. Talos [researchers also discovered eight vulnerabilities](https://blog.talosintelligence.com/talos-discovers-11-vulnerabilities-between-microsoft-adobe-software-disclosed-on-patch-tuesday/) in CLIPSP.SYS, a driver used to implement Client License System Policy on Windows 10 and 11.

### Why do I care?

Talos discovered three issues, TALOS-2024-1971 (CVE-2024-38062) and TALOS-2024-1970 (CVE-2024-38062) and TALOS-2024-1969 (CVE-2024-38187), an adversary could exploit by sending the targeted system a specially crafted license blob, which could lead to a denial of service. TALOS-2024-1964 (CVE-2024-38184) is exploited in the same way, but in this case, could allow the adversary to bypass the usual security checks that take place and allow them to ta...