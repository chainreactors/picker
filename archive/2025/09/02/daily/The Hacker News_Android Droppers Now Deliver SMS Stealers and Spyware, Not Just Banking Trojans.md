---
title: Android Droppers Now Deliver SMS Stealers and Spyware, Not Just Banking Trojans
url: https://thehackernews.com/2025/09/android-droppers-now-deliver-sms.html
source: The Hacker News
date: 2025-09-02
fetch_date: 2025-10-02T19:32:15.611213
---

# Android Droppers Now Deliver SMS Stealers and Spyware, Not Just Banking Trojans

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

# [Android Droppers Now Deliver SMS Stealers and Spyware, Not Just Banking Trojans](https://thehackernews.com/2025/09/android-droppers-now-deliver-sms.html)

**Sep 01, 2025**Ravie LakshmananMobile Security / Malvertising

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijJTcif6mcxfb0YF4WaePfUiiiwhcgupvhbcFV3JtSeX062w3y-3p9kovXrMdVBZb8UJP5I7vbMWpErQ98KYLIYxZTr8gWFLG6mdmqhfWguMObzyFuBiYSGHNZzazDRATloxNhKk5tfLxsOb0kSeY9HutT39mOtdIX83qx4GzyirtBvhTigG3tsH7MAbdF/s790-rw-e365/android-trojan.jpg)

Cybersecurity researchers are calling attention to a new shift in the Android malware landscape where dropper apps, which are typically used to deliver banking trojans, to also distribute simpler malware such as SMS stealers and basic spyware.

These campaigns are propagated via dropper apps masquerading as government or banking apps in India and other parts of Asia, ThreatFabric [said](https://www.threatfabric.com/blogs/android-droppers-the-silent-gatekeepers-of-malware) in a report last week.

The Dutch mobile security firm said the change is driven by [recent security protections](https://thehackernews.com/2025/08/google-to-verify-all-android-developers.html) that Google has piloted in select markets like Singapore, Thailand, Brazil, and India to block sideloading of potentially suspicious apps requesting dangerous permissions like SMS messages and [accessibility services](https://thehackernews.com/2025/08/new-android-malware-wave-hits-banking.html), a heavily abused setting to carry out malicious actions on Android devices.

"Google Play Protect's defences, particularly the targeted Pilot Program, are increasingly effective at stopping risky apps before they run," the company said. "Second, actors want to future-proof their operations."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"By encapsulating even basic payloads inside a dropper, they gain a protective shell that can evade today's checks while staying flexible enough to swap payloads and pivot campaigns tomorrow."

ThreatFabric said that while Google's strategy ups the ante by blocking a malicious app from being installed even before a user can interact with it, attackers are trying out new ways to get around the safeguards – an indication of the endless game of whack-a-mole when it comes to security.

This includes designing droppers keeping in mind Google's Pilot Program, so that they don't seek high-risk permissions and serve only a harmless "update" screen that can fly past scanning in the regions where the initiative has gone live.

But it's only when the user clicks the "Update" button does the actual payload get fetched from an external server or unpacked, which then proceeds to seek the necessary permissions to fulfil its objectives.

"Play Protect may display alerts about the risks, as a part of a different scan, but as long as the user accepts them, the app is installed, and the payload is delivered," ThreatFabric said. "This illustrates a critical gap: Play Protect still allows risky apps through if the user clicks Install anyway, and the malware still slips through the Pilot Program."

One such dropper is RewardDropMiner, which has been found to serve along with spyware payloads a Monero cryptocurrency miner that can be activated remotely. Recent variants of the tool, however, no longer include the miner functionality.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB67d4wudHZf6b3oAu9vv5g3djdg8D_zcMMzoGI4NGbQliko8UIO0Nx1ZYnmMDDQVgVqOVDmWmSHiIlmSvJifu8LedVrW28ehAZ7I2_5ihbIMh7Rr4Wm9ZAP0aQqMv5DwPppJYWG4WGtdOSIUIy9WtPrsAzyorj3uf5F3MmbOoTQppaEonVeDYIeNKi3Eo/s2600/apps.png)

Some of the malicious apps delivered via RewardDropMiner, all targeting users in India, are listed below -

* PM YOJANA 2025 (com.fluvdp.hrzmkgi)
* °RTO Challan (com.epr.fnroyex)
* SBI Online (com.qmwownic.eqmff)
* Axis Card (com.tolqppj.yqmrlytfzrxa)

Other dropper variants that avoid triggering Play Protect or the Pilot Program include SecuriDropper, Zombinder, BrokewellDropper, HiddenCatDropper, and TiramisuDropper.

When reached for comment, Google told The Hacker News it has not found any apps using these techniques distributed via the Play Store and that it's constantly adding new protections.

"Regardless of where an app comes from – even if it's installed by a 'dropper' app – Google Play Protect helps to keep users safe by automatically checking it for threats," a spokesperson said.

"Protection against these identified malware versions was already in place through Google Play Protect prior to this report. Based on our current detection, no apps containing these versions of this malware have been found on Google Play. We're constantly enhancing our protections to help keep users safe from bad actors."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as Bitdefender Labs has warned of a new campaign that's using malicious ads on Facebook to peddle a free premium version of the TradingView app for Android to ultimately deploy an improved version of the [Brokewell](https://thehackernews.com/2025/08/hook-android-trojan-adds-ransomware.html) banking trojan to monitor, control, and steal sensitive information from the victim's device.

No less than 75 malicious ads have been run since July 22, 2025, reaching tens of thousands of users in the European Union alone. The Android attack wave is just one part of a larger malvertising operation that has abused Facebook Ads to also target Windows desktops under the guise of various financial and cryptocurrency apps.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoGat4RZRcLC2helJHPZFiNFijAS7Zbn9D6L7fdsJWgFyqAvQ4S8yBVIPG65BLJ50gt53hXK9zc-MUXILx1chuSGD9MSyWlocO9BAaX-s840CBLHa2c4dFi3EW7gROziz96qQrtOSB2JNN30mfhDafX2uRY_FfxH3dc4nmvstWnLfBMNEamFD93G5iIuYm/s2600/ads.jpg)

"This campaign shows how cybercriminals are fine-tu...