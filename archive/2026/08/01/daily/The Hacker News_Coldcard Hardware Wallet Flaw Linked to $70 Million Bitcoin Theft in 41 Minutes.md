---
title: Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes
url: https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html
source: The Hacker News
date: 2026-08-01
fetch_date: 2026-08-02T05:11:27.083777
---

# Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes

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

# [Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes](https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html)

**Swati Khandelwal**Aug 01, 2026Vulnerability / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiea5Kw_2TLtPI4Ts3s3anmPIQr3S8VxO0G9yL-UV1dSlRrW1Z_L41XoHcSFuk2ThCBDKLFy-xZl_y7DnA0FM2nWHk4G1TpV2iMx6-X6EDT3gK7s0pJu6e1wMUoEsuPifcXseXuqOIHL3W9voWoD_se5gKJPyii4X0mJY7sxJ3uOPlTWVfAyrKs4ixa-18/s1700-e365/coldcard.jpg)

An attacker drained 1,196 Bitcoin addresses in 41 minutes on July 30, taking 1,082.65 BTC worth about $70.2 million at the time. Galaxy Research [mapped](https://x.com/glxyresearch/status/2083181683067506899) the sweep and tied it to a firmware flaw in **Coldcard**, the Bitcoin-only hardware wallet made by Canadian firm **Coinkite**.

A March 2021 firmware integration error routed seed generation to a deterministic software pseudorandom number generator (PRNG) instead of the STM32 hardware random number generator (RNG).

Block says an attacker who can determine or sufficiently constrain the device UID, timer state, and prior RNG-call history can reproduce candidate output streams offline without accessing the device. Candidate seeds can then be checked by deriving their addresses and comparing them with public blockchain data.

Coinkite shipped emergency firmware for every affected model and release track on July 31, but installing it does not repair an existing seed. Coinkite tells owners with exposed seeds to generate a new one on patched firmware and [move their coins](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Restoring the old seed to updated firmware or another wallet carries the weakness forward. No public report has reconstructed a victim's seed and matched it to a drained address.

[Block traced the fault](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware) to Coldcard's production config, which defines MICROPY\_HW\_ENABLE\_RNG as zero because Coinkite supplies its own hardware-RNG wrapper. The libngu library checked whether the macro existed rather than whether it was enabled, binding the build to MicroPython's Yasmarang fallback. The MicroPython fallback was initialized from the chip's unique ID and timer registers and collected no fresh entropy after initialization.

Coinkite [estimates effective entropy](https://blog.coinkite.com/entropy-technical-backgrounder/) at roughly 40 bits on the Mk3 and about 72 bits on the Mk4, Mk5 and Q, against 128 bits for a 12-word BIP-39 seed. Block does not give one practical figure. It sets conditional ceilings below 240.7 and 273.3 and warns that the latter is not equivalent to 73-bit cryptographic security. It published no brute-force benchmark.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8GjgEMi4p2nxRVMSL1wIDYptawGTGnlc8-fYJtWBUimP3npqIEzteQEnZhu_FJwe7TSM2R1NwbuKQPhrtKQf9ZcMa2Is-Z4avebAPSLgDA5SLuWqnZXltrOG7tH9xfwKmuVy0N8MFZ6aU2tEyiqP047ZXU1ugWR_TCPwzSTNuD0uQuIlRqhgeCCAVMe8/s1700-e365/HOjysfkWAAAfi_G.jpg) |
| Image Source: Galaxy Research |

The later-model reseed raises the number of candidates, but Block says practical cost depends on available UID information, boot timing, prior RNG calls and derivation cost.

Exposure depends on the firmware running when the seed was created, not the version installed now:

* **Mk2 and Mk3:** Coinkite lists Mk3 versions 4.0.1 through 4.1.9, fixed in 4.2.0, and does not name Mk2. Block places both Mk2 and Mk3 versions 4.0.0 through 4.1.9 on the vulnerable path.
* **Mk4 and Mk5:** anything before 5.6.0.
* **Q:** anything before 1.5.0Q.
* **Edge builds:** before 6.6.0X for Mk4 and Mk5, before 6.6.0QX for Q.

Coinkite says a seed built with at least 50 fair, independent, private dice rolls is not at risk from this bug alone. If the number or privacy of the rolls is uncertain, Coinkite says to migrate. A strong, unique BIP-39 passphrase creates a separate wallet the seed words cannot reach on their own, but the company still recommends replacing the seed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Multisig helps only when the quorum is not built entirely from affected devices. TAPSIGNER, OPENDIME and SATSCARD use different codebases and are unaffected.

No one has named the attacker. Galaxy, which mapped the 1,196-address sweep, said it found no other Bitcoin transactions in the previous 30 days with the same 30 sat/vB, no-change signature.

It [warned](https://x.com/glxyresearch/status/2083255552633635183) that the pattern identifies the operator, not the theft, because a sweep "looks the same as if a coin owner chose to move coins."

The disclosure follows Coinspect's [Ill Bloom](https://thehackernews.com/2026/07/attackers-exploit-ill-bloom.html) research in early July, a separate weak-PRNG flaw in older software wallets tied to more than $5 million drained from addresses across Bitcoin, Ethereum, Tron, Rootstock and Polygon since May.

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
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Bitcoin](https://thehackernews.com/search/label/Bitcoin), [cryptocurrency](https://thehackernews.com/search/label/cryptocurrency), [cryptography](https://thehackernews.com/search/label/cryptography), [Cybercrime](https://thehackernews.co...