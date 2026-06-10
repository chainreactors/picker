---
title: New FROST Attack Lets Websites Track What Sites and Apps You Open via SSD Timing
url: https://thehackernews.com/2026/06/new-frost-attack-lets-websites-track.html
source: The Hacker News
date: 2026-06-09
fetch_date: 2026-06-10T06:17:16.380603
---

# New FROST Attack Lets Websites Track What Sites and Apps You Open via SSD Timing

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

# [New FROST Attack Lets Websites Track What Sites and Apps You Open via SSD Timing](https://thehackernews.com/2026/06/new-frost-attack-lets-websites-track.html)

**Swati Khandelwal**Jun 09, 2026Browser Security / Privacy

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSiGrvsR8kJp_r8gce1LkFY4oJRt8-0dafO2RdcOzCwQqWy6XrnkRXpGX94NwPbvEupsU7ZhXAUEtKg5Xdl4y_o_IYsi4XLHIo9JSMNcto6JGG76vhkWSOvYa0So2tkUyQovyFwtB8Anpq6SLILSwzd0iXO_fzq4KIwpdG6F1yFIuhJpnXf1lgGIupiSRv/s1700-e365/frost.jpg)

A malicious website can work out which sites you visit and which apps you open, using nothing but JavaScript and the timing of your SSD. The attack, called **FROST**, needs no native code, no extension, and no permission prompt.

You open the page, leave the tab sitting there, and it watches the drive for contention in the background.

Researchers at Graz University of Technology built it and described it in [a new paper](https://hannesweissteiner.com/pdfs/frost.pdf) set to appear at DIMVA 2026. It abuses a storage feature present in every major desktop browser, and the underlying timing channel works on both macOS and Linux.

SSD timing attacks are not new. Last year the same group published [Secret Spilling Drive](https://www.ndss-symposium.org/ndss-paper/secret-spilling-drive-leaking-user-behavior-through-ssd-contention/), which read user behavior off a drive by watching how reads slow down when something else is using it. The catch was that it needed native code on the machine, through a low-level interface like Linux's io\_uring. FROST drops that requirement. It runs inside the browser sandbox, which turns a local attack into a remote one.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

You no longer have to be on the machine to pull it off.

The same Graz lab has done this before. Its [SnailLoad attack](https://thehackernews.com/2024/06/new-snailload-attack-exploits-network.html) inferred the sites and videos a victim loaded from network latency alone, no JavaScript at all.

## How FROST Attack Works

The way in is the [Origin Private File System](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system), or OPFS, a storage feature browsers added in 2023 so web apps like in-browser editors and IDEs can keep files on disk. OPFS gives each origin its own sandboxed slice of the file system, and because that slice is walled off, it skips the permission prompt a page normally needs to reach your files. No dialog, no click. A site can just start writing.

Normally the operating system hides disk timing behind the page cache, serving repeated reads from memory so they never touch the drive.

FROST gets around this by creating a file larger than the machine's RAM. The cache cannot hold all of it, so reads keep landing on the SSD. On Chrome and Safari, OPFS can grow to 60% of disk space, far more than enough; Firefox caps each origin lower, though an attacker can spread the load across multiple origins to get past that.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSO1Btzew4fL3KYXmxHna8sWl2QN9GI6i3SpJ8rG5HUW4s4GHE0sB9xFG0ZpCanXY23mWi02zlSJYlo9ojnmTiIMusBynJIrSStwdA0gEgIkqgNzNSXhclVWZvDCwwVxBXiGWV8iDlct6BNaj8oF2IKqHtg95yBJ8I52o0vWKR0ALWP0ow8GXCvVnOZUao/s1700-e365/working-1.jpg)

The attacker's code then reads random 4 kB chunks of that file in a loop, and times each read with performance.now(). Browsers blunt their timers by default to make this kind of measurement harder, but the attacker sharpens the resolution back up by switching on cross-origin isolation, which it can do freely on its own page.

When you open a site or launch an app on the same drive, that activity competes with the attacker's reads, and the timing shifts measurably. A neural network trained on those traces identifies the site or app.

The accuracy is the uncomfortable part. On a Mac, against the top 50 websites, FROST identified the site being visited with an F1 score of 88.95% in a closed-world test, and held at 86.95% in an open-world test that added 300 sites it had never seen. For ten native, pre-installed macOS apps, it reached 95.83%. The team also built a covert channel on the same signal, moving data from a cooperating native app to the malicious page at 661.63 bit/s on Linux and 719.27 bit/s on macOS through OPFS. The native attack was faster at its best, but that is a lot of data for code stuck inside a browser sandbox.

While the timing channel also works on Linux, the team ran the full classifier only on macOS, so those fingerprinting numbers are a macOS result. FROST also only picks up activity on the same disk as its OPFS file.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

A single-drive laptop puts everything on that disk; a multi-drive workstation hides whatever runs on a separate drive, though app startups that touch the home directory tend to leak anyway.

## What You Can Do

Not much, for now. Google, Mozilla, and Apple were all told before publication. Google's Chromium team does not treat fingerprinting as a security vulnerability. Apple called it out of scope but left room for a mitigation later. Mozilla acknowledged it and has shipped nothing. There is no CVE, and no public evidence that the technique has been used in the wild.

That leaves the defenses thin. The measurement only runs while the attacker's page is open, so closing the tab ends that run. Watching your browser's storage for an unexplained multi-gigabyte file is another tell, though browsers do not make OPFS usage easy to see.

On Linux, systems running profile-sync-daemon, a utility that keeps the browser profile in RAM, are incidentally protected against the zero-click version, because OPFS writes never reach the SSD. The weaker variant, where a page uses a file-picker dialog to get you to select a large file yourself, still works.

The fixes that would actually c...