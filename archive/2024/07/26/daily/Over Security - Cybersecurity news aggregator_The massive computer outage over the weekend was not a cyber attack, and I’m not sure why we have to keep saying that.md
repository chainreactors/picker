---
title: The massive computer outage over the weekend was not a cyber attack, and I’m not sure why we have to keep saying that
url: https://blog.talosintelligence.com/threat-source-newsletter-july-25-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-26
fetch_date: 2025-10-06T17:44:01.176686
---

# The massive computer outage over the weekend was not a cyber attack, and I’m not sure why we have to keep saying that

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

# The massive computer outage over the weekend was not a cyber attack, and I’m not sure why we have to keep saying that

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, July 25, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

You’re not going to believe this, but there was a lot of misinformation on social media over the weekend after the massive CrowdStrike/Microsoft outage.

As [airlines cancelled flights](https://www.usatoday.com/story/money/2024/07/19/global-outage-communications-systems/74465953007/), hospitals had to reschedule patients and some companies just flat-out couldn’t work on Friday, people were quick to assume that the outage, which was actually [caused by a faulty CrowdStrike Falcon update](https://www.bbc.com/news/articles/cp4wnrxqlewo), [was a cyber attack](https://x.com/search?q=crowdstrike%20hack&src=typed_query).

Media headlines posed the question: [“Cyber attack, or outage?”](https://www.dailymail.co.uk/sciencetech/article-13650599/microsoft-outage-cyberattack.html) [Social posters](https://x.com/SprinterFamily/status/1814278292414853552) quickly assumed this was some sort of “hack.”

On the one hand, I get it. Seeing a “blue screen of death,” often with code that looks indecipherable, has been ingrained into our heads that it’s a “hack,” because that’s how they’ve always been displayed in works of fiction or as the generic image of a “hack” anytime there is actually a real cyber attack.

That’s not to say there aren’t [many lessons to be learned](https://www.cbsnews.com/baltimore/news/cybersecurity-expert-says-microsoft-outage-shows-importance-of-preparedness/) from this outage, and at some point, we’ll be ready to dig into those. But also calling this a cyber attack can spread unnecessary FUD, especially when threat actors are trying to capitalize on the outage to spread malware in [*actual* cyber attacks](https://www.securityweek.com/crowdstrike-incident-leveraged-for-malware-delivery-phishing-scams/).

## The one big thing

Business email compromise (BEC) and ransomware were the [top threats observed by Cisco Talos Incident Response (Talos IR) in the second quarter of 2024](https://blog.talosintelligence.com/ir-trends-ransomware-on-the-rise-q2-2024/), accounting for 60 percent of engagements. Although there was a decrease in BEC engagements from last quarter, it was still a major threat for the second quarter in a row. There was a slight increase in ransomware where Talos IR responded to Mallox and Underground Team ransomware for the first time this quarter, as well as the previously seen Black Basta and BlackSuit ransomware operations.

### Why do I care?

Within BEC attacks, adversaries will compromise legitimate business email accounts and use them to send phishing emails to obtain sensitive information, such as account credentials. Adversaries can also use compromised accounts to send emails with fraudulent financial requests, such as changing bank account information related to payroll or vendor invoices. Targeting employees’ personal mobile devices can be an effective method for initial access because they may not have the same security controls as their corporate devices. Organizations should ensure SMS phishing scams are included in security awareness training for employees.

### So now what?

The lack of MFA remains one of the biggest impediments for enterprise security. All organizations should implement some form of MFA, such as [Cisco Duo](https://www.cisco.com/c/en/us/products/security/adaptive-multi-factor-authentication.html). The implementation of MFA and a single sign-on system can ensure only trusted parties are accessing corporate email accounts to prevent the spread of BEC.

# Top security headlines of the week

**A false narrative spread over the weekend that Southwest Airlines was using a very old version of Windows, which allowed it to escape the CrowdStrike-related outage.** Many news outlets reported that Southwest’s system relies on Windows 3.1, released more than 20 years ago. However, this does not actually appear to be the case, though Southwest’s systems may still be outdated compared to its competitors. Instead, Southwest may have been largely unaffected by the outage simply because it doesn’t use CrowdStrike. Delta, American, Spirit, Frontier, United and Allegiant airlines all reported that they were affected by the outage, forcing the cancellation of thousands of flights across the globe. The source of the story that Southwest uses Windows 3.1 appears to come from posts on social media, the original one of which provided no sources, links or background information to back this statement up. Another popular piece of fake news that made the rounds during the widespread outage was that the Las Vegas Sphere was a victim of the outage, with a fake image spreading online appearing to show the “blue screen of death” on the outside of the concert and event venue. ([Kotaku](https://kotaku.com/southwest-airlines-windows-3-1-blue-screen-crowdstrike-1851603013), [OSNews](https://www.osnews.com/story/140301/no-southwest-airlines-is-not-still-using-windows-3-1/))

**U.K. police arrested a teenager suspected of being a member of the Scattered Spider hacking group and a perpetrator of the massive MGM ransomware attack last year.** The arrest is part of a larger investigation conducted by the National Crime Agency in the U.K. and the U.S.’s FBI into a hacking group that is known to breach networks, steal data and deploy ransomware. While not named explicitly in the arrest announcement, this group is largely known as Scattered Spider. The group breached MGM’s network last year, taking hotel and casino services offline for several days, even just forcing some casino operations to stop altogethe...