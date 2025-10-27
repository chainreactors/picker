---
title: Windows BitLocker Screwed without a Screwdriver
url: https://media.ccc.de/v/38c3-windows-bitlocker-screwed-without-a-screwdriver
source: Instapaper: Unread
date: 2025-01-03
fetch_date: 2025-10-06T20:12:10.694884
---

# Windows BitLocker Screwed without a Screwdriver

[![media.ccc.de logo, a lucky cat holding a play icon](/assets/frontend/voctocat-header-b587ba587ba768c4a96ed33ee72747b9a5432b954892e25ed9f850a99c7d161c.svg)](/)

- System
- Light
- Dark

|  |  |
| --- | --- |
| [News](/news.atom) |  |
| [RSS, last 100](/updates.rdf) |  |
| [Podcast feed of the last two years](/podcast-hq.xml) | [SD quality](/podcast-lq.xml "Podcast feed of the last two years (SD)") |
| [Podcast audio feed of the last year](/podcast-audio-only.xml) |  |
| [Podcast archive feed, everything older than two years](/podcast-archive-hq.xml) | [SD quality](/podcast-archive-lq.xml "Podcast archive feed, everything older than two years (SD)") |
| Podcast feeds for 38c3 | |
| [webm](https://media.ccc.de/c/38c3/podcast/webm-hq.xml "webm") | [SD quality](https://media.ccc.de/c/38c3/podcast/webm-lq.xml "webm (SD)") |
| [mp4](https://media.ccc.de/c/38c3/podcast/mp4-hq.xml "mp4") | [SD quality](https://media.ccc.de/c/38c3/podcast/mp4-lq.xml "mp4 (SD)") |
| [opus](https://media.ccc.de/c/38c3/podcast/opus.xml "opus") |  |
| [mp3](https://media.ccc.de/c/38c3/podcast/mp3.xml "mp3") |  |
| [vtt](https://media.ccc.de/c/38c3/podcast/vtt.xml "vtt") |  |
| [srt](https://media.ccc.de/c/38c3/podcast/srt.xml "srt") |  |

|  |  |
| --- | --- |
| [News](/news.atom) |  |
| [RSS, last 100](/updates.rdf) |  |
| [Podcast feed of the last two years](/podcast-hq.xml) | [SD quality](/podcast-lq.xml "Podcast feed of the last two years (SD)") |
| [Podcast audio feed of the last year](/podcast-audio-only.xml) |  |
| [Podcast archive feed, everything older than two years](/podcast-archive-hq.xml) | [SD quality](/podcast-archive-lq.xml "Podcast archive feed, everything older than two years (SD)") |
| Podcast feeds for 38c3 | |
| [webm](https://media.ccc.de/c/38c3/podcast/webm-hq.xml "webm") | [SD quality](https://media.ccc.de/c/38c3/podcast/webm-lq.xml "webm (SD)") |
| [mp4](https://media.ccc.de/c/38c3/podcast/mp4-hq.xml "mp4") | [SD quality](https://media.ccc.de/c/38c3/podcast/mp4-lq.xml "mp4 (SD)") |
| [opus](https://media.ccc.de/c/38c3/podcast/opus.xml "opus") |  |
| [mp3](https://media.ccc.de/c/38c3/podcast/mp3.xml "mp3") |  |
| [vtt](https://media.ccc.de/c/38c3/podcast/vtt.xml "vtt") |  |
| [srt](https://media.ccc.de/c/38c3/podcast/srt.xml "srt") |  |

1. [browse](/b)
2. [congress](/b/congress)
3. [2024](/b/congress/2024)
4. event

[![conference logo](https://static.media.ccc.de/media/congress/2024/logo.svg)](/c/38c3)

# Windows BitLocker: Screwed without a Screwdriver

[th0mas](/search?p=th0mas)

[![

](https://static.media.ccc.de/media/congress/2024/816-7de6f4a3-1ef5-51df-bcb4-0203669eeb52_preview.jpg)](https://cdn.media.ccc.de/congress/2024/h264-hd/38c3-816-eng-Windows_BitLocker_Screwed_without_a_Screwdriver.mp4)

[Stage HUFF](/c/38c3/Stage%20HUFF)
Playlists:
['38c3' videos starting here](/v/38c3-windows-bitlocker-screwed-without-a-screwdriver/playlist)
/
[audio](/v/38c3-windows-bitlocker-screwed-without-a-screwdriver/audio)

* 56 min
* 2024-12-28
* 2024-12-30
* 29.2k
* [Fahrplan](https://events.ccc.de/congress/2024/hub/event/windows-bitlocker-screwed-without-a-screwdriver/)

Ever wondered how Cellebrite and law enforcement gain access to encrypted devices without knowing the password? In this talk, we’ll demonstrate how to bypass BitLocker encryption on a fully up-to-date Windows 11 system using Secure Boot. We’ll leverage a little-known software vulnerability that Microsoft has been unable to patch since 2022: bitpixie (CVE-2023-21563).

We'll live-demo the exploit, and will walk through the entire process—from the prerequisites and inner workings of the exploit to why Microsoft has struggled to address this flaw. We'll also discuss how to protect yourself from this and similar vulnerabilities.

BitLocker is Microsoft’s implementation of full-volume encryption. It offers several modes of operation, but the most widely used is Secure Boot-based encryption.

Many consumer and corporate clients use it, and it’s starting to be enabled by default under "Device Encryption" on newer Windows 11 installations.

In this mode, the harddrive is encrypted at rest but is automatically unsealed when a legit windows boots, meaning users don't need a separate decryption password. They just have to sign in with their usual user account.

Unfortunately, this configuration has been broken for quite a while. Hardware attacks against a dTPM are widely known, but software attacks are possible as well, at least since 2022, when Rairii discovered the bitpixie bug (CVE-2023-21563).

While this bug is 'fixed' since Nov. 2022 and publically known since 2023, we can still use it today with a downgrade attack to decrypt BitLocker.

In this talk, we'll dive into:

- How does Secure Boot work, and what role does the TPM play?

- How can Bitlocker leverage the TPM?

- How does the bitpixie exploit work? What are PXE boot and BCD?

- What are the prerequisites for running this exploit?

- How can you protect yourself against it?

- Why is it so challenging for Microsoft to fully fix this?

- How does this affect Linux secure boot?

Licensed to the public under http://creativecommons.org/licenses/by/4.0

### Download

#### Video

* [MP4](#mp4)
* [WebM](#webm)

[Download 1080p

eng-deu
827 MB](https://cdn.media.ccc.de/congress/2024/h264-hd/38c3-816-eng-deu-Windows_BitLocker_Screwed_without_a_Screwdriver_hd.mp4)

[Download 576p

eng-deu
182 MB](https://cdn.media.ccc.de/congress/2024/h264-sd/38c3-816-eng-deu-Windows_BitLocker_Screwed_without_a_Screwdriver_sd.mp4)

[Download 1080p

eng-deu
454 MB](https://cdn.media.ccc.de/congress/2024/webm-hd/38c3-816-eng-deu-Windows_BitLocker_Screwed_without_a_Screwdriver_webm-hd.webm)

[Download 576p

eng-deu
178 MB](https://cdn.media.ccc.de/congress/2024/webm-sd/38c3-816-eng-deu-Windows_BitLocker_Screwed_without_a_Screwdriver_webm-sd.webm)

#### These files contain multiple languages.

This Talk was translated into multiple languages. The files available
for download contain all languages as separate audio-tracks. Most
desktop video players allow you to choose between them.

Please look for "audio tracks" in your desktop video player.

#### Audio

[Download mp3

eng
51 MB](https://cdn.media.ccc.de/congress/2024/mp3/38c3-816-eng-Windows_BitLocker_Screwed_without_a_Screwdriver_mp3.mp3)

[Download mp3

deu
51 MB](https://cdn.media.ccc.de/congress/2024/mp3-translated/38c3-816-deu-Windows_BitLocker_Screwed_without_a_Screwdriver_mp3-2.mp3)

[Download opus

eng
39 MB](https://cdn.media.ccc.de/congress/2024/opus/38c3-816-eng-Windows_BitLocker_Screwed_without_a_Screwdriver_opus.opus)

[Download opus

deu
34 MB](https://cdn.media.ccc.de/congress/2024/opus-translation/38c3-816-deu-Windows_BitLocker_Screwed_without_a_Screwdriver_opus-2.opus)

### Embed

### Share:

### Tags

[38c3](/tags/38c3)
[816](/tags/816)
[2024](/tags/2024)
[Stage HUFF](/c/38c3/Stage%20HUFF)

by
[Chaos Computer Club e.V](//ccc.de)
––
[About](/about.html)
––
[Apps](/about.html#apps)
––
[Imprint](//ccc.de/en/imprint)
––
[Privacy](/about.html#privacy)
––
[c3voc](//c3voc.de/)