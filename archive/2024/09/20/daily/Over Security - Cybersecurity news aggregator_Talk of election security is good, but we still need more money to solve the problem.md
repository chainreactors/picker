---
title: Talk of election security is good, but we still need more money to solve the problem
url: https://blog.talosintelligence.com/threat-source-newsletter-sept-19-24/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-20
fetch_date: 2025-10-06T18:29:13.086922
---

# Talk of election security is good, but we still need more money to solve the problem

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

# Talk of election security is good, but we still need more money to solve the problem

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, September 19, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Last week, six Secretaries of State [testified to U.S. Congress](https://www.youtube.com/watch?v=OrbFLbGTChM&ab_channel=AssociatedPress) about the current state of election security ahead of November’s Presidential election.

Some of the same topics came up as usual — disinformation campaigns, influence from foreign actors, and the physical protection of poll workers on election day.

It’s good that these conversations are continuing after the various revelations that came out after the 2016 presidential election, and election security is an issue globally, especially this year when there are major elections taking place in hundreds of countries.

As with many things in politics and life, though, there is still an issue of money.

Talk of the importance of election security is positive, but at the end of the day, states and municipalities will need monetary and human resources to implement the appropriate defenses and protect everything from voting machines to online vote-tallying systems and social media disinformation campaigns.

Arizona Secretary of State Adrian Fontes used his time in front of Congress to ask for additional funding, because his state has been unable to execute all their election security goals.

“None of this is free and none of it is cheap,” he said. “Our operations, administration and security depend on intermittent, rare and never enough funding for the Help America Vote Act grants that we are occasionally given by Congress.”

Additional federal funds became available for U.S. elections in 2017 after the Department of Homeland Security deemed election systems to be critical infrastructure. But this year, Congress only allocated $55 million in federal grant dollars to states for security and other improvements to elections. For comparison’s sake, presidential and Congressional candidates in the U.S. spent [$14 billion on their election campaigns,](https://www.bbc.com/news/av/election-us-2020-54696386) more than double the amount from 2016.

At the time, Republican lawmakers in the House voted to totally zero out the fund for the Help America Vote Act, or HAVA, grants, which have existed since 2002.

One lobbyist even told [the Stateline outlet earlier this year](https://stateline.org/2024/06/19/states-struggle-with-unreliable-federal-funding-for-making-sure-elections-are-secure/) that many states were trying to stretch the money they do get from the HAVA program across multiple years for fear of a lack of funding in the coming election cycles.

JP Martin, deputy communications director for the Arizona secretary of state, said in that same article that Arizona (a crucial swing state in most presidential elections) has had to put a hiring freeze in place because a lack of federal funding.

So, talk, awareness and planning to secure elections are all positive things. But at the end of the day, all these technologies and solutions, and the people that provide them, cost money.

## The one big thing

Cisco Talos’ Vulnerability Research team discovered [two vulnerabilities](https://blog.talosintelligence.com/vulnerability-roundup-sept-11-2024/) have been disclosed and fixed over the past few weeks. Talos discovered a time-of-check time-of-use vulnerability in Adobe Acrobat Reader, one of the most popular PDF readers currently available, and an information disclosure vulnerability in the Microsoft Windows AllJoyn API.

### Why do I care?

AllJoyn is a DCOM-like framework for creating method calls or sending one-way signals between applications on a distributed bus. It primarily is used in internet-of-things (IoT) devices to tell the devices to perform certain tasks, like turning lights on or off or reading the temperature of a space. [TALOS-2024-1980](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1980) (CVE-2024-38257) could allow an adversary to view uninitialized memory on the targeted machine. Adobe Acrobat Reader, one of the most popular pieces of PDF reading software currently available, contains a time-of-check, use-after-free vulnerability that could trigger memory corruption, and eventually, arbitrary code execution.

### So now what?

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org, and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website.

# Top security headlines of the week

**Experts and governments are still unpacking a wave of pager and handheld radio explosions in the Middle East.** The attacks appeared to target members of the armed group Hezbollah in Lebanon when hundreds of devices exploded simultaneously on Tuesday, killing multiple people. The international community has been left wondering if this was some type of cyber attack or intentional physical implants in the devices. Messages sent at the time of the attack appeared to come from Hezbollah leadership but instead triggered the explosions. Most analysts are assuming that this was a hardware supply chain attack, in which the pagers were tampered with somehow during manufacturing or while they were in transit. Supply chain attacks are normally carried out at the software level. So far, no one has taken credit for the attacks, though Hezbollah is blaming Israel, one of its chief antagonists. ([Reuters](https://www.reuters.com/world/middle-east/dozens-hezbollah-members-wounded-lebanon-when-pagers-exploded-sources-witnesses-2024-09-17/), [BBC](https://www.bbc.com/news/articles/cz04m913m49o))

**Ransomware gangs are increasingly lever...