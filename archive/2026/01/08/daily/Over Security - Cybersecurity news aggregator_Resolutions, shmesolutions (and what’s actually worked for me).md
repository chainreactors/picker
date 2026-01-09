---
title: Resolutions, shmesolutions (and what’s actually worked for me)
url: https://blog.talosintelligence.com/resolutions-shmesolutions-and-whats-actually-worked-for-me/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-08
fetch_date: 2026-01-09T03:31:42.993888
---

# Resolutions, shmesolutions (and what’s actually worked for me)

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

# Resolutions, shmesolutions (and what’s actually worked for me)

By
[Amy Ciminnisi](https://blog.talosintelligence.com/author/amy-ciminnisi/)

Thursday, January 8, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

I went to bed at 8:30 p.m. on New Year’s Eve, and I think that’s pretty indicative of how I approach the whole idea of New Year’s resolutions.

I love to count down to the new year with loved ones as much as the next person, but I have really conflicted feelings about traditional resolutions. On one hand, it’s great to have goals for the future and pick a day to start putting them into action. On the other, why wait until the New Year, and why pick goals that are often wildly unsustainable? It feels like it just promotes an “all or nothing” approach, and starts the year on a disappointing note if you stumble even a little. Life happens, and many resolutions don’t give enough grace.

Here are some resolutions I failed at this past year:

* Lift weights three days/week for a whole year: Close, but no cigar!
* Journal at least one sentence every day: Yeah, I failed at this one pretty quickly. I’m not a journal person.
* Knit at least three sweaters: I made a shirt, almost finished a vest, and spent a ton of money on yarn.

I have done a lot of things I’m proud about this year, so then... what *has* worked? An intention that I’ve held throughout the year is turning “shoulds” into setting plans into motion right away. For example, “I should host a one-time book club to discuss my favorite book” becomes “I just posted in my neighborhood Facebook page to find people who are interested and pick a date.” Or “I should finish my certification” becomes “I just set a weekly three-hour calendar block, and I won’t move it unless there’s an emergency.”

That shift in mindset reminds me a lot of what works in cybersecurity. Our industry is full of ambitious, high-level goals: “Eliminate all vulnerabilities,” “achieve zero trust,” or “stop every threat.” These aspirations are important, but the reality is that security happens in small, consistent actions: patching systems as soon as updates are available, educating teams on the latest phishing techniques, reviewing logs regularly, or simply responding quickly to a new alert.

Just like with personal resolutions, there’s often pressure in security to be perfect, to never let anything slip through the cracks. Even the organizations that have amazing budget and headcount will face challenges and setbacks, and no environment is ever perfectly secure. What matters most is how we respond in the moment, learn from what’s happened, and keep moving forward.

So as we head into 2026, whether you’re setting personal goals or planning your organization’s security strategy, consider focusing less on flawless resolutions and more on building habits that adapt to change. Celebrate the small wins, reflect on what you’ve accomplished, and don’t be afraid to pivot when things don’t go as planned. Show up every day and take that next step.

## The one big thing

Earlier today, Cisco Talos [disclosed a sophisticated threat actor](https://blog.talosintelligence.com/uat-7290) we track as UAT-7290, who has been active since at least 2022. UAT-7290 is tasked with gaining initial access as well as conducting espionage-focused intrusions against critical infrastructure entities in South Asia. UAT-7290's arsenal includes a malware family consisting of implants we call RushDrop, DriveSwitch, and SilentRaid. Our findings indicate that UAT-7290 conducts extensive technical reconnaissance of target organizations before carrying out intrusions.

### Why do I care?

UAT-7290 targets telecom and network infrastructure, which, if compromised, can have cascading impacts on national security, business operations, and customer data. Their advanced tactics, use of publicly available exploits, and ability to establish persistent footholds make detection and remediation difficult.

### So now what?

Review and apply the latest ClamAV and Snort signatures (see the [blog](https://blog.talosintelligence.com/uat-7290)) to detect and block UAT-7290’s malware and activity. Audit your edge devices (especially those exposed to the internet) for signs of compromise, weak credentials, or unpatched vulnerabilities, and prioritize patching and hardening them. Make sure your incident response plans are ready to address potential intrusions involving advanced persistent threats (APTs).

## Top security headlines of the week

**U.S. cyber pros plead guilty over** **BlackCat** **ransomware activity**
Two US citizens plead guilty to working as ALPHV/BlackCat ransomware affiliates in 2023. Along with an unnamed third conspirator, they were previously employed by security firms Sygnia and DigitalMint. ([DarkReading](https://www.darkreading.com/cyber-risk/us-cyber-pros-plead-guilty-over-ransomware-activity))

**European** **Space Agency** **(ESA)** **confirms breach after hacker offers to sell data**
The ESA has confirmed that some of its systems have been breached and is working on securing compromised devices. The hacker offered to sell 200GB of allegedly stolen data from ESA’s systems, including files from private Bitbucket repositories. ([SecurityWeek](https://www.securityweek.com/european-space-agency-confirms-breach-after-hacker-offers-to-sell-data/))

**Sophisticated** **ClickFix** **campaign targeting hospitality sector**
Fake Booking reservation cancellations and fake BSODs trick victims into executing malicious code leading to RAT infections. ([SecurityWeek](https://www.securityweek.com/sophisticated-clickfix-campaign-targeting-hospitality-sector/)) ([The Hacker News](https://thehackernews.com/2026/01/fake-booking-emails-redir...