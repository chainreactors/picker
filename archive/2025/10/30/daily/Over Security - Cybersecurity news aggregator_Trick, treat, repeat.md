---
title: Trick, treat, repeat
url: https://blog.talosintelligence.com/trick-treat-repeat/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-30
fetch_date: 2025-10-31T03:14:22.385881
---

# Trick, treat, repeat

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

# Trick, treat, repeat

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, October 30, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

This one is pretty much an updated, Halloween-themed version of my newsletter from [July](https://blog.talosintelligence.com/patch-track-repeat/), including data up through Q3.

October 14th has passed, so [free support for Windows 10](https://www.microsoft.com/en-us/windows/end-of-support) has come to an end, leaving you with no more fixes unless you’re willing to pony up. While users in many countries must now pay to get Windows 10 security updates (the "trick"), private users in the European Economic Area get free security updates (the "treat") until Oct. 14, 2026. This special reward, won after [consumer rights groups pushed](https://www.euroconsumers.org/wp-content/uploads/2025/09/Euroconsumers_vs_Microsoft_092025.pdf) Microsoft to do better under EU law,  means no $30 fee, no reward points, and no cloud backup needed... just a Microsoft account.

There's another trick: The treat is for consumers, not companies, and there are some technical prerequisites (described [here](https://www.microsoft.com/en-us/windows/extended-security-updates)).

While Cybersecurity Awareness Month is coming to end, you still have a chance to reach out to friends and family and encourage them to update their software (one of the [Core4 Messages](https://www.staysafeonline.org/cybersecurity-awareness-month) this year). Get them to enable the Extended Security Updates (ESU), update to Windows 11, or migrate to any other OS that will receive future patches.

Patching is critical. In Q3, we did not run short on vulnerabilities.

![](https://blog.talosintelligence.com/content/images/2025/10/blog_CVEline.jpg)

Figure 1. Total number of CVEs per year.

With roughly 35,000 CVEs by the end of September, we are still tracking a pace of about 130 CVEs per day. If the almost-linear trend continues, we will land at round about 47,000 for 2025. And for legal purposes, I am **not** challenging anyone to break the barrier of 50,000!

This is not just about theoretical vulnerabilities. [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (KEVs) are also on the rise. In comparison, the number of KEVs stayed nearly the same between 2023 and 2024, with 187 and 186, respectively.

![](https://blog.talosintelligence.com/content/images/2025/10/blog_KEVline.jpg)

Figure 2. Total number of KEVs per year.

With 183 at the end of Q3, I think it is safe to say we are going to surpass the number this year. (Spoiler: At the time of writing, there were already 210.) KEVs that affect network-related gear are up by 3% to 28%, which is not a massive increase but for sure a relevant portion. Overall, vendor diversity also continues to expand, increasing from 61 in July to 79 so far this year.

![](https://blog.talosintelligence.com/content/images/2025/10/blog_pie.jpg)

Figure 3. CVE from year added to KEV in 2025.

While the oldest CVE added to the catalog was from 2017 last time, the third quarter introduced a few new negative records from [2007](https://nvd.nist.gov/vuln/detail/CVE-2007-0671), [2013](https://nvd.nist.gov/vuln/detail/CVE-2013-3893), [2014](https://nvd.nist.gov/vuln/detail/cve-2014-3931), and [2016](https://nvd.nist.gov/vuln/detail/CVE-2016-10033).

While this isn't a part of our Q3 data, [CVE-2025-59287](https://www.cve.org/CVERecord?id=CVE-2025-59287) caught my attention late Friday afternoon. I didn’t expect WSUS service to be publicly exposed to the internet, but it found its way into the KEV, too.

In a pumpkin shell: Keep stalking those bugs and patching your spells, because vulnerabilities won’t patch themselves. Happy Halloween!

## The one big thing

We're introducing the Tool Talk series, where Talos shares open-source tools alongside practical insights, tips, and enhancements to help cybersecurity professionals and researchers work smarter and more effectively.

[Our first post](https://blog.talosintelligence.com/dynamic-binary-instrumentation-dbi-with-dynamorio) introduces dynamic binary instrumentation (DBI) and provides a step-by-step guide to building your own DBI tool using the open-source DynamoRIO framework on Windows 11. DBI lets you analyze and modify running programs — crucial for malware analysis, security audits, reverse engineering, and performance profiling — even when you don’t have the original source code. The post covers DynamoRIO’s strengths, compares it to other frameworks, and offers practical examples, including sample code from our GitHub repository.

### Why do I care?

If you’re interested in malware analysis, debugging, or getting a deeper look inside how binaries behave at runtime, this blog shows you how to do all that without needing source code access. DBI tools like DynamoRIO are essential for modern security research, especially for bypassing common malware defenses and anti-analysis tricks.

### So now what?

Ready to get hands-on? Follow the blog’s step-by-step instructions to build your own DBI client, test it out, and explore the example code provided. Whether you’re looking to automate malware analysis, profile software, or just tinker with low-level instrumentation, you’ll find everything you need to kickstart your own DBI projects.

## Top security headlines of the week

**Microsoft issues emergency patch for critical Windows Server bug**
This CVE is a remote code execution (RCE) flaw in WSUS, which is part of Windows Server and allows administrators to schedule, manage, and deploy patches, hotfixes, service packs, and other updates. ([DarkReading](https://www.darkreading.com/vulnerabilities-th...