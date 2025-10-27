---
title: 60 New Malicious Packages Uncovered in NuGet Supply Chain Attack
url: https://thehackernews.com/2024/07/60-new-malicious-packages-uncovered-in.html
source: The Hacker News
date: 2024-07-12
fetch_date: 2025-10-06T17:46:10.914740
---

# 60 New Malicious Packages Uncovered in NuGet Supply Chain Attack

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [60 New Malicious Packages Uncovered in NuGet Supply Chain Attack](https://thehackernews.com/2024/07/60-new-malicious-packages-uncovered-in.html)

**Jul 11, 2024**Ravie LakshmananSoftware Security / Threat Intelligence

[![NuGet Supply Chain Attack](data:image/png;base64... "NuGet Supply Chain Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAI5AWPHBqq4TRW5st_IPJKlITC848GP2gRZnE7sADmXyariSsJIKDKGIS_NBprhzAOeMYGXuG207VmmlPP09D702sWpeAc4FUd5JFqonHCOuGrtTi8XLL8DDTJ1lQk-AArEuAcNEDcvhvgaZsdHpENPRaTONqnVwgeGHP_lj1DMNq-wMWkC0d-ueCT1N6/s790-rw-e365/hacking.png)

Threat actors have been observed publishing a new wave of malicious packages to the NuGet package manager as part of an ongoing campaign that began in August 2023, while also adding a new layer of stealth to evade detection.

The fresh packages, about 60 in number and spanning 290 versions, demonstrate a refined approach from the previous set that [came to light](https://thehackernews.com/2023/10/malicious-nuget-packages-caught.html) in October 2023, software supply chain security firm ReversingLabs said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attackers pivoted from using NuGet's MSBuild integrations to "a strategy that uses simple, obfuscated downloaders that are inserted into legitimate PE binary files using Intermediary Language (IL) Weaving, a .NET programming technique for modifying an application's code after compilation," security researcher Karlo Zanki [said](https://www.reversinglabs.com/blog/malicious-nuget-campaign-uses-homoglyphs-and-il-weaving-to-fool-devs).

The end goal of the counterfeit packages, both old and new, is to deliver an off-the-shelf remote access trojan called [SeroXen RAT](https://thehackernews.com/2023/10/malicious-nuget-package-targeting-net.html). All the identified packages have since been taken down.

[![NuGet Supply Chain Attack](data:image/png;base64... "NuGet Supply Chain Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlUqB5JdSDC-_c5_pP1w_769BHMh0WII-oa_MWjk-e9lVLfZSvVJ8_u0xKcEo-FgpQ2ZIxURTmftcEnBv68HFypBh7d5ZsTNay-UQ94tUFpQAko7Pk_fF_xJZLQq0Ny_h2aZ2md-_FESRvJr5Z07ZnWJv08J53i2si88HqBceCu1GsXc9QQMlkUDiFdaYN/s790-rw-e365/dll.png)

The latest collection of packages is characterized by the use of a novel technique called [IL weaving](https://www.codecrafting.tips/code-chronicles-21-il-weaving-technique/) that makes it possible to inject malicious functionality to a Portable Executable (PE) .NET binary associated with a legitimate NuGet package.

This includes taking popular open-source packages like [Guna.UI2.WinForms](https://www.nuget.org/packages/Guna.UI2.WinForms) and patching it with the aforementioned method to create an imposter package that's named "Gսոa.UI3.Wіnfօrms," which uses homoglyphs to substitute the letters "u," "n," "i," and "o" with their equivalents "ս" (\u057D), "ո" (\u0578), "і" (\u0456). and "օ" (\u0585).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Threat actors are constantly evolving the methods and tactics they use to compromise and infect their victims with malicious code that is used to extract sensitive data or provide attackers with control over IT assets," Zanki said.

"This latest campaign highlights new ways in which malicious actors are scheming to fool developers as well as security teams into downloading and using malicious or tampered with packages from popular open source package managers like NuGet."

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

[Code Injection](https://thehackernews.com/search/label/Code%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[software security](https://thehackernews.com/search/label/software%20security)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first...