---
title: Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS
url: https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
source: The Hacker News
date: 2026-08-03
fetch_date: 2026-08-04T05:01:12.383851
---

# Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS

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

![cybersecurity](data:image/svg+xml;base64...)

# [Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS](https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html)

**Ravie Lakshmanan**Aug 03, 2026Mobile Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvbg0AbgcDL8IouGo4deahk3vOuegzB-hxhUxAok05EuI5uuYJUDP-mUVS1w-gr9Oedf6JzF9qEB3l8MWVnsFGkmZ4ZorInHavwKWrQ7toTmv64uc4EnJdoFDqGlDPQsgcTwnJo8rlZyfG9yFu60fNE51Di00aVdZoiv5YMIvobc6xuWZhT_cKDk3ikV-P/s1700-e365/apple.jpg)

An unknown Chinese-speaking threat actor has been observed running a campaign targeting Apple iOS devices by leveraging a publicly leaked version of the **DarkSword** exploit kit.

Attack surface management platform Censys said it identified the threat actor running more than 100 web properties, most of which are fake Amazon Web Services (AWS) sign-in pages on a domain that also hosts the exploit toolkit.

"The hosting concentrates in Hong Kong but reaches into Japan, the United States, and Europe," Censys researcher Aidan Holland [said](https://censys.com/blog/darkswords-panel-sprawl/) in an analysis published on July 31, 2026.

DarkSword, discovered and detailed earlier this year by Google Threat Intelligence Group (GTIG), iVerify, and Lookout, refers to a [full-chain exploit kit](https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html) that is believed to have been used by commercial surveillance vendors and suspected state-sponsored actors in disparate campaigns targeting Saudi Arabia, Turkey, Malaysia, and Ukraine since at least November 2025.

The kit, which specifically targets iOS versions 18.4 through 18.7, has been observed to employ watering holes as a starting point to trigger now-patched vulnerabilities in Apple's mobile operating system to execute JavaScript that ultimately facilitates the deployment of GHOSTBLADE, an information-stealing malware.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The use of DarkSword has since [expanded](https://thehackernews.com/2026/03/ta446-deploys-leaked-darksword-ios.html) in scope following a [public leak of its source code](https://github.com/ghh-jb/DarkSword), prompting other threat actors to join the exploitation bandwagon.

The latest findings from Censys show that the login page for a panel called "DarkSword Admin" matches seven hosts across three countries as of July 30, 2026, in addition to a Singapore-based host ("38.181.52[.]95") running three distinct exploit-panel front ends and a Hong Kong host that bundles an Apple ID credential-harvesting decoy ("103.106.190[.]217").

One such login panel served on the IP address "38.22.89[.]117:8888" contains Chinese-language field labels for "username," "password," and "Log in." The other six IP addresses are below -

* 103.97.128[.]67:8888
* 162.4.136[.]30:8888
* 223.26.63[.]56:8888
* 151.243.126[.]191:8888
* 107.175.49[.]181:3000
* 103.238.129[.]112:3000

The attack flow is fairly consistent in that it begins when a victim reaches one of the operator's domains - an AWS-console impersonation subdomain or an Apple ID sign-in page - causing a malicious iframe element to load JavaScript that fires the DarkSword chain and finally deploys GHOSTBLADE modules.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjC2023_FhgdkmFuhq6rIpbwUNR_BRF2d6leerjBE3rlWRO5QDUYkYmRzrYUKm8tzmdzv35Uq2vAY3Ilfl9tihn2Z3YwvYkNaleges5YehaHvUIOV7RN0QOTpvrbHF6o54ZW36S3rmsKcrB_AX-sKXAXnNprsi7zSjfvxLU-Yq4PFDSj5U_fUbpo4yfQENP/s1700-e365/C2-FLOW.jpg)

On successful exploitation, the implant delivers keychain, iCloud, and Wi-Fi credential-dumping modules and commences the file-exfiltration sweep. The harvested data is then packaged and transmitted to attacker-controlled endpoints. The attacker then logs in to one of the panels, namely DarkSword Admin, Decode Dashboard, or C2 Control Panel, to extract the pilfered data.

The IP addresses associated with the two other login panels are as follows -

* 103.226.155[.]200 (Decode Dashboard)
* 103.226.155[.]201 (Decode Dashboard)
* 202.8.120[.]249 (Decode Dashboard)
* 103.106.190[.]217 (C2 Control Panel), which also co-hosts the Apple ID decoy sign-in page

"This cluster runs the leaked kit rather than a reimplementation, and the evidence is a shared staging-page hash plus Russian-language code comments carried over from the leaked source," Holland said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

What's more, the Singaporean host (now no longer active) has been found to host an administration panel for [Coruna](https://thehackernews.com/2026/03/coruna-ios-exploit-kit-uses-23-exploits.html), another iOS exploit kit that predates DarkSword and goes after iOS versions 3.0 through 17.2.1. There is some evidence to suggest that a threat actor known as UNC6353 has leveraged both exploit kits in its attacks aimed at Ukrainian targets.

Censys said it also discovered an open directory listing in Frankfurt ("93.152.221[.]37") that exposes the operator's tooling, including an SSH key comment "jkcing@apt," a web-content fuzzer, and references to a previously undocumented malware family referred to as "Thorn C2."

"The 'C2 Control Panel' login itself is a visually distinct build from the other two panels: a near-black #06060d background, a #ff0050 red accent, an animated particle-canvas effect, a group name rendered directly on the page (亚太集团, 'Asia-Pacific Group'), and a visible Telegram contact link, hxxps://t[.]me/YATA0000," it noted. "That's the first direct contact channel we've recovered for this operator; the other panels give us a login gate and nothing else."

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
[**Share on Linkedin](#link_share...