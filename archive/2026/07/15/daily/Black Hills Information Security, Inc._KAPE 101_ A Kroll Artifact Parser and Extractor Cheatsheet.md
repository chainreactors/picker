---
title: KAPE 101: A Kroll Artifact Parser and Extractor Cheatsheet
url: https://www.blackhillsinfosec.com/kape-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2026-07-15
fetch_date: 2026-07-16T04:58:05.861681
---

# KAPE 101: A Kroll Artifact Parser and Extractor Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/traditional-penetrating-testing/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [Web Application Testing](https://www.blackhillsinfosec.com/services/web-application-testing/)
  + [ActiveSOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [Fusion PenTest](https://www.blackhillsinfosec.com/fusion-penetration-testing/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [ActiveSOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
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

15
Jul
2026

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [DFIR](https://www.blackhillsinfosec.com/category/dfir/), [Guest Author](https://www.blackhillsinfosec.com/category/author/guest-author/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Artifact Extraction](https://www.blackhillsinfosec.com/tag/artifact-extraction/), [Gerard Johansen](https://www.blackhillsinfosec.com/tag/gerard-johansen/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/), [KAPE](https://www.blackhillsinfosec.com/tag/kape/), [Windows Forensic Artifacts](https://www.blackhillsinfosec.com/tag/windows-forensic-artifacts/)

# [KAPE 101: A Kroll Artifact Parser and Extractor Cheatsheet](https://www.blackhillsinfosec.com/kape-cheatsheet/)

Written by [Gerard Johansen](https://www.linkedin.com/in/gerardjohansen/) || [irproactive.com](https://www.irproactive.com/) || Guest Author

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/07/kape101_header-1.png)

*This article was originally published in the InfoSec Survival Guide: Orange Book — Incident Response. Read it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-infosec-survival-guide-orange-book/), or grab it on the [Spearphish General Store](https://spearphish-general-store.myshopify.com/collections/infosec-survival-guides/products/the-infosec-survival-guide-orange-book-incident-response) (free digital download or a $1.25 physical copy, your call).*

*Spend time performing forensic analysis on the Windows Operating System and you’ll see a host of artifacts that can be used to identify adversary activity. From changes to the registry to the System Resource Utilization Monitor, Windows artifacts run deep. The challenge is locating, extracting, and parsing these artifacts in an efficient manner.*

This is where the [Kroll Artifact Parser and Extractor (KAPE)](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape) comes into play. KAPE gives analysts and incident responders the capability to collect specific artifacts and parse them into an easily analyzable format. Available free to individuals working in their own environment, KAPE is capable of handling a wide range of artifact extraction and parsing for faster, more efficient analysis.

## The Artifact Extractor

The Artifact Extractor allows analysts to gather key artifacts related to adversary activity. In this example, our analyst will leverage KAPE to extract a Basic Triage package that contains a variety of artifacts. This is useful in a couple of different cases. For example, KAPE is leveraged by analysts who usually have local access to a system and want to extract key artifacts as part of an initial analysis. In other circumstances, KAPE can be run against a mounted disk image or a virtual disk, which allows the analyst to work with the file system. If it can be mounted and given a drive letter, KAPE can be used.

> **Pro Tip:** It is tempting to focus on individual artifacts, such as extracting the Windows Prefetch files to identify suspicious executions. Instead, focus on extracting a collection of artifacts that you can continually use as the investigation progresses to avoid repeatedly going back to extract more data.

### Extracting Artifacts to a Virtual Disk

In the following case, the analyst is using KAPE to extract key artifacts and aggregate them into a virtual disk. This approach extracts key artifacts for follow-on analysis but also places them into a container that is easy to copy and share:

1. In the top left of the KAPE GUI, select **Use Target options.**
2. Complete the Target options by selecting the source. Select the **C:\** directory. **Note:** KAPE will only extract the artifacts that are selected.
   1. For the Target destination, select an applicable directory. **Note:** The Flush option will delete all files in the directory before the output is processed. Keep that in mind.
3. In this example, use the **VHDX** option for the container.
   1. A good practice is to use the system name for the **Base name** field.
4. Once these are completed, click **Execute.**

You will be left w...