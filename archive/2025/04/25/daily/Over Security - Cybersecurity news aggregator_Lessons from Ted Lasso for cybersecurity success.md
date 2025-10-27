---
title: Lessons from Ted Lasso for cybersecurity success
url: https://blog.talosintelligence.com/lessons-from-ted-lasso-for-cybersecurity-success/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-25
fetch_date: 2025-10-06T22:06:24.195026
---

# Lessons from Ted Lasso for cybersecurity success

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

# Lessons from Ted Lasso for cybersecurity success

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Thursday, April 24, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

"Be curious, not judgmental," Ted Lasso says, misattributing Walt Whitman. We forgive Ted because... well, he's Ted Lasso.

If you’ve not watched the first season of Ted Lasso, there is a defining moment where Ted confronts a nefarious bully. While putting him in his place with kindness and skill, Ted refers to this quote. It’s a defining moment not only for Ted but for the secondary and tertiary characters in the scene. One of the questions that I'm asked most when public speaking is “How do I get into Talos?” For people considering a new career, it’s “How do I get into cybersecurity?” To all those questions, my answer is "Be curious, not judgmental."

I think there is no greater skill necessary in security than intellectual curiosity. If you have that, you can learn the rest. The hiring process to get in the door at Talos is extremely challenging and the candidates are incredible. That's why when I interview candidates for various roles in Talos I rarely, if ever, fixate on a niche skillset, instead focusing on the prospective employee’s intellectual curiosity. I ask weird questions that don’t seem related to the specific job role, not in an effort to throw them off but simply because I am curious and hope that they are as well.

*Do you like to read? Do you ever read books outside of your normal wheelhouse? What are some favorite fiction and non-fiction books? Do you have a favorite craft or hobby? How many different Linux distributions have you installed? What are your 5 favorite board games? Do you play video games, and if so, what are a few favorites from each platform and decade?*

These kinds of questions help me identify what kind of innate curiosity that the prospective candidate possesses and from their answers we will invariably fall down a rabbit hole while my co-workers shake their heads at me in disdain.

Beyond that, I always listen for my favorite answer: “I don’t know, but...” There’s no better answer to a very difficult question than “I don’t know, but I’d probably try X,” or “I don’t know, but I’d love to learn...”

Barbecue sauce.

## The one big thing

Cisco Talos has released a blog post on the initial access broker (IAB) we call [“ToyMaker”](https://blog.talosintelligence.com/introducing-toymaker-an-initial-access-broker/) — a financially-motivated threat actor. They deploy their custom-made backdoor we call “LAGTOY” and extract credentials from the victim enterprise. LAGTOY can be used to create reverse shells and execute commands on infected endpoints.

### Why do I care?

A compromise by LAGTOY may result in access handover to a secondary threat actor. Specifically, we’ve observed ToyMaker hand over access to Cactus, a double extortion gang who employed their own tactics, techniques and procedures (TTPs) to carry out malicious actions across the victim’s network. [Our blog](https://blog.talosintelligence.com/introducing-toymaker-an-initial-access-broker/) details a timeline with turnaround time from ToyMaker to Cactus.

### So now what?

Cisco Talos has released information to help ensure protection including techniques and related IOCs. Check out the [blog post](https://blog.talosintelligence.com/introducing-toymaker-an-initial-access-broker/) for full details.

## Top security headlines of the week

**Apple says zero-day bugs exploited against ‘specific targeted individuals’ using iOS.** Apple has released new software updates across its product line to fix two security vulnerabilities, which the company said may have been actively used to hack customers running its mobile software, iOS. ([TechCrunch](https://techcrunch.com/2025/04/16/apple-says-zero-day-bugs-exploited-against-specific-targeted-individuals-using-ios/))

**Microsoft purges millions of cloud tenants in the wake of Storm-0558.** In an effort to thwart state-sponsored activity stemming from preventable security issues, Microsoft is making significant efforts to purge inactive Azure cloud tenants and take comprehensive inventory of cloud and network assets. [(DarkReading](https://www.darkreading.com/cloud-security/microsoft-millions-cloud-tenants-storm-0558))

**Researchers warn of critical flaw found in Erlang OTP SSH.** The vulnerability could allow unauthenticated attackers to gain full access to a device. Many of these devices are widely used in IoT and telecom platforms. ([cybersecuritydrive](https://www.cybersecuritydive.com/news/researchers-warn-of-critical-flaw-found-in-erlang-otp-ssh/745900/))

**CISA flags actively exploited vulnerability in SonicWall SMA devices.** The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added a security flaw impacting SonicWall Secure Mobile Access 100 Series gateways to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation. ([The Hacker News](https://thehackernews.com/2025/04/cisa-flags-actively-exploited.html))

## Can’t get enough Talos?

* [Talos Takes: Year in Review Special: Part 3](https://www.buzzsprout.com/2018149/episodes/16988482)
* [TL,DR: Attacks on identity, and Multi Factor Authentication](https://youtu.be/2SXpiZfcIh8)
* [Unmasking the new XorDDoS controller and infrastructure](https://blog.talosintelligence.com/unmasking-the-new-xorddos-controller-and-infrastructure/)

## Upcoming events where you can find Talos

* [RSA](https://www.rsaconference.com/usa) (Apr. 28 – May 1) San Francisco, CA
* [PIVOTcon](https://pivotcon.org/) (May 7 – 9) Malaga, Spain
* [CTA TIPS 2025](https://www.cyberthreatalliance.org/tips-confer...