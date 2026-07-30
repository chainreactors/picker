---
title: Report As You Go: Maintaining Good Documentation for SOC Analysts
url: https://www.blackhillsinfosec.com/report-as-you-go-soc/
source: Black Hills Information Security, Inc.
date: 2026-07-29
fetch_date: 2026-07-30T04:51:16.268133
---

# Report As You Go: Maintaining Good Documentation for SOC Analysts

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

29
Jul
2026

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Guest Author](https://www.blackhillsinfosec.com/category/author/guest-author/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [SOC](https://www.blackhillsinfosec.com/category/soc/)
[Blue Book](https://www.blackhillsinfosec.com/tag/blue-book/), [Dan Rearden](https://www.blackhillsinfosec.com/tag/dan-rearden/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [Report As You Go: Maintaining Good Documentation for SOC Analysts](https://www.blackhillsinfosec.com/report-as-you-go-soc/)

by [Dan “Haircutfish” Rearden](https://linkedin.com/in/danrearden/) | [haircutfish.com](https://haircutfish.com) | Guest Author

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/07/reporting_header.png)

*This article was originally published in the InfoSec Survival Guide: Blue Book — SOC Analysts. Read it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-infosec-survival-guide-blue-book/), or grab it on the [Spearphish General Store](https://spearphish-general-store.myshopify.com/collections/infosec-survival-guides/products/the-infosec-survival-guide-orange-book-incident-response) (free digital download or a $1.25 physical copy, your call).*

Working in the SOC can be a grind. Whether triaging alerts, escalating to clients, or just trying to understand why users download malicious files, we feel the need to get through tickets as fast as possible. But in that rush, we can actually hinder our progress and slow ourselves down.

### Structure

What can we do to make tickets, notes, and escalations aid the SOC in the past, present, and future? Using structure, “building upon,” and clear and concise direction, we can set ourselves and the SOC up for success.

In one of Jason Blanchard’s “Job Hunt Like a Hacker” BHIS livestreams, he emphasized using bullet points when listing job experience rather than a big wall of text, as “people will get lost and stop reading.” I took this advice to heart in the way I structure the internal notes of my tickets.

I use structured, cascading bullet points to document each step taken and each piece of evidence discovered during triage. This format makes it easy for any teammate to pick up where I left off — or for a lead to QA my work without asking me to explain it.

**For Example:**

* IP address (123.456.789.10) has a Geolocation of Cold Lake, Alberta, Canada
  + Malicious on AbuseIPDB and VirusTotal
    - AbuseIPDB Link
    - VirusTotal Link

### Building Upon

Now that we know how to structure our notes, what should we actually document? While triaging the alert, begin with steps taken. This could be “- Ran query: {the query itself or link to SIEM platform of query used}”, “- Investigated User’s recent login history”, etc. From there, gather evidence (log data, artifacts, screenshots, etc.) pertaining to the events that occurred and add them to your notes as you discover them.

Just because you add something to your notes, doesn’t mean it’s set in silicon (excuse my play on words…). If an event or evidence is not actually linked to the alert, you can remove it. It’s better to capture too much and trim later than to miss something you’ll need to reconstruct hours or days from now. This is a key part of the “Report-As-You-Go” process.

### Clear and Concise Direction

We have our structure and our evidence… now what? It’s time to edit down and proofread what we have in the internal so that it only contains necessary information. Clear away any rabbit holes or evidence not pertinent to the alert in question. Your thought process should be apparent from the information you present. A final bullet point stating your verdict will enhance this clarity, such as “- Atypical behavior of user, will escalate and confirm expected.”

**Here’s an example of a finished internal update:**

* SentinelOne Query used
  + https:mXdr.AlkaliLakefacility.com/aGFpcmN1dGZpc2guY29t
* IP address (123.456.789.10) has a Geolocation of Cold Lake, Alberta, Canada
  + User doesn’t typically log in for IP address
  + Malicious on AbuseIPDB and VirusTotal
    - AbuseIPDB Link
    - VirusTotal Link
* User downloaded 2k files over an hour time frame from the Weapon-X SharePoint
  + https:mXdr.AlkaliLakefacility.com/bWVkaXVtLmNvbS9AaGFpcmN1dGZpc2g=
* A...