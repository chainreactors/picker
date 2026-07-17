---
title: New ClickLock macOS Stealer Kills Apps Every 210ms Until Victims Type Their Password
url: https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:24.101759
---

# New ClickLock macOS Stealer Kills Apps Every 210ms Until Victims Type Their Password

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [New ClickLock macOS Stealer Kills Apps Every 210ms Until Victims Type Their Password](https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html)

**Swati Khandelwal**Jul 16, 2026Malware / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4iNrh8DJbIsaAsGTCFlS4kGWAwdRNMghQm9-o8MV8X2txyJ4iTH1P4g7v5sdjuhw9dOeozn9Q6GenUi4wxBTw9uyoJ1D2j5WIcwCWuTk5XEVyGqjAg4jmP4kOEMp2qtd0BnPiVwrz2MJnTwaAnQP0jR3yCGvojGLQMOEc9syp00LKXIkbjUZrWqh0_GSe/s1700-e365/macos-stealer.jpg)

**ClickLock Stealer**, a new macOS infostealer, answers a victim's refusal by killing their apps on a loop until they hand over the login password. It arrives as a command pasted into Terminal, asks for the password behind a fake system dialog, and when the victim cancels, installs two LaunchAgents and quietly exits.

At the next login, Finder, the Dock, Spotlight, Terminal, Activity Monitor, and the major browsers start dying every 210 milliseconds, for up to 83 hours, leaving one password box on a dead desktop. Type it, and the machine gives up the Keychain, the browser credentials, and the crypto wallets.

Group-IB's [telemetry](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/) counts at least 100 targets across 33 countries since May, over half of them in Europe. Its analysts assume from the code structure that the malware is still under development. Uploaded to VirusTotal on June 9, the orchestrator script had [zero detections](https://www.virustotal.com/gui/file/3ce0504ba65f8d56f83d7fef45faeaeb31e4e5aa9b872b56610b5f2558231caa/) there when Group-IB analyzed it.

And the analysts never found the front door. They have the whole payload chain and not one of the lure pages. The IOC list carries three compromised payload hosts and no lure domain: the landing page design, the domains serving it, and whatever drives traffic to them are all unconfirmed.

A completed run leaves the operator holding the validated macOS login password, Chrome's Safe Storage AES key, and a ZIP with browser credentials and cookies, crypto wallet extension storage, desktop wallet files, password manager vaults, the Keychain, shell history, and FileZilla's saved server credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The Safe Storage key is the one that lasts. It encrypts Chrome's saved passwords and cookies on disk, so `Login Data` and `Cookies` are decrypted offline, on the attacker's machine, whenever they get to it. Group-IB's advice to anyone who ran this: revoke active browser sessions, treat every saved password, cookie, and wallet key as gone, and change them.

## Comply now, or comply at next login

The refusing user is not an edge case. They are what the design is for. Cancel the first dialog, and the script drops `com.authirity.plist` and `com.chromer.plist` into `~/Library/LaunchAgents/`, then leaves.

The first fires the 210-millisecond kill loop until a password lands. The second launches its own kill loop at 0.2-second intervals for up to 3,000,000 seconds, roughly 34.7 days, while a background process queries the Keychain for Chrome's Safe Storage key every half second.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgx_-YTju-8-m9SpquhHdNVPs38RnMWlSGVmHXCC9NK3isdoEpLEUaL5XoozxiEOEb1tJHbxyY9Yr7vaZuX_yufITdoXbpECZyolnd4H_xXVrMNmA-JTVDt_k6_LZa1X_a-_TtDBZM3QCNXhR4RO5Y_KCWFg-Vm-YJvhLHnFA-AI7Zky13g4kxoBhPQP14/s1700-e365/group-ib.jpg)

That query raises a real macOS prompt, and the loop holds the desktop hostage until the victim approves it. Activity Monitor and Terminal are on both kill lists. A third loop kills NotificationCenter for six hours, so no Gatekeeper warning renders. If Terminal lacks Full Disk Access, the orchestrator opens System Settings to the right pane and walks the victim through granting it.

The front end is [ClickFix](https://attack.mitre.org/techniques/T1204/004/). Group-IB assesses that with high confidence and has never seen it. The script takes a `RAY_ID` as its first argument and opens with a fake Cloudflare CAPTCHA banner over a progress bar cycling twelve status lines in ten seconds. Neither does anything. They exist to reassure someone who has just pasted a command into a terminal.

Underneath, `script.sh` disables keyboard interrupts, hides the cursor, and pulls four payloads from two compromised sites. Two pipe straight into bash. Two land in a hidden `$HOME/.cacheb/`. The soft ask is an `osascript` dialog wearing a downloaded Apple icon and the victim's real username, and whatever gets typed is checked against `dscl /Local/Default -authonly` first, so only a working password is worth sending.

Almost none of that is new. Microsoft [documented](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/) the same `dscl` validation in SHub Stealer in May, alongside [AMOS](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html) and [MacSync](https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html) in the same wave of macOS ClickFix campaigns. Telegram exfil and LaunchAgent persistence are boilerplate.

The backdoor, **goyim**, is roughly 80 percent a copy of the public deploy script for [GSocket](https://github.com/hackerschoice/gsocket), an open-source tunneling toolkit from The Hacker's Choice. Its authors pitch the `gs-netcat` component as an encrypted reverse backdoor that needs no C2 server of its own. It rides a relay instead.

Group-IB traced this copy to an operator relay at `gsnc[.]eu:67`, with the binary pulled from gsocket.io itself. The stealer payloads sit on three compromised domains with clean reputations, one of them a hacked WordPress site, and the haul leaves through three Telegram bots. Group-IB observed no dedicated command-and-control infrastructure.

[![](data:image/png;base64...)](https://blogger.googleusercon...