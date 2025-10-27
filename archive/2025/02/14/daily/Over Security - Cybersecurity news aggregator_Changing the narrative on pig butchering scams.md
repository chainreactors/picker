---
title: Changing the narrative on pig butchering scams
url: https://blog.talosintelligence.com/changing-the-narrative-on-pig-butchering-scams/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-14
fetch_date: 2025-10-06T20:37:59.028921
---

# Changing the narrative on pig butchering scams

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

# Changing the narrative on pig butchering scams

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, February 13, 2025 14:05

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source Newsletter.

Love is in the air this week. Wait, is that love? Or is it some tech bro with a housing development company (that would totally love to meet in person but can’t this week) emailing you about an investment opportunity in his cryptocurrency scheme?

You may be seeing a lot of ‘Beware of romance/ pig butchering scams’ articles around Valentines Day. This isn’t really one of those. Although, if said tech bro initiates a course of love bombing mixed in with wire transfer requests, report that dude quicker than the roadrunner declares “meep meep”.

I recently came across an article on [The Hacker News](https://thehackernews.com/2024/12/interpol-pushes-for-romance-baiting-to.html) that talked about how Interpol is pushing for a “linguistic shift” when it comes to pig butchering scams. They’re advocating for the term to be replaced by ‘romance baiting’.

In a statement, Interpol explained their reasoning:

*"The term 'pig butchering' dehumanizes and shames victims of such frauds, deterring people from coming forward to seek help and provide information to the authorities,"*

Pig butchering originates from a Chinese phrase. Its meaning is derived from “fattening a pig before the slaughter”. When we put that in the context of online scams, the emphasis is on the victim, with some not so nice connotations (and a certain sense of inevitability attached to it).

By flipping the script and renaming pig butchering as romance baiting, Interpol suggests this could have a positive effect on the psychological nature of being targeted:

*"Words matter. We've seen this in the areas of violent sexual offences, domestic abuse, and online child exploitation. We need to recognize that our words also matter to the victims of fraud," INTERPOL Acting Executive Director of Police Services Cyril Gout said.*

*"It's time to change our language to prioritize respect and empathy for the victims, and to hold fraudsters accountable for their crimes."*

I wholeheartedly agree. Victim blaming only causes more harm. The more we can do to encourage people to report perpetrators, without feeling a sense of shame, the better.

What do you think? Will you be changing the narrative the next time you talk about romance scams? Are there any other terms in our industry that potentially put more focus on the victim than the adversary?

## Newsletter reader survey

**We want your feedback! Tell us your thoughts and five lucky readers will receive Talos Swag boxes.**

[Launch survey](https://forms.office.com/r/PhJ1FFRfHe)

### The one big thing

In the [latest Talos Vulnerability Deep Dive](https://blog.talosintelligence.com/small-praise-for-modern-compilers-a-case-of-ubuntu-printing-vulnerability-that-wasnt/), the team picked out something that had caught their attention during an earlier investigation of the macOS printing subsystem: IPP over USB specification, which defines how printers that are available over USB can only still support network printing via Internet Printing Protocol (IPP). During this new investigation, Talos decided to look at how other operating systems handle the same functionality.

The result? Some pretty good news actually. Although the potential vulnerability Talos discusses in [this article](https://blog.talosintelligence.com/small-praise-for-modern-compilers-a-case-of-ubuntu-printing-vulnerability-that-wasnt/) is very real, mitigating circumstances make it less severe. The vulnerability is discovered and made unexploitable by modern compiler features, and we are highlighting this as a rare win.

### Why do I care?

We often hear of all the failings of software and vulnerabilities and mitigation bypasses, and we felt we should take this opportunity to highlight the opposite. In this case, modern compiler features, static analysis via -Wstringop-overflow and strong mitigation via FORTIFY\_SOURCE, saved the day.

### So now what?

The modern compiler features detailed above should always be enabled by default. Additionally, those compiler warnings are only useful if someone actually reads them. Check out [this excellent write up](https://blog.talosintelligence.com/small-praise-for-modern-compilers-a-case-of-ubuntu-printing-vulnerability-that-wasnt/) of the vulnerability, and the proof of concept.

### Top security headlines of the week

[Lawmakers unite to push forward Cyber Force:](https://www.politico.com/newsletters/weekly-cybersecurity/2025/02/10/lawmakers-unite-to-push-forward-cyber-force-00203283) “A group of House lawmakers are working to keep the idea of creating a Cyber Force at the Pentagon a top cyber policy topic on Capitol Hill this year.” (Politico).

[Authorities Disrupt 8Base Ransomware:](https://www.securityweek.com/authorities-disrupt-8base-ransomware-arrest-four-russian-operators/) “The 8Base ransomware group’s infrastructure has been disrupted and leaders have been arrested in an international law enforcement operation, Europol announced.” (Security Week)

[Magecart Attackers Abuse Google Ad Tool to Steal Data:](https://www.darkreading.com/cyberattacks-data-breaches/magecart-attackers-abuse-google-ad-tool-steal-data) “Attackers are smuggling payment card-skimming malicious code into checkout pages on Magento-based e-commerce sites by abusing the Google Tag Manager ad tool.” (Dark Reading).

[Update to iOS 18.3.1 Right Now. There’s a ‘Sophisticated Attack’ Risk, Apple Says:](https://www.vice.com/en/article/apple-says-update-to-ios-18-3-1-immediately/) “A physical attack may disable USB Restricted Mode on a locked device...