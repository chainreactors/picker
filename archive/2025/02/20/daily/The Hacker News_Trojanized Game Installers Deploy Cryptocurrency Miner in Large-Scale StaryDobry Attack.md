---
title: Trojanized Game Installers Deploy Cryptocurrency Miner in Large-Scale StaryDobry Attack
url: https://thehackernews.com/2025/02/trojanized-game-installers-deploy.html
source: The Hacker News
date: 2025-02-20
fetch_date: 2025-10-06T20:39:22.632225
---

# Trojanized Game Installers Deploy Cryptocurrency Miner in Large-Scale StaryDobry Attack

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

# [Trojanized Game Installers Deploy Cryptocurrency Miner in Large-Scale StaryDobry Attack](https://thehackernews.com/2025/02/trojanized-game-installers-deploy.html)

**Feb 19, 2025**The Hacker NewsWindows Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj86ugAL7x4EghNsHHh_LHlDsUGj3E8JnGFOYMJmtSWE88IBvJ4YagyZ-n-puZn5okN5xg8qrxkC7suD_yWnncK7fNQ7DL-QIYJJNnJXVHBedUxTF2GxMyVXlo1G2_pQT-ihFtqsUtXssWmj4oHlZDWNksUa0D-tw0cQI0e732kZGETYbcS7gInwO0Psig/s790-rw-e365/game.png)

Users who are on the lookout for popular games were lured into downloading trojanized installers that led to the deployment of a cryptocurrency miner on compromised Windows hosts.

The large-scale activity has been codenamed **StaryDobry** by Russian cybersecurity company Kaspersky, which first detected it on December 31, 2024. It lasted for a month.

Targets of the campaign include individuals and businesses worldwide, with Kaspersky's telemetry finding higher infection concentrations in Russia, Brazil, Germany, Belarus, and Kazakhstan.

"This approach helped the threat actors make the most out of the miner implant by targeting powerful gaming machines capable of sustaining mining activity," researchers Tatyana Shishkova and Kirill Korchemny [said](https://securelist.com/starydobry-campaign-spreads-xmrig-miner-via-torrents/115509/) in an analysis published Tuesday.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The XMRig cryptocurrency miner campaign employs popular simulator and physics games like BeamNG.drive, Garry's Mod, Dyson Sphere Program, Universe Sandbox, and Plutocracy as lures to initiate a sophisticated attack chain.

This involves uploading poisoned game installers crafted using [Inno Setup](https://jrsoftware.org/isinfo.php) onto various torrent sites in September 2024, indicating that the unidentified threat actors behind the campaign had carefully planned the attacks.

Users who end up downloading these releases, also called "repacks" are served an installer screen that urges them to proceed with the setup process, during which a dropper ("unrar.dll") is extracted and executed.

The DLL file continues its execution only after running a series of checks to determine if it's running in a debugging or sandboxed environment, a demonstration of its highly evasive behavior.

Subsequently, it polls various sites like api.myip [.]com, ip-api [.]com, and ipwho [.]is to obtain the user's IP address and estimate their location. If it fails in this step, the country is defaulted to China or Belarus for reasons that are not wholly clear.

The next phase entails gathering a fingerprint of the machine, decrypting another executable ("MTX64.exe"), and writing its contents to a file on disk named "Windows.Graphics.ThumbnailHandler.dll" in either the %SystemRoot% or %SystemRoot%\Sysnative folder.

Based on a legitimate open-source project called [EpubShellExtThumbnailHandler](https://github.com/Aeroblast/EpubThumbnailHandler), MTX64 modifies the Windows Shell Extension Thumbnail Handler functionality for its own gain by loading a next-stage payload, a portable executable named Kickstarter that then unpacks an encrypted blob embedded within it.

The blob, like in the previous step, is written to disk under the name "Unix.Directory.IconHandler.dll" in the folder %appdata\Roaming\Microsoft\Credentials\%InstallDate%\.

The newly created DLL is configured to retrieve the final-stage binary from a remote server that's responsible for running the miner implant, while also continuously checking for taskmgr.exe and procmon.exe in the list of running processes. The artifact is promptly terminated if any of the processes are detected.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The miner is a slightly tweaked version of XMRig that uses a predefined command line to initiate the mining process on machines with CPUs that have 8 or more cores.

"If there are fewer than 8, the miner does not start," the researchers said. "Moreover, the attacker chose to host a mining pool server in their own infrastructure instead of using a public one."

"XMRig parses the constructed command line using its built-in functionality. The miner also creates a separate thread to check for process monitors running in the system, using the same method as in the previous stage."

StaryDobry remains unattributed given the lack of indicators that could tie it to any known crimeware actors. That said, the presence of Russian language strings in the samples alludes to the possibility of a Russian-speaking threat actor.

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Gaming Security](https://thehackernews.com/search/label/Gaming%20Security)[hacking](https...