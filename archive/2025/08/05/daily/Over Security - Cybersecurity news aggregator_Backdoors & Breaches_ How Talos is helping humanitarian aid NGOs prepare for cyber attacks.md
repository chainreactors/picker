---
title: Backdoors & Breaches: How Talos is helping humanitarian aid NGOs prepare for cyber attacks
url: https://blog.talosintelligence.com/backdoors-breaches-how-talos-is-helping-humanitarian-aid-ngos-prepare-for-cyber-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-05
fetch_date: 2025-10-07T00:49:31.312404
---

# Backdoors & Breaches: How Talos is helping humanitarian aid NGOs prepare for cyber attacks

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

![](/content/images/2025/03/backdoors_header_v2-1-.jpg)

# Backdoors & Breaches: How Talos is helping humanitarian aid NGOs prepare for cyber attacks

By
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/)

Monday, August 4, 2025 12:00

[Headlines](/category/headlines/)

* In 2023, Talos collaborated with NetHope and Cisco Crisis Response to create a customized Backdoors & Breaches expansion deck for international humanitarian organizations, addressing their unique cybersecurity challenges.
* The new expansion deck helps NGOs with constrained budgets improve proactive security and incident response skills through engaging tabletop exercises that are specific to their technical, political, and logistical challenges.
* Hundreds of expansion decks have been distributed to international NGOs, and Talos has received positive feedback for their practicality and relevance.
* Building on this success, we partnered with NGO-ISAC to develop a United States-specific deck for domestic NGOs, enhancing their cybersecurity preparedness.

---

## Humanitarian organizations and the cybersecurity landscape

Hello friends! My name is Joe Marshall and I work at Cisco Talos as a cyber threat researcher and security strategist. Throughout my travels with Talos, I’ve met extraordinary individuals and organizations who fight injustices in a variety of ways: caring for children, feeding the unhoused, promoting democracy, protecting the environment, or resettling refugees who are fleeing from war.

In moments of unimaginable crisis and pain, the international non-governmental organization (NGO) folks I met are on the front lines distributing aid, documenting human rights abuses, assisting first responders, and offering comfort to people who have had their worlds upended. I unabashedly admire and respect them.

Unfortunately, international NGOs have historically struggled in cybersecurity. No matter an NGO’s size, limited donor and grant dollars mean that sustaining the organization competes with delivering aid, leaving little (if any) funding for cybersecurity. As a result, public sector offensive actors, [mercenary spyware](https://blog.talosintelligence.com/mercenary-intellexa-predator/) organizations, and [state-sponsored actors](https://blog.talosintelligence.com/tinyturla-next-generation/) take advantage of this to target or financially exploit these NGOs, even though they are assisting some of the most vulnerable people in the world. No one gets a pass in this modern era of cybercrime!

## Helping the helpers

In 2023, the [Cisco Crisis Response](https://www.cisco.com/c/en/us/about/csr/impact/cisco-crisis-response.html) (CCR) team — a group that helps local agencies and communities prepare for, respond to, and sustainably rebuild from crises — approached my team at Talos with a rare opportunity to help incorporate cybersecurity into their work alongside their partner, NetHope.

[NetHope](https://nethope.org/) is a humanitarian assistance organization that “helps our nonprofit Members effectively address the world’s most pressing challenges through collaboration, collective action and the smarter use of technology.” They also host the NetHope Global Summit, a yearly gathering of international NGOs to discuss technical issues and solutions to enable their member NGOs’ missions.

Before this project, I was not well-versed in the challenges of the NGO cybersecurity landscape or operating realities. Every business vertical is unique, and my first few meetings with NetHope forced me to confront the stark realities of the [cybersecurity poverty line](https://www.cyberthreatalliance.org/cta-webinar-the-cybersecurity-divide-addressing-the-cyber-poverty-line/). With NGOs’ limited cybersecurity budgets, expertise, and resources, I knew our project had to have a low barrier to entry.

After much brainstorming, I suggested that we create an NGO-centric version of the popular cybersecurity tabletop exercise, “Backdoors & Breaches,” to keep workers’ incident response skills sharp.

## What is a tabletop exercise?

A tabletop exercise (TTX) is a group thought experiment. The “Game Master” presents various scenarios and variables to their players, who are usually team leaders in their business, to see how they respond as a group. At a high level, TTXs are a way to help your team prepare for worst-case scenarios and cost-effectively develop plans and responses to a variety of incidents. As they say, “Fortune favors the prepared.”

For example, a hospital might want to conduct a TTX to develop and test incident response and data recovery if hackers were to attack their electronic health records. An electric utility company might conduct a TTX to test critical infrastructure restoration and coordination with emergency responders. And, of course, a humanitarian assistance organization may need to protect itself against cyber attacks to keep their life-saving work going!

## An introduction to Backdoors & Breaches

Backdoors & Breaches is a card-based TTX developed and published under a GNU license by [Black Hills Information Security](https://www.blackhillsinfosec.com/). It’s a novel game designed to teach both technical and non-technical players cybersecurity incident response in a format similar to the popular Dungeons & Dragons roleplaying game. Here’s an example of gameplay at the RSA Conference, with the digital version of the game:

If you want to accommodate a specific technical aspect of security, like industrial control systems, the cloud, or threat hunting, you can modify Backdoors & Breaches with expansion decks. Customizing cards to reflect your team's unique circumstances can result in better buy-in and even a higher level of preparedness when a breach occurs.

## Talos and NetHope create a new expansion

It was this potential customization th...