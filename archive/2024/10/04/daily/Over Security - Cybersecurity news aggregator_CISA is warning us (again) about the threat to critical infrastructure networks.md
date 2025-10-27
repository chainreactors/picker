---
title: CISA is warning us (again) about the threat to critical infrastructure networks
url: https://blog.talosintelligence.com/threat-source-newsletter-oct-3-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-04
fetch_date: 2025-10-06T18:52:26.533011
---

# CISA is warning us (again) about the threat to critical infrastructure networks

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

# CISA is warning us (again) about the threat to critical infrastructure networks

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, October 3, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Government-run water systems and other critical infrastructure are still at risk from state-sponsored actors, according to a [renewed warning](https://www.cisa.gov/news-events/alerts/2024/09/25/threat-actors-continue-exploit-otics-through-unsophisticated-means) from the U.S. Cybersecurity and Infrastructure Security Agency.

CISA released an advisory last week on the matter of days after a small water treatment facility in Kansas was [forced into manual operations](https://www.securityweek.com/kansas-water-facility-switches-to-manual-operations-following-cyberattack/) after a cyber attack.

I feel like this is just the latest in a string of warnings that we’ve been talking about since the [Colonial Pipeline attack in 2021](https://blogs.cisco.com/security/key-takeaway-from-the-colonial-pipeline-attack) that forced a gasoline shortage across the Eastern U.S. We’ve been discussing the importance of defending critical infrastructure [for years now](https://youtu.be/mPcA-Ho6pFs), so what’s new now?

For starters, it seems like the frequency of these attacks [seems to be on the rise](https://therecord.media/cisa-warns-of-attacks-aginst-water-systems-arkansas-city). And many efforts to regulate cybersecurity policies and procedures in the industry have thus far fallen flat.

The White House is [reportedly working on rolling out a second wave of cybersecurity recommendations](https://www.wsj.com/articles/fears-of-weakness-in-water-cybersecurity-grow-after-kansas-attack-67ca2dd2) for water treatment facilities on the back of the attack in Kansas that affected the public water supply of 11,000 people. Although the cyber attack did not actually affect anyone from getting their water, it does raise the question of how much of an issue this could be if a state-sponsored actor were to target a facility in a town with a larger population, or if there weren’t backup plans in place to operate the facility manually.

The U.S. Environmental Protection Agency (EPA) said last year that it had to [pull a memo](https://therecord.media/epa-says-litigation-from-republicans-and-water-companies-forced-withdrawal-of-cyber-memo) outlining cybersecurity standards at water treatment plants because of constant legal action from state and federal lawmakers and private water companies. And the American Water Works Association (a non-profit lobbying organization representing more than 50,000 members) has [advocated for facilities and groups like the AWWA to write their own cybersecurity policies](https://therecord.media/water-industry-wants-to-write-its-own-cyber-rules) rather than relying on the U.S. government.

All of that is to say, despite what lessons we thought we learned from Colonial Pipeline, none of those lessons have been able to be put into practice, and we’re still where we were with cybersecurity policies and regulations three years ago.

Despite urging from the industry and some lawmakers, I’ve yet to see these groups write any of their own policies, so even if they have that power, they don’t seem to be taking advantage of it. So when CISA puts out this type of alert again in a few months after whatever future incident lies ahead, I would expect to see more action from all parties involved rather than another round of words warning that attacks can, and will, happen.

## The one big thing

Talos has [recently observed an attack](https://blog.talosintelligence.com/threat-actor-believed-to-be-spreading-new-medusalocker-variant-since-2022/) leading to the deployment of a MedusaLocker ransomware variant known as “BabyLockerKZ.” This actor has been active since at least late 2022 and targets organizations worldwide, although the number of victims was higher than average in EU countries until mid-2023 and, since then, in South American countries. We assess with medium confidence that the actor is financially motivated, likely working as an IAB or an affiliate of a ransomware cartel.

### Why do I care?

The actor behind these attacks seems to be particularly active, infecting more than 100 organizations per month, according to Talos telemetry. This reveals the professional and highly aggressive nature of the attacks and is coherent with the activity we would expect from an IAB or ransomware affiliate. As with any ransomware, BabyLockerKZ looks to encrypt targets’ files and lock them down until the target pays the request ransom.

### So now what?

Talos has released several new Snort rules and ClamAV signatures that detect the activity of this group and BabyLockerKZ. This group is also known to use several publicly available tools in their attacks, such as [Mimikatz](https://malpedia.caad.fkie.fraunhofer.de/details/win.mimikatz), which are well-known to the security community at this point. For more on living-off-the-land binaries (LoLBins) that attackers like this one are increasingly using, read our [blog post here](https://blog.talosintelligence.com/hunting-for-lolbins/).

# Top security headlines of the week

**International law enforcement agencies worked together to arrest and unmask four individuals believed to be associated with the LockBit ransomware group.** As part of this campaign, investigators have also linked one of the LockBit members to Evil Corp, a Russian-backed cybercrime gang. At a press conference announcing the arrests, representatives from the U.K.’s National Crime Agency said that Evil Corp maintained a “privileged” relationship with the Russian government and was often asked to carry out targeted cyber attacks against NATO countries. LockBit is tr...