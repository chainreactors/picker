---
title: PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords
url: https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
source: The Hacker News
date: 2026-07-03
fetch_date: 2026-07-04T05:49:52.885247
---

# PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords

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

# [PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords](https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html)

**Ravie Lakshmanan**Jul 03, 2026Credential Theft / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEmcBMGUjTwe51gVQWP401twHYLMUOocwG9nYkgadlFV6cmGXrPS-3PeNTg_GJOaUVohWILNXgIC8ufSkPqXRbW1wIyvUr5JEKCrrMI3_hlN8uFtxpf-sBn743tQmlK2ipu_qWtY3k18cPkaQ6XGJnR7RPjuMOWkYwcmJ5XSnSNQHbNpkEgyyP29hJA6j2/s1700-e365/macos-malware.jpg)

Cybersecurity researchers have flagged a new macOS information stealer called **PamStealer** that employs a series of clever tricks to infect systems and siphon sensitive data.

The stealer, discovered by Jamf Threat Labs, is distributed as a compiled AppleScript (.scpt) file impersonating Maccy, a legitimate open-source clipboard manager. It has been codenamed PamStealer owing to its ability to validate the victim's login password through the macOS Pluggable Authentication Modules ([PAM](https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html)) before capturing it.

The malware is delivered in two stages: A compiled AppleScript distributed inside a disk image that's designed to download and stage a follow-on payload. The secondary artifact is a Rust-based infostealer capable of credential theft, browser data collection, persistence, and exfiltration.

The initial access vector for the malware is a lookalike site ("maccyapp[.]com") that mimics [Maccy](https://maccy.app/) ("maccy[.]app"). The AppleScript ("Maccy.scpt") present within the disk image executes a self-contained JavaScript for Automation (JXA) downloader that fetches and stages the stealer payload using native Objective-C APIs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

What's notable here is that the script, once launched via the Script Editor, displays instructions to run it using the "⌘ + R" keyboard shortcut or clicking the Run button from the Script Editor, causing the malicious logic hidden in the file below a large block of empty lines to be executed.

"Notably, this works even when the file still carries the com.apple.quarantine attribute, which is what makes the approach attractive to attackers as Apple continues to tighten Gatekeeper and Terminal," security researcher Thijs Xhaflaire [said](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/). "Combined with a Rust-based second stage and a password capture workflow that validates credentials locally through PAM, the result is a quieter execution chain than we typically observe in commodity macOS stealers."

The AppleScript dropper incorporates environment-aware features that allow the execution to continue only after fingerprinting the host and determining it's running on Apple Silicon. It does this by deriving a key based on the fingerprint, which includes details like the CPU architecture, locale, keyboard layout, and the time zone, and then using it to unlock an encrypted configuration that contains the payload URL and install path.

On Intel-based Macs, the derived decryption key differs and fails to decode the configuration, resulting in the termination of the dropper. The script also avoids execution within sandboxed or analysis environments, as well as systems whose time zone, system locale, and keyboard input resolve to countries located in Eastern Europe, such as Russia, Belarus, Kazakhstan, Armenia, Azerbaijan, Kyrgyzstan, Moldova, Tajikistan, Uzbekistan, Turkmenistan, and Georgia.

Once the checks pass, the script reaches out to the external server and downloads a Mach-O binary written in Rust that masquerades as the Finder app and is responsible for harvesting data from web browsers, cryptocurrency wallet extensions, iCloud Keychain, and clipboard content. The captured information is then encrypted and exfiltrated to attacker-controlled infrastructure ("avenger-sync[.]live") over an outbound HTTP request.

Besides coercing the user into granting it full file system access, the stealer serves a native password prompt that collects the victim's system password, and then validates the entered password by cross-checking it via the PAM API. If the validation fails, it asks the user to re-enter the password, and repeats the loop until the correct password is supplied.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

"Once a valid password is captured, the stealer shows a second, counterfeit alert: 'Maccy is damaged and can't be opened. You should move it to the Trash,' a close copy of the genuine Gatekeeper message," Jamf said. "This is a decoy. By the time it appears, the payload has already run, captured the password and registered for persistence, so the message serves only to make the victim discard the lure and assume the download was broken."

Also built into the Rust binary is a small arm64 Mach-O that impersonates macOS System Settings and is used for setting up persistence.

The development has [prompted](https://github.com/p0deje/Maccy) Alex Rodionov, the developer of Maccy, to [include](https://github.com/p0deje/Maccy/commit/72bf797b234d7f13fb2826d0f76211e10b72851b) a warning on their website and the GitHub repository, urging users to stay away from fake websites mimicking the tool. "Beware of fake websites impersonating Maccy. Malicious sites (such as maccyapp[.]net and maccyapp[.]com) distribute malware disguised as Maccy. Maccy[.]app is the only official website," Rodionov said.

"Together, these behaviors illustrate how commodity macOS stealers continue to evolve, adopting quieter execution chains and native implementations that reduce tradit...