---
title: Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit
url: https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html
source: The Hacker News
date: 2026-06-12
fetch_date: 2026-06-13T06:12:07.231948
---

# Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit

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

# [Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit](https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html)

**Swati Khandelwal**Jun 12, 2026Linux / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoaB3XILLCN-oMr8vicgye6mcqKGYsgqgxPAGunmwASyrP3c7XgAxJTV8tsVPuRSmJ8ia7SZdS8hyphenhyphenb6moPI2QiwkdKoI2E_zchlBfqx1KnfFpb3yKHQQY6qCWyKmkSK_12texqsHTxtYnv8kMMpzJ-SEFxR7Ougz0axLPVr5zDAWQiZY8pEtUUL8L4hmri/s1700-e365/arch-hack.jpg)

Attackers took over more than 400 packages in the Arch User Repository (AUR) this week and rewrote their build scripts to install a credential stealer on any machine that built them.

The malware is a Rust binary built to harvest developer secrets. When it lands with root, it can also load an eBPF rootkit to hide itself. The AUR is Arch Linux's community package collection, and it is separate from the official Arch repositories, which were not affected.

If you installed or updated an AUR package on or after June 11, check it against the current affected-package lists before trusting the host. The list of names is large, still growing, and not yet complete.

This attack goes after the trust model, not a software flaw. The compromised packages kept their names, their histories, and the trust that came with them. Only the build instructions changed.

The trap sat in the recipe, leaving the package itself looking exactly like the software users meant to install. No exploit, no zero-day, and no sign Arch's own systems were breached.

The attackers adopted abandoned packages, edited the build files, and let users run the payload for them. Sonatype, which named the campaign [Atomic Arch](https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency), found them going after orphaned projects: packages whose maintainers had walked away, leaving them open for anyone to adopt.

They also spoofed git commit metadata so the changes looked like they came from a long-standing maintainer, an account an Arch Linux Trusted User later confirmed was never compromised.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Once a package was adopted, its PKGBUILD or .install script was edited to run npm install atomic-lockfile during the build, pulling the malicious npm package alongside a couple of legitimate ones for cover. That package, atomic-lockfile@1.4.2, carries a preinstall hook that runs a bundled Linux ELF named deps. Build the package, and the binary runs.

Confirmed examples reported to the Arch mailing list include the alvr and premake-git packages.

## What the malware does

Independent researcher Whanos [reverse-engineered](https://ioctl.fail/preliminary-analysis-of-aur-malware/) the deps payload and describes a Rust credential stealer aimed at developer workstations and build systems. It collects:

* Cookies, tokens, and local storage from Chromium-based browsers (Chrome, Edge, Brave, and many more)
* Session data from Electron apps, including Slack, Discord, and Microsoft Teams
* GitHub, npm, and HashiCorp Vault tokens, plus OpenAI/ChatGPT bearer material and account metadata
* SSH keys, known\_hosts, and shell histories
* Docker and Podman credentials and VPN profiles

Stolen files go out over HTTP to temp.sh. Command and control runs through a Tor onion service via a local loopback proxy.

For persistence, it installs a systemd service with Restart=always. With root it copies itself under /var/lib/ and writes a unit under /etc/systemd/system/; as a normal user it uses the home directory and a per-user unit under ~/.config/systemd/user/. Either way, it wants to come back.

Early write-ups oversold the eBPF rootkit. It is optional, and it only loads when the binary already has root and the right capability. It is not used to gain privileges. When it does activate, it hides the malware's own processes, process names, and socket inodes from standard tools, using pinned BPF maps named hidden\_pids, hidden\_names, and hidden\_inodes, and it kills attempts to attach a debugger.

That changes the cleanup advice. Removing the AUR package is not enough once the payload has run. A package manager can remove the files it knows about. It cannot prove the machine is clean after a rootkit-capable payload has had a chance to execute.

The binary also stages a second file tied to monero-wallet-gui that the analysis flags as a possible, unanalyzed cryptominer. An eBPF rootkit bolted onto a smash-and-grab stealer is unusual, and it is why this one is worth more than a shrug.

## Scope, and a second wave

Sonatype's first write-up counted more than 20 hijacked packages. Within a day, community trackers and the Arch [aur-general thread](https://lists.archlinux.org/archives/list/aur-general%40lists.archlinux.org/thread/FGXPCB3ZVCJIV7FX323SBAX2JHYB7ZS4/) had cataloged over 400, with one master list compiled by grepping the AUR git mirror, putting it around 408, and consolidated lists climbing higher.

The atomic-lockfile npm package itself showed only 134 weekly downloads on [Socket](https://socket.dev/npm/package/atomic-lockfile) before it was pulled from the registry, so the real exposure is the AUR build path rather than npm installs.

A second wave used bun install js-digest, pushed from a separate set of accounts that community trackers link to the same npm publisher as atomic-lockfile. Its payload is a different binary, a separate ELF by its hash, that the community also flagged as malicious.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

How far this wave has spread is still being counted. Early breakdowns listed a few dozen packages, while later grep-based searches of the AUR mirror returned much higher numbers that may include churn as commits are removed. Either way, it is not a footnote to the first wave, so check for both atomic-lockfile and js-digest.

## What to do now

Arch maintainers ...