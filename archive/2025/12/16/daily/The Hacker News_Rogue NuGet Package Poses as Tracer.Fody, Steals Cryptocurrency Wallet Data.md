---
title: Rogue NuGet Package Poses as Tracer.Fody, Steals Cryptocurrency Wallet Data
url: https://thehackernews.com/2025/12/rogue-nuget-package-poses-as-tracerfody.html
source: The Hacker News
date: 2025-12-16
fetch_date: 2025-12-17T03:20:27.971940
---

# Rogue NuGet Package Poses as Tracer.Fody, Steals Cryptocurrency Wallet Data

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

# [Rogue NuGet Package Poses as Tracer.Fody, Steals Cryptocurrency Wallet Data](https://thehackernews.com/2025/12/rogue-nuget-package-poses-as-tracerfody.html)

**Dec 16, 2025**Ravie LakshmananCybersecurity / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEia6FxrdzMepgwKkHbdQyn-9xpiZ9an3eTxENAvy8AZ8sKO43S3KW5Lum4lXXo9PU8NbrVcoTYI4pEoX6MCEJjHPgh4qk5N7wjclH_8IrY_h_2mByqU7H-e8GsRgsJeXcB9bBNDFdkFOLtmqBidpS5YLn1Jbgu4bL9I3yuG8WFT58zGVDNCua4K_6yOHUnT/s790-rw-e365/nuget.jpg)

Cybersecurity researchers have discovered a new malicious NuGet package that typosquats and impersonates the popular .NET tracing library and its author to sneak in a cryptocurrency wallet stealer.

The malicious package, named "[Tracer.Fody.NLog](https://www.nuget.org/packages/Tracer.Fody.NLog)," remained on the repository for nearly six years. It was published by a user named "csnemess" on February 26, 2020. It masquerades as "[Tracer.Fody](https://www.nuget.org/packages/Tracer.Fody)," which is maintained by "[csnemes](https://github.com/csnemes/tracer)." The package continues to remain available as of writing, and has been downloaded at least 2,000 times, out of which 19 took place over the last six weeks for version 3.2.4.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

"It presents itself as a standard .NET tracing integration but in reality functions as a cryptocurrency wallet stealer," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-nuget-package-typosquats-popular-net-tracing-library). "Inside the malicious package, the embedded Tracer.Fody.dll scans the default Stratis wallet directory, reads \*.wallet.json files, extracts wallet data, and exfiltrates it together with the wallet password to threat actor-controlled infrastructure in Russia at [176.113.82[.]163](https://www.virustotal.com/gui/ip-address/176.113.82.163/)."

The software supply chain security company said the threat leveraged a number of tactics that allowed it to elude casual review, including mimicking the legitimate maintainer by using a name that differs by a single letter ("csnemes" vs. "csnemess"), using Cyrillic lookalike characters in the source code, and hiding the malicious routine within a generic helper function ("Guard.NotNull") that's used during regular program execution.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilNnG3aob3x7ss4oC0f07_YM24F5D94XFGtlc6rKNRV3HzTdV82Y8qABhJEQ0vcGIadYbApGAc8jLeQv8hii2rDSUUZEwV-z-gBDyk6PbX5APyUa_vjgvxAKUZDsC_WGUvwaBOeWocxq-E1pjJsq4vYWpaswYABp_R29SS0x2eHAHsMtI72k56cmf887we/s790-rw-e365/tracer.jpg)

Once a project references the malicious package, it activates its behavior by scanning the default Stratis wallet directory on Windows ("%APPDATA%\\StratisNode\\stratis\\StratisMain"), reads \*.wallet.json files and in-memory passwords, and exfiltrates them to the Russian-hosted IP address.

"All exceptions are silently caught, so even if the exfiltration fails, the host application continues to run without any visible error while successful calls quietly leak wallet data to the threat actor's infrastructure," Boychenko said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

Socket said the same IP address was previously put to use in December 2023 in [connection](https://x.com/aSteveCleary/status/1730994352132911613) with another NuGet impersonation attack in which the threat actor published a package named "Cleary.AsyncExtensions" under the alias "stevencleary" and incorporated functionality to siphon wallet seed phrases. The package was so-called to disguise itself as the [AsyncEx NuGet library](https://github.com/StephenCleary/AsyncEx).

The findings once illustrate how malicious typosquats mirroring legitimate tools can stealthily operate without attracting any attention across the open-source repository ecosystems.

"Defenders should expect to see similar activity and follow-on implants that extend this pattern," Socket said. "Likely targets include other logging and tracing integrations, argument validation libraries, and utility packages that are common in .NET projects."

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[NuGet](https://thehackernews.com/search/label/NuGet)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[typosquatting](https://thehackernews.com/search/label/typosquatting)

Trending News

[![Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stronger Data Theft Features](data:image/svg+xml;base64... "Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stronger Data Theft Features")

Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stronger Data Theft Features](https://thehackernews.com/2025/12/android-malware-fvncbot-seedsnatcher.htm...