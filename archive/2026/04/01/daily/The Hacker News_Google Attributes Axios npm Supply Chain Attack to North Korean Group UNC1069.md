---
title: Google Attributes Axios npm Supply Chain Attack to North Korean Group UNC1069
url: https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html
source: The Hacker News
date: 2026-04-01
fetch_date: 2026-04-02T04:31:36.435649
---

# Google Attributes Axios npm Supply Chain Attack to North Korean Group UNC1069

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Google Attributes Axios npm Supply Chain Attack to North Korean Group UNC1069](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html)

**Ravie Lakshmanan**Apr 01, 2026Threat Intelligence / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4u0-_Mq5eI-6nWqV9d-E4BTvsdeDTEcK8Bo7pHnANyD6m8b8d5dPcx86sb1P-PjfLce84hgNF8ja8y2tvnYjlmvE4VGzyvAyGqd6TGOxYei3Oz-F_IvVEDxAvamRe4acysr0FqtfWgbLbDhBQxy6ovy2_V47P2d-1qDZig0pcPPnxTCEGfTzKnUXnJEgU/s1700-e365/axios-northkorea.jpg)

Google has [formally attributed](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) the [supply chain compromise](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html) of the popular Axios npm package to a financially motivated North Korean threat activity cluster tracked as **UNC1069**.

"We have attributed the attack to a suspected North Korean threat actor we track as UNC1069," John Hultquist, chief analyst at Google Threat Intelligence Group (GTIG), told The Hacker News in a statement.

"North Korean hackers have deep experience with supply chain attacks, which they've historically used to steal cryptocurrency. The full breadth of this incident is still unclear, but given the popularity of the compromised package, we expect it will have far reaching impacts."

The development comes after [threat actors seized control](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html) of the package maintainer's npm account to push two trojanized versions 1.14.1 and 0.30.4 that introduced a malicious dependency named "plain-crypto-js" that's used to deliver a cross-platform backdoor capable of infecting Windows, macOS, and Linux systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Rather than introducing any code changes to Axios, the attack leverages a postinstall hook within the "package.json" file of the malicious dependency to achieve stealthy execution. Once the compromised Axios package is installed, npm automatically triggers the execution of malicious code in the background.

Specifically, the "plain-crypto-js" package functions as a "payload delivery vehicle" for an obfuscated JavaScript dropper dubbed SILKBELL ("setup.js"), which fetches the appropriate next-stage from a remote server based on the victim's operating system.

As previously detailed by The Hacker News, the Windows execution branch delivers PowerShell malware, a C++ Mach-O binary for macOS, and a Python backdoor for Linux systems. The dropper also performs a cleanup to remove itself and replace the "plain-crypto-js" package's "package.json" file with a clean version that does not have the postinstall hook.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-INPXY0ZSI_LBYJhbmZyqamH1PQlfh5ZfryzZIPg0Nn_ojjuKO1XO2RHZn7PZfkSw_jIew5EJoEHmrcJD3P3a-KG1Q5C5ofTMzfU28IE_Jha5sGl8E1XRJRorEQZidf-i9QKCt7FP96GFKrl2aYRqghFIjzz3ihMXw9cuFRhVXgmuMbjOIF5vClUOsLTu/s1700-e365/elastic.jpeg) |
| Image Source: Elastic Security Labs |

The backdoor, codenamed WAVESHAPER.V2, is assessed to be an updated version of [WAVESHAPER](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html), a C++ backdoor deployed by UNC1069 in attacks aimed at the cryptocurrency sector. The threat actor has been operational since 2018. The supply chain attack's links to UNC1069 were first flagged by Elastic Security Labs, citing functionality overlaps.

The three WAVESHAPER.V2 variants support four different commands, while beaconing to the command-and-control (C2) server at 60-second intervals -

* **kill**, to terminate the malware's execution process.
* **rundir**, to enumerate directory listings, along with file paths, sizes, and creation/modification timestamps.
* **runscript**, to run AppleScript, PowerShell, or shell commands based on the operating system.
* **peinject**, to decode and execute arbitrary binaries.

"WAVESHAPER.V2 is a direct evolution of WAVESHAPER, a macOS and Linux backdoor previously attributed to UNC1069," Mandiant and GTIG said. "While the original WAVESHAPER uses a lightweight, raw binary C2 protocol and employs code packing, WAVESHAPER.V2 communicates using JSON, collects additional system information, and supports more backdoor commands."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"Despite these upgrades, both versions accept their C2 URL dynamically via command-line arguments, share identical C2 polling behaviors and an uncommon User-Agent string, and deploy secondary payloads to identical temporary directories (e.g., /Library/Caches/com.apple.act.mond)."

The links to North Korea are also bolstered by the fact that the macOS binary [references](https://www.elastic.co/security-labs/axios-supply-chain-compromise-detections) developer build paths like "Jain\_DEV/client\_mac/macWebT/macWebT," where "macWebT" links directly to [BlueNoroff's "webT" module](https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/) from [RustBucket](https://thehackernews.com/2023/04/lazarus-subgroup-targeting-apple.html) and [Hidden Risk](https://thehackernews.com/2024/11/north-korean-hackers-target-crypto.html) malware campaigns in 2023, according to researcher [Giuseppe Massaro](https://gist.github.com/N3mes1s/0c0fc7a0c23cdb5e1c8f66b208053ed6).

To [mitigate the threat](https://www.upwind.io/feed/from-nodes-to-snakes-npm-supply-chain), users are advised to audit dependency trees for compromised versions (and downgrade to a safe version, if found), pin Axios to a known safe version in the "package-lock.json" file to prevent accidental upgrades, check for presence of "plain-crypto-js" in "node\_modules," terminate malicious processes, block C2 domain ("sfrclak[.]com," IP address: ...