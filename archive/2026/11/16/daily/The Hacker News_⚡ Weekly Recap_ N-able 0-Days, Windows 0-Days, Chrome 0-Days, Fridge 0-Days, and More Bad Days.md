---
title: ⚡ Weekly Recap: N-able 0-Days, Windows 0-Days, Chrome 0-Days, Fridge 0-Days, and More Bad Days
url: https://thehackernews.com/2026/11/weekly-recap-n-able-0-days-windows-0.html
source: The Hacker News
date: 2026-11-16
fetch_date: 2026-11-17T09:57:54.631847
---

# ⚡ Weekly Recap: N-able 0-Days, Windows 0-Days, Chrome 0-Days, Fridge 0-Days, and More Bad Days

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [⚡ Weekly Recap: N-able 0-Days, Windows 0-Days, Chrome 0-Days, Fridge 0-Days, and More Bad Days](https://thehackernews.com/2026/11/weekly-recap-n-able-0-days-windows-0.html)

**Ravie Lakshmanan**Nov 16, 2026Cybersecurity News / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMhM3PBYlJasSU7OztYuQsJDnDRFYwqV1-X9Nt1mTlAhFe0YQXSr0XrdCfo47u2DGAE8qSNw32LuPlMxoeTOBjakeXiHpHjFSXw7rsy8FdCldY2E6MuX9uKGM2McoGsaXUGDY2MYBsRAGXUDMGqzkT4wWlEezGDQho_f7d6MYNG2HAeW9FKeldRJrh0kj3/s1700-nu-rw-lo-l85-e365/recaps.jpg)

A default password opened doors it never should have. A trusted update delivered malware. Even a security feature became a way to break in. Different stories, same problem: the things meant to protect us aren't always doing their job.

Meanwhile, AI is making bug hunting faster, old flaws are still paying off, and attackers keep finding easy ways in. Some attacks take real skill. Others barely need any.

This week's stories show both sides. Here's what happened.

## **⚡ Threat of the Week**

**[N-able 0-Days Exploited for Dropping Crypto Miners](https://thehackernews.com/2026/11/hackers-exploit-n-central-flaws-to.html)** — A new set of vulnerabilities tracked as 4EverAble2Shell has come under active exploitation, with attackers exploiting it to deploy cryptocurrency miners on vulnerable servers. According to Huntback, the activity has successfully compromised 21 N-central servers across the U.S., South Africa, Canada, the U.K., Germany, France, and Sweden. Patches for the flaw are expected to be released N-able today.

[![Secrets Strategy for Developer](data:image/png;base64... "Secrets Strategy for Developer")

## One Secrets Strategy for Developer and AI Agent Credentials

Developer secrets and AI-agent credentials may look like separate issues, but they introduce the same access risks. Read our guide to see how a shared secrets management framework can secure developer secrets and make sure that AI agents don’t see or store raw credentials.](https://thehackernews.uk/developer-secrets)
[Read Now ➝](https://thehackernews.uk/developer-secrets)

## **🔔 Top News**

* **[Compromised bee-js and Swarm Desktop Steal Swarm Wallet Keys](https://thehackernews.com/2026/11/hackers-compromise-etherspheres-bee-js.html)** — Threat actors [compromised](https://socket.dev/blog/bee-js-compromise) @ethersphere/bee-js, the JavaScript client for the Swarm storage network, with a new postinstall hook in version 13.3.0 that downloads a second stage responsible for stealing the Swarm node's wallet key and installing a backdoor. "On Linux and macOS, the backdoor is a Go remote shell," SafeDep [said](https://safedep.io/blog/ethersphere-bee-js-npm-compromise). "On Windows, it is a hidden ScreenConnect client that runs as SYSTEM." The same malicious code was subsequently distributed via Swarm Desktop 0.56.2 on GitHub. The activity has since been linked to a campaign called [SleepyDuck](https://thehackernews.com/2025/11/malicious-vsx-extension-sleepyduck-uses.html) (EtherDuck), which is [known](https://pluto.security/blog/sleepyduck-malware-open-vsx-extensions/) to spread malicious Solidity extensions through Open VSX. "The attacker controlled two Ethersphere GitHub accounts. GitHub activity logs attribute 13 pushes on November 6 to long-time maintainer nugaon," SafeDep added. "That day the attacker injected GitHub Actions workflows to steal CI credentials, and the attempts failed. Two days later, the attacker used the release bot bee-worker to publish the malicious releases. How the attacker got into either account remains unknown."
* **[Nightmare Eclipse New SignDrop 0-Day](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html)** — Security researcher Abdelhamid Naceri (aka Chaotic Eclipse) released a new Windows zero-day exploit that can let attackers gain SYSTEM privileges. Called [SignDrop](https://github.com/MSNightmare/SignDrop), it has been described as a Windows Common Log FileSystem (CLFS) authentication zero-day local privilege escalation flaw. "The vulnerability [turns a defense](https://support.microsoft.com/en-us/servicing/os/windows/2025/03/common-log-file-system-clfs-authentication-mitigation) into an attack surface," Cyderes said. "Microsoft added HMAC-based authentication codes to CLFS log files specifically to block the class of logic bugs caused by improper validation of CLFS data structures, which accounted for 19 of 24 CLFS CVEs over five years. SignDrop abuses the signing mechanism itself: it forces clfs.sys to create a .cnpf signature file as SYSTEM in an attacker-controlled location, producing a privileged file-creation primitive at an attacker-selected path. Because the resulting file retains attacker-accessible security attributes, the exploit reopens it and replaces the CLFS-generated content with an embedded payload DLL." Microsoft said it's investigating the reported vulnerability. In late September, the researcher also released an exploit for [BigDiskBuster](https://github.com/MSNightmare/BigDiskBuster), a denial-of-service (DoS) flaw impacting Microsoft Defender that's similar to UnDefend and prevents the application from performing platform/signature updates.
* **[Default Admin Password Lets Researchers Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)** — New research found that it's possible to take over customer accounts at two major automakers, and use them to remotely unlock and start a test car, flash headlights, and sound horns after finding an administration console on the brands' login servers still protected by its default password. Both apps signed customers in through ForgeRock, an identity platform now part of Ping Identity. The carmakers [remediated](https://samcurry.net/forgerock) the flaw approximately two hours after responsible disclosure.
* **[Google Patches Actively Exploited Chrome 0-Day](https://thehackernews.com/2026/11/google-issues-chrome-security-update....