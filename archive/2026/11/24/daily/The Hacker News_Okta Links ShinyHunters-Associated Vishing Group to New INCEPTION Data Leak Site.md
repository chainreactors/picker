---
title: Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site
url: https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html
source: The Hacker News
date: 2026-11-24
fetch_date: 2026-11-25T10:48:29.524969
---

# Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site](https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html)

**Ravie Lakshmanan**Nov 24, 2026Cybercrime / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjete6dy8Fmd7sbjqKI5GKSySXkcnz4NF__irfVMBHzgRIDUnpGHtvRIbCywZYYsoKsnMdPhvanoXcnXbYvZpMjL2lL6d_F9a4ErEaI5rH_boPedH_ru2Ush9wonb8tYhGNVM6M_01DTue1THY7uGMbuKBJKNgMbrACkxHCGJiJylHWoxkkpCXNr2Z_CIdf/s1700-nu-rw-lo-l85-e365/leaks.jpg)

A threat cluster previously assessed to be affiliated with the [ShinyHunters](https://thehackernews.com/2026/09/shinyhunters-claims-fbi-breach-says-it.html) extortion crew may have rebranded and continued operations under a new name called [INCEPTION](https://ransomware.live/group/Inception), according to Okta's Threat Intelligence team.

The cluster, dubbed **O-UNC-053**, is characterized by the use of [voice phishing](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html) (aka vishing) attacks to trick targets into entering credentials in phishing pages and approving multi-factor authentication (MFA). Okta said it's been tracking the group since March 2026.

The identity and access management provider said targets of this cluster previously had stolen data published to the ShinyHunters data leak site (DLS). However, as of November 16, 2026, a new data leak site operating under the name INCEPTION has listed the data siphoned from O-UNC-053 targets.

"While this threat cluster has changed their brand affiliation, the operators remain active in targeting organizations with voice phishing attacks and account takeovers resulting in data theft and extortion," Okta researchers Moussa Diallo and Katie Nickels [said](https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/) in a report shared with The Hacker News.

Social engineering and credential harvesting attacks mounted by O-UNC-053 have targeted a broad range of sectors, including technology, healthcare, biotechnology, financial services, insurance, entertainment, gaming, retail, transportation, hospitality, and legal.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Similar to [O-UNC-066](https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html) and [UNC6671](https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html), the newly identified cluster also relies on a phishing kit to intercept authentication flows and capture a user's credentials and MFA codes. However, the kit is not designed to bypass phishing-resistant methods like passkeys and Okta FastPass.

"While interacting with targeted users on the phone, the operators socially engineer them into sharing factors like one-time passcodes and approving push notifications," Okta said. "If successful, the operators gain access to SaaS applications and exfiltrate sensitive data, which is often used to extort targets under the threat of releasing it on a data leak site."

Domains created by the group are registered through NiceNIC, Spaceship, Tucows, and NameSilo, with the domain names using the following patterns -

* legal-<target>[.]com
* legaldept-<target>[.]com
* <target>[.]legal
* <target>-legal[.]com

The use of "legal" themes in these attacks is said to have started in October 2026, and is often registered on or within a day of a campaign starting. Prior campaign waves have employed help desk-, support-, and claims-related themes for the registered domains.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSoxhGgF97bcN7wu_BaaYyfLSwNn75aEYhfVe2Bt4n4NelPQjR8m4Pz66DzTVLWbdSl-PQExA5TNwRRgbwKvRiBJRLqZFddPKogzY3fG9SkKP1WZpdevRLDUjFI4J-i2Y2REQbBiddCukMfEjtgNjAzVVqF-jt2s_DTBh-dHbIYEzYMcZeLimS7L7cN3VL/s1700-nu-rw-lo-l85-e365/map.png)

These findings also dovetail with an [alert](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt) from Palo Alto Networks Unit 42, which has warned of widespread vishing activity using legal-themed domains that either begin with "legal-" or end with "-legal" using the ".com" top-level domain.

More than 70 such domains have been observed since October 2026, it said, adding each domain is specifically created for an intended target operating in different industries, like cryptocurrency, financial services, healthcare, high technology, and hospitality, among others.

"Registered in rapid evening batches and shielded behind Cloudflare, these web-only domains deploy a filtered kit that delivers tailored content to intended victims while routing visitors it is not configured to attack to the targeted organization's legitimate Okta or NetIQ sign-in flow," ReversingLabs researcher Robert Simmons [said](https://www.reversinglabs.com/blog/threat-researchers-notebook-sso-vishing-campaign-associated-with-emerging-inception-extortion-group#iocs).

Some of the confirmed domains linked to the activity are listed below -

* legal-pepsico[.]com
* legal-paychex[.]com
* legal-duolingo[.]com
* activisionblizzard-legal[.]com
* legal-westernunion[.]com
* legal-dropbox[.]com
* legal-indeed[.]com
* legal-creditkarma[.]com
* legal-amd[.]com
* legal-grubhub[.]com
* legal-twitch[.]tv

The crux of the campaign is to tailor the landing page to the specific identity provider of the target, while filtering unwanted visitors and forwarding them to the organization's authentication infrastructure, such as Okta.

"Throughout our tracking of O-UNC-053 between March and September 2026, we observed the names of targeted entities appear on the ShinyHunters DLS between 1 and 28 days after the phishing infrastructure was registered," Okta noted.

However, it's unclear at this stage if the published data on the INCEPTION site is authentic and whether they are running the site themselves or are collaborating with another extortion gan...