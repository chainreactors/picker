---
title: What Does Sandboxing and Reverse Engineering 643 Salat Stealer Malicious Software Samples Lead To And Who Is Its Author Maxim Vladimirovich Nesterenko?
url: https://ddanchev.blogspot.com/2026/11/what-does-sandboxing-and-reverse.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-11-18
fetch_date: 2026-11-19T09:46:01.247191
---

# What Does Sandboxing and Reverse Engineering 643 Salat Stealer Malicious Software Samples Lead To And Who Is Its Author Maxim Vladimirovich Nesterenko?

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Wednesday, November 18, 2026

### [What Does Sandboxing and Reverse Engineering 643 Salat Stealer Malicious Software Samples Lead To And Who Is Its Author Maxim Vladimirovich Nesterenko?](https://ddanchev.blogspot.com/2026/11/what-does-sandboxing-and-reverse.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCXX7GPFMn00ZApv4K2OWfi73hbE9iVDrojW6Pms-aYCBHHWN-hBCz_6BwXpiVygTknaLiOf45HhzTXb8shzEY9EuDxoIOn3z8Nnf7xjEDOWSH0eQJEkv2o1e_BRJu_Pk88i-zXg9Bao2lXzlffHNupAv0D1z5GIakka5lNHctlyRtLP3pFIFA/s1600/Screenshot_159.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCXX7GPFMn00ZApv4K2OWfi73hbE9iVDrojW6Pms-aYCBHHWN-hBCz_6BwXpiVygTknaLiOf45HhzTXb8shzEY9EuDxoIOn3z8Nnf7xjEDOWSH0eQJEkv2o1e_BRJu_Pk88i-zXg9Bao2lXzlffHNupAv0D1z5GIakka5lNHctlyRtLP3pFIFA/s270/Screenshot_159.png)

Dear blog readers,

This is Dancho.

I recently decided to take a deeper look inside the inner workings and network C&C communication network and infrastructure using 643 Salat Stealer samples which I on purposely sandboxed and reverse engineered in bulk with the idea to not just look for similarities which are evident in over 87% of the samples but also pin point and look for additional clues about how the Salat Stealer malicious software works and functions.

As you can see in the attached screenshot the embedded resolver certificate references Vladimir Putin's email Barack Obama and Kurwa bobr which is a Polish Internet meme and catchphrase which translated into Fucking beaver and there's also a "Я люблю сосать" message in the actual sample and also the following messages.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9bu4aqCI5UENNKOgLnPfl4pJdRFL0klb6olhLN64G3Tgo_POcl4BJSD_LsE5VzayxnUoVn3zK7ayWa-GvS6SvCV0SLudTupHUJ2U81GSogLpyOImL10PZajifHIQuaC2NQXO2LGZGtOBUSNzvwwWQtEmgyZ2Uk5rMvfQLhInm02R_wAiQBOfp/s320/Screenshot_161.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9bu4aqCI5UENNKOgLnPfl4pJdRFL0klb6olhLN64G3Tgo_POcl4BJSD_LsE5VzayxnUoVn3zK7ayWa-GvS6SvCV0SLudTupHUJ2U81GSogLpyOImL10PZajifHIQuaC2NQXO2LGZGtOBUSNzvwwWQtEmgyZ2Uk5rMvfQLhInm02R_wAiQBOfp/s368/Screenshot_161.png)

In this analysis I'll discuss in-depth how the Salat Stealer malicious software works and functions and elaborate in-depth on its network C&C command infrastructure and will also discuss several insecure coding practices that the malicious software authors seem to have neglected which is great news.

**Some details on the C&C infrastructure include which are encoded in all the samples:**

hxxp://salator.es - 195.208.61.205

hxxp://wruser.org - 195.208.61.205

hxxp://websalat.top - 185.53.179.136

hxxp://sa1atik.cn - 46.173.27.15 - Usmondzhon Zakirov - Email: istan4urka@gmail.com

hxxp://morkovka.cn

hxxp://webrat.su - sosincorp@gmail.com

hxxp://sa1atik.cn

MD5: 929e2b172bfda207f2b5491831da8dce

SHA256: 6135c3ae6a101a06638e209cd14999d786e724f21a65c52833e40b727f1d5de8

**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX-LjFV-9MUuKJgTW5YpDxE5IXFHCW2XhrHd8vU_AP_v8y58dmULMcQGgl3VgFHiLl7xUupkOcxkeqUHSEHsHii6jPggKjcvbFBkcsZD5r1wffGT4rpT3E6t8SXWeYIhdLrTJuzTdwrVj5DRSLs5C5aW5EK6ZpD46rNZbPwxB7laTAHAyCsiia/s320/Screenshot_162.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX-LjFV-9MUuKJgTW5YpDxE5IXFHCW2XhrHd8vU_AP_v8y58dmULMcQGgl3VgFHiLl7xUupkOcxkeqUHSEHsHii6jPggKjcvbFBkcsZD5r1wffGT4rpT3E6t8SXWeYIhdLrTJuzTdwrVj5DRSLs5C5aW5EK6ZpD46rNZbPwxB7laTAHAyCsiia/s884/Screenshot_162.png)

Also the following:**

hxxp://salator.es/sa1at

hxxp://wruser.org/sa1at

hxxp://websalat.top/sa1at

hxxp://sa1atik.cn/sa1at

hxxp://wruser.org:992/sa1at - prioritized if winws.exe is running; appended otherwise

Configuration tables use a 129-word rotate/XOR transform, 4096-bit modular exponentiation with exponent65537, hex decoding, cumulative XOR, repeating XOR, another hex decode and AES-GCM. Seed `biba` derives key `93851482190d261c1302a29caa569522` through cumulative XOR of raw MD5(seed). Repeating-XOR secret is `d0af20d0bbd18ed0b1d0bbd18e20d181d0bed181d0b0d182d18c`. Decoder computation was checked against an AES-GCM known-answer vector and endpoint authentication tags.

## Transport and decentralized fallback

Transport selection/failover includes QUIC HTTP/3 and ordinary Go HTTP. `tryRQ` constructs \*\*HTTP GET requests with bodies\*\*, Content-Type `application/octet-stream`, to the selected URL directly. Body obfuscation is repeating XOR followed by cumulative XOR, not AES. Numeric JSON keys/opcodes are used. An IP-host branch sets HTTP Host to `google.com`; this does not make Google a malicious destination or prove successful domain fronting. An encrypted embedded blob was verified to decode to a 91-certificate CA trust bundle, not an executable second stage.

Gorilla WebSocket sessions provide interactive channels, with destinations supplied through commands. A single fixed built-in WSS destination was not established.

Exact TON discovery seeds:

- `hxxp://tonapi.io/v2/dns/webratpanel.ton/resolve`

- `hxxp://tonapi.io/v2/dns/remoteadministratortool.ton/resolve`

- `hxxp://shyetootval.ton`

- `hxxp://webratxaye1.ton`

Public RPC: `https://ton.access.orbs.network/route/1/mainnet/toncenter-api-v2/runGetMethod`

Embedded DNS root: `Ef\_lZ1T4NCb2mwkme9h2rJfESCE0W34ma9lWp7-\_uY3zXDvq`

TONAPI processing reads `wallet.address`. Raw account bytes, represented as 64 hex characters with optional `0:` prefix, decode into a NUL-trimmed comma-separated candidate list. Direct TON DNS calls `dnsresolve` with SHA256(wallet) category and follows contract records to terminal wallet bytes. Accepted candidates become `https://<candidate>/sa1at/` and populate primary/alternate buckets. Current replacement hosts remain unknown without external record data. \*\*TONAPI, Orbs and the root contract are public infrastructure, not proof of attacker ownership; avoid unconditional provider-wide blocking.\*\*

Startup creates mutex \*\*`Global\WEBR\_93FBTYWPXRVS`\*\*. Installation follows successful initial communications and response gates: numeric key1 must be0 or1, key2 must parse, and a second response must be nonempty and begin `[` or `{`. A marker check can skip installation.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjH2fKJw4kDZbayBR7hhnjn6S0LEQHukx0gTYkMwPZf8gPOY8ZiashZLNv7hx9URP1zt7nvmsq_dTiqK_NZRk9VphBeliHh0lr2hMMdDdUhgY24LTcaXuIBpRrsyOyVOXULk_VCw-x7XGw3DDJ-M1KO3OSKdZfJvCaI7ttPDPjJj3RoC2L5raO/s320/Screenshot_160.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjH2fKJw4kDZbayBR7hhnjn6S0LEQHukx0gTYkMwPZf8gPOY8ZiashZLNv7hx9URP1zt7nvmsq_dTiqK_NZRk9VphBeliHh0lr2hMMdDdUhgY24LTcaXuIBpRrsyOyVOXULk_VCw-x7XGw3DDJ-M1KO3OSKdZfJvCaI7ttPDPjJj3RoC2L5raO/s379/Screenshot_160.png)

Copies use selected existing Program Files/Program Files(x86)/LocalAppData directories with AppData fallback, variable process-derived basenames and HIDDEN|SYSTEM attributes. Scheduled task name is `\` plus installed basename without extension, executing the copied path with logon/time triggers and a constructed three-minute repeat interval. Failed task setup falls back to \*\*HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\*\*, value basename-without-extension, data installed executable path. There is no universal installed filename or task name. A GUID-shaped host-specific marker derives from MD5(HWID+hostname+`WF8wvauqSa11NbxrdPwN`).

The installation path launches an embedded PowerShell script attempting Defender directory exclusions for...