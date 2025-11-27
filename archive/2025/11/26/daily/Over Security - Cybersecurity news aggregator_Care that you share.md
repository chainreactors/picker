---
title: Care that you share
url: https://blog.talosintelligence.com/care-that-you-share/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-26
fetch_date: 2025-11-27T03:12:50.229485
---

# Care that you share

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

# Care that you share

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Wednesday, November 26, 2025 12:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week's edition of the Threat Source newsletter.

Back in April, I [wrote](https://blog.talosintelligence.com/care-what-you-share/) about the risks of unintentionally leaking information while using search engines. Since then, I’ve been thinking: Life doesn’t just happen in front of a keyboard. There’s a social side, too (or so I’m told). With Thanksgiving around the corner, it seems the perfect time to flip the script and focus on a different but related concept: Care *that* you share.

For my non-American friends, who may be enjoying just another Thursday, stick with me. This season brings heightened risks everywhere. Many teams are running with skeleton crews, whether due to holiday mode (family, turkey, football, days off) or the year-end compliance push (hello, [NIS2](https://blog.talosintelligence.com/what-is-nis2-and-how-can-you-best-prepare-for-the-new-cybersecurity-requirements-in-the-eu/) and DORA). At the same time, on the other side of the fence, attackers ramp up their efforts; globally, Black Friday and similar events are peak periods for phishing campaigns, often targeting credentials with fake employee perk emails and other seasonal lures.

So, why emphasize “care that you share?”

Recently, I visited a university of applied sciences to give a guest lecture and learn more about the projects students are working on. It was a great experience, though preparing for an audience of students (not my usual crowd) was challenging. What do they already know? What topics interest them? Should I give them some history of STIX/TAXII? Geopolitical tensions? Honestly speaking, none of this was interesting to me when I was a student. I chose to start simple, discussing what threats and the [DKIW pyramid](https://en.wikipedia.org/wiki/DIKW_pyramid) were, and then focusing on CVE, CVSS, and KEV — one of my favorite [topic clusters](https://blog.talosintelligence.com/trick-treat-repeat/).

To my surprise, not only did the students engage and ask questions, but they also stuck around late on a Friday afternoon, diving into discussions about software supply chain risks and beyond. I don’t remember ever staying at university past 6:00 p.m. on a Friday as a student! A week later, when they presented their projects — many centered on authentication, TOTP, and SmartCards — I was genuinely impressed by their ideas and the real-world problems they were addressing.

“Care that you share” is a mindset that helps us appreciate the knowledge exchange that happens in person, too.

Whether sharing stories over dinner, IOCs over email, or ideas in a classroom, let’s all take a moment to consider not just what we share, but how and why we share it. I’ll admit, I sometimes hesitate to share certain stories myself, worried they might seem too obvious or uninteresting, or maybe even dumb. But more often than not, those moments of openness lead to the best conversations and new perspectives.

This rings especially true during busy or understaffed times, when teams are stretched thin. It’s tempting to keep things to ourselves to avoid “bothering” others. In reality, sharing a helpful tip, a concern, or just a quick update can make all the difference for colleagues who might be juggling extra responsibilities or missing context.

So this holiday season, care that you share. Thoughtful communication isn’t just about protecting information — it’s also about supporting each other, especially when resources are limited. You never know who might benefit from what you have to offer, yourself included.

## The one big thing

Last week, Cisco Talos announced [an initiative to retire outdated ClamAV signatures](https://blog.clamav.net/2025/11/clamav-signature-retirement-announcement.html) to reduce database sizes and improve efficiency by focusing on currently relevant threats. Starting Dec. 16, 2025, the “main.cvd” and “daily.cvd” databases will be cut roughly in half, offering smaller downloads and reduced resource usage. Retired signatures may be reintroduced if old threats reappear, and only supported ClamAV container images will remain available on Docker Hub to enhance security and management.

### Why do I care?

Smaller signature databases mean faster updates, lower bandwidth and storage requirements, and improved performance, especially on resource-constrained systems. By focusing detection on active threats, ClamAV can more efficiently protect against current malware without being bogged down by obsolete signatures.

### So now what?

We will continue to monitor the activity of retired signatures and will restore any that are needed to protect the community. Stay attentive and request the reinstatement of retired signatures if older threats reappear. In the meantime, we recommend that ClamAV container image users select a feature release tag rather than a specific minor release tag to stay up to date with security updates and bug fixes.

## Top security headlines of the week

**Second Sha1-Hulud wave affects 25,000+ repositories via npm preinstall credential theft**
The new supply chain campaign, dubbed Sha1-Hulud, has compromised hundreds of npm packages, uploaded to npm between November 21 and 23, 2025. The attack has impacted popular packages from Zapier, ENS Domains, PostHog, and Postman, among others. ([The Hacker News](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html))

**FBI: Cybercriminals stole $262M by impersonating bank support teams**
Since January 2025, the FBI's Internet Crime Complaint Center (IC3) has received over 5,100 complaints, with the attacks impacting individuals, as wel...