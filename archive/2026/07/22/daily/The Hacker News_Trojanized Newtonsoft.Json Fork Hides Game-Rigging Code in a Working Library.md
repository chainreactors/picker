---
title: Trojanized Newtonsoft.Json Fork Hides Game-Rigging Code in a Working Library
url: https://thehackernews.com/2026/07/trojanized-newtonsoftjson-fork-hides.html
source: The Hacker News
date: 2026-07-22
fetch_date: 2026-07-23T05:11:48.422432
---

# Trojanized Newtonsoft.Json Fork Hides Game-Rigging Code in a Working Library

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Trojanized Newtonsoft.Json Fork Hides Game-Rigging Code in a Working Library](https://thehackernews.com/2026/07/trojanized-newtonsoftjson-fork-hides.html)

**Ravie Lakshmanan**Jul 22, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmbnZz5gT311oKvULmSO8GP7t6_iPwyHkyn18YX9gpWaA6McGU3BUywygV6gyQ_WBntQjd4mCBZC7mVug_axlJpTqNM2GblbuYyYMf6Np-Zm6P5dvmWeA_aoyZ4bckOlXoAfMC8yXacUfCPHocS9azMsxW7cYbLy6e6iVNH6EMVduEZTLFT_CyAYmud78K/s1700-e365/json-pack.jpg)

Cybersecurity researchers have discovered a NuGet typosquat that's unlike the typical information-stealing malware distributed via package registries: usual info-stealers: it's designed to rig live game results on Digitain.

The package, named "[Newtonsoftt.Json.Net](https://www.nuget.org/packages/Newtonsoftt.Json.Net/)," masquerades as the Newtonsoft.Json library and is a trojanized fork. Seven versions of the package have been published to the NuGet repository: 11.0.4, 11.0.5, 11.0.7, 11.0.8, 11.0.9, 11.0.10, and 11.0.11. The package has been downloaded about 1,200 times to date.

The package has been unlisted by its owner MagicalPuff96, meaning it will not be [surfaced via a search](https://www.nuget.org/packages?q=Newtonsoftt.Json.Net) on NuGet. However, the artifacts are still available for download from the registry.

"The trojan rigs Digitain, an online betting platform, and in later generations, exfiltrates rigged round results to an attacker-controlled server, utilizing the header X-Seq-ApiKey: theperfectheist2025," according to [JFrog](https://jfrog.com/blog/nuget-typosquat-targets-betting-platform/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

What's notable about the package is that it specifically goes after a single entity, while functioning as expected for other users.

"Developers who install it by typo get a real, working Newtonsoft.Json build; the malicious behavior begins after the host initializes JsonConvert.DefaultSettings, and can only succeed on systems that expose the target's specific game backend method, and only after a delay," Guy Korolevski, JFrog security researcher, said.

All seven published versions contain the same trojanized fork of Newtonsoft.Json 13.0. spread across three generations that were published between August 13 and October 10, 2025.

The backdoor initiates itself via the DefaultSettings property setter, which has been altered such that it invokes attacker-controlled code to introduce a randomized delay as a way to sidestep detection before the malicious functionality is fired. The end goal is to target servers running Digitain's crash-game backend, and exfiltrate rigged results to a hard-coded exfiltration point ("185.126.237[.]64:5341") by masquerading it as telemetry data.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyth-ODC0TqlzqN95TZJryqe071XTQ8YevKb5O01SVloXTKDpfoabxkZWW5rMsfH0rhyphenhyphenVXlgjdkC_JYWyQAoUW_sgpTSiUTZAeCRy02zbsScD4O4Bis1dU4YKwiPnnwFT3ZA55QCs4dDrtCbMZOM39BjaNJhfoACdJO-ESdPK7NiyYqCgsiR45uh5BcMjl/s1700-e365/post.jpg)

"What changes across versions is the obfuscation, the rigging strategy, and the exfiltration path," JFrog explained. "The progression shows the author iteratively hardening the payload: Gen-1 was a local-only rigging proof of concept; Gen-2 added exfiltration but hid it behind reflection and ConfuserEx, Gen-3 cleaned up the rigging and stabilized the exfiltration, with 11.0.11 left completely unobfuscated, consistent with an accidental clean build being published."

The primary victim of the rigging is Digitain, the operator of the FG-Crash betting game. The package metadata has been found to leak an internal Digitain repository URL seven times (in all the package versions), indicating the author had access to FG-Crash's source code.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

"The trojan only activates when JsonConvert.DefaultSettings is assigned and only patches a method present in the FG-Crash backend," Korolevski said. "Non-targeted consumers may see only a working JSON library and no rigging behavior, which is exactly what makes this typosquat attack so effective."

"There is no credential theft, persistence, or lateral-movement capability in the payload. Its sole purpose is to compromise the integrity of the crash game. Other developers who installed this package may not even notice that they installed malware, or have any negative results in their application since it is only targeting a specific organization."

To counter the threat, developers are advised to remove the typosquat package, block the command-and-control (C2) address, and pin Newtonsoft.Json to a known-good version via packages.lock.json. Digitain, for its part, has revealed it's been aware of the issue and that it has taken steps to resolve it. That having said, the full extent of the exposure remains unknown.

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
[![Facebook Messenger](data:...