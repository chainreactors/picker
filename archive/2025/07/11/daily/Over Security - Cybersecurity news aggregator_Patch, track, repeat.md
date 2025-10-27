---
title: Patch, track, repeat
url: https://blog.talosintelligence.com/patch-track-repeat/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-11
fetch_date: 2025-10-06T23:39:47.424844
---

# Patch, track, repeat

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

# Patch, track, repeat

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, July 10, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

We’ve made it halfway through 2025 already! It’s been a while since I last wrote about CVEs and how [free support for Windows 10 will end on October 14, 2025](https://www.microsoft.com/en-us/windows/end-of-support), leaving you with no more security fixes.

While the CVE system remains the global standard for vulnerability reporting, [recent developments](https://krebsonsecurity.com/2025/04/funding-expires-for-key-cyber-vulnerability-database/) have sparked concerns within the community about its long-term stability. Currently, the program operates solely as a U.S. government-funded initiative. Following the last-minute funding extension, we’re now seeing competing ideas and projects emerging. Whether it’s the [CVE Foundation](https://www.thecvefoundation.org/) working to transition from a single funding stream to a diversified and stable model, [ENISA’s EUVD](https://euvd.enisa.europa.eu/), or the [Global CVE Allocation System](https://gcve.eu/) (GCVE), the landscape is changing.

On one hand, a multi-source environment enhances availability and resilience. On the other, this fragmentation raises practical concerns for both researchers and practitioners. We now face questions like “Where should I report a vulnerability?” and “How do I integrate and correlate vulnerability data across multiple sources with multiple identifiers?”

Looking back at the first six months of this year, we see that the rapid pace of CVE publications in 2024 has continued into 2025, with no signs of slowing down. In fact, the current trend suggests that 2025 will surpass last year’s total of a little more than 40,000 CVEs. To illustrate: the first half of 2024 saw an average of 113 CVEs published per day, whereas the first half of 2025 is running at a rate of 131 CVEs per day.

![](https://blog.talosintelligence.com/content/images/2025/07/070825_threatsource_blog_CVEline.jpg)

What concerns me even more is the steep increase in Known Exploited Vulnerabilities (KEVs). It wasn’t just the spike in March — we’re seeing a generally sharper rise overall.

![](https://blog.talosintelligence.com/content/images/2025/07/070825_threatsource_blog_KEVline.jpg)

Vendor diversity also continues to expand, increasing from 45 vendors during the first half of last year to 61 so far this year. Additionally, the proportion of KEVs affecting network-related gear has grown from 22.5% in 2024 to 25% in 2025.

But there’s a small piece of good news: So far, I haven’t seen any CVEs from as far back as 2012 being added to the KEV catalogue like we saw [last year](https://blog.talosintelligence.com/patch-it-up-old-vulnerabilities-are-everyones-problems/). This time, the oldest additions “only” go back to 2017.

![](https://blog.talosintelligence.com/content/images/2025/07/070825_threatsource_blog_pie.jpg)

Keep in mind that the CVE year merely indicates when a vulnerability was reserved or assigned. The vulnerability itself may have existed for many years prior. For example, [the recent sudo/chroot issue](https://www.csoonline.com/article/4018715/how-a-12-year-old-bug-in-sudo-is-haunting-linux-users.html) remained undiscovered for over 12 years.

In a nutshell: Keep tracking, keep patching. Vulnerabilities certainly won’t patch themselves.

## The one big thing

Microsoft’s [July 2025 security update](https://blog.talosintelligence.com/microsoft-patch-tuesday-july-2025/) addresses 132 vulnerabilities, including 14 marked as “critical,” with several remote code execution (RCE) issues affecting Windows, Office, SharePoint and Hyper-V. Although none have been exploited in the wild yet, some vulnerabilities — like those in SharePoint and SPNEGO NEGOEX — are more likely to be targeted and could allow attackers to execute code remotely or locally.

### Why do I care?

These vulnerabilities could let attackers take control of your systems, steal information or disrupt business operations, even if you haven’t seen any attacks yet. If you’re running Windows servers, SharePoint or Microsoft Office, your environment could be at risk, especially for organizations that rely on these products daily.

### So now what?

Don’t wait. Make sure you’re applying Microsoft’s July patches as soon as possible. If you use Cisco Security Firewall or SNORT®, update your rulesets to the latest versions to maximize your protection.

## Top security headlines of the week

**Alleged Chinese hacker tied to Silk Typhoon arrested for cyberespionage**
A Chinese national was arrested in Milan, Italy for allegedly being linked to the state-sponsored Silk Typhoon hacking group, which is responsible for cyberattacks against U.S. organizations and government agencies. ([Bleeping Computer](https://www.bleepingcomputer.com/news/security/alleged-chinese-hacker-tied-to-silk-typhoon-arrested-for-cyberespionage/))

**Jailbreaking AI with information overload**
Researchers say you can trick AI chatbots like ChatGPT or Gemini into teaching you how to make a bomb or hack an ATM if you make the question complicated, full of academic jargon, and cite sources that do not exist. ([404 Media](https://www.404media.co/researchers-jailbreak-ai-by-flooding-it-with-bullshit-jargon/))

**SatanLock is shutting down**
The announcement that the group was closing its doors first came through its official Telegram channel and dark web leak site. Hunters International, another well-known ransomware group, also recently announced that it was shutting down its operations. ([Dark Reading](https://www.darkreading.com/threat-intelligence/satanlock-ransomware-group-...