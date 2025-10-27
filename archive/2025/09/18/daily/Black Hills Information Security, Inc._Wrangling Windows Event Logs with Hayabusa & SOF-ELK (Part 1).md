---
title: Wrangling Windows Event Logs with Hayabusa & SOF-ELK (Part 1)
url: https://www.blackhillsinfosec.com/wrangling-windows-event-logs-with-hayabusa-sof-elk-part-1/
source: Black Hills Information Security, Inc.
date: 2025-09-18
fetch_date: 2025-10-02T20:18:11.684452
---

# Wrangling Windows Event Logs with Hayabusa & SOF-ELK (Part 1)

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

17
Sep
2025

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Hunt Teaming](https://www.blackhillsinfosec.com/category/blue-team/hunt-teaming/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/)
[evtx](https://www.blackhillsinfosec.com/tag/evtx/), [hayabusa](https://www.blackhillsinfosec.com/tag/hayabusa/), [SOF-ELK](https://www.blackhillsinfosec.com/tag/sof-elk/)

# [Wrangling Windows Event Logs with Hayabusa & SOF-ELK (Part 1)](https://www.blackhillsinfosec.com/wrangling-windows-event-logs-with-hayabusa-sof-elk-part-1/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/PCake-Headshot-462x625-1-150x150.jpg)

| [Patterson Cake](https://www.blackhillsinfosec.com/team/patterson-cake/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/Win_logs_header.png)

Event Logs are one of my favorite Windows artifacts, but they are voluminous, and only a small percentage of events provide value during most security investigations. There are typically a few hundred thousand event log entries on a single Windows endpoint and, though they are not difficult to acquire, parsing, filtering, and searching to effectively and efficiently derive actionable intelligence can be challenging. In part 1 of this post, we’ll discuss how *Hayabusa* and “Security Operations and Forensics ELK” (*SOF-ELK*) can help us wrangle EVTX files (Windows Event Log files) for maximum effect during a Windows endpoint investigation! In part 2, we’ll discuss scaling this to many systems in conjunction with my “Rapid Endpoint Investigations” workflow (<https://github.com/secure-cake/rapid-endpoint-investigations>; <https://www.youtube.com/live/XfUjST9kXdU?feature=shared>).

*Hayabusa* meaning “peregrine falcon” in Japanese, is the namesake of a pretty sick Suzuki sport bike, as well as a Windows event log “fast forensic timeline generator and threat hunting tool.” *Hayabusa* was created and is supported by Yamato Security, with over 4,000 SIGMA rules and more than 170 built-in detection rules to help us find the event log entries we are looking for! When we run *Hayabusa* against our EVTX files, we get timeline output in CSV or JSON file format with rule “hits” containing date/timestamp, rule title, severity level (“info” to “emergency”), and event details.

You can check out the *Hayabusa* GitHub repo here: <https://github.com/Yamato-Security/hayabusa>

When performing Windows endpoint investigations, with a typical average of 200K-500K event log entries per host, we can use *Hayabusa* to reduce and prioritize our event analysis. We’ll get around 75% reduction in event-log entries in our *Hayabusa* timeline output, which is hugely significant, but this still leaves us with tens of thousands of entries per endpoint. We can prioritize our investigation by further filtering our *Hayabusa* output by severity, focusing on high-severity rule hits, e.g. “critical” and “high.” Even with this level of reduction and prioritization, we may still be wrangling many thousands of entries, which can be challenging via Excel or another CSV/JSON tool!

Enter “Security Operations and Forensics ELK,” aka *SOF-ELK*, which is a “big data analytics platform focused on the typical needs of computer forensic investigators/analysts,” available in a prepackaged Virtual Machine, with prebuilt parsers for *Hayabusa* ingestion (among many other log/file types), and an intuitive web UI for searching and filtering. Thank you, Phil Hagen!

You can check out the *SOF-ELK* GitHub repo, download a prepackaged VM, etc. here: <https://github.com/philhagen/sof-elk>

To recap, EVTX files are a useful Windows endpoint investigative artifact, *Hayabusa* can help us find events of interest, and *SOF-ELK* can help us ingest, parse, and then search, sort, and filter our EVTX output. Let’s get into the nuts and bolts of how we can accomplish this for a single Windows endpoint.

First, visit the *Hayabusa* GitHub repo and download the latest stable release to your analysis system. Note that Windows, Mac, and Linux are supported platforms. I’ll be using the Windows version (v.3.3.0 at the time of this writing – *hayabusa-3.3.0-win-x64.zip*): <https://github.com/Yamato-Security/hayabusa/releases/tag/v3.3.0>

I’ll extract the *hayabusa-3.3.0-win-x64.zip* file to “C:\Tools” and stage my test case EVTX files in a “D:\cases\test\_case\_evtx” directory.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/Win_logs_01.png)

Next, I’ll op...