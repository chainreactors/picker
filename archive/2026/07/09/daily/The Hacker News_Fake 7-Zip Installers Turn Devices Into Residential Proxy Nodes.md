---
title: Fake 7-Zip Installers Turn Devices Into Residential Proxy Nodes
url: https://thehackernews.com/2026/07/fake-7-zip-installers-turn-devices-into.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:14.412583
---

# Fake 7-Zip Installers Turn Devices Into Residential Proxy Nodes

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

# [Fake 7-Zip Installers Turn Devices Into Residential Proxy Nodes](https://thehackernews.com/2026/07/fake-7-zip-installers-turn-devices-into.html)

**Ravie Lakshmanan**Jul 09, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0R7K2HuXIaXAr6VokIBdoRH5Zk8L2jJMM5abiDPtiOsT3DsQnI-FRSuTO02mekKGj2Cup9RBBYgAhyo92KHjyCTsMuctH8lYgwysOxpLpHp9uIuL7xBEuojc83nmWH7pcA1KRlu8W9-7b1caaoQMaNX2qATV_7e-CwoPSFk08VwjbRx2M-fgfMcjN3KeW/s1700-e365/7-zip-malware.png)

Cybersecurity researchers have [disclosed](https://www.infoblox.com/blog/threat-intelligence/fake-installers-fake-reviews-fake-services-real-proxies-real-victims/) details of a new threat actor dubbed **Lurking Lizard** that has been operating an end-to-end malicious residential proxy business using an infrastructure comprising more than 230 lookalike domains.

The activity dates back to at least August 2022, according to DNS threat intelligence firm Infoblox. Once such campaign, [observed](https://www.malwarebytes.com/blog/threat-intel/2026/02/fake-7-zip-downloads-are-turning-home-pcs-into-proxy-nodes) earlier this year, involved the actor luring victims with a trojanized 7-Zip installer hosted on a domain named "7zip[.]com," covertly recruiting compromised devices as proxy nodes.

Lurking Lizard is also known to impersonate major proxy providers, including [IPIDEA](https://thehackernews.com/2026/01/google-disrupts-ipidea-one-of-worlds.html), SmartProxy (now Decodo), IP Royal, and 911Proxy, not to mention going to the extent of running fake "independent" review sites to drive traffic to its own scam storefronts. Interestingly, IPIDEA's infrastructure was dismantled by Google in an operation earlier this January.

Subsequent findings from Proxyway have [uncovered](https://proxyway.com/research/we-tested-smartproxyorg-ip-pool-findings) that 773,087 unique IP addresses linked to SmartProxy were also present in a publicly available IPIDEA IP dataset comprising 16,192,293 unique IPs, indicating SmartProxy either "resells IPIDEA's infrastructure directly or uses it as a significant IP source."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

WHOIS analysis and infrastructure fingerprinting suggest that Lurking Lizard is a China-based actor, with the illicit scheme also using popular VPNs and services like HeroSMS as decoys to distribute the proxy malware.

One of the notable aspects of the adversary's modus operandi revolves around acquiring domains when they expire to inherit their accumulated history and legitimacy, a technique known as drop-catching. In some cases, the attacker has taken advantage of the perceived legitimacy surrounding incorrectly referenced domain names (e.g., "7zip[.]com" instead of "7-zip[.]org") to use them to their advantage.

Further analysis of the [IPLogger URL](https://iplogger.org/) ("iplogger[.]com/mnWD") embedded within the samples tied to the 7-Zip campaign has uncovered that the same underlying infrastructure has been used to serve fake installers for 7-Zip, WhatsApp, tools falsely claiming TikTok and YouTube downloaders, and WireVPN.

The use of WireVPN branding represents the latest evolution of the campaign, using a multi-pronged approach to target users across operating systems, including Android, macOS, and Windows. One such Android app, called "[wirevpn - Fast Unlimited Proxy](https://play.google.com/store/apps/details?id=com.wirevpn.freevpn)" and developed by a U.K.-based firm named [WEILAI NETWORK TECHNOLOGY CO., LIMITED](https://find-and-update.company-information.service.gov.uk/company/13720448), has amassed more than 1 million downloads, although it's unclear if these downloads are organic.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFws7IQROTartOIbFrvGuHVg-CnaicfO7pEjspplOMZdL1MLLUvfezDDNfd18wmWNOSVceu1e0MHBRIx5g8FyeL_c8AlXSogMtdEdtyYOf2yBR4Xul1MtuOEQ0aZDiUepASpcQPVeui9MlWDpa7LkTJ8TOuHVOY7XHiGcFj02CMSWaCNa05hjZ76OL7Hfe/s1700-e365/proxy.jpg)

"In the original 7-Zip campaign, victims were directed to malicious installers through tutorial content, search-driven discovery, and lookalike domains," Infoblox said. "Whether similar techniques are driving users to the current desktop variants is unclear, but the mobile applications may serve as an additional acquisition channel."

It's also unclear if the same proxy functionality -- i.e., an exit node funneling third-party traffic through victims' devices -- is present in the mobile applications, and if it's just limited to the desktop applications. Regardless, they paint a picture of what appears to be an unlawful proxy business that fuels a coordinated ecosystem spanning victim acquisition, proxy infrastructure, marketing, and monetization.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The result is an end-to-end operation that goes through two distinct stages:

* Trojanized installers, mobile applications, and other lures recruit victim devices into an actor-controlled proxy botnet.
* The pool is then monetized through lookalike proxy service brands, while fake review sites help drive traffic to the actor’s storefronts.

"We are struck by the parallels between the recently exposed criminal activity in the residential proxy space and malvertising that plagues affiliate advertising," Infoblox said. "There's an obvious story: Your TV may be part of a giant botnet conducting attacks across the internet. But the real story is far more complex, and solutions are still elusive."

"Rather than operating a single malware campaign, Lurking Lizard manages multiple stages of the residential proxy lifecycle for several ...