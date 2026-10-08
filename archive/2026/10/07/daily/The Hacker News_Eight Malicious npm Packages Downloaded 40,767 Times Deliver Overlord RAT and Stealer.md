---
title: Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord RAT and Stealer
url: https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html
source: The Hacker News
date: 2026-10-07
fetch_date: 2026-10-08T08:08:36.010661
---

# Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord RAT and Stealer

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord RAT and Stealer](https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html)

**Ravie Lakshmanan**Oct 07, 2026Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgopANe3MXyNNOXog__x1pF53wYoQxinI47tN9gLrZSzJfumz-Dg05ZfyjiGsqF47Pugj71iZ1buX7OEiupWYa09xVQdu7DKOMX5NO-uGKCF0UjNila0x5fNiYw5NWEX1TUQTPidjT5NnGmPwM_6mGfKcOxqcjZuPAZLdzRX5u_TXJM76GQ6mQOkikw_kxo/s1700-nu-rw-lo-l85-e365/npm-malware.jpg)

Cybersecurity researchers have disclosed details of a long-running npm supply chain malware campaign that pushes information stealers and remote access trojans (RAT) to compromised hosts.

The campaign has been codenamed **MALFEX** by [CloudSEK](https://www.cloudsek.com/blog/malfex-malicious-npm-postinstall-supply-chain-campaign) and [Checkmarx](https://checkmarx.com/zero-post/malfex-npm-malware-campaign-three-payloads-and-an-adversary-that-signs-their-work/). The activity is assessed to be the work of a lone threat actor who appears to have published 12 packages since August 2023, eight of which have been flagged as malicious.

* The attack is designed to infect Windows systems through three separate pathways -
* A loader for [Overlord](https://github.com/vxaboveground/Overlord), an open-source RAT written in Go that uses Solana transactions to extract the command-and-control (C2) address
* A chain that installs movinlike, a Node.js stealer targeting Discord, browsers, Telegram, and cryptocurrency wallets, and
* A downloader

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The list of identified malicious packages is below -

* tlxbnhd
* tldriver
* mxdriver
* img-to-native
* native-runner
* function-flag (Still live)
* function-color (Still live)
* cdn-img-fetch (Still live)

In all, these packages have been collectively downloaded 40,767 times. Of these, 37,419 downloads correspond to "function-flag," making it the largest driver of this activity. The package was first published in July 2024. The latest version was released on August 4, 2025.

The project description for the npm package features a welcome message written in Portuguese that states: "This project was created with a lot of love and dedication by the Malfex team, whose owner is Murizada."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7Tm9dJYQ14c87MhbFukC1Z1T4qlxyjfhM7jSHOsWAHjG_lVqYs3lYd2-YtmaOjSKp4YhzscLXA4SMRbCOLkNN8zq86_FWwJpVDnhEl2DntqNxGfVH4pFhHqZBRoqsIULKLMSXL4Sf2Ijgde0wUAo_WZD6tOVs45-GPLeWi8AUz05dNELqIuuHYhsSnm8S/s1700-nu-rw-lo-l85-e365/aes.jpg)

Three of the packages, "tlxbnhd," "tldriver," and "mxdriver," act as Overlord RAT loaders, with the malicious code triggered via lifecycle hooks to download and run a Windows executable.

A second subset of the npm packages, such as "img-to-native," requires "cdn-img-fetch" to retrieve and execute a Go executable, which then fetches a Node.js stealer capable of harvesting sensitive data.

Present within "function-flag" is a postinstall hook that runs a JavaScript payload to download a payload from a remote server. Each version of the package has been found to serve a payload from a different location. The "function-color" package embeds no payload of its own, but lists "function-flag" as a dependency.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

"In 1.7.3, the current latest version, the postinstall script runs example.js, which calls the package's ASCII art function with the Bloody font," Checkmarx said. "That font value triggers a hidden routine that downloads node.exe from cdnzona.discloud.app, a host on a Brazilian application hosting service, saves it to %APPDATA%\node.exe, and runs it with its window hidden."

Interestingly, Overload RAT has been observed in two other campaigns since July 2026: one involving the [exploitation of WordPress flaws](https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html) (CVE-2026-63030 and CVE-2026-60137, aka wp2shell) and a [macOS campaign](https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/) in which a fake Zoom installer is used to deploy the RAT. The fake Zoom installer campaign shares tactical overlaps with a suspected North Korea-aligned threat cluster dubbed [UNK\_DeadDrop](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html).

"The operator is Portuguese-speaking, the git commits sit at -0300, one repository description is in Portuguese, and the GitHub display name and email give a common Brazilian handle," CloudSEK said. "None of this is an argument that the campaign targets Brazil. It is a piece of attribution to the operator's own linguistic space and nothing more. The delivery is npm and Discord, both of which are global; the second-stage targeting is opportunistic."

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

[Malware](https://thehackernews.com/search/label/Malware), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain), [Windows Security](htt...