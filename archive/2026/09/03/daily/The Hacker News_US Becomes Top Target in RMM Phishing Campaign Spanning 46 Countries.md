---
title: US Becomes Top Target in RMM Phishing Campaign Spanning 46 Countries
url: https://thehackernews.com/2026/09/us-becomes-top-target-in-rmm-phishing.html
source: The Hacker News
date: 2026-09-03
fetch_date: 2026-09-04T06:44:14.621246
---

# US Becomes Top Target in RMM Phishing Campaign Spanning 46 Countries

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [US Becomes Top Target in RMM Phishing Campaign Spanning 46 Countries](https://thehackernews.com/2026/09/us-becomes-top-target-in-rmm-phishing.html)

**The Hacker News**Sep 03, 2026Social Engineering / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_OZ4yHwsQM1Z9se2g-uJPuSkiSNpmyWCCi_a9dKpH9jnTuFYyts16e2gdkB45YknrA-nuzp6-mbEi-1adV92N-7aBjfYL69ECPlWOV7a5xb5rG6kqsMzc3WJ0-lXLBMO86aB3WTJ6MFLR0N0YbC8TElIg0-Jh6SIDe8mc3nCyzoE6zugVDFHFfjPEGkI/s1700-nu-rw-lo-l85-e365/targets.jpg)

An RMM phishing campaign initially associated with Canadian targeting due to its use of Canada Revenue Agency (CRA) tax forms as lures has turned out to be part of a broader campaign spanning 46 countries.

Around **45% of observed activity was associated with the United States**, making it the campaign's top geographic target. [ANY.RUN](https://any.run/?utm_source=thehackernews&utm_medium=article&utm_campaign=rmm&utm_content=landing&utm_term=030926) research connected 601 cases to the wider operation, which uses fake documents to trick victims into installing legitimate remote monitoring and management (RMM) software.

The attackers adapt their lures to different targets, using shipping and UPS communications, Adobe PDFs, tax notices, US Social Security Administration themes, invoices, and other documents. Rapidly rotated, disposable Vercel infrastructure makes the campaign harder to track and detect.

## US-First Threat with Daily Infrastructure Rotation

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwT-vGJh7x8TPQQLRJmZ22vvyxZmHptTJe4EyO8JPAkgceWgoArUe5D21o35QMox4JLiV3df524AfS1CILbekiKs24BQJGgeCAj1gRi9rninQWx4VQizZ7LlNPbERXIKoGY72fLYNwvw8h8DBmd_t9TYhOTaByHQuFCTxr9bdEpMF0kXMucylEA0hw-n8/s1700-nu-rw-lo-l85-e365/1.png) |
| Threat overview by ANY.RUN |

The campaign’s infrastructure changes significantly faster than its attack pattern. ANY.RUN researchers identified **425 kit URLs across 240 hosts, 94% of which were observed for only a single day**.

The operation has used Vercel, GitHub Pages, Netlify, compromised websites, and other infrastructure for delivery. Payloads have also been staged through services including Amazon S3, Cloudflare R2, GitHub, DigitalOcean Spaces, Dropbox, and GoFile.

Despite this rapid rotation, the phishing kit leaves more persistent fingerprints. Shared assets such as *font1.woff2*, recurring image resources, and the *secure.html → project/\*.zip* delivery structure helped researchers connect otherwise separate infrastructure to the same campaign.

Education, technology, and government are among the top targeted industries. Banking, finance, and manufacturing are also prominently present.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1zjUldsGCzMdFBCZpDE_nztC3SI9Q-kiXUmRZMs9CtaqLUQJyLUf02cMWsqe5eFQa8jkFsl4TE-Ot1WaLmP-Qznm30JSlrFjkam_zV8_HtDRhomCO0AaKl7eBgRk4KCF51R_TnC6huuYbuDjDO9_KFfMeQDhMp6tlGyCEThyphenhyphenGJIU3szCZmzRE2hJwzDw/s1700-nu-rw-lo-l85-e365/6.png) |
| Attack chain overview by ANY.RUN |

Individual domains and RMM products are disposable, while the underlying delivery chain is more stable. This shows why detection cannot depend solely on malware verdicts, reputation, or individual IOCs.

To detect these patterns and distinguish legitimate RMM use from abuse, SOC teams need access to the full behavioral context behind suspicious activity.

Respond faster and reduce risk in your company with deeper visibility and intel from 16K+ organizations. [Power your SOC with ANY.RUN](https://any.run/enterprise/?utm_source=thehackernews&utm_medium=article&utm_campaign=rmm&utm_content=enterprise&utm_term=030926#contact-sales)

## **Key Detection Takeaways for SOC Teams**

* **Build a product-agnostic defense:** legitimate software can be abused and switched between vendors, leading to visibility gaps. Maintain focus on delivery chain and unauthorized remote-access activity.
* **Detect around campaign patters:** Instead of relying only on domains, which in this campaign get rotated daily, prioritize more stable kit indicators, including the *fmtt / font1.woff2, icons8-microsoft-word-94.png* asset, and the *secure.html → project/\*.zip* chain.
* **Establish mail-layer controls and raise user awareness:** SOC teams should account for password-protected archive delivery.
* **Give analysts behavioral and threat context:** [ANY.RUN's Interactive Sandbox](https://any.run/features/?utm_source=thehackernews&utm_medium=article&utm_campaign=rmm&utm_content=features&utm_term=030926) exposed the campaign's browser activity, scripts, processes, downloads, and network behavior, while [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=thehackernews&utm_medium=article&utm_campaign=rmm&utm_content=lookup&utm_term=030926) connected persistent indicators to related infrastructure and cases.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisgdoyUyQBjxA9hM9FZhqQsJxWW9q3CCsE3GCl1a-KnBXG89Hpuv7k1a01osVapk7syuTKPk0tcMd-25irEI8-weBzSHeckIBO30or8GUjZLg7XM9jNgT02zO6keR2RErE60C8YKVSEdbqwJEh-PG8CzkmCuy7YuSEip4R7Gd7fpbWk8ePjd2NCLvRNXw/s1700-nu-rw-lo-l85-e365/7.png) |
| One of the lures, an Adobe phishing page, analyzed within ANY.RUN Interactive Sandbox |

As attackers increasingly combine legitimate software, trusted services, and disposable infrastructure, security teams need to access and operationalize in-depth threat context.

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[*...