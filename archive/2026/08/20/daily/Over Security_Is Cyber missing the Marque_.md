---
title: Is Cyber missing the Marque?
url: https://blog.talosintelligence.com/is-cyber-missing-the-marque/
source: Over Security
date: 2026-08-20
fetch_date: 2026-08-21T03:04:52.918121
---

# Is Cyber missing the Marque?

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

# Is Cyber missing the Marque?

By
[Mick Baccio](https://blog.talosintelligence.com/author/nohackme/)

Thursday, August 20, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

*Welcome to this week’s edition of the Threat Source newsletter.*

Hello friend.

I’m [Mick](https://www.linkedin.com/in/nohackme/).

This is my first Threat Source newsletter, so I should probably introduce myself before I start telling you all the things I think you should be paying attention to. With assistance from an unnamed LLM, my bio reads like this:

> *Mick Baccio is a globally recognized security strategist with a career spanning offensive operations, threat intelligence, and national-level incident response. He currently advises organizations around the world through his role at Talos, helping security leaders improve operations through data-informed approaches. Mick was the first-ever Chief Information Security Officer for a U.S. presidential campaign (2020) and previously served in multiple White House administrations as Threat Intelligence Branch Chief.*

> *In his spare time, Mick is the Founder and President of THRUNT**®** Corp, IANS Faculty, and a KC7 Cyber Foundation board member.*

> *DEFCon Goon and Purveyor of Fine Experience.*

> *Veteran.*

I also have a cat named qwerty and own too many Air Jordans.

I’ve spent most of my career somewhere in the intersection of threat intelligence, cybersecurity, government, and the people trying to make sense of all of it. These days, i spend a lot of time thinking about the decisions we make about security ripple outward, often in ways we didn't consider. Most of my ramblings will probably center around that. There will be threats. There will be intelligence. Occasionally something weird, but always something that caught my eye, and maybe worth checking out.

Which brings us this week. I picked a hell of a week to start.

Last Wednesday, the White House issued a presidential memorandum titled “Expanding Capabilities to Combat Transnational Cyber-Enabled Crime.” You should probably [read it](https://www.whitehouse.gov/presidential-actions/2026/08/expanding-capabilities-to-combat-transnational-cyber-enabled-crime/). The memorandum directs the DOJ and DHS to establish a program that can use private companies to conduct cyber operations against transnational criminal organizations outside the United States — beyond providing intelligence and assisting in the investigation. The memorandum explicitly envisions private companies conducting cyber surveillance and cyber effects operations under the direction and delegated authority of the U.S. government.

This is a pretty big thing.

For years, this industry has debated where line should exist between defending a network and reaching through the wire. We’ve debated hack back, active defense, attribution, proportional response, collateral damage, and what roles private companies have in offensive cyber operations. This is absolutely not “[hack back](https://www.congress.gov/bill/115th-congress/house-bill/4036/text)" and calling it that misses important oversight built into the memorandum.

At the same time, let’s be clear about what we are reading. The United States is creating a mechanism for private companies to participate directly in government-authorized offensive cyber operations against systems outside the United States. There will be plenty of debate whether this is good or bad policy; I will leave that for someone else. I’m much more interested in the operational questions it creates.

Who establishes attribution strongly enough to authorize an operation? What happens when criminal and state infrastructure overlap? What happens when infrastructure is compromised and used as an ORB? Who owns access discovered during one of these operations? How is intelligence collected by a private company handled? What happens when a company conducting these operations also provides security services in that country?

Most importantly (in my head): What happens when another country discovers that employees of an American cybersecurity company are conducting offensive operations against infrastructure inside its borders?

This is not an argument against disrupting cybercrime. I’m all for it. These are questions about what happens when we fundamentally change who gets to do the disrupting.

[Read the memorandum](https://www.whitehouse.gov/presidential-actions/2026/08/expanding-capabilities-to-combat-transnational-cyber-enabled-crime/).

Seriously.

What we have today is a framework. In 60 days, we should have a much better idea of what this will look like in practice, so circle that on your calendar. The memorandum gives DOJ and DHS 60 days to establish the operating procedures for the program, and no operation can be approved until those procedures are in place.

In the area between “private cybersecurity company” and “authorized participant in U.S. offensive cyber operations,” the threat model for that company and its employees just changed considerably.

The biggest question isn’t “Does this work?”

It’s whether we’ve fully considered what happens if it does.

[Read the memorandum](https://www.whitehouse.gov/presidential-actions/2026/08/expanding-capabilities-to-combat-transnational-cyber-enabled-crime/).

And in 60 days, come back and ask again.

## The one big thing

Talos posted two blogs on [UAT-10147](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations), a recently discovered Chinese-speaking cybercrime group that uses agentic AI to orchestrate sophisticated post-compromise operations across global web servers. UAT-10147 uses AI to generate operational playbooks, automate exploits, and develop custom malware. This includes the newly identifi...