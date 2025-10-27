---
title: North Korean Hackers Target Developers with Malicious npm Packages
url: https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html
source: The Hacker News
date: 2024-08-31
fetch_date: 2025-10-06T18:12:55.013074
---

# North Korean Hackers Target Developers with Malicious npm Packages

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

# [North Korean Hackers Target Developers with Malicious npm Packages](https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html)

**Aug 30, 2024**Ravie LakshmananCryptocurrency / Malware

[![Malicious npm Packages](data:image/png;base64... "Malicious npm Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIpR87w3MZzu3tokB-OtMJ8c8lZGfO0E5AK6xJpWlKFjH5q3OlkKo1bDpp45nFMMi-DbSl_VmO-Lc3IkmZv5ZJQDOhiR9Sv001aIAo3pfiDoe65VswkeNBAfWXYovZ11pYgAXM_4URIYGiBJrRP0_rj2qel7cNWTaP3zY_Jo4YXFDxds6OuMr3AtS3fW9T/s790-rw-e365/crypto.png)

Threat actors with ties to North Korea have been observed publishing a set of malicious packages to the npm registry, indicating "coordinated and relentless" efforts to target developers with malware and steal cryptocurrency assets.

The latest wave, which was observed between August 12 and 27, 2024, involved packages named temp-etherscan-api, ethersscan-api, telegram-con, helmet-validate, and qq-console.

"Behaviors in this campaign lead us to believe that qq-console is attributable to the North Korean campaign known as 'Contagious Interview,'" software supply chain security firm Phylum [said](https://blog.phylum.io/north-korea-still-attacking-developers-via-npm/).

Contagious Interview refers to an [ongoing campaign](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html) that seeks to compromise software developers with information stealing malware as part of a purported job interview process that involves tricking them into downloading bogus npm packages or fake installers for video conferencing software such as MiroTalk hosted on decoy websites.

The end goal of the attacks is to deploy a Python payload named InvisibleFerret that can exfiltrate sensitive data from cryptocurrency wallet browser extensions and set up persistence on the host using legitimate remote desktop software such as AnyDesk. CrowdStrike is tracking the activity under the moniker Famous Chollima.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The newly observed helmet-validate package adopts a new approach in that it embeds a piece of JavaScript code file called config.js that directly executes JavaScript hosted on a remote domain ("ipcheck[.]cloud") using the [eval() function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval).

"Our investigation revealed that ipcheck[.]cloud resolves to the same IP address (167[.]88[.]36[.]13) that mirotalk[.]net resolved to when it was online," Phylum said, highlighting [potential links](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html) between the two sets of attacks.

The company said it also observed another package called sass-notification that was uploaded on August 27, 2024, which shared similarities with previously uncovered npm libraries like [call-blockflow](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html). These packages have been attributed to another North Korean threat group called [Moonstone Sleet](https://thehackernews.com/2024/08/north-korean-hackers-moonstone-sleet.html).

"These attacks are characterized by using obfuscated JavaScript to write and execute batch and PowerShell scripts," it said. "The scripts download and decrypt a remote payload, execute it as a DLL, and then attempt to clean up all traces of malicious activity, leaving behind a seemingly benign package on the victim's machine."

### Famous Chollima Poses as IT Workers in U.S. Firms

The disclosure comes as CrowdStrike linked [Famous Chollima](https://www.crowdstrike.com/adversaries/famous-chollima/) (formerly BadClone) to [insider threat operations](https://thehackernews.com/2024/08/doj-charges-nashville-man-for-helping.html) that entail infiltrating corporate environments under the pretext of legitimate employment.

"Famous Chollima carried out these operations by obtaining contract or full-time equivalent employment, using falsified or stolen identity documents to bypass background checks," the company [said](https://www.crowdstrike.com/resources/reports/threat-hunting-report/). "When applying for a job, these malicious insiders submitted a résumé typically listing previous employment with a prominent company as well as additional lesser-known companies and no employment gaps."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

While these operations are predominantly financially motivated, a subset of the incidents are said to have involved the exfiltration of sensitive information. CrowdStrike said it has identified the threat actors applying to or actively working at more than 100 unique companies over the past year, most of which are located in the U.S., Saudi Arabia, France, the Philippines, and Ukraine, among others.

Prominently targeted sectors include technology, fintech, financial services, professional services, retail, transportation, manufacturing, insurance, pharmaceutical, social media, and media companies.

"After obtaining employee-level access to victim networks, the insiders performed minimal tasks related to their job role," the company further said. "In some cases, the insiders also attempted to exfiltrate data using Git, SharePoint, and OneDrive."

"Additionally, the insiders installed the following RMM tools: RustDesk, AnyDesk, TinyPilot, VS Code Dev Tunnels, and Google Chrome Remote Desktop. The insiders then leveraged these RMM tools in tandem with company network credentials, which allowed numerous IP addresses to connect to the victim's system."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_sha...