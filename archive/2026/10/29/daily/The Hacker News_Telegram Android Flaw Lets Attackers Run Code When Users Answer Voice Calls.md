---
title: Telegram Android Flaw Lets Attackers Run Code When Users Answer Voice Calls
url: https://thehackernews.com/2026/10/telegram-android-flaw-lets-attackers.html
source: The Hacker News
date: 2026-10-29
fetch_date: 2026-10-30T07:56:33.623300
---

# Telegram Android Flaw Lets Attackers Run Code When Users Answer Voice Calls

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Telegram Android Flaw Lets Attackers Run Code When Users Answer Voice Calls](https://thehackernews.com/2026/10/telegram-android-flaw-lets-attackers.html)

**Swati Khandelwal**Oct 29, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguzUg6G-A4KdRvBuhj9LZ93cFfXfvMNkg3dJO0H9sfNJ3MTlecsgLEMIk5TnIrdl2N6UGB8D9rlqLduGEZVm7X-XrWZr6Xh5ZrVp38x5uTd1vHyHGcjRR2N3gctNen-CBSz8JihnNL57galBoeOVKwG5w3qsOZnqmGYdkxzjurrI3QWolmS1Qfz_E_Wog/s1700-nu-rw-lo-l85-e365/telegram.jpg)

A flaw in Telegram for Android could be chained with two other bugs to take full control of a victim's phone through a voice call, once the victim answered, according to security startup NebuSec.

The attacker needed only an ordinary Telegram account. Telegram fixed the flaw in version 12.10.4 of the app, released in late September, and NebuSec [disclosed it on October 29](https://x.com/nebusecurity/status/2115601122727702634).

Combined with an information-leak bug, the flaw gives the attacker an escape from the Telegram app to Android, NebuSec co-founder and chief executive Eten Zou told The Hacker News. Adding an Android root exploit then gives full control of the phone, including its messages, microphone and camera.

The flaw can be triggered in every version from 8.6.2 through 12.10.3, Zou said. Those versions came out between March 2022 and September 2026.

The company confirmed it in private voice calls on ARM64-based phones and has no evidence so far that it directly affects Telegram's iOS and desktop apps or group calls.

Anyone using Telegram for Android should make sure the app is on version 12.10.4 or later. The version number appears at the bottom of the app's Settings page. The flaw had no CVE identifier as of October 29.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The attack needs the victim to be called and to answer, Zou said, so setting Telegram's call privacy option to "Nobody" blocks it, and so does declining the call.

NebuSec has not seen the flaw used in real attacks, and believes no one else had realized it could be turned into remote code execution.

NebuSec reported the flaw to Telegram on September 26, after version 12.10.4 had shipped. Telegram acknowledged the report but did not believe the flaw could be turned into remote code execution, so no CVE was assigned and no bug bounty was paid, Zou said. The Hacker News has asked Telegram for comment.

During a Telegram call, the two apps send each other short messages to set up the call and report its state. One type, called MediaState, reports whether the microphone is muted, whether the camera is on, and how the video is rotated.

The flaw was in the code that reads MediaState messages. That code did not handle missing fields correctly and accessed memory it should not, according to NebuSec.

[Telegram's published source code](https://github.com/DrKLO/Telegram/blob/9552e5541e1274b9557c9832b204dbfcaf44b3dc/TMessagesProj/jni/voip/tgcalls/v2/Signaling.cpp#L718-L738) for version 12.10.3 contains a flaw that matches that description, a review by The Hacker News found. When a MediaState message included a rotation value, the code checked that value. It then read a different field, the video state, even if the message had no such field.

[Version 12.10.4](https://github.com/DrKLO/Telegram/blob/c84801762fd5f936c8296ecf09a14a48ebfc4fe4/TMessagesProj/jni/voip/tgcalls/v2/Signaling.cpp#L725-L745) reads the rotation value from the right field. The calling code that uses this message was switched on in version 8.6.2, the first version NebuSec names.

Telegram's Android, iOS, and desktop apps use one shared library, called tgcalls, for calls. A change labeled "[Fix camera rotation](https://github.com/TelegramMessenger/tgcalls/commit/a6ea40ebf18233fad5aae29aa3d30561f839a6a8)" made the same correction in tgcalls on April 21, 2026.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoQ03PBDidX4BiA8uT7eS-PDiJApWFJPeKitS2EFYDoa5m26vjSv0RjjuRnfqxKe5VcnjjNH00tsB9mwipxOYdcNufhhcQybp1YZ0mTwdDm15SuGXK5tbdox1jiKapx7GqyfiycrAxHgxhYyFHDc9ZWkeNXzBTnGY1cuBbn4Sf-oxSjUElAYPoDqXBh1M/s1700-nu-rw-lo-l85-e365/telegram.gif)

Telegram's iOS source code included that change from [version 12.7](https://github.com/TelegramMessenger/Telegram-iOS/tree/release-12.7/submodules/TgVoipWebrtc), released in May, and the desktop app's code from [version 7.0.1](https://github.com/telegramdesktop/tdesktop/tree/v7.0.1/Telegram/ThirdParty), released in July. Telegram for Android received it in version 12.10.4 in September.

Whether the earlier code could be exploited in those apps has not been shown.

NebuSec's video shows two phones, one marked as the attacker and one as the victim. The victim accepts a Telegram call. About half a minute into the call, the victim's phone switches to its home screen, the app icons fall down the screen, and a "HACKED BY NEBUSEC" logo appears.

The video does not show which Telegram or Android version the victim's phone was running. No technical write-up of the flaw was on NebuSec's website as of October 29, so the attack chain, including the two other bugs, depends on the video and on what the company says.

NebuSec, a startup [backed by Y Combinator](https://www.ycombinator.com/companies/nebusec), says its Code Security product, which runs on OpenAI's GPT-5.4 model, found the flaw. In July, the company described [an Android exploit chain](https://thehackernews.com/2026/07/researchers-show-single-malicious.html) that started with a Firefox flaw and reached the kernel of an ARM64 device running Android 17.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Separately, the Zero Day Initiative (ZDI) [published an advisory](https://www.zerodayinitiative.com/advisories/ZDI-26-757/) on October 15 about an unpatched flaw in rlottie, the library Telegram apps have used to draw ani...