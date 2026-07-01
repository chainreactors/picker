---
title: RustDuck Botnet Rebuilds in Rust to Hijack Routers and Servers for DDoS
url: https://thehackernews.com/2026/06/rustduck-botnet-rebuilds-in-rust-to.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:40.202640
---

# RustDuck Botnet Rebuilds in Rust to Hijack Routers and Servers for DDoS

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

# [RustDuck Botnet Rebuilds in Rust to Hijack Routers and Servers for DDoS](https://thehackernews.com/2026/06/rustduck-botnet-rebuilds-in-rust-to.html)

**Swati Khandelwal**Jun 30, 2026Botnet / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2XzOOqoX4E_CfxUMxd0YAH9MRjvZ8-kBBiVhd2VvCvbie3zla8PA80fO2xZ4Ux3_gmreVKG7ANFrSGpDk1lsURfQZuVVapjqi565oGmkqImmFdiQsQFL5z7V9s7TTkH4KgmGbEFnpdAQz94DrXip4q8Qa-ec9K1B1cmeL3szEBWUq9nX-MWppatyug3A/s1700-e365/RustDuck.jpg)

A new two-stage malware family called **RustDuck** is hijacking home routers, IP cameras, Android boxes, and poorly secured servers, then stitching them into a network built to knock websites and online services offline.

Researchers at QiAnXin's XLab have tracked it since February 2026, and say the real story is not how big it is today, but how fast it is changing.

The end goal is a distributed denial-of-service (DDoS) attack: flooding a target with junk traffic from the infected machines until it buckles.

RustDuck is one more entrant in a crowded field, but it stands out for two reasons. It is being rewritten from the C programming language into Rust, and its newer versions go to unusual lengths to avoid being studied or shut down.

## How it spreads

RustDuck does not lean on a single clever trick. It sprays a mix of old, well-known weaknesses and hopes one sticks. The first is the oldest in the book: devices left on the internet with weak or default passwords on their remote-login services (Telnet and SSH). Guess the password, walk in.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The second is unpatched device bugs. XLab [says](https://blog.xlab.qianxin.com/rustduck-en/) RustDuck goes after exposed Android debugging interfaces and flaws in gear from TVT (DVRs and cameras), Ruijie, TP-Link, and ZTE, plus a handful of named, years-old vulnerabilities that still litter the internet:

* CVE-2017-17215, a remote code execution bug in [Huawei HG532 routers](https://nvd.nist.gov/vuln/detail/CVE-2017-17215) that the original Mirai-style botnets abused back in 2017.
* CVE-2025-29635, a command-injection flaw in discontinued D-Link DIR-823X routers that [Akamai watched Mirai variants exploit](https://www.akamai.com/blog/security-research/cve-2025-29635-mirai-campaign-targets-d-link-devices) in March 2026. CISA [added it to its Known Exploited Vulnerabilities list](https://thehackernews.com/2026/04/cisa-adds-4-exploited-flaws-to-kev-sets.html) the next month.
* CVE-2024-1781, a command-injection bug in [Totolink X6000R](https://nvd.nist.gov/vuln/detail/CVE-2024-1781) routers, whose maker never responded to the disclosure.
* CVE-2018-8007, a remote code execution path in [Apache CouchDB](https://docs.couchdb.org/en/stable/cve/2018-8007.html) that an authenticated admin can abuse.

The third path is web software. RustDuck also targets known holes in ThinkPHP, Jenkins, and Hadoop YARN, which stretches its reach from cheap home hardware to exposed server software.

XLab counted more than 20 internet addresses spreading the malware, with the busiest at 176.65.139[.]204.

## What makes it tricky

RustDuck installs in two stages: a small loader that decrypts and unpacks a heavier core module. That core is where the interesting engineering lives, and it is the part being rewritten in Rust.

Rust binaries are generally tougher for analysts to take apart than the C that has powered device malware for years, and XLab says RustDuck's Rust core shows real depth in how it derives its keys, hides from analysis, and talks to its servers. The switch points to active development, not a quick re-skin of leaked code.

The bigger tell is how hard the newer samples work to stay hidden. Before doing anything, RustDuck runs a checklist to decide whether it has landed in a security researcher's lab instead of on a real victim's device. It looks for analysis tools like Wireshark and gdb, for debuggers attached to its own process, for the fingerprints of a honeypot trap, even for virtual-machine hardware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihafeXlSAzzDhfqlB7aNBQrgWRhBtNeKxjS1skZlNPTTxo0qgt9YM4taSc_4ypz7e4hyphenhyphen5O7XaEaYebZ_HtaFMRbyJlYz2xIQtWoh_rkjuIO43iL_IAcRR1TfuGnFFFYswnDKjTX3-kIbQDxHRdJE4iI8kJ1SCNQs7y8kWAFXaTzFb9uKfH-CDSOjafUHA/s1700-e365/malware.png)

Each hit adds points to a risk score. Cross a threshold, and the malware erases its traces and quits before anyone can watch it run.

Two of those checks stand out. One quietly tries to reach an internet address that is reserved for testing and should never answer; if something replies, RustDuck knows it is inside a fake network built to fool malware, and bails.

Another compares two clocks to catch sandboxes that speed up time to rush malware into showing its hand.

Its communications are locked down to match. RustDuck encrypts its traffic with modern ciphers: **ChaCha20-Poly1305** for the handshake, AES-GCM once it is taking commands. It derives its keys with HKDF-SHA256 and a Curve25519 exchange, rotates them every ten minutes, and dresses the connection up to look like ordinary encrypted web traffic so it blends in.

Once a device checks in, the operators can send a short list of orders: start an attack, stop it, report status, switch to new control servers, or quietly upgrade the malware to a newer build. The control addresses lean on free dynamic-DNS services like duckdns.org, which is where the "Duck" in the name comes from.

## This fits a bigger pattern

RustDuck is not the first botnet to reach for Rust. In April 2025, Fortinet documented [RustoBot](https://www.fortinet.com/blog/threat-research/new-rust-botnet-rustobot-is-routed-via-routers), a Rust-based botnet that spread through Totolink and other routers to run DDoS attacks, using the same recipe: cheap routers, a modern language, and flood traffic on demand.

[![Cybersecurity](data:image/png;base64...)](https:...