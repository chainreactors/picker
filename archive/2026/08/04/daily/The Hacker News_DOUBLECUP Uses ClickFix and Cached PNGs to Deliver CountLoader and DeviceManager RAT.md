---
title: DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT
url: https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html
source: The Hacker News
date: 2026-08-04
fetch_date: 2026-08-05T04:59:47.944024
---

# DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT

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

![cybersecurity](data:image/svg+xml;base64...)

# [DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT](https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html)

**Ravie Lakshmanan**Aug 04, 2026Social Engineering / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0MM7WIz9TI9RxDFZ-toTt_tLMlGIJGGyqnPZ5m68ft2_h16hOepWgOlGkRdx7KdUaRjz7GxanOYCp3167ZvcaWo1MV9ihUjZb6dHyX4Ss8SV6X4GGpobunHDfXs83HKppsCR-TT8quPfiNmH1Z-7EvWRZ4cdyHsHRsmlVshEJpDa76yUCjaWy0-xXaeeS/s1700-e365/double.jpg)

A new Russian loader-as-a-service (LaaS) codenamed **DOUBLECUP** has been using [ClickFix](https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html) lures as a way to stage malware-laced PNG images in victims' browser cache and ultimately deliver **CountLoader** and a previously undocumented remote access trojan called **DeviceManager**.

"The first stage drops a steganographic PNG image into the browser's cache, retrieves its hidden content, and executes the second stage," SOCRadar [said](https://socradar.io/blog/doublecup-clickfix-loader-devicemanager-rats/) in a technical report. "This second stage decrypts the final payload in memory via a custom SHA-256 stream cipher in Counter (CTR) mode along with bitwise XOR using the victim's public IP address as the cryptographic key."

Payloads delivered via the loader service include [CountLoader](https://thehackernews.com/2026/06/weedhack-attacks-minecraft-users.html), with variants for both Windows and macOS, and DeviceManager, which utilizes [EtherHiding](https://thehackernews.com/2026/07/dprk-linked-macos-malvertising-uses.html) to resolve its command-and-control (C2) infrastructure and communicate with the server over HTTP or DNS tunneling.

The service is assessed to be active since early June 2026, with the core developers providing operators with licenses and a client agent to help create campaigns and load payloads by embedding the required code in their ClickFix landing pages. Each license comes with a unique key and contains metadata including the client's IP address, active days, label, and version. Multiple campaigns can be orchestrated per license.

SOCRadar said its investigation sprang forth from an open directory at "213.139.77[.]109:9090" that left several testing files that were later [identified](https://urlscan.io/result/019f57c1-ef15-73ff-9660-d16363fe8f6b/) as part of the DOUBLECUP license panel.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The Go-based Windows GUI client also offers operators the ability to update configurations, update the software, and issue commands directly via a Broadcast Pane, while a Payload Builder Pane allows threat actors to set up the command that's triggered via a ClickFix decoy. This involves setting up the domain, slug, steganography method, embed type, archive format, action, and payload URLs.

"This generates a configuration endpoint at https://{domain}/{slug}/api/config," SOCRadar said. "A GET request to this endpoint returns DOUBLECUP's configuration data, which includes the steganographic image URL hosted on the target domain, image size, the session endpoint, and browser-specific commands tailored for Chrome, Edge, Firefox, Brave, and Opera."

The attack also requires operators to inject necessary frontend code onto their ClickFix site to trigger the malicious code. This involves the following steps -

* Fetching the /api/config endpoint, prefetching the steganographic image, registering a session, and evaluating the browser User-Agent string to select the appropriate browser payload
* Displaying ClickFix instructions, copying the browser-matched command to the victim's clipboard, and initiating a polling mechanism to execute the final redirect

Operators can opt to incorporate additional obfuscation or anti-analysis mechanisms into their payloads, but these extra steps remain solely their responsibility. Meanwhile, a Telegram bot (@harrypoterlohBOT) is used to track client visits, send commands, deliver keys, and receive payload callbacks via a designated DOUBLECUP URL.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4VtMFBN7S0p6Gd1QrDFulZzu5doOdKEe6A4daQ2JUDb9H1t6V2xvCl_oN6nCwCNuw0ozG0aK_g3g_gjOi6NY6LXLJHkB6atWOVwLUcy2ojmN7p_umsNBQMzL19XwpBGlg2voDCc-EaED9JMPz8L9nnXafwWvDQd6nyzh4SXHHKgUjFXo3zuMIMDQ5XmQr/s1700-e365/doubleclickfix.jpg)

Interestingly, the bot is managed by a threat actor named "johnnysilverhe," who has also [published](https://dex.koi.security/reports/vsc/751eda1b-25c9-4087-9046-2b1836925c03/0.0.67) a suspicious Microsoft Visual Studio Code (VS Code) extension named [Agent IDE](https://marketplace.visualstudio.com/items?itemName=johnnysilverhe.agent-ide) in the official marketplace.

Campaigns using DOUBLECUP have leveraged a cluster of bogus sites impersonating CRM login pages, including NetSuite, Odoo, HubSpot, and Salesforce, to deliver the loader via embedded iframe elements, which then pave the way for ClickFix commands that, upon execution, search the browser cache for the PNG image and extract from it malicious JavaScript, VBScript, or PowerShell to launch the next-stage component.

At this point, the C2 server is notified of a successful infection. The second-stage then acts as a dropper to deploy an encrypted payload and then redirect the victim to a destination page. The payload employs environmental keying as an anti-analysis technique to ensure that it's unpacked only on the victim's machine.

This is accomplished by passing the victim machine's public IPv4 address as a seed into a key derivation function to generate the cryptographic key necessary to decode the payload. The decryption process fails on any machine other than the intended target, as it would yield the wrong key.

The attack chain ends with the stager reconstructing the final payload and executing it. One of the malware families propagated via this method is an updated Windows and macOS version of CountLoader, which comes with new capabilities to establish persistence using scheduled tasks, audit installed browser extensions for cryptocurrency wallets, and profile the host to check if Signal's desktop app is installed.

"CountLoader also includes a function t...