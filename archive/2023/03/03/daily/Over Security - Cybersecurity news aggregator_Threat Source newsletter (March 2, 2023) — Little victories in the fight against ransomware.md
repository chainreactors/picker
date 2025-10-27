---
title: Threat Source newsletter (March 2, 2023) — Little victories in the fight against ransomware
url: https://blog.talosintelligence.com/threat-source-newsletter-march-2-2023-little-victories-in-the-fight-against-ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-03
fetch_date: 2025-10-04T08:34:48.169295
---

# Threat Source newsletter (March 2, 2023) — Little victories in the fight against ransomware

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

# Threat Source newsletter (March 2, 2023) — Little victories in the fight against ransomware

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, March 2, 2023 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

For years, we as a cybersecurity community have been discussing ways we can fight the global ransomware problem. This included things like pushing for more sanctions against international ransomware groups, new laws from federal governments and decreased access to virtual currency often used by actors to stay undetected.

Now, here’s the crazy thing: It might be working.

As Talos [discussed in our Year in Review report](https://talosintelligence.com/resources/586), ransomware engagements made up a smaller portion of Cisco Talos Incident Response’s engagements in 2022 compared to the previous year, and there’s been a greater democratization of ransomware families, meaning they’re less siloed and more focused into a few larger groups.

A study from b[lockchain analysis group Chainanalysis](https://blog.chainalysis.com/reports/crypto-ransomware-revenue-down-as-victims-refuse-to-pay/) also found that ransomware groups extorted about $456.8 million from victims in 2022, a roughly 40 percent decrease from 2021 and 2020. The Wall Street Journal also [recently reported](https://www.wsj.com/articles/ransomware-attacks-decline-as-new-defenses-countermeasures-thwart-hackers-23b918a3) that the U.S. government finally feels it's on the offensive when it comes to ransomware.

U.S. Deputy Attorney General Lisa Monaco told the paper that recent ransomware trends reflect "the pivot that we have made to a posture where we’re on our front foot. We’re focusing on making sure we’re doing everything to prevent the attacks in the first place.”

Yes, there are still major ransomware attacks happening ([take the recent Dole cyber attack](https://securityboulevard.com/2023/02/ransomware-attack-brings-dole-operations-to-a-temporary-halt/) that halted production briefly for the food giant). But I feel like it’s not being talked about enough that defenders may be actually making some headway here thanks to private companies (like Talos) and global governments working together.

It seems to be a confluence of several things and not just one magic solution. Governments are taking more [frequent and serious action](https://www.techtarget.com/searchsecurity/news/252527188/DOJ-charges-accused-Lockbit-ransomware-actor) to sanction ransomware actors and the individuals behind them, such as the [recent penalties against Trickbot members](https://www.washingtonpost.com/technology/2023/02/09/ransomware-trickbot-cybercrime-sanctions/). And some actors are even [being arrested](https://www.techtarget.com/searchsecurity/news/252527188/DOJ-charges-accused-Lockbit-ransomware-actor) and being served criminal charges and jail time.

With improved backups, many ransomware targets are also bouncing back better than ever before and can hopefully avoid paying the requested ransom to their attackers. And asset seizures and freezes have even forced some [ransomware groups to lay off people](https://www.businessinsider.com/hackers-ransomware-getting-laid-off-amid-better-cybersecurity-report-2023-2).

2022 could be an aberration. As we also pointed out in our Year in Review, there was a brief pause in ransomware activity at the onset of Russia’s invasion of Ukraine. It could also just be that the defenders got lucky.

This isn’t the time to take our foot off the gas and start turning our attention toward things like AI chatbots — ransomware continues to be a major threat to everyone, including some of society’s most important institutions like hospitals and schools. But I do think it’s important to step back every once in a while to enjoy the victories.

## The one big thing

The U.S. Cybersecurity and Infrastructure Security Agency is warning that attackers [are actively exploiting CVE-2022-36537](https://www.cisa.gov/news-events/alerts/2023/02/27/cisa-adds-one-known-exploited-vulnerability-catalog), an unspecified vulnerability in ZK Framework AuUploader. This poses a significant threat to the software supply chain if any instances are still unpatched, and CISA warned the vulnerability “poses a significant risk to the federal enterprise.” Attackers are reportedly using the vulnerability to install backdoors on servers, specifically through ConnectWise's R1Soft Server Backup Manager, which utilizes the ZK Framework.

### Why do I care?

ZK is an open-source Ajax Web app framework written in Java, allowing users to create GUIs for web applications without a deep knowledge of programming. Many open-source projects and software utilize the framework, so the impact of this vulnerability could be wide-reaching. Open-source reporting indicates that attackers could exploit the vulnerability in ConnectWise R1Soft to bypass authentication, upload a backdoor and gain the ability to execute remote code.

### So now what?

Researchers first disclosed this vulnerability in October, so projects and products that utilize the framework have had plenty of time to patch. ConnectWise released its [own patch on Oct. 28](https://www.connectwise.com/company/trust/security-bulletins/r1soft-and-recover-security-bulletin).

## Top security headlines of the week

The Pentagon is investigating a potential yearslong email leak from the U.S. military’s Special Operations Command. A security researcher discovered that anyone who knew the IP address of the server could access the data without a password. However, the server was secured once the researcher disclosed their findings. The emails leaked included information about U.S. military contracts and messa...