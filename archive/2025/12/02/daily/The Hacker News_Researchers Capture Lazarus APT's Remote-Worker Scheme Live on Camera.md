---
title: Researchers Capture Lazarus APT's Remote-Worker Scheme Live on Camera
url: https://thehackernews.com/2025/12/researchers-capture-lazarus-apts-remote.html
source: The Hacker News
date: 2025-12-02
fetch_date: 2025-12-03T03:17:10.157422
---

# Researchers Capture Lazarus APT's Remote-Worker Scheme Live on Camera

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Capture Lazarus APT's Remote-Worker Scheme Live on Camera](https://thehackernews.com/2025/12/researchers-capture-lazarus-apts-remote.html)

**Dec 02, 2025**The Hacker NewsIdentity Theft / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhI7iqT0Bhea1lAfLcWDV9wdSMUF0e52uuWuaAYhgPboMKaSB_lC85jky5JWFRVCNc9X82mFfqDT8WeB0d9J2WCe6jM6fVswAMJZytpPlTVcvBOzRLAosqZV8ld6QTAEz4LedSA_x3J9jqigF7Di_tF-utWG7jQbVdy_eCjkVeeTMYMCX_AHWL1UhrOEkY/s790-rw-e365/korean.jpg)

A joint investigation led by Mauro Eldritch, founder of **[BCA LTD](https://bca.ltd)**, conducted together with threat-intel initiative **[NorthScan](https://northscan.co/)** and **[ANY.RUN](https://any.run),** a solution for interactive malware analysis and threat intelligence, has uncovered one of North Korea's most persistent infiltration schemes: a network of remote IT workers tied to Lazarus Group's Famous Chollima division.

For the first time, researchers managed to watch the operators work **live**, capturing their activity on what they believed were real developer laptops. The machines, however, were fully controlled, long-running sandbox environments created by ANY.RUN.

## The Setup: Get Recruited, Then Let Them In

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiq8AW_f2v2hR7ubKeeMIcX6Wwrnh48Qwynyc26bjs4vhMNVZbFQ75uZ_NGnS4PYc6IRVkgBTCNwRtVZWaFqwzvQ-i27_u2lmHFtMimfMGyHem6OKYtEunM1jIyR5gziwYPZIfevcTqHdF958k-tMu_hjAJhnaUiwA-4vgMNoBqesxFhHlluy3-GqEdM1Q/s790-rw-e365/image.png) |
| Screenshot of a recruiter message offering a fake job opportunity |

The operation began when NorthScan's **Heiner García** impersonated a U.S. developer targeted by a Lazarus recruiter using the alias "Aaron" (also known as "Blaze").

Posing as a job-placement "business," Blaze attempted to hire the fake developer as a frontman; a known Chollima tactic used to slip North Korean IT workers into Western companies, mainly in the **finance, crypto, healthcare, and engineering** sectors.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTQyqy9QLhGjvQATjcBSGQE8Z-iU5tG0XK2gsQyuXbvNgE2JFGE8Lyn_153fYTBv2PoEROJG0eF081nrcAzvvKi8tGBCtEXmsXrbozJ90YezEwwaSHNMzdHrP6d7PN3hslOjHGHV_AFI54NuTSO-Rf0nrrcoGI8SEppDPeS6lyPBg7_wLq9EdsCAGJGZU/s790-rw-e365/image2.png) |
| The process of interviews |

The scheme followed a familiar pattern:

* steal or borrow an identity,
* pass interviews with AI tools and shared answers,
* work remotely via the victim's laptop,
* funnel salary back to DPRK.

Once Blaze asked for full access, including SSN, ID, LinkedIn, Gmail, and 24/7 laptop availability, the team moved to phase two.

## The Trap: A "Laptop Farm" That Wasn't Real

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg17CVPB1MlehqhVg73d5ezAv8VXp0H2YApx_1kOeWVfZWEjEp1-xQPcdAruMbLojTP0g4QzoNhFkSjswNWpWQbMhiNwpSF3ME50OxRP7X8qUM3hWCgQZoyeuG9kaRrsTfhhqgwSmHQFXs5xxqjuc1mwlqtXzPVekARyF0Yt0553PmvCYpoovZ7tB51oU/s790-rw-e365/image3.png) |
| A safe virtual environment provided by ANY.RUN's Interactive Sandbox |

Instead of using a real laptop, BCA LTD's Mauro Eldritch deployed the ANY.RUN Sandbox's virtual machines, each configured to resemble a fully active personal workstation with usage history, developer tools, and U.S. residential proxy routing.

The team could also force crashes, throttle connectivity, and snapshot every move without alerting the operators.

## What They Found Inside the Famous Chollima's Toolkit

The sandbox sessions exposed a lean but effective toolset built for identity takeover and remote access rather than malware deployment. Once their Chrome profile synced, the operators loaded:

* **AI-driven job automation tools** (Simplify Copilot, AiApply, Final Round AI) to auto-fill applications and generate interview answers.
* **Browser-based OTP generators** (OTP.ee / Authenticator.cc) for handling victims' 2FA once identity documents were collected.
* **Google Remote Desktop**, configured via PowerShell with a fixed PIN, providing persistent control of the host.
* Routine **system reconnaissance** (dxdiag, systeminfo, whoami) to validate the hardware and environment.
* Connections consistently routed through **Astrill VPN**, a pattern tied to previous Lazarus infrastructure.

In one session, the operator even left a Notepad message asking the "developer" to upload their ID, SSN, and banking details, confirming the operation's goal: full identity and workstation takeover without deploying a single piece of malware.

## A Warning for Companies and Hiring Teams

Remote hiring has become a quiet but reliable entry point for identity-based threats. Attackers often reach your organization by targeting individual employees with seemingly legitimate interview requests. Once they're inside, the risk goes far beyond a single compromised worker. An infiltrator can gain access to internal dashboards, sensitive business data, and manager-level accounts that carry real operational impact.

Raising awareness inside the company and giving teams a safe place to check anything suspicious can be the difference between stopping an approach early and dealing with a full-blown internal compromise later.

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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
[**Share on Hacker News](#link_share)...