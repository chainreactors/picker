---
title: Checking in on the state of cybersecurity and the Olympics
url: https://blog.talosintelligence.com/threat-source-newsletter-july-12-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-12
fetch_date: 2025-10-06T17:45:44.248849
---

# Checking in on the state of cybersecurity and the Olympics

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

# Checking in on the state of cybersecurity and the Olympics

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, July 11, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

With the 2024 Olympics’ Opening Ceremony only two weeks away now, there is one thing that’s an absolute guarantee of one thing happening during the traditionally unpredictable games: Cyber attacks.

Every time there is a new Olympic Games, there’s a renewed discussion about how threat actors, hacktivists and state-sponsored groups are all gearing up to try to disrupt the games in some way. The Opening Ceremony at the 2018 Olympic Games in South Korea was disrupted by a major cyber attack called [Olympic Destroyer](https://blog.talosintelligence.com/olympic-destroyer/), briefly pausing ticket-taking operations and taking down several Olympics-related websites.

And for this year’s Summer Games, France faces an “[unprecedented level of threat](https://www.weforum.org/agenda/2024/06/paris-olympics-2024-cybersecurity-experts-cyber-threats/),” according to the head of the country’s cybersecurity agency.

That’s because, in our modern day, there is just simply so much to protect. Ninety-nine percent of modern communication occurs over a network at this point, especially when you’re talking about an international event. That means protecting individual inboxes, mail servers, third-party messaging apps, virtual meetings and more.

Each attendee of the games is going to bring in their own devices, too, and connect to whatever public network the Olympics stands up at the arenas or fields where competitions are taking place. That’s tens of thousands of new potential entry points for threat actors.

There are also domains, subdomains, hosts, web applications and third-party cloud resources that the Games rely on, all with their own attack surfaces.

A [study from Outpost24 earlier this year](https://www.darkreading.com/vulnerabilities-threats/paris-olympics-cybersecurity-at-risk-via-attack-surface-gaps) found that the security for all these factors is stronger than when Russia hosted the 2018 FIFA World Cup, which came with a similar set of circumstances and popularity to the Olympics.

Even if a threat actor isn’t successful in some widespread breach that makes international headlines, even smaller-scale threats and actors are just hoping to cause chaos.

Last month, a fake AI-generated movie trailer seemed to show famous actor Tom Cruise condemning the International Olympic Committee in a [fake documentary for Netflix](https://www.cnn.com/2024/06/03/tech/russia-paris-olympics-influence-ops/index.html). That made its rounds on Telegram, along with many threats around [terrorist attacks](https://www.npr.org/2024/06/06/nx-s1-4975698/the-paris-olympics-is-already-facing-cybersecurity-threats) in the hope of scaring attendees away and making the Games seem under-attended.

Other actors are just [looking to spread general misinformation](https://apnews.com/article/france-election-disinformation-russia-olympics-be18d688677240686df200096018f221), capitalizing on recent protests and elections in France to, in their mind, sow chaos in an already chaotic time for the country.

France has been preparing for the bevy of threats with [hundreds of penetration tests](https://www.weforum.org/agenda/2024/06/paris-olympics-2024-cybersecurity-experts-cyber-threats/), tabletop exercises and, of course, [partnering with Cisco](https://www.cisco.com/c/m/fr_fr/official-partner-paris-2024.html) to protect the Olympic Games.

## The one big thing

Based on a [comprehensive review](https://blog.talosintelligence.com/common-ransomware-actor-ttps-playbooks/) of more than a dozen prominent ransomware groups, Talos identified several commonalities in tactics, techniques and procedures (TTPs), along with several notable differences and outliers. Talos’ studies indicate that the most prolific ransomware actors prioritize gaining initial access to targeted networks, with valid accounts being the most common mechanism. Phishing for credentials often precedes these attacks, a trend observed across all incident response engagements, consistent with our 2023 Year in Review report. Over the past year, many groups have increasingly exploited known and zero-day vulnerabilities in public-facing applications, making this a prevalent initial access vector.

### Why do I care?

Key findings indicate that many of the most prominent groups in the ransomware space prioritize establishing initial access and evading defenses in their attack chains, highlighting these phases as strategic focal points. Within the past year, many groups have exploited critical vulnerabilities in public-facing applications, becoming a prevalent attack vector, which we addressed later, indicating an increased need for appropriate security controls and patch management. Ransomware actors also continue to apply a significant focus to defense evasion tactics to increase dwell time in victim networks.

### So now what?

Our blog post includes several recommendations for how potential targets can protect against the TTPs these groups use. That includes consistently applying patches and updates to all systems and software to address vulnerabilities promptly and reduce the risk of exploitation and implement strong password policies that require complex, unique passwords for each account. Additionally, enforce multi-factor authentication (MFA) to add an extra layer of security.

# Top security headlines of the week

**Apple IDs are being targeted in a new SMS-based phishing scam.** Security researchers say that adversaries are sending text messages to iPhone users in the U.S. disguised to look like they’re from Apple but actually intended to steal their Apple l...