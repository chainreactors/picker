---
title: Link up, lift up, level up
url: https://blog.talosintelligence.com/link-up-lift-up-level-up/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-29
fetch_date: 2025-10-07T00:50:18.464437
---

# Link up, lift up, level up

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

# Link up, lift up, level up

By
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/)

Thursday, August 28, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

As summer retreats into the rear-view mirror, I’d like to take a moment to reflect on one of my favorite things about the cybersecurity profession: the community. Earlier this month, I attended [Black Hat USA 2025](https://www.blackhat.com/us-25/) and [DEF CON 33](https://defcon.org/) in scalding hot Las Vegas, NV. We often refer to it as “hacker summer camp,” where all the security nerds of various stripes congregate to eat, drink, party, hack and reforge or make new bonds of fellowship with other awesome hackers. Hacker summer camp is, simply put, a whirlwind of activity, from the talks to see, villages to visit, parties to attend, and knowledge to gain. In 5 days, I think I walked almost 30 miles. By the end I was exhausted, but happy to have learned so much and see many of my hacker friends.

For all the fun and learning you can have at summer camp, it's a very privileged position to be able to attend. Las Vegas is [not a cheap town](https://www.thestreet.com/travel/las-vegas-strip-faces-same-problem-as-disney-world-its-just-too-expensive). Hotels, flights and food — everything, really — is more expensive than average. A Black Hat badge is $1,000+, and DEF CON $500+. If you’re new to this space and early in your career, or your company doesn’t have the money to send you, the FOMO can be real. Earlier in my career, getting the opportunity to visit hacker summer camp — either with my company covering my costs or me paying out of pocket — wasn’t going to happen.

I bring this up not to flex that I went to BH/DEF CON, but to tell you that as good as those conferences are, there is [*so much more*](https://infosec-conferences.com/)*.* Do not be daunted by what is inaccessible but know that there are other conferences out there for like-minded hackers who want to learn and share knowledge with you, wherever you are in the world. Are you in high school? I promise you there are [clubs and organizations](https://hackclub.com/) there to help you. College? There are student clubs and organizations there that will welcome you. And if you’re looking for projects and [contests](https://hackaday.io/contests), there are quite a few out there. And [hackathons](https://www.openhackathons.org/s/upcoming-events)? [I got you covered](https://www.hackerearth.com/challenges/), fam.

It’s also important to know that there are smaller information security conferences around the world. Perhaps the most popular and usually super local is Bsides. [Check them out](https://bsides.org/w/page/12194156/FrontPage) — their website has a calendar that might have one local to you.

Infosec is as much a calling as it is a career. You were drawn to this space for a reason — and finding friends and colleagues who match your vibe is important to both grow as a human, but also to maintain a healthy relationship with this industry, especially one that’s notoriously capable of burning you out. We as humans are social creatures, and we need social interaction, even if it’s limited doses (I see you, introverts). Our professions are a natural magnet to pull others into our orbit. I can tell you so many of the things that I consider personal career milestones happened because I talked with fellow security practitioners over drinks or a meal, and something [truly wonderful happened](https://blog.talosintelligence.com/project-powerup-ukraine-grid/).

So go find your people, lean into the things you are a total security nerd about, and enjoy the fellowship and growth. You’ll be all the better for it.

## The one big thing

Last week, [Talos shared that ransomware attacks in Japan](https://blog.talosintelligence.com/ransomware_incidents_in_japan_during_the_first_half_of_2025/) surged by about 1.4 times in the first half of 2025, with small and medium-sized companies (especially manufacturing) being the hardest hit. The Qilin group was the most active, and a new player, "Kawa4096," also began targeting Japanese businesses. Even though some major ransomware groups were shut down, new threats are quickly taking their place.

### Why do I care?

The ransomware landscape is always changing, and it often highlights vulnerabilities in small and mid-sized businesses in critical industries like manufacturing. With new ransomware groups like Kawa4096 emerging and techniques evolving, the risks are growing, and attackers are finding new ways to target organizations that may not have strong defenses.

### So now what?

While small- to mid-size manufacturing companies are the most targeted in Japan, it’s important for all businesses to stay updated on threats, invest in cybersecurity, and train their teams to spot suspicious activity. ClamAV detections are also available in the [blog](https://blog.talosintelligence.com/ransomware_incidents_in_japan_during_the_first_half_of_2025/).

## Top security headlines of the week

**Organizations warned of exploited Git vulnerability**
The US cybersecurity agency CISA on Monday warned that the flaw, tracked as CVE-2025-48384 (CVSS score of 8.1), is an arbitrary file write during the cloning of repositories with submodules that use a ‘recursive’ flag. ([SecurityWeek](https://www.securityweek.com/organizations-warned-of-exploited-git-vulnerability/))

**CISA updates SBOM recommendations**
The document is primarily meant for federal agencies, but CISA hopes businesses will also use it to push vendors for software bills of materials. ([Cybersecurity Dive](https://www.cybersecuritydive.com/news/cisa-sbom-software-bill-of-materials-guidance-update/758414/))

**AI-p...