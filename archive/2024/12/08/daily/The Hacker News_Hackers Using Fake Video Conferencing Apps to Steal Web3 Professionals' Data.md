---
title: Hackers Using Fake Video Conferencing Apps to Steal Web3 Professionals' Data
url: https://thehackernews.com/2024/12/hackers-using-fake-video-conferencing.html
source: The Hacker News
date: 2024-12-08
fetch_date: 2025-10-06T19:38:49.601526
---

# Hackers Using Fake Video Conferencing Apps to Steal Web3 Professionals' Data

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

# [Hackers Using Fake Video Conferencing Apps to Steal Web3 Professionals' Data](https://thehackernews.com/2024/12/hackers-using-fake-video-conferencing.html)

**Dec 07, 2024**Ravie LakshmananMalware / Web3 Security

[![Fake Video Conferencing Apps](data:image/png;base64... "Fake Video Conferencing Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdRkUBM6XaBNcsjyGOz_dA3Du5DBpPc-UEWV4qFZPhyphenhyphenKT5MMjIgQf21Ii3HahX4xWLi6Jpzx7RvOLPD11IE_uM-J4XKCdNI8KUfhA9rwJEEJOFtgwbRnX41h-cSjriTD-7VVhwUyA1_ADXodka-X2ZCevyOd02ljhF3IEvgdu8hbaA0l5ZOSSMqTFrOKfx/s790-rw-e365/web3-malware.png)

Cybersecurity researchers have warned of a new scam campaign that leverages fake video conferencing apps to deliver an information stealer called [Realst](https://thehackernews.com/2023/07/rust-based-realst-infostealer-targeting.html) targeting people working in Web3 under the guise of fake business meetings.

"The threat actors behind the malware have set up fake companies using AI to make them increase legitimacy," Cado Security researcher Tara Gould [said](https://www.cadosecurity.com/blog/meeten-malware-threat). "The company reaches out to targets to set up a video call, prompting the user to download the meeting application from the website, which is Realst infostealer."

The activity has been codenamed Meeten by the security company, owing to the use of names such as Clusee, Cuesee, Meeten, Meetone, and Meetio for the bogus sites.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attacks entail approaching prospective targets on Telegram to discuss a potential investment opportunity, urging them to join a video call hosted on one of the dubious platforms. Users who end up on the site are prompted to download a Windows or macOS version depending on the operating system used.

Once installed and launched on macOS, users are greeted with a message that claims "The current version of the app is not fully compatible with your version of macOS" and that they need to enter their system password in order for the app to work as expected.

This is accomplished by means of an osascript technique that has been [adopted](https://thehackernews.com/2024/08/new-macos-malware-cthulhu-stealer.html) by several macOS stealer families such as Atomic macOS Stealer, Cuckoo, MacStealer, Banshee Stealer, and Cthulhu Stealer. The end goal of the attack is to steal various kinds of sensitive data, including from cryptocurrency wallets, and export them to a remote server.

The malware is also equipped to steal Telegram credentials, banking information, iCloud Keychain data, and browser cookies from Google Chrome, Microsoft Edge, Opera, Brave, Arc, Cốc Cốc, and Vivaldi.

[![Fake Video Conferencing Apps](data:image/png;base64... "Fake Video Conferencing Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYuTLHj_b_qNKPRERBY7xs4jACz0islJ1WFbSZa_A2D5N-HnsDZ-jCmh5MVDhjGwYvT8bAlMIb2T_ZZrljKh8uqGY_CY0LUCVBTdZDSwLmo47yq5mv4OIGGPSTKZLHzf_AaFDeElyYxv00acSCd1JYsUV9Oz4IZNh3rCFIw4Ht4BOG62q3966PVvUQFzOs/s790-rw-e365/apps.png)

The Windows version of the app is a Nullsoft Scriptable Installer System (NSIS) file that's signed with a likely stolen legitimate signature from Brys Software Ltd. Embedded within the installer is an Electron application that's configured to retrieve the stealer executable, a Rust-based binary, from an attacker-controlled domain.

"Threat actors are increasingly using AI to generate content for their campaigns," Gould said. "Using AI enables threat actors to quickly create realistic website content that adds legitimacy to their scams, and makes it more difficult to detect suspicious websites."

This is not the first time fake meeting software brands have been leveraged to deliver malware. Earlier this March, Jamf Threat Labs [revealed](https://thehackernews.com/2024/03/hackers-target-macos-users-with.html) that it detected a counterfeit website called meethub[.]gg that was used to propagate a stealer malware that shares overlaps with Realst.

Then in June, Recorded Future [detailed](https://thehackernews.com/2024/06/warning-markopolos-scam-targeting.html) a campaign dubbed markopolo that targeted cryptocurrency users with bogus virtual meeting software to drain their wallets by using stealers like Rhadamanthys, Stealc, and Atomic.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as the threat actors behind the [Banshee Stealer](https://thehackernews.com/2024/08/new-banshee-stealer-targets-100-browser.html) macOS malware [shut down their operations](https://x.com/vxunderground/status/1861148329884753939) after the [leak of their source code](https://github.com/vxunderground/MalwareSourceCode/tree/main/MacOS). It's unclear what prompted the leak. The malware was advertised on cybercrime forums for a monthly subscription of $3,000.

It also follows the emergence of new stealer malware families like [Fickle Stealer](https://www.trellix.com/blogs/research/new-stealer-uses-invalid-cert-to-compromise-systems/), [Wish Stealer](https://www.cyfirma.com/research/wish-stealer/), [Hexon Stealer](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding/), and [Celestial Stealer](https://www.trellix.com/blogs/research/anatomy-of-celestial-stealer-malware-as-a-service-revealed/), even as users and businesses searching for pirated software and AI tools are being targeted with RedLine Stealer and [Poseidon Stealer](https://www.esentire.com/blog/poseidon-stealer-uses-sora-ai-lure-to-infect-macos), respectively.

"The attackers behind this campaign are clearly interested in gaining access to organizations of Russian-speaking entrepreneurs who use software to automate business processes," Kaspersky [said](https://securelist.ru/redline-stealer-in-activators-for-business-software/111241/) of the RedLine Stealer campaign.

Found this article interesting? Follow us on [Google News](https://news.google.com/...