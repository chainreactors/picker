---
title: New Mandrake Spyware Found in Google Play Store Apps After Two Years
url: https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html
source: The Hacker News
date: 2024-07-31
fetch_date: 2025-10-06T17:46:58.905851
---

# New Mandrake Spyware Found in Google Play Store Apps After Two Years

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

# [New Mandrake Spyware Found in Google Play Store Apps After Two Years](https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html)

**Jul 30, 2024**Ravie LakshmananMobile Security / Spyware

[![Mandrake Spyware](data:image/png;base64... "Mandrake Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4LbXPeVZKVfmJCuoOi0N2kt7iFS02UwVsrfQO364C3B8Gb09tSCQxshhcOC5ZuhKnQaTauYH0OkpOZH0vmlplCObtOpph5P1y3_xwcCTo4I7mF95qPTCe0hXoPAhyphenhyphenETI63JJSEIvCnMCf_qAy7mYIOABLgVZiRGlsOO2Dsnxgz-Q5V08oPv0gEzKwCAtn/s790-rw-e365/android.png)

A new iteration of a sophisticated Android spyware called **Mandrake** has been discovered in five applications that were available for download from the Google Play Store and remained undetected for two years.

The applications attracted a total of more than 32,000 installations before being pulled from the app storefront, Kaspersky said in a Monday write-up. A majority of the downloads originated from Canada, Germany, Italy, Mexico, Spain, Peru, and the U.K.

"The new samples included new layers of obfuscation and evasion techniques, such as moving malicious functionality to obfuscated native libraries, using certificate pinning for C2 communications, and performing a wide array of tests to check if Mandrake was running on a rooted device or in an emulated environment," researchers Tatyana Shishkova and Igor Golovin [said](https://securelist.com/mandrake-apps-return-to-google-play/113147/).

Mandrake was [first documented](https://www.bitdefender.com/blog/labs/mandrake-owning-android-devices-since-2016/) by Romanian cybersecurity vendor Bitdefender in May 2020, describing its deliberate approach to infect a handful of devices while managing to lurk in the shadows since 2016. The malware has yet to be attributed to a threat actor or group.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The updated variants are characterized by the use of [OLLVM](https://github.com/obfuscator-llvm/obfuscator/wiki) to conceal the main functionality, while also incorporating an array of sandbox evasion and anti-analysis techniques to prevent the code from being executed in environments operated by malware analysts.

The list of apps containing Mandrake is below -

* AirFS (com.airft.ftrnsfr)
* Amber (com.shrp.sght)
* Astro Explorer (com.astro.dscvr)
* Brain Matrix (com.brnmth.mtrx)
* CryptoPulsing (com.cryptopulsing.browser)

The apps pack in three stages: A dropper that launches a loader responsible for executing the core component of the malware after downloading and decrypting it from a command-and-control (C2) server.

[![Mandrake Spyware](data:image/png;base64... "Mandrake Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlXh7cynF3Hz-wEhPDgRsHPM29VlU4kRydwz4wOY8lUzvsj1QE_2HDGgBKjuxbgAhZmJLoyO484qFxojsv3S_awhfI6fbuUIP_BTV4a0DXdBWMQYMYSKhQ78xZ5QGZTwxwYyLPs6Lr679lgwLqqAgL1UKWiObW8z_qQ0uuSwXAoeSDI-B5fGVAD8ms8Mwh/s790-rw-e365/Mandrake_04.png)

The second-stage payload is also capable of collecting information about the device's connectivity status, installed applications, battery percentage, external IP address, and current Google Play version. Furthermore, it can wipe the core module and request for permissions to draw overlays and run in the background.

The third-stage supports additional commands to load a specific URL in a WebView and initiate a remote screen sharing session as well as record the device screen with the goal of stealing victims' credentials and dropping more malware.

"Android 13 introduced the 'Restricted Settings' feature, which prohibits sideloaded applications from directly requesting dangerous permissions," the researchers said. "To bypass this feature, Mandrake processes the installation with a ['session-based](https://developer.android.com/reference/android/content/pm/PackageInstaller.Session)' [package installer](https://thehackernews.com/2022/08/cybercriminals-developing-bugdrop.html)."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Russian security company described Mandrake as an example of a dynamically evolving threat that's constantly refining its tradecraft to bypass defense mechanisms and evade detection.

"This highlights the threat actors' formidable skills, and also that stricter controls for applications before being published in the markets only translate into more sophisticated, harder-to-detect threats sneaking into official app marketplaces," it said.

When reached for comment, Google told The Hacker News that it's continuously shoring up Google Play Protect defenses as new malicious apps are flagged and that it's enhancing its capabilities to include [live threat detection](https://thehackernews.com/2024/05/android-15-introduces-new-features-to.html) to tackle obfuscation and anti-evasion techniques.

"Android users are automatically protected against known versions of this malware by Google Play Protect, which is on by default on Android devices with Google Play Services," a Google spokesperson said. "Google Play Protect can warn users or block apps known to exhibit malicious behavior, even when those apps come from sources outside of Play."

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#...