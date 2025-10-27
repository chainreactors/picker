---
title: Over a Dozen Malicious npm Packages Target Roblox Game Developers
url: https://thehackernews.com/2023/08/over-dozen-malicious-npm-packages.html
source: The Hacker News
date: 2023-08-24
fetch_date: 2025-10-04T12:04:03.286228
---

# Over a Dozen Malicious npm Packages Target Roblox Game Developers

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

# [Over a Dozen Malicious npm Packages Target Roblox Game Developers](https://thehackernews.com/2023/08/over-dozen-malicious-npm-packages.html)

**Aug 23, 2023**Ravie LakshmananSoftware Security / Malware

[![Roblox Game Developers](data:image/png;base64... "Roblox Game Developers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjw5WioLH4sVWYPVGuxL2tuG88DHAgG6SiFfA1_196R6ZU38lIdJsjXAFxytOAOrwI3x1_uLJ9-yTVJX0WGkmG5JfURo8--EMbdrHLaWx_tROly-pczTrsv2gxvS0qMtxRL7oeG50PEI3JCW-f601ZU3N32g5B-4xocBw5SacKDvQ-k3AHwUplF0YcYzeGL/s790-rw-e365/gacming.jpg)

More than a dozen malicious packages have been discovered on the npm package repository since the start of August 2023 with capabilities to deploy an open-source information stealer called **Luna Token Grabber** on systems belonging to Roblox developers.

The ongoing campaign, first detected on August 1 by ReversingLabs, employs modules that masquerade as the legitimate package [noblox.js](https://www.npmjs.com/package/noblox.js), an API wrapper that's used to create scripts that interact with the Roblox gaming platform.

The software supply chain security company described the activity as a "replay of an attack [uncovered](https://thehackernews.com/2021/10/malicious-npm-libraries-caught.html) two years ago" in October 2021.

"The malicious packages [...] reproduce code from the legitimate noblox.js package but add malicious, information-stealing functions," software threat researcher Lucija Valentić [said](https://www.reversinglabs.com/blog/fake-roblox-api-packages-luna-grabber-npm) in a Tuesday analysis.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The packages were cumulatively downloaded 963 times before they were taken down. The names of the rogue packages are as follows -

* noblox.js-vps (versions 4.14.0 to 4.23.0)
* noblox.js-ssh (versions 4.2.3 to 4.2.5)
* noblox.js-secure (versions 4.1.0, 4.2.0 to 4.2.3)

While the broad contours of the latest attack wave remain similar to the previous one, it also exhibits some unique characteristics of its own, notably in the deployment of an executable that delivers Luna Grabber.

[![Roblox Game Developers](data:image/png;base64... "Roblox Game Developers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0Fgc7g-o9642EhHvEaSwgJE45iFI22tSYGNFXHUgQf2Zk9_BbcVh0HXmft5uhX6DyLazoMBkLuh5Fb6oKYEYMiDV0zOn-fS0dQmegJh2hy2BxrJyQ2Gx_TqM2J-Pc_FmOkYzUKBwFqpl5s86UJSS2bBFH5b_xPFoBv2nTXsgPWSn_jRkPVhG4c9R5w7Ou/s790-rw-e365/noblox.jpg)

The development is one of the rare instances of a multi-stage infection sequence uncovered on npm, ReversingLabs said.

"With malicious campaigns that target the software supply chain, the difference between sophisticated and unsophisticated attacks often comes down to the level of effort the malicious actors make to disguise their attack and make their malicious packages look legitimate," Valentić pointed out.

The modules, in particular, cleverly conceal their malicious functionality in a separate file named postinstall.js that's invoked after installation.

That's because the genuine noblox.js package also employs a [file with the same name](https://github.com/noblox/noblox.js/blob/master/postinstall.js) to display a thank you message to its users alongside links to its documentation and GitHub repository.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The bogus variants, on the other hand, utilize the JavaScript file to verify to see if the package is installed on a Windows machine, and if so, download and execute a second-stage payload hosted on Discord CDN, or alternatively, show an error message.

ReversingLabs said that the second-stage continued to evolve with each iteration, progressively adding more functionality and obfuscation mechanisms to thwart analysis. The primary responsibility of the script is to download [Luna Token Grabber](https://github.com/Smug246/Luna-Grabber), a Python tool that can siphon credentials from web browsers as well as Discord tokens.

However, it appears that the threat actor behind the npm campaign appears to have opted only to harvest system information from victims using a configurable builder made available by the author(s) behind Luna Token Grabber.

This is not the first time Luna Token Grabber has been spotted in the wild. Earlier this June, Trellix [disclosed](https://thehackernews.com/2023/06/new-golang-based-skuld-malware-stealing.html) details of a new Go-based information stealer called Skuld that overlaps with the malware strain.

"It highlights yet again the trend of malicious actors using typosquatting as a technique to fool developers into downloading malicious code under the guise of similarly named, legitimate packages," Valentić said.

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

[Gaming Software](https://thehackernews.com/search/label/Gaming%20Software)[NPM Malware](https://thehackernews.com/search/label/NPM%20Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix ...