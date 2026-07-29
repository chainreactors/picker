---
title: Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process
url: https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:26.763583
---

# Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process

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

# [Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process](https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html)

**Swati Khandelwal**Jul 28, 2026Linux / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0zv7PihU6xAba7-fb5OY-Xv5YIEPM1HhmCu2ET65l5TSKYrPh6q4pYVQRNJtHb9RkvO1oNsBBrsxs50Hm_GRnPKCu4XoG1hhtPOoeGILfRHN99ICGSO72NOGQ6AdUc_haCrQvHRUn4YiyFmCy99WgH1v4-4GRLirZzsV1b5MmCjfTX3a2yWmg1tWOr38/s1700-e365/tengu-botnet.jpg)

A new Mirai-derived botnet called **Tengu** can use a compromised Linux device's hardware watchdog to trigger a reboot when defenders kill its main process.

If that happens, Tengu's other persistence mechanisms get another chance to relaunch it. Nozomi Networks Labs observed the dropper reaching its honeypots through Telnet credential brute force.

Tengu supports 25 distributed denial-of-service (DDoS) methods. It can also run a SOCKS5 proxy, execute shell commands, and collect system and network data. The malware can update itself and retrieve additional Executable and Linkable Format (ELF) or Android package (APK) payloads.

Nozomi listed architecture-specific samples for i386, amd64, MIPS, ARM, PowerPC, and m68k. The report identifies no specific vendor or device model. It also names no operator, infection count, or real-world DDoS victims. It shows what Tengu can do, not how far it has spread.

Defenders should start by removing internet exposure for Telnet and other unnecessary administrative services and replacing default credentials. Nozomi also recommends updating firmware, segmenting Internet of Things (IoT) networks, and reviewing systemd services, init scripts, shell startup files, and cron-related paths before returning a suspected device to service.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Nozomi Networks Labs [published its analysis](https://www.nozominetworks.com/blog/tengu-a-modernized-mirai-that-doesnt-want-to-leave) on July 27, 2026. Nozomi said Tengu's persistence and self-defense code made it stand out among the Mirai-derived samples it tracks. "Most Mirai variants implement few, if any, of these self-defense capabilities," the researchers said.

Once running, the bot forks a detached guardian that checks the principal malware process every 60 seconds and relaunches the installed binary if it stops. It can also create a fake systemd service, add init and RC scripts, alter shell startup files, and mark its installed binary immutable. A cron-based persistence routine is present, but Nozomi said its reference to /proc/self/exe appears unfinished or broken.

A second mechanism abuses the device's hardware watchdog. A background worker masquerades as [kworker/0:0], reopens the watchdog device if available, arms it with an approximately 30-second timeout, and sends keepalive signals only while the main malware process remains alive. Kill the process and the watchdog stops getting fed, allowing the device to reboot. Tengu's other persistence mechanisms can then try to relaunch it.

Tengu also carries a hardcoded list of reboot and shutdown utilities. It overwrites their ELF headers with the string ELFOOD, which can interfere with the normal commands defenders may use to restart or safely power down a compromised device.

The analyzed sample was configured to communicate with a command-and-control (C2) server at 64[.]89.163.8 over TCP port 9931. Registration, heartbeat traffic, and command output are sent in plaintext, while server commands and updates use a custom ChaCha20/Poly1305-like authenticated encryption scheme.

Tengu can also obtain a C2-supplied content identifier from an InterPlanetary File System (IPFS) gateway on the same server, validate the result as an ELF or APK, and execute or install it.

Nozomi assessed that the APK path likely targets poorly secured [Android TV boxes](https://thehackernews.com/2026/05/mirai-based-xlabsv1-botnet-exploits-adb.html) or similar devices, but did not document confirmed Android victims.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

[URLhaus independently recorded](https://urlhaus.abuse.ch/host/64.89.163.8/) 17 malware URLs at 64[.]89.163.8 beginning June 17, 2026. The records included a shell script, multiple ELF files tagged as Mirai, and an APK. URLhaus's most recent payload entries were first seen on July 7, and all 17 URLs were offline as of July 28.

URLhaus does not identify the files as Tengu. As of July 28, none of the SHA-256 hashes listed on its host record matched the sample hash published by Nozomi. Its telemetry therefore confirms only malicious Mirai-related hosting at the address.

The Hacker News has reached out to Nozomi Networks for additional details about Tengu's observed scale, infrastructure status, and sample linkage, and will update the story with any response.

Neither Nozomi nor URLhaus establishes whether the C2 service on port 9931 or the IPFS gateway on port 8080 was reachable. URLhaus's status applies only to its listed download URLs. Nozomi also does not say whether the configured C2 server at 64[.]89.163.8:9931 issued any commands.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitte...