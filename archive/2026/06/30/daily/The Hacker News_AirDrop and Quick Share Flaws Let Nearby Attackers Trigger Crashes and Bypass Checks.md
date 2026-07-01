---
title: AirDrop and Quick Share Flaws Let Nearby Attackers Trigger Crashes and Bypass Checks
url: https://thehackernews.com/2026/06/airdrop-and-quick-share-flaws-let.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:41.149497
---

# AirDrop and Quick Share Flaws Let Nearby Attackers Trigger Crashes and Bypass Checks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [AirDrop and Quick Share Flaws Let Nearby Attackers Trigger Crashes and Bypass Checks](https://thehackernews.com/2026/06/airdrop-and-quick-share-flaws-let.html)

**Swati Khandelwal**Jun 30, 2026Vulnerability / Wireless Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCyrr25-wXst4kOLIEi1-Q1d5XMVDCvWqUacEoSRsLn6C5CbKoXGLb4nzTB-DVr9cLOkyuIT5wyMrQICAVhQFlTsXrR_Ng9CBBXPZGeK_rLtOVXh5C8CsrZHaGyJ5WukGI3vTpMOw1S09_U9j_s5rzEFcYq55g7ZmOthGTPw5XxJJkALMH9VOxr0DjX8Vi/s1700-e365/share-ai.jpg)

Two researchers have found six security flaws in **AirDrop** and **Quick Share**, the wireless features that beam files between nearby devices with no cables or shared network.

An attacker within wireless range, with just a laptop and no prior connection, can crash the sharing service on a Mac or iPhone set to receive from anyone, with no tap or prompt.

The same research found Quick Share flaws that bypass Samsung's session checks and trigger a potentially exploitable crash in Google's Windows app.

The two features run inside an ecosystem of more than five billion active Apple and Android devices, though the tested bugs hit specific implementations and versions.

The work, laid out in a [new research paper](https://arxiv.org/abs/2606.26967) by Arash Ale Ebrahim and Nils Ole Tippenhauer of the CISPA Helmholtz Center for Information Security, is the first to pull both stacks apart side by side, above the radio layer, where discovery becomes session handling, parsing, and trust decisions.

The fixes have already started. Apple has patched one of the three AirDrop bugs and assigned it a CVE, though the advisory is not yet public; the other two are still in coordinated disclosure. Google paid a bounty for the Windows flaw and has landed a code fix, with its CVE still pending.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Samsung's two bugs were handed to Google and remain under investigation. No public reports of these flaws being exploited have surfaced as of this writing.

## Three ways to knock out Apple's sharing

All three AirDrop flaws end in the same crash: they take down sharingd, the background service on macOS and iOS that handles AirDrop. The catch is that this service also runs AirPlay, Handoff, Universal Clipboard, Continuity Camera, and NameDrop, so one crash takes the whole set down together.

The simplest of the three needs only a single malformed request sent to a device with AirDrop set to receive from "Everyone." Send those crash messages on a loop, about one every two seconds, and the features stay down for as long as the attacker keeps going. In the researchers' test, no legitimate AirDrop transfer got through while the attack ran.

Two of the three are more than AirDrop bugs, because they live in shared Apple frameworks. The broadest is a stack overflow in Foundation's XML property list parser, triggered by a small file with around 200 nested layers.

Any Apple app that opens an untrusted file of that type could hit the same parser path, across macOS, iOS, watchOS, tvOS, and visionOS. The researchers reproduced the AirDrop crashes on macOS 15.7.4, macOS 26.3, iOS 18.x, and iOS 26.3; an older iOS 16 build was not affected.

## The Quick Share bugs, and a fix that broke

On Android, two flaws in Samsung's Quick Share let an attacker skip past the handshake that is supposed to lock down a session. One lets an unverified device start driving the connection before any encryption is set up.

The other lets some control messages pass unencrypted even after a secure session exists. An attacker on the same Wi-Fi network could use that gap to force a connection into an "accepted" state, keep it alive, or make the server return attacker-supplied IP and port values. Neither was shown to steal files, but both defeat the protections the system promises.

The researchers tested these on a Galaxy S23 Ultra and noted that other Android makers' versions of Quick Share need separate checking.

The most serious flaw is in Google's Quick Share for Windows. It is a memory bug that surfaces when two connections collide at the right instant, leaving the program using a chunk of memory it has already thrown away.

That is the kind of bug that can sometimes be turned into running attacker code, and the researchers say the path is plausible here because a Windows defense called Control Flow Guard is switched off in the app.

They confirmed a crash but did not build a working exploit. Google acknowledged it, paid a bounty, and has now landed a fix; the CVE is still pending.

It is not the first time Quick Share for Windows has been here. SafeBreach reported a [10-bug code-execution chain in 2024](https://thehackernews.com/2024/08/researchers-uncover-10-flaws-in-googles.html) (CVE-2024-38271 and CVE-2024-38272), then [returned in 2025 to bypass Google's fixes](https://thehackernews.com/2025/04/google-patches-quick-share.html) (CVE-2024-10668). The new use-after-free adds another entry to a pattern of the same component being patched and probed again.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The detail that stings: the program's own source code carried a comment admitting a prior bug in that exact spot, reading "We had a bug here, caused by a race with EncryptionRunner." The fix written to handle it reintroduced the same kind of flaw.

## The risk is local, not remote

The key limit is range. These are local attacks, not internet-wide ones: the attacker has to be within about 10 to 30 meters or on the same local network.

While less sweeping than a remote bug, a single attacker in a crowded place like an airport, train, or conference can still reach many devices at once. The researchers tested only their own hardware and have [released their tools openly](https://zenodo.org/records/20442029) so other security teams can reproduce the findings.

On a Mac or iPhone, install Apple's latest update...