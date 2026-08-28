---
title: Next.js Patches Critical AVIF and Windows Flaws Enabling Unauthenticated RCE
url: https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html
source: The Hacker News
date: 2026-08-27
fetch_date: 2026-08-28T13:37:58.373711
---

# Next.js Patches Critical AVIF and Windows Flaws Enabling Unauthenticated RCE

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Next.js Patches Critical AVIF and Windows Flaws Enabling Unauthenticated RCE](https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html)

**Swati Khandelwal**Aug 27, 2026Vulnerability / Web Security

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYbQmCgjQOeGU5sXrRRnYNbfxDed_Evv1vYrDL4L4NOguQ5wIxE6glQW7yQvhR1Dzs4Gbddc2ktadXWc2VkaGHE4pvMmjaXHMRuepjwrzefXNHb6B3Shk51VRBQw0etS5WWsS9JuNN4q_Y8lDSFtzKNEgi2X-NvAllwzw5_03HwGdC7iNJc6METEjcUNc/s1700-e365/nodejs.gif) |
| Credit: Hacktron |

Vercel has released security patches for two critical-severity vulnerabilities in the Next.js web framework, both of which allow unauthenticated remote code execution, one exploitable via specially crafted AVIF image files and the other through a path traversal flaw affecting servers that use a Windows filesystem.

The Windows path traversal, tracked as **CVE-2026-75604** (CVSS score: 9.0), affects Next.js applications that use both the Pages Router and App Router without Cache Components when the server uses a Windows filesystem.

Linux and macOS deployments are not affected.

"There is no known workaround for affected windows-hosted applications. You should upgrade immediately if your server is hosted on Windows," [Vercel said in its advisory](https://github.com/vercel/next.js/security/advisories/GHSA-p293-qw3h-jr36).

The fixes are available in Next.js 15.5.24 (Maintenance LTS) and 16.3.3 (Active LTS), published on August 25, 2026. Affected users can upgrade by running npm install next@15.5.24 for the 15.5 line or npm install next@16.3.3 for the 16.3 line.

Applications hosted on Vercel are protected from both vulnerabilities and require no upgrade, Vercel said in [a changelog entry](https://vercel.com/changelog/nextjs-august-2026-security-release) published August 25.

The vulnerability affects Next.js versions 13.4 through 15.5.23 and versions 16.0 through 16.3.2.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The attack mechanism was not disclosed in the advisory. Vercel's changelog also credited the researchers evolutionstorm and B0RI with the responsible disclosure of the Windows vulnerability.

### AVIF Image Optimization Flaw

Next.js uses the sharp image processing package to optimize images, and sharp relies on the libheif C library to parse AVIF files.

A critical heap buffer overflow in libheif can lead to remote code execution when Next.js processes an attacker-controlled AVIF image ([GHSA-2xp9-vwfh-vxw4](https://github.com/vercel/next.js/security/advisories/GHSA-2xp9-vwfh-vxw4), CVSS v4: 9.5).

The underlying vulnerability, disclosed by the libheif maintainers as [GHSA-g89c-p67h-r497](https://github.com/strukturag/libheif/security/advisories/GHSA-g89c-p67h-r497), involves a heap buffer overflow in the library's image scaling code.

All libheif versions through v1.23.1 are affected. The AVIF advisory covers Next.js versions 10.0.0 through 15.5.23 and all 16.x releases through 16.3.2.

A crafted AVIF file that contains nested identity-derivation and auxiliary item references causes libheif to build a decoded image with two Alpha plane entries at different bit depths.

The scaler allocates a destination buffer sized for the first, 8-bit Alpha entry but then writes 16-bit sample values from the second entry into that same buffer, overwriting approximately 16,384 bytes past the allocation boundary.

The researchers credited in the advisory, rootxharsh as Finder and KarimPwnz as Coordinator, released a full Python proof-of-concept alongside the libheif disclosure that reproduces the heap corruption under an address sanitizer build.

The libheif advisory credited rootxharsh as Finder and KarimPwnz as Coordinator, but Vercel's changelog attributed the disclosure to the [Hacktron team](https://x.com/HacktronAI/status/2092940768336109647).

"We were able to get RCE using this on multiple applications," the researchers said in the [libheif advisory](https://github.com/strukturag/libheif/security/advisories/GHSA-g89c-p67h-r497).

The proof-of-concept demonstrates the out-of-bounds write, and the researchers' claim of remote code execution on multiple applications has not been independently corroborated.

Next.js enables AVIF optimization only when a site explicitly adds image/avif to the formats configuration in next.config.js. Deployments without that configuration are not exposed to this flaw.

The patched Next.js releases turn off AVIF optimization entirely until the upstream fix propagates from libheif. The Hacker News confirmed on August 27, 2026, via the libheif GitHub releases page that v1.23.2 had not been published.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Vercel had scheduled the August patches for August 26 as part of its monthly security cadence, but moved the release forward by one day after discovering an additional critical-severity vulnerability in one of its upstream dependencies.

"Earlier today, we moved the release forward after identifying an additional critical severity vulnerability in one of our upstream dependencies," Josh Story, Karim Rahal, and Sebastian Silbermann said in [Vercel's security blog post](https://nextjs.org/blog/august-2026-security-release).

The August release is the second under Vercel's formal monthly security program, which the company announced in July 2026.

"The volume of vulnerability research across the industry is rising fast, driven by LLM-assisted discovery," Andrew Imm and Josh Story said in the [July 13 program announcement](https://nextjs.org/blog/next-security-release-program).

The [first scheduled release](https://nextjs.org/blog/july-2026-security-release), published on July 21, addressed nine vulnerabilities in Next.js 16.2.11 and 15.5.21, covering denial-of-service, server-side request forgery, and middleware bypass classes.

Users already on those July patches still need the August upgrade.

Next...