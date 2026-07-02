---
title: SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT
url: https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:21.296638
---

# SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT

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

# [SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT](https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html)

**Ravie Lakshmanan**Jul 01, 2026Malware / SEO Poisoning

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbKfADFEhazeaRztmVJkTBhFqZxALUDBwsOV_25bWjZ6Qm3pCBoSSawssWOOJC2ZQ7M6hrUDRXLfR5gcpWRkkaSdNtSPCz-FLrG5Dy4-Y-IzEMt_souSqJuc3JK9FNQ9p2-dT7Ojf3ufzPkWBpLNyDAVeeuYS7Ya-BJWT4MmAHz7OjHvwjMSCfF5Jvahyphenhyphenj/s1700-e365/SEO-MALWARE.jpg)

Unknown threat actors are leveraging the ScreenConnect remote access tool as a way to deploy and execute [AsyncRAT](https://www.forcepoint.com/blog/x-labs/asyncrat-reloaded-python-trycloudflare-malware).

Kaspersky said the activity is part of a "massive, multi-domain, multi-language" campaign that distributes malicious installer archives hosted on spoofed websites.

These installers masquerade as popular software like OBS Studio, DNS Jumper, DS4Windows, and Bandicam, among others. The Russian cybersecurity company said it identified more than 90 domain names localized across 10 languages, including English, Russian, Chinese, German, French, Spanish, Portuguese, and Arabic. Some of these domains were set up between August 2025 and March 2026.

"The malicious archives bundle a legitimate, signed Microsoft install.exe binary alongside a rogue install.res.1033.dll library," security researcher Denis Kulik [said](https://securelist.com/tr/the-soc-files-screenconnect-campaign-with-asyncrat/120472/). "It is loaded onto the device via DLL side-loading and deploys the ScreenConnect service, which awaits further instructions from the threat actors."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"This allowed the attackers to maintain control over compromised endpoints, with victims ranging from individual users to organizations."

Once ScreenConnect is up and running, the service creates and executes a PowerShell script ("Fj5NmEsp9EuKrun.ps1"), which configures Microsoft Defender exclusions, disables User Account Control (UAC) prompts, and then creates a Visual Basic Script (VBScript) file called "installer\_method3\_stream.vbs."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1hJV3xz-yT0czNtUzFEoirdeGaAA3zWuPLvZSpnXDBCK_TlksWOkQQYZlaZ2_E_R5D-eW4dzTGldz3eLcxESWP5DzWq1X4PQ0o3T5mOevVyH-khqq1R6tOo8UFvczB5Z-qy7YbgTI1BUG_gVSFGdkewhOLxltxRqObEXyCU5ABzoRtH7iUJkRO6a42XGn/s1700-e365/ss.png)

The script, for its part, creates a set of five files in the "C:\Users\Public directory" -

* msgbox.txt
* secret\_bytes.txt
* 1.vb
* cap.ps1
* script.vbs

In the next stage, it triggers the execution of "script.vbs," a script that's responsible for terminating all active PowerShell processes and running "cap.ps1" in a hidden window. The primary goal of the PowerShell script is to read the contents of the "secret\_bytes.txt" file, extract from it the AsyncRAT module, and run it using [process hollowing](https://attack.mitre.org/techniques/T1055/012/).

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The malware then establishes a connection to a remote server ("mora1987.work[.]gd"), allowing the threat actor to covertly control infected Windows systems, steal sensitive data, and monitor user activity by recording screen content.

Persistence is established by means of a scheduled task ("MasterPackager.Updater") that's activated every two minutes to execute "script.vbs," ensuring that the entire attack is run after a system reboot.

"The threat actor disguises ScreenConnect as popular utilities and distributes it through fraudulent websites that mimic official product pages," Kaspersky said. "The attackers leverage search engine optimization techniques to push these sites to the top of search results in engines like Google and Bing."

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

[AsyncRAT](https://thehackernews.com/search/label/AsyncRAT), [DLL side-loading](https://thehackernews.com/search/label/DLL%20side-loading), [Malware](https://thehackernews.com/search/label/Malware), [powershell](https://thehackernews.com/search/label/powershell), [process hollowing](https://thehackernews.com/search/label/process%20hollowing), [remote access tool](https://thehackernews.com/search/label/remote%20access%20tool), [ScreenConnect](https://thehackernews.com/search/label/ScreenConnect), [SEO poisoning](https://thehackernews.com/search/label/SEO%20poisoning)

⚡ Top Stories This Week

[![Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](data:image/svg+xml;base64... "Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability")

Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)

[![...