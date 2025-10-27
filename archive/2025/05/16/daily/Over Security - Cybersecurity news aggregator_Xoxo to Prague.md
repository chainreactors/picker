---
title: Xoxo to Prague
url: https://blog.talosintelligence.com/xoxo-to-prague/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-16
fetch_date: 2025-10-06T22:27:17.951763
---

# Xoxo to Prague

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

# Xoxo to Prague

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, May 15, 2025 14:01

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

I haven’t been to Prague in a while, which is a pity. It’s a wonderful city — great people, amazing food. I’ve visited customers there, held team meetings at the local office (shoutout to Petr!) and spent some memorable summer days off. But none of those are why I’m sending my greetings this time.

Last week, anyone trying to access LockBit’s dark web affiliate panels was greeted by a defaced page with the message:

> "Don't do crime CRIME IS BAD xoxo from Prague”

Alongside the message was a download link for a compressed archive called “paneldb\_dump.zip” —  a 7.5MB file that extracts to a 26MB clear-text SQL dump containing 20 tables. The breach exposed a rare, unfiltered look into LockBit’s operations.

While most articles focused on the nearly 60,000 Bitcoin addresses or the credentials for 75 admins and affiliates (all with plaintext passwords), I have to admit that I was mesmerized by the “chats” table. 4,423 messages distributed across 208 victims, spanning from Dec. 2024 to April 2025, these chats reveal the raw tactics, ransom demands and negotiation strategies of both affiliates and victims. Sometimes there was just a single unanswered message; in other cases, over 300 messages included “technical support” for unrecoverable files, and even requests for refunds.

Ransom demands varied widely, from just a few thousand dollars to as much as $2 million in one notable case. There were also several instances of confusion — some mistakenly thought the demand was "100,000 bitcoins" when it was actually "100,000 dollars in bitcoin.” Additionally, there was a case involving a hosting company breach, where it was the company’s customers who ultimately suffered the consequences. The chat exposed that LockBit encrypted all the data with the same key; even though not all victims were willing or able to pay the ransom, LockBit insisted the hoster pay the full amount, making it difficult to collect the asked ransom.

Negotiations were often pressured by tight deadlines, but European bank holidays on Good Friday, Easter Monday and May 1st further complicated the situation. Multiple times there were situations where the ransom demand increased after a specific deadline. I even found messages from victims asking for more time so they could gather funds in smaller amounts to avoid detection under local anti-money laundering laws.

In another chat, a victim tried to negotiate by pleading inability to pay a $100k ransom, only to be told, “Seven directors at 14k can’t chime in?” This clearly shows that the “Analytics Department” of LockBit did their homework.

The level of “trust” placed in affiliates was also striking. Messages included:

![](https://blog.talosintelligence.com/content/images/2025/05/rounded2.png)

Interestingly, that last service was offered for an extra fee. Let me share some of their $10,000 “tips” for free:

![](https://blog.talosintelligence.com/content/images/2025/05/rounded_1.png)

With these $10,000 tips, I personally think it would be better to get advice before an incident from [Talos Incident Response](https://talosintelligence.com/incident_response). They can also provide guidance and proactive support as part of the Talos IR Retainer.

The LockBit leak is a rare window into the mechanics of cybercrime and the human stories behind the headlines. And, for now, xoxo to Prague.

## The one big thing

[Cisco Talos has observed a growing trend of attack kill chains being split into two stages](https://blog.talosintelligence.com/redefining-initial-access-brokers/) — initial compromise and subsequent exploitation — executed by separate threat actors. In response to these evolving threats, we have refined the definitions of initial access brokers (IABs) to include subcategories such as financially-motivated initial access (FIA), state-sponsored initial access (SIA), and opportunistic initial access (OIA).

### Why do I care?

This trend complicates traditional threat modeling and actor profiling, as it requires understanding the intricate relationships and interactions between various groups. For example, hunting and containment strategies that may defend against one type of IAB may not be suitable for another.

### So now what?

We have identified [several methods](https://blog.talosintelligence.com/compartmentalized-threat-modeling/) for analyzing compartmentalized attacks and propose an extended Diamond Model, which adds a “Relationship Layer” to enrich the context of the relationships between the four features. Familiarize yourself with the new taxonomy we propose, and incorporate this new methodology for modeling and tracking compartmentalized threats into your toolkit.

## Top security headlines of the week

**Operation Moonlander**
A criminal proxy network that has been around for more than 20 years and was built on thousands of infected IOT and end-of-life (EoL) devices was dismantled in an international operation. ([U.S. Attorney’s Office](https://www.justice.gov/usao-ndok/pr/botnet-dismantled-international-operation-russian-and-kazakhstani-administrators))

**Supply Chain Compromise**
A deprecated node.js package with more than 40k downloads per week, ‘rand-user-agent' has been compromised with a malicious payload dubbed “[RATatouille](https://www.aikido.dev/blog/catching-a-rat-remote-access-trojian-rand-user-agent-supply-chain-compromise)”. This is a clear case of a supply chain attack. ([Aikido](https://www.aikido.dev/blog/catching-a-rat-remote-access-trojian-rand-user-agent-supply-chain-compromise))

**Ascension Health Data Breac...