---
title: ClickFix Smuggles Payloads Through Browser Cache to Bypass Windows Run Limits
url: https://thehackernews.com/2026/10/clickfix-smuggles-payloads-through.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:36.083527
---

# ClickFix Smuggles Payloads Through Browser Cache to Bypass Windows Run Limits

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [ClickFix Smuggles Payloads Through Browser Cache to Bypass Windows Run Limits](https://thehackernews.com/2026/10/clickfix-smuggles-payloads-through.html)

**Ravie Lakshmanan**Oct 06, 2026Social Engineering / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8Vjgif5jASBMNSuYjBnVZcm9vGO378mJ7VTFTNo9HRROtViKbP_Nm0F0vf626be5n4cwnfDdqgfWVzjKrKboh0BnbM8ALWzt-W7kNq4PSc_TOUbNlwps6sCQgfNyK5DhXk3FHZCuJSo8D2eMOm4r89VmhNa6l5gPpadRZSgTuB_N2yPZlwj0voYddOoVr/s1700-nu-rw-lo-l85-e365/clickfix.jpg)

A new type of **[ClickFix](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html)** [attack](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html) is using compromised websites to trick users into executing a malicious payload cached in a web browser's cache.

"Instead of downloading and executing remote payloads like the typical attack pattern, in this attack, the websites pre-fetch a script payload into the browser cache disguised as a PNG file," the Microsoft Threat Intelligence team [said](https://x.com/MsftSecIntel/status/2106197481960706155) in a post on X.

Thus, when the victim is prompted to paste and execute a malicious command – as is the case with ClickFix attacks – it executes the cached website content that's already on the device.

What's notable about this [browser cache smuggling](https://thehackernews.com/2025/10/hackers-exploit-wordpress-themes-to.html#clickfix-becomes-stealthy-via-cache-smuggling) approach is that it allows the attackers to conceal the payload script and bypass [character limit restrictions](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) imposed on [Windows Run](https://devblogs.microsoft.com/commandline/the-new-run-dialog-faster-cleaner-and-more-capable/) (aka the Run dialog). The Windows Run dialog, triggered by Win + R, truncates any input that exceeds approximately 260 characters.

In the attack chain observed by Microsoft, the staged payload is a Visual Basic Script (VBScript), which then invokes "cmd.exe" to recursively enumerate files whose names start with "f\_" in the browser's profile folder such as "%LOCALAPPDATA%\Mozilla\Firefox\Profiles."

"It compares each file's byte length with an expected value," Microsoft explained. "Rather than searching for a marker within the contents like previous attacks, it copies a size-matching cache entry to %LOCALAPPDATA%\Temp\t.vbs, giving the cached payload a VBScript extension, then executes it with wscript.exe. Copy output and errors are suppressed. The expected size varies across variants."

The VBScript is also designed to harvest host information via Windows Management Instrumentation ([WMI](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)), fetch a PowerShell script ("v.ps1") from an external server ("cocojambo[.]us[.]com/alfa"), and then launch it. The PowerShell script serves as a conduit for an intermediate PowerShell payload that's responsible for downloading the next stage ("cab.dat").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Once the file is downloaded, its contents are read and executed in a hidden window. The attack eventually paves the way for .NET assemblies that are loaded into memory and inject code into a newly launched legitimate Windows process ("[timeout.exe](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/timeout)") with an aim to target browser and device credentials.

What's more, the injected process launches PowerShell to obtain a secondary in-memory stage from "capsysnet[.]vg" and initiate outbound connections to "ciliabula[.]cc."

This is not the first time payloads have been staged in the browser cache as part of ClickFix attacks. In October 2025, Expel [documented](https://thehackernews.com/2025/10/hackers-exploit-wordpress-themes-to.html#clickfix-becomes-stealthy-via-cache-smuggling) an attack chain that employed cache smuggling to deliver a malware-laced ZIP archive. The activity was subsequently [identified](https://expel.com/blog/along-for-the-ride-when-legitimate-software-becomes-a-signed-malware-loader/) as a [red team engagement](https://x.com/Intrinsec/status/1980249658396999763) conducted by Intrinsec.

[ClickFix](https://www.netsecurity.com/the-alarming-rise-of-fix-type-cyber-attacks-how-clickfix-filefix-consentfix-are-taking-over-the-internet/) has become an exceedingly popular social engineering technique over the past two years. The fact that the attack turns the victim into a delivery channel for executing malware has made it an attractive initial access method for cybercriminals and nation-state actors alike.

In a proof-of-concept (PoC) exploit released in August 2025, CloudSEK [demonstrated](https://www.cloudsek.com/blog/trusted-my-summarizer-now-my-fridge-is-encrypted----how-threat-actors-could-weaponize-ai-summarizers-with-css-based-clickfix-attacks) how artificial intelligence (AI) summarization systems embedded in email clients, browser extensions, and productivity platforms can be weaponized to deliver ransomware via ClickFix.

Specifically, the payloads are embedded within HTML content using CSS-based obfuscation methods, such as zero-width characters, white-on-white text, and off-screen positioning, that make them invisible to the human eye, but are parsed by AI systems. This invisible prompt injection is then used to generate summaries containing attacker-controlled ClickFix instructions.

The attack employs a method known as prompt overdose to repeat the payload dozens of times so that it dominates the model's context window and steers output generation.

"When such crafted content is indexed, shared, or emailed, any automated summarization process that ingests it will produce summaries containing attacker-controlled ClickFix instructions," CloudSEK said. "The observed outcome confirms that prompt over...