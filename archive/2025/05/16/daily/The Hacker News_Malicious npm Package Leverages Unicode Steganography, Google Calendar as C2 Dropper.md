---
title: Malicious npm Package Leverages Unicode Steganography, Google Calendar as C2 Dropper
url: https://thehackernews.com/2025/05/malicious-npm-package-leverages-unicode.html
source: The Hacker News
date: 2025-05-16
fetch_date: 2025-10-06T22:29:01.608938
---

# Malicious npm Package Leverages Unicode Steganography, Google Calendar as C2 Dropper

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

# [Malicious npm Package Leverages Unicode Steganography, Google Calendar as C2 Dropper](https://thehackernews.com/2025/05/malicious-npm-package-leverages-unicode.html)

**May 15, 2025**Ravie LakshmananMalware / Threat Intelligence

[![Malicious npm Package](data:image/png;base64... "Malicious npm Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKUJ4RXtmMbXxq4NaRwal0kbQQuRdctdPUXIv70obQhzGhc7LObtaSHs8zgjG28BvtSX0Q7-16sSYPYdnsc1_kkblxArzlSW9KptLEI1Zf8l5Fr-mg6SiuFED-DoYnGeChMSj4795bZITfavy830RdQ4V8FYLOljgsRwIQZWJn05c6NWLWLOfcbYpxqVXY/s790-rw-e365/npm-malware.jpg)

Cybersecurity researchers have discovered a malicious package named "os-info-checker-es6" that disguises itself as an operating system information utility to stealthily drop a next-stage payload onto compromised systems.

"This campaign employs clever Unicode-based steganography to hide its initial malicious code and utilizes a Google Calendar event short link as a dynamic dropper for its final payload," Veracode said in a r[eport](https://www.veracode.com/resources/sophisticated-npm-attack-leveraging-unicode-steganography-and-google-calendar-c2) shared with The Hacker News.

"Os-info-checker-es6" was [first published](https://www.npmjs.com/package/os-info-checker-es6?activeTab=versions) in the npm registry on March 19, 2025, by a user named "kim9123." It has been downloaded [2,001 times](https://npm-stat.com/charts.html?package=os-info-checker-es6) as of writing. The same user has also [uploaded](https://www.npmjs.com/package/skip-tot?activeTab=versions) another npm package called "skip-tot" that lists "os-info-checker-es6" as a dependency. The package has been downloaded [94 times](https://npm-stat.com/charts.html?package=skip-tot).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While the initial five versions exhibited no signs of data exfiltration or malicious behavior, a subsequent iteration uploaded on May 7, 2025, has been found to include obfuscated code in the "preinstall.js" file to parse Unicode "Private Use Access" characters and extract a next-stage payload.

The malicious code, for its part, is designed to contact a Google Calendar event short link ("calendar.app[.]google/<string>") with a Base64-encoded string as the title, which decodes to a remote server with the IP address "140.82.54[.]223." In other words, Google Calendar is a [dead drop resolver](https://thehackernews.com/2025/02/new-malware-campaign-uses-cracked.html) to obfuscate the attacker-controlled infrastructure.

[![Malicious npm Package](data:image/png;base64... "Malicious npm Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoFzLy94EkFg02Mywk43Kw_xJqZuvhVRc_gSkCz2w2EIxRn2vEoqoqzG7FPcwQ6k4yYnYyC0pHJ_a66smgaobAYPe2YTo5fugzLYD-EVSVcQOdHYykZ-IMyknq3YgcCzrVL_UYbjJuWIAkkM3kzDuA5-ISebxllY_24TquTjPxK6CU2DS6ay-RQkdUwvyk/s790-rw-e365/code.png)

However, no additional payloads are distributed at this point. This either indicates that the campaign is either still a work in progress, or currently dormant. Another possibility is that it has already concluded, or that the command-and-control (C2) server is designed to respond only to specific machines that meet certain criteria.

"This use of a legitimate, widely trusted service like Google Calendar as an intermediary to host the next C2 link is a clever tactic to evade detection and make blocking the initial stages of the attack more difficult," Veracode said.

[![Malicious npm Package](data:image/png;base64... "Malicious npm Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhIHOt8Cspr-OHJvi5-K2cbjgl0FmEog_q8nIHQuHNgoRw729AX5NQ9bPZjzAUMzFvcF-zDVKHa46vGqfjnsWkoVrmbaDAAlmkEswM1re1e-N8MXNOAifS6jOgFcB9CtOI4GfZhmAJgOkgBNYJ47-puwxyl01G4K8FZZXUYKx5WxL3gnTvBZvKPBiBL2Dc/s790-rw-e365/invite.png)

The application security company and Aikido, which also [detailed](https://www.aikido.dev/blog/youre-invited-delivering-malware-via-google-calendar-invites-and-puas) the activity, further noted that three other packages have listed "os-info-checker-es6" as a dependency, although it's suspected that the dependent packages are part of the same campaign -

* vue-dev-serverr
* vue-dummyy
* vue-bit

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The os-info-checker-es6 package represents a sophisticated and evolving threat within the npm ecosystem," Veracode said. "The attacker demonstrated a progression from apparent testing to deploying a multi-stage malware."

The disclosure comes as software supply chain security company Socket highlighted typoquatting, Go repository caching abuse, obfuscation, multi-stage execution, slopsquatting, and abuse of legitimate services and developer tools as the six main adversarial techniques adopted by threat actors in the first half of 2025.

"To counter this, defenders must focus on behavioral signals, such as unexpected postinstall scripts, file overwrites, and unauthorized outbound traffic, while validating third-party packages before use," security researchers Kirill Boychenko and Philipp Burckhardt [said](https://socket.dev/blog/malicious-open-source-packages-2025-mid-year-threat-report).

"Static and dynamic analysis, version pinning, and close inspection of CI/CD logs are essential to detecting malicious dependencies before they reach production."

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
[**Share on Hacker News]...