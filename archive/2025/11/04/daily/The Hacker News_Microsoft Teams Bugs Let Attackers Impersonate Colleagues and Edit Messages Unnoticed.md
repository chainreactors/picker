---
title: Microsoft Teams Bugs Let Attackers Impersonate Colleagues and Edit Messages Unnoticed
url: https://thehackernews.com/2025/11/microsoft-teams-bugs-let-attackers.html
source: The Hacker News
date: 2025-11-04
fetch_date: 2025-11-05T03:12:47.093837
---

# Microsoft Teams Bugs Let Attackers Impersonate Colleagues and Edit Messages Unnoticed

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Microsoft Teams Bugs Let Attackers Impersonate Colleagues and Edit Messages Unnoticed](https://thehackernews.com/2025/11/microsoft-teams-bugs-let-attackers.html)

**Nov 04, 2025**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPxhWGZawWeHzNGIbomWP8Nbdh5Dd6tcZRBCwh1fzvzwLRHHrOAdfio4nT7DL5Lq7_v0S8mDZ5JcWhL_B75AVaO8pYvvxHr5UbkNOaALx-O3Xj2msk9pV1vHsgTDQjCYfED7yaajgRNK5Qarl8aAWqwk6W0GYG5DwB9MGPnXdrgRhGpgIyNdu5FYPJtPF5/s790-rw-e365/ms-teams.jpg)

Cybersecurity researchers have disclosed details of four security flaws in Microsoft Teams that could have exposed users to serious impersonation and social engineering attacks.

The vulnerabilities "allowed attackers to manipulate conversations, impersonate colleagues, and exploit notifications," Check Point [said](https://blog.checkpoint.com/research/exploiting-trust-in-collaboration-microsoft-teams-vulnerabilities-uncovered/) in a report shared with The Hacker News.

Following responsible disclosure in March 2024, some of the issues were addressed by Microsoft in August 2024 under the CVE identifier CVE-2024-38197, with subsequent patches rolled out in September 2024 and October 2025.

In a nutshell, these shortcomings make it possible to alter message content without leaving the "Edited" label and sender identity and modify incoming notifications to change the apparent sender of the message, thereby allowing an attacker to trick victims into opening malicious messages by making them appear as if they are coming from a trusted source, including high-profile C-suite executives.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The attack, which covers both external guest users and internal malicious actors, poses grave risks, as it undermines security boundaries and enables prospective targets to perform unintended actions, such as clicking on malicious links sent in the messages or sharing sensitive data.

On top of that, the flaws also made it possible to change the display names in private chat conversations by modifying the conversation topic, as well as arbitrarily modify display names used in call notifications and during the call, permitting an attacker to forge caller identities in the process.

"Together, these vulnerabilities show how attackers can erode the fundamental trust that makes collaboration workspace tools effective, turning Teams from a business enabler into a vector for deception," the cybersecurity company [said](https://research.checkpoint.com/2025/microsoft-teams-impersonation-and-spoofing-vulnerabilities-exposed/).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6hrixGfHAtSBkAwSBIk-0f2VSLtLXAVas3sAm20uynFUfc_u8nOvEiBbZ6SL8HzsW3b9HiMI86JvulwORmIn1sX7pEQXxVLVIoSBma_mGvocwUx1o2qEGDjyNxr09hyphenhyphen6RGh1fPH9E2LG3PZwH963CExTOi4TjsnvenDNMOsmWEiZwTKcYHGbCuk2K6Plf/s2600/ceo.jpg)

Microsoft has described [CVE-2024-38197](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38197) (CVSS score: 6.5) as a medium-severity spoofing issue impacting Teams for iOS, which could allow an attacker to alter the sender's name of a Teams message and potentially trick them into disclosing sensitive information through social engineering ploys.

The findings come as threat actors are [abusing](https://thehackernews.com/2025/07/hackers-leverage-microsoft-teams-to.html) Microsoft's enterprise communication platform in various ways, including approaching targets and persuading them to grant remote access or run a malicious payload under the guise of support personnel.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Microsoft, in an [advisory](https://thehackernews.com/2025/10/threatsday-bulletin-ms-teams-hack-mfa.html#how-threat-actors-abuse-microsoft-teams) released last month, said the "extensive collaboration features and global adoption of Microsoft Teams make it a high-value target for both cybercriminals and state-sponsored actors" and that its messaging (chat), calls, and meetings, and video-based screen-sharing features are weaponized at different stages of the attack chain.

"These vulnerabilities hit at the heart of digital trust," Oded Vanunu, head of product vulnerability research at Check Point, told The Hacker News in a statement. "Collaboration platforms like Teams are now as critical as email and just as exposed."

"Our research shows that threat actors don't need to break in anymore; they just need to bend trust. Organizations must now secure what people believe, not just what systems process. Seeing isn't believing anymore, verification is."

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Microsoft Teams](https://thehackernews.com/search/label/Microsoft%20Teams)[social engineering](https://thehackernews.com/search/label/social%20engineering)[Spoofing Attack](https://thehackernews.com/search/label/Spoofing%20Attack)[Threat Intelligence](https://thehackernews.com/sear...