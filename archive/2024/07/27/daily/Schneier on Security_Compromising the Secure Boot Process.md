---
title: Compromising the Secure Boot Process
url: https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html
source: Schneier on Security
date: 2024-07-27
fetch_date: 2025-10-06T17:47:12.339215
---

# Compromising the Secure Boot Process

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Compromising the Secure Boot Process

This [isn’t good](https://arstechnica.com/security/2024/07/secure-boot-is-completely-compromised-on-200-models-from-5-big-device-makers/):

> On Thursday, researchers from security firm Binarly revealed that Secure Boot is completely compromised on more than 200 device models sold by Acer, Dell, Gigabyte, Intel, and Supermicro. The cause: a cryptographic key underpinning Secure Boot on those models that was compromised in 2022. In a public GitHub repository committed in December of that year, someone working for multiple US-based device manufacturers published what’s known as a platform key, the cryptographic key that forms the root-of-trust anchor between the hardware device and the firmware that runs on it. The repository was located at https://github.com/raywu-aaeon/Ryzen2000\_4000.git, and it’s not clear when it was taken down.
>
> The repository included the private portion of the platform key in encrypted form. The encrypted file, however, was protected by a four-character password, a decision that made it trivial for Binarly, and anyone else with even a passing curiosity, to crack the passcode and retrieve the corresponding plain text. The disclosure of the key went largely unnoticed until January 2023, when Binarly researchers found it while investigating a supply-chain incident. Now that the leak has come to light, security experts say it effectively torpedoes the security assurances offered by Secure Boot.
>
> […]
>
> These keys were created by AMI, one of the three main providers of software developer kits that device makers use to customize their UEFI firmware so it will run on their specific hardware configurations. As the strings suggest, the keys were never intended to be used in production systems. Instead, AMI provided them to customers or prospective customers for testing. For reasons that aren’t clear, the test keys made their way into devices from a nearly inexhaustive roster of makers. In addition to the five makers mentioned earlier, they include Aopen, Foremelife, Fujitsu, HP, Lenovo, and Supermicro.

Tags: [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [keys](https://www.schneier.com/tag/keys/), [passwords](https://www.schneier.com/tag/passwords/), [supply chain](https://www.schneier.com/tag/supply-chain/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on July 26, 2024 at 12:21 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html) •
[49 Comments](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html#comments)

### Comments

I Own My Computer •
[July 26, 2024 2:17 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html/#comment-439617)

And why “This isn’t good”?

Things are turning very idiotic very fast. AV companies dictate what software I can run on MY computer. It’ well known fact that certain AV product blocks running the well-known and useful tool “netcat”, among other, legit software. Now some hardware vendors and one BIG software vendor from Redmond dictates me what I can boot on the computer I paid for my hard-earned salary. Already long time we don’t own software any more, it’s so called “licensed” to us. What, hardware is now following that move? So we don’t own it any more and “license” it and HW vendor dictates what for I can use it? Rubbish!

I’m very glad that those keys leaked, I’m very glad that this “secure boot” is broken and I’m shocked when Bruce Schneier calls it “This isn’t good”?

Jodie Snow •
[July 26, 2024 2:38 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html/#comment-439618)

[Here’s the PDF report](https://web.archive.org/web/20240726085758if_/https%3A//22222483.fs1.hubspotusercontent-na1.net/hubfs/22222483/Reports/PKfail%20-%20Binarly%20Research%20Report%20July%2025%202024.pdf).

Keep in mind that if AMI manages their keys so poorly that they can *accidentally* leak onto Github, it’s likely that at least one intelligence agency already had a spy get hired there to obtain the key (among other things).

JerryK •
[July 26, 2024 5:02 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html/#comment-439620)

While writing firmware for a chip vendor years ago, my employer was frequently badgered by its customers for pre-release versions (that is, not fully tested and sometimes not even entirely finished) of our software. Our marketing weasels were always happy to oblige. Despite promises that “this was only for testing; we will not release this”, customers often did just that. Where marketing staff call the shots, quality control is impossible.

Jon (a different Jon) •
[July 26, 2024 5:55 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html/#comment-439623)

Sorta goes to show: It ain’t the theory, it’s the implementation.

J.

Clive Robinson •
[July 26, 2024 9:34 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html/#comment-439624)

@ ALL,

As pointed out a long time ago on this blog “code signing” has a large number of ways to fail. Therefore way back then it was sensible to treat it as insecure.

But about the worst failure for “code signed” software systems is disclosure of a root, master, or class key from which all others are derived. Because that in effect allows forgeries to be made by anyone who knows how to read a web page or two.

Back then it was stated that we needed a better way to do the “root of trust” thing. Back then as now there was only two general ways to do things,

1, Symmetric KeyMat by a secure second channel.
2, Use Asymmetric KeyMat verified by a trusted root / master key of which the Public half was “embedded”.

In over forty years we’ve still not come up with a way to remove the failings of a single “root of trust” that “the industry” will use…

Clive Robinson •
[July 26, 2024 10:41 PM](https://www.schneier.com/blog/archives/2024/07/compromising-the-secure-boot-process.html/#comment-439625)

@ ALL,

Re : Fun thought for you all.

As several people pointed out about the various reasons Secure Boot and similar came into existance was not to protect the end user as Microsoft and others have claimed. But it was as the Fritz-Chip or DRM replacement. Needed due to effectively the same “Root of trust” leak we see with Secure Boot. It was of the DVD CSS “Player Key” reverse engineered by “DrinkOrDie”[1]. That gave us the likes of DeCSS that so upset DVD producers like Disney and Co. They pressured the likes of Microsoft and Intel to come up with a way to “Protect their IP Rights”.

Well for those that know what to do, this “PKfail” key leakage will enable the use of “Shims” in drivers etc to “Rip Media” of even the more mo...