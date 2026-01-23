---
title: I scan, you scan, we all scan for... knowledge?
url: https://blog.talosintelligence.com/i-scan-you-scan-we-all-scan-for-knowledge/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-22
fetch_date: 2026-01-23T03:33:05.103352
---

# I scan, you scan, we all scan for... knowledge?

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

# I scan, you scan, we all scan for... knowledge?

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Thursday, January 22, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

*“Upon us all a little rain must fall” — Led Zeppelin, via Henry Wadsworth Longfellow*

I recently bumped into a colleague with whom I spent several years working in an MSSP environment. We had very different roles within the organization, so our viewpoints, both then and now, were very different. He asked me the question I hear almost every time I speak somewhere: “What do you think are the most essential things to protect your own network?” This always leads to my top answer — the one that no one ever wants to hear.

“Know your environment.”

It led me down a path of thinking about how cyclical things are in the world of cybersecurity and how we, the global “we”, have slipped back to a place where reconnaissance is too largely ignored in our day-to-day workflow.

Look, I know that we all have alert fatigue. We’re managing too many devices, dealing with too many data points, generating too many logs, and facing too few resources to handle it all. So my “Let’s not ignore reconnaissance” mantra might not be regarded well at first.

Here’s the thing: It’s always tempting to trim your alerts and reduce your ticketing workload. After all, attack signals seem more “impactful” by nature, right? But I've always believed it’s a mistake to dismiss reconnaissance events to clear the way for analysts to look for the “real” problems. I always go back to my first rule: “Know your environment.” The bad actors are only getting better at the recon portion, both on the wire and in social engineering.

AI tooling has made a lot of the most challenging aspects of reconnaissance automagical. If you search the dark web for postings from initial access brokers (IABs), you’ll find that they excel in reconnaissance and understanding your ownenvironment. They’re quick to find every Windows 7 machine still on your network, not to mention your unpatched printers, smart fridges, and vulnerable thermostats.

I get that we can’t get spun up about every half-open SYN, but spotting when these events form a pattern is exactly what we’re here for, and it’s as important as tracking down directory traversal attempts.

*“Behind the clouds is the sun still shining;
Thy fate is the common fate of all...” — Henry Wadsworth Longfellow*

## The one big thing

Cisco Talos researchers recently [discovered and disclosed vulnerabilities](https://blog.talosintelligence.com/foxi-and-epic-games/) in Foxit PDF Editor, Epic Games Store, and MedDream PACS, all of which have since been patched by the vendors. These vulnerabilities include privilege escalation, use-after-free, and cross-site scripting issues that could allow attackers to execute malicious code or gain unauthorized access.

### Why do I care?

 These vulnerabilities could have enabled attackers to escalate privileges, execute arbitrary code, or compromise sensitive systems, potentially leading to data breaches or system outages. Even though patches are available, unpatched systems remain at risk.

### So now what?

Organizations should make sure all affected software is updated with the latest patches and review security monitoring for signs of exploitation attempts. Additionally, defenders should implement layered defenses and educate users on the risks of opening suspicious files or clicking unknown links to reduce the likelihood of successful attacks.

## Top security headlines of the week

**How a hacking campaign targeted high-profile Gmail and WhatsApp users across the Middle East**
TechCrunch analyzed the source code of the phishing page, and believes the campaign aimed to steal Gmail and other online credentials, compromise WhatsApp accounts, and conduct surveillance by stealing location data, photos, and audio recordings. ([TechCrunch](https://techcrunch.com/2026/01/16/how-a-hacking-campaign-targeted-high-profile-gmail-and-whatsapp-users-across-the-middle-east/?utm_source=tldrinfosec))

**LastPass warns of fake maintenance messages targeting users' master passwords**
The campaign, which began on or around Jan. 19, 2026, involves sending phishing emails claiming upcoming maintenance and urging them to create a local backup of their password vaults in the next 24 hours. ([The Hacker News](https://thehackernews.com/2026/01/lastpass-warns-of-fake-maintenance.html))

**Everest Ransomware claims McDonalds India breach involving customer data**
The claim was published on the group’s official dark web leak site earlier today, January 20, 2026, stating that they exfiltrated a massive 861GB of customer data and internal company documents. ([HackRead](https://hackread.com/everest-ransomware-mcdonalds-india-breach-customer-data/))

**North Korea-linked hackers pose as human rights activists, report says**
North Korea-linked hackers are using emails that impersonate human rights organizations and financial institutions to lure targets into opening malicious files. ([UPI](https://www.upi.com/Top_News/World-News/2026/01/19/North-Korea-hackers-Konni-spear-phishing-APT-Genians/5761768807686/?utm_source=tldrinfosec))

**Hackers use LinkedIn messages to spread RAT malware through DLL sideloading**
The attack involves approaching high-value individuals through messages sent on LinkedIn, establishing trust, and deceiving them into downloading a malicious WinRAR self-extracting archive (SFX). ([The Hacker News](https://thehackernews.com/2026/01/hackers-use-linkedin-messages-to-spread.html))

## Can’t get enough Talos?

[**Engaging Cisco Talos Incident Response is just the beginning**](https://blogs.cisco.com/security/en...