---
title: PNLD Breach Exposes U.K. Police and Government Contact Details on Dark Web
url: https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html
source: The Hacker News
date: 2026-08-03
fetch_date: 2026-08-04T05:01:12.521908
---

# PNLD Breach Exposes U.K. Police and Government Contact Details on Dark Web

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

![cybersecurity](data:image/svg+xml;base64...)

# [PNLD Breach Exposes U.K. Police and Government Contact Details on Dark Web](https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html)

**Swati Khandelwal**Aug 03, 2026Data Breach / Dark Web

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguFnLbEr199EuLksobp-I8Z6liAUmM4EKRi94ttPtanQN2aiwvNh1qHK_kkGhOBfWTzLzANlQ3jd6FmJOHWbdn8rFfg1sHvYqmBaVM5kfak1JxRhqPEfNR94zY_pibMdsbWMIx8gqcZZjoYLhKk03Gw3PrYKF6JQzrNLV6HiE5U7UtYPSwmH-OmDmjl8c/s1700-e365/exfilsquad.jpg)

The Police National Legal Database (PNLD) has confirmed that police, government and customer contact information was compromised and published on the dark web.

The data included names, organisations and work email addresses belonging to police officers, police staff, criminal justice professionals, government partners and customers.

The incident, identified on July 26, also exposed some names and email addresses belonging to people who had submitted questions through Ask the Police. That exposure could make phishing messages targeting named officers appear more convincing, according to [UK government guidance](https://www.ncsc.gov.uk/guidance/data-breaches).

PNLD said, "There is no evidence to suggest that passwords or other security credentials have been compromised." The service provides legal information, products and services to UK police forces and criminal justice organisations. It is not the Police National Computer or the Police National Database, is not a crime-recording system, and does not hold confidential information about victims, witnesses or offenders.

PNLD says it contacted all affected organisations and provided them with further information and guidance. Affected Ask the Police users have already received an email with more information and guidance. It notified the Information Commissioner's Office (ICO) and is working with the National Crime Agency (NCA) and specialist cybersecurity organisations.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

As of August 3, 2026, it had not publicly disclosed how many people were affected, when the intrusion began, how long access lasted, or how much information was taken.

PNLD's [official breach notice](https://www.pnld.co.uk/~/article/?id=7ebf3c0e-598e-f111-8077-7ced8d3aa78f) describes the exposed fields but provides no victim total. PNLD reported 108,429 police registrations and support for all 43 Home Office police forces in its [2025-26 annual summary](https://www.pnld.co.uk/assets/Annual-Summary-25-26). That is a user-base figure, not a breach-victim count.

PNLD said in its [2023-24 annual summary](https://www.pnld.co.uk/assets/annual-summary-2023-24) that the database uses Microsoft Power Platform technology. The Hacker News confirmed on August 3, 2026, that the breach-notice page referenced assets hosted on Microsoft's content.powerapps.com domain. That corroborates the platform connection but does not show how the attacker obtained the data.

[VenariX reviewed](https://venarix.com/blog/exfilsquad-targets-misconfigured-microsoft-power-pages-portals) samples associated with 11 of **ExfilSquad**'s 15 claimed victims and found Dataverse-consistent structures across all 11. In the Houston case, it confirmed that a public portal returned records without authentication and that those records were consistent with data published by the group.

VenariX assessed the likely campaign-level path as a public [Power Pages site](https://thehackernews.com/2024/11/thn-recap-top-cybersecurity-threats_25.html) with broad Anonymous Users access to Dataverse tables. The path also required an [enabled Power Pages Web API](https://learn.microsoft.com/en-us/power-pages/configure/webapi-how-to) or legacy OData feed.

[Microsoft's documentation](https://learn.microsoft.com/en-us/power-pages/security/assign-table-permissions) says granting the Anonymous Users role access to a table makes its data visible to anyone visiting the site. Its [Web API documentation](https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview) says the /\_api interface follows the table permissions attached to each web role.

VenariX said the evidence "does not yet confirm that every organization was affected through an exposed Power Apps portal or the same configuration issue." As of August 3, 2026, neither PNLD's notice nor VenariX's report identified a PNLD-specific endpoint, permission setting, API route, or supporting log.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

At this stage, the Power Pages link remains a hypothesis to test rather than an explanation of the PNLD breach.

Microsoft provides a [tenant-level governance control](https://learn.microsoft.com/en-us/power-pages/security/disable-anonymous-access) that blocks unauthenticated users from reading Dataverse data while still allowing public form submissions.

VenariX recommends that Power Pages operators also review Anonymous Users table permissions, Web API settings, and legacy OData feeds, then validate access from an unauthenticated browser session. Those measures address the configuration pattern identified by VenariX, not a confirmed PNLD root cause.

ExfilSquad [listed PNLD on its leak site](https://www.ransomlook.io/group/exfilsquad) on July 26, but PNLD has not attributed the incident to the group. VenariX found no evidence of ransomware deployment, malware use, lateral movement or exploitation of a software vulnerability in the campaign material it examined.

PNLD has not publicly disclosed the exact access route, the number of unique people affected or the full volume of data published.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**...