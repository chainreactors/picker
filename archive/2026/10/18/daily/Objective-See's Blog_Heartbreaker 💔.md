---
title: Heartbreaker 💔
url: https://objective-see.org/blog/blog_0x8A.html
source: Objective-See's Blog
date: 2026-10-18
fetch_date: 2026-10-19T07:07:12.557508
---

# Heartbreaker 💔

* [![](/images/logoApple.png)

  Objective-See

  a non-profit 501(c)(3) foundation.](/index.html)
* [ ]

  + [![](/images/aboutIcon.png)
    About](/about.html)
  + [![](/images/conferenceIcon.png)
    #OBTS](https://objectivebythesea.org/)
  + [![](/images/bookIcon.png)
    Book Series](https://taomm.org/)
  + [![](/images/weIcon.png)
    Objective-We](/we.html)
  + [![](/images/steveIcon.png)
    Objective-Steve](/steve.html)
  + [![](/images/storeIcon.png)
    Our Store/Swag](https://objective-see.myshopify.com/)
  + [![](/images/malwareIcon.png)
    Malware Collection](https://github.com/Objective-see/Malware)
* Support Us!
* [![](/images/blogIcon.png)

  Blog](/blog.html)
* [![](/images/productsIcon.png)

  Tools](/tools.html)
* [![](/images/aboutIcon.png)

  About](/about.html)

---

Heartbreaker 💔

Metamorphic ransomware comes for macOS

Patrick Wardle · October 18, 2026

The **Objective-See Foundation** is supported by:

[![](https://objective-see.org/images/friends/iru.png)](https://www.iru.com)

[![](https://objective-see.org/images/friends/panw.png)](https://www.paloaltonetworks.com)

[![](https://objective-see.org/images/friends/jamf.png)](https://www.jamf.com/?utm_source=objective-see&utm_medium=sponsored-link&utm_campaign=next-gen-security&utm_content=2021-02-05_protect)

[![](https://objective-see.org/images/friends/MoonlockLogoMacPaw.png)](https://moonlock.com)

[![](https://objective-see.org/images/friends/threatLocker.webp)](https://www.threatlocker.com/)

[![](https://objective-see.org/images/friends/malwarebytes.png)](https://www.malwarebytes.com/)

[![](https://objective-see.org/images/friends/iVerify.png)](https://www.iverify.io)

[![](https://objective-see.org/images/friends/huntress.png)](https://hubs.ly/Q02BYLy80)

[![](https://objective-see.org/images/friends/rippling.png)](https://www.rippling.com/products/it?utm_source=web&utm_medium=hosted-asset&utm_program=experimental-engagement&utm_campaign=US-IT-Partnership-Objectivebythesea-2026&utm_product=it)

[![](https://objective-see.org/images/friends/northpole.png)](https://northpole.security)

### Background

Recently, I presented “***Practical Ransomware Detection on macOS (via Maths, Not AI)***” at both [MacSysAdmins](https://www.macsysadmin.se/) and [Virus Bulletin](https://www.virusbulletin.com/conference/vb2026/).

The talk’s abstract describes the presentation well:

> Ransomware remains a serious threat to macOS users, especially as Apple devices continue to gain traction in the enterprise. Despite its many variants, most ransomware shares a fundamental behaviour: rapidly transforming user files into encrypted data.
>
> This talk presents a practical, maths-driven approach to generically detecting and stopping ransomware on macOS. While this approach builds on established ideas, it is now far more practical with Apple’s Endpoint Security framework. By leveraging Endpoint Security and entropy-based analysis, we can distinguish benign file activity from encryption and further differentiate encrypted data from compressed data using simple mathematical heuristics. This approach avoids signatures and machine learning, instead relying on observable behaviour and measurable properties of data.
>
> We will walk through the implementation in a free, open-source tool, including real-world testing, and demonstrate the approach against macOS ransomware samples. We will also acknowledge limitations and possible avenues for evasion.
>
> The result is a lightweight, explainable, and practical method for detecting ransomware on macOS using maths, not AI.

I've just uploaded the full slides here:

[Practical Ransomware Detection on macOS (via Maths, Not AI)](https://speakerdeck.com/patrickwardle/practical-ransomware-detection-on-macos-via-maths-not-ai)

The talk revisited my earlier research, “[***Towards Generic Ransomware Detection***](https://objective-see.org/blog/blog_0x0F.html),” which led to the original release of [RansomWhere?](https://objective-see.org/products/ransomwhere.html), a free, open-source tool designed to protect macOS users from, well, ransomware!

The central idea remains just as relevant today: by monitoring for the rapid creation or modification of encrypted files by untrusted processes, we can generically detect most—perhaps even all—macOS ransomware:

![](../images/blog/blog_0x8A/1.png)
A Ransomware Heuristic

Though it is not exactly the most sophisticated heuristic, it has held up remarkably well over the years! Best of all, it gave me an excuse to incorporate maths into the presentation:

![](../images/blog/blog_0x8A/2.jpeg)
Math is Life

So what was new in my talk? First, thanks to Apple’s Endpoint Security framework, I showed how RansomWhere? can now implement this heuristic far more efficiently and comprehensively. Even cooler, IMHO, was a discussion of Heartbreaker: a previously unknown and undetected ransomware sample targeting macOS that attempts to metamorphically rebuild itself.

In this blog post, we’ll analyze Heartbreaker, recover files encrypted by it, explore its unusual self-rebuilding machinery, and finally pit it against our generic ransomware-detection heuristic.

### Analyzing Heartbreaker

Want to play along? You can grab the sample from Objective-See's public macOS malware collection:

[Heartbreaker](https://github.com/objective-see/Malware/blob/main/HeartBreaker.zip) (password: `infect3d`).

Heartbreaker was originally [uploaded to VirusTotal](https://www.virustotal.com/gui/file/6bdf42a575d2daee3de2530161cb5b1fef6ca78b4abfa74f329d6b6c72890d18) in May 2025. As of this writing, it remains undetected by all of the antivirus engines on the site:

![](../images/blog/blog_0x8A/3.png)
Heartbreaker remains undetected

It was discovered there by Megan Carney, who will present her hunting approach in “[Lessons from Threat Hunting for Malware Triage](https://objectivebythesea.org/v9/talks.html)” at the upcoming Objective by the Sea v9 conference!

Initial triage reveals an ad hoc-signed ARM64 (Apple silicon) Mach-O binary named `heartbreaker`:

```
% file heartbreaker
heartbreaker: Mach-O 64-bit executable arm64

% codesign -dvv heartbreaker
Identifier=heartbreaker-e2c97a640967e3f6
Format=Mach-O thin (arm64)
CodeDirectory v=20400 size=58520 flags=0x20002(adhoc,linker-signed) hashes=1825+0
Signature=adhoc
```

Next, if we extract strings embedded in the `heartbreaker` binary, we encounter the following:

```
% strings heartbreaker

Encrypting file:
HEARTBREAKER WARNING!
Your system has been encrypted!
Please send 0.003 BTC ...

[dependencies]
aes-gcm = "0.10.3"
mimicore = { git = "https://github.com/saaaarwar/mimicore" }

Writing source to: modified_source.rs
Writing Cargo.toml to:
Writing build.rs to:
Running cargo build
Saving new executable

Transforming source code
METAMORPHIC_MARKER_START
METAMORPHIC_MARKER_END
```

Interesting! From the strings alone, the binary certainly smells like ransomware. The Rust dependencies also reveal its implementation language, while the `mimicore` dependency and `METAMORPHIC_MARKER_*` strings immediately piqued my interest.

Of course, one should never base an analysis solely on embedded strings. Instead, think of them as signposts that guide further investigation. With that in mind, let’s move into an isolated virtual machine and observe the binary at runtime.

Running [FileMonitor](https://objective-see.org/products/utilities.html#FileMonitor) alongside the sample lets us observe its filesystem activity:

```
# FileMonitor.app/Contents/MacOS/FileMonitor -filter heartbreaker

"event" : "ES_EVENT_TYPE_NOTIFY_OPEN",
"file" : {
    "destination" : "/Users/user/Downloads/file.txt",
    ...

"event" : "ES_EVENT_TYPE_NOTIFY_WRITE",
"file" : {
    "destination" : "/Users/user/Downloads/file.txt",
    ...

"event" : "ES_EVENT_TYPE_NOTIFY_RENAME",
"file" : {
    "source" : "/Users/user/Downloads/file.txt",
    "destination" : "/Users/user/Downloads/file.txt.heartbreaker",
    ...
```

Specifically, Heartbreaker recu...