---
title: 148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet
url: https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:50:00.714067
---

# 148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet

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

# [148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet](https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html)

**Swati Khandelwal**Jul 14, 2026Browser Security / Malvertising

[![DDoS Botnet](data:image/png;base64... "DDoS Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAJ1TN76Et1GvWFCTaivnNcys4rEEVk1QEd6WIb0wu3cxroYcwng-0a0uM8eyHdrOuiHLU8lFJg5eFzSbZj95aEfXVnletlFE9BKsDJP_0uV4w9-YbHg7p9LuMyRMcj4rJPftYmIYCcD3_VmbgFrGuaJ6yqUuJgIvVtbqlNUPrkJO2FSuFQ6dJ7gzKFV0/s1700-e365/lucide-botnet.jpg)

A campaign of 148 npm packages disguised as student web proxies turned visitors' browsers into a distributed denial-of-service botnet for roughly two weeks in May, according to new research from JFrog.

The packages did not go after the developers who might install them. The operators used the registry as free hosting for a booby-trapped proxy site and let the students who came to dodge school web filters supply the attack traffic.

The packages shipped under names like charlie-kirk, ilovefemboys, and miguelphonk, each carrying a proxy app branded "Lucide" and dressed as a tutoring landing page called Riverbend Tutoring or Northstar Tutoring.

On the surface, the proxy worked, letting students slip past content filters to reach games and blocked sites. Underneath, it loaded a remote code loader whose payload the operators could swap at will, plus a WebSocket flood generator built to speak the Wisp proxy protocol. Anyone who opened a page joined the swarm without knowing it.

None of this runs at install time. The packages carry no lifecycle hooks and no native build scripts, and they were never written to be imported into a project.

The self-replicating [Shai-Hulud worm](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) that hit more than 500 packages in September 2025 harvested developer secrets and republished itself with stolen tokens. Days before it, a [phishing attack on the maintainer known as qix](https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html) slipped wallet-draining code into chalk, debug, and 16 other packages with billions of weekly downloads between them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Those attacks fire the moment a package installs and target the people building software. This one skips the build pipeline and waits in a browser tab.

An earlier [advisory from SafeDep](https://safedep.io/malicious-npm-terminal3airport-proxy-adware-spam/) cataloged 141 of the packages in May and read the operation as adware and registry abuse: popunder ads, third-party monetization scripts, and Google Analytics tracking bolted onto a Scramjet proxy aimed at students. That held up for what was visible on the surface.

[JFrog pulled the thread](https://research.jfrog.com/post/lucide-proxy-npm-malware-campaign/) further. The team deobfuscated the app's entry bundle, a 5.4 MB single line of JavaScript that unpacked into more than 20,600 lines of readable code, and recovered archived payloads from the Wayback Machine to reconstruct the campaign's timeline.

Two modules sat underneath the adware, both firing before the React interface renders.

The first, which JFrog calls **G2**, is a remote script loader, and it fetches code about as unsafely as possible. It pulls JavaScript from a GitHub repository through the jsDelivr CDN, points at the mutable main branch instead of a pinned commit, ships no Subresource Integrity check, and runs whatever comes back with the proxy site's own origin privileges: full access to cookies, local storage, and same-origin endpoints.

A no-referrer policy keeps the request from advertising where it came from. Whoever holds the GitHub account behind it can change the code running in every visitor's browser whenever they want.

[![DDoS Botnet](data:image/png;base64... "DDoS Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuL6ulZ7H9zKk5PsH406YkUZX8UOKHFaA2cXSSKenZL34mPuhQYCPIzwmTHI3F7T7y7Oqp9-gQ54QS53PYMkFWeVshbKDcUd8vFo4ccYHo3JEe-kkiJWgaggZbGZWaZPW_5v4amPuIHxAJbxMqxKUkAs71DU9ZkQE8TVjvIeh2j5uDnm8NFzufs9Z2e0w/s1700-e365/lucide-proxy-website-archive.png)

The repository was returning a 404 by the time JFrog looked, but an archived copy from May 30 preserved what it had served: a crude HTTP flood. Every 500 milliseconds, the script builds a fresh one-million-character string and fires it as a no-cors POST at cdn.caan.edu, which JFrog identifies as the public domain of a nursing school in Matteson, Illinois.

The requests never wait for a response, so they stack up. JFrog clocks each active visitor at roughly 2 MB per second of upload, meaning a thousand open proxy tabs would push around 2 GB per second at the target. A randomized query parameter defeats caching proxies, and no-cors skips the CORS preflight, so nothing throttles the packets.

The second module, **I2**, is the sharper one. It fetches a plain text file, websocket.txt, holding a target WebSocket URL and a socket count capped between 1 and 1,024, then opens that many connections in a staggered loop. The archived config aimed each browser at 30 connections to a Wisp endpoint on lunaron[.]top, itself a live proxy busy injecting malvertising.

[Wisp](https://github.com/MercuryWorkshop/wisp-protocol) is a low-overhead Mercury Workshop protocol for tunneling many TCP and UDP sockets over a single WebSocket, and it is common plumbing in the same browser-proxy scene these packages imitate.

Once connected, each browser sets its socket to binary mode and, every 100 milliseconds, sends a valid Wisp CONNECT frame followed by a CLOSE frame, both pointed at localhost:1. The frames are correct little-endian Wisp packets, so the target is not the student's own machine. It is the remote Wisp server on the far end of the connection.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj9cpbdlGJAX8DjNAhr...