---
title: Cybersecurity on a budget: Strategies for an economic downturn
url: https://blog.talosintelligence.com/cybersecurity-on-a-budget-strategies-for-an-economic-downturn/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-29
fetch_date: 2025-10-30T03:12:39.968693
---

# Cybersecurity on a budget: Strategies for an economic downturn

[Blog](/)

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

# Cybersecurity on a budget: Strategies for an economic downturn

By
[Jerzy ‘Yuri’ Kramarz](https://blog.talosintelligence.com/author/jerzy/),
[Nate Pors](https://blog.talosintelligence.com/author/nate/),
[David Roman](https://blog.talosintelligence.com/author/david-roman/)

Wednesday, October 29, 2025 06:00

[The Need to Know](https://blog.talosintelligence.com/category/the-need-to-know/)

* During economic uncertainty, businesses face the challenge of maintaining strong cybersecurity while managing tightened budgets.
* Cyber threats can become more numerous, motivated, and persistent during economic downturns, making the need for resilient, cost-effective security measures critical.
* This blog shares practical strategies to help absorb budget cuts while minimizing the damage to an organization’s cybersecurity posture.

---

## Learning from history

As many seasoned industry professionals remember, 2008 – 2010 was a tough time for the tech industry as well as the larger U.S. economy. During the Great Recession, unemployment rose as high as 10%, and IT and cybersecurity budgets were certainly not spared. During the 2020 COVID-19 crisis, the need for tech workers and larger IT budgets to support remote work was so strong that it outweighed the global economic slowdown. As a result, many new IT professionals never experienced what a real recession feels like.

The FBI noted a [22.3% increase in cybercrime complaint submissions](https://archives.fbi.gov/archives/news/stories/2010/march/ic3_031710/internet-crime-complaints-on-thr-rise) from 2008 – 2009, which some attributed in part to unemployed, financially desperate tech workers turning their skillsets to crime. At that time, threat actors mostly targeted individuals in the form of scams, fraud, and other crimes. In today’s environment, a similar economic downturn could easily lead to a surge in the number and talent of ransomware operators.

Why? Unlike in the Great Recession, most corporate networks are now remote- or hybrid-enabled by default. While nothing about a network’s attack surface would inherently change due to an economic downturn, any increase in the number and skill level of attackers, decrease in the number and skill of defenders, or decrease in the quality of security measures could have devastating consequences for the IT environment owner.

## Defend legacy hardware/software

As was painfully highlighted in recent years by Salt Typhoon incursions into telecommunications networks, working with legacy hardware and software is a risk many businesses take. As belts tighten during an economic downturn, cybersecurity budgets will decrease, and many businesses will inevitably need to postpone technology upgrades beyond end of life. While this introduces risk, there are a few solid strategies to mitigate that risk.

### Defense in depth and zero trust

While these terms were both solid contenders for the No. 1 Sales Buzzword of 2023, they reflect a valuable underlying principle: Assume the adversary is going to gain a foothold and architect accordingly.

If a business must continue to use 40% legacy firewalls and only has budget to replace 60%, those legacy firewalls should be positioned in the interior of the network versus on the perimeter and logically separated so an adversary cannot “island-hop” from one to the next using the same vulnerability. If a legacy server must be positioned in a public-facing location, it should be placed in a tightly-controlled DMZ where compromise of that server would not lead to further network intrusion.

No breach is desirable, but you can minimize the potential for lateral movement.

### Lock down unnecessary functionality

Many vulnerable applications and systems are targeted via plugins or extra features that an organization isn’t even using. The classic example is a webserver with an abandoned WordPress plugin that later is discovered to be vulnerable. Another example is the SSH login method on a VMWare ESXi hypervisor — an organization may accidentally leave this enabled and allow an adversary to log in as root.

For vulnerable systems and software, it is critical to review what is strictly necessary for it to operate and disable all other functionalities. This is an important part of attack surface reduction.

## Optimize open- and closed-source software

While closed-source commercial security tools usually offer the easiest setup and best overall experience, transitioning a budget-constrained organization to a blend of commercial and open-source software may be the right answer for maximum efficacy. Here are some rules of thumb for selection.

### Open source

Open-source software excels when the product does not depend on frequent updates or detailed technical support. Initial setup may be involved and challenging, but financial savings can be significant. A good current example is the Zeek network security monitor, which is not a standalone security product but significantly enhances network-based detection capabilities. An open-source SIEM solution that may be suitable for smaller businesses is Security Onion.

### Closed source/commercial

For solutions that depend on frequent updates, particularly time-sensitive signature/definition updates, commercial security solutions are the only answer. This primarily includes endpoint detection and response (EDR)/antivirus (AV), firewall, and DNS security solutions. Recognizing that this is a mandatory expenditure will help solidify planning for other areas of cost savings.

## Configure what you already have

For organizations that don’t have the budget for new security systems, making the most of what you already have can go a long way to ensure that basic level of security and hardening is applied. For further information beyond what is reflected below, consider reading [this paper](https://b...