---
title: Threat Source newsletter (March 16, 2023) — A deep dive into Talos' work in Ukraine
url: https://blog.talosintelligence.com/threat-source-newsletter-march-16-2023-a-deep-dive-into-talos-work-in-ukraine/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-17
fetch_date: 2025-10-04T09:52:23.531497
---

# Threat Source newsletter (March 16, 2023) — A deep dive into Talos' work in Ukraine

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

# Threat Source newsletter (March 16, 2023) — A deep dive into Talos' work in Ukraine

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, March 16, 2023 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
[Ukraine](https://blog.talosintelligence.com/category/ukraine/)

Welcome to this week’s edition of the Threat Source newsletter.

We’re written a ton about Cisco Talos’ support of Ukraine and our friends and allies there. Now, we encourage you to watch and listen to the folks who have been working hands-on there.

The latest episode of ThreatWise TV from Hazel Burton is the closest look yet at the team Talos assembled in the days after Russia invaded Ukraine to help defend critical infrastructure, intelligence partners and government agencies in Ukraine. You can watch the full documentary above, or over on YouTube [here](https://youtu.be/czrJGym7sR4).

## The one big thing

We have new research out on a [never-before-seen threat actor called YoroTrooper](https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/) that’s carrying out a variety of espionage activity in Europe and Asia. This group has targeted several high-profile government organizations, including one in the European Union, stealing sensitive information such as login credentials, browser histories and cookies, system information and screenshots.

### Why do I care?

While YoroTrooper uses malware associated with other threat actors, such as PoetRAT and LodaRAT, we believe this is a new cluster of activity from an entirely new threat actor. YoroTrooper is clearly going after major targets and has already been successful, so everyone should be on the lookout for these attacks, but especially users and organizations in Commonwealth of Independent States (CIS) countries.

### So now what?

YoroTrooper creates malicious domains and spoofs commonly visited URLs that look like they belong to government agencies in the targeted countries to host its malware. So any time you go to open an email attachment or click on a link in an email, triple check to make sure it’s really where you want to go, or that you can verify the sender. Additionally, the blog outlines a range of protections in Cisco Secure products that can defend and detect this group’s actions.

## Top security headlines of the week

The APLHV ransomware cartel claims to have **successfully stolen data belonging to Amazon’s Ring smart home company.** The ransomware gang’s dark website threatened to leak the data earlier this week, though it showed no evidence of a successful attack. Ring said on Tuesday that it had “no indications that Ring has experienced a ransomware event.” ALPHV, which is known for the BlackCat malware, usually encrypts targets’ data and threatens to leak the stolen information if the victim does not pay the requested ransom payment. Politico also reported this week that Ring will openly share recorded footage with local law enforcement, even if the camera’s user declines to do so, sparking questions about who owns security footage on private property and whether users are compelled to share those recordings. ([Vice](https://www.vice.com/en/article/qjvd9q/ransomware-group-claims-hack-of-amazons-ring), [TechCrunch](https://techcrunch.com/2023/03/14/ring-alphv-ransomware-attack/), [Politico](https://www.politico.com/news/2023/03/07/privacy-loophole-ring-doorbell-00084979))

Sensitive information from D.C. Health Link — the online health insurance marketplace for Washington, D.C. — is **reportedly for sale on the dark web,** potentially affecting White House staff and members of Congress. An internal memo last week warned of a "significant data breach” that potentially exposed the personal information of thousands of federal employees and warned potential victims that their data may have been compromised. As many as 21 members from the U.S. House and Senate could be affected, all of whom get their insurance through the program. In all, 56,415 customers were affected, according to the exchange. ([CBS News](https://www.cbsnews.com/news/data-breach-washington-dc-health-link-user-data-sold-dark-web-congress/), [Roll Call](https://rollcall.com/2023/03/14/house-senate-members-affected-in-dc-health-link-breach-total-21/))

Microsoft **released its monthly security update Tuesday,** disclosing 83 vulnerabilities across the company’s hardware and software line, including two issues that are actively being exploited in the wild, continuing a trend of zero-days appearing in Patch Tuesdays over the past few months. Two of the vulnerabilities included in March’s security update have been exploited in the wild, according to Microsoft, including one critical issue. One of the zero-days included this month, CVE-2023-23397, is a privilege escalation vulnerability in Microsoft Outlook that could force a targeted device to connect to a remote URL and transmit the Windows account's Net-NTLMv2 hash to an adversary. To trigger this vulnerability, a user doesn’t even need to open the email or preview it, the vulnerability is triggered as soon as the email is retrieved by the targeted email server. ([Cisco Talos](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-march-2023-snort-rules-and-prominent-vulnerabilities/), [SecurityWeek](https://www.securityweek.com/microsoft-patch-tuesday-zero-day-attacks/))

## Can’t get enough Talos?

* [Talos Takes Ep. #130: There’s not actually more spam during tax season, just different spam](https://www.buzzsprout.com/2018149/episodes/12413790)
* [Researcher Spotlight: How David Liebenberg went from never having opened Terminal to hunting international APTs](https://blog.talosintelligence.com/researcher-spotlight-david-liebenberg-terminals-to-apts/)
* [YoroTroop...