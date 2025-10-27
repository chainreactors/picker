---
title: Discord Introduces DAVE Protocol for End-to-End Encryption in Audio and Video Calls
url: https://thehackernews.com/2024/09/discord-introduces-dave-protocol-for.html
source: The Hacker News
date: 2024-09-24
fetch_date: 2025-10-06T18:34:07.100964
---

# Discord Introduces DAVE Protocol for End-to-End Encryption in Audio and Video Calls

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Discord Introduces DAVE Protocol for End-to-End Encryption in Audio and Video Calls](https://thehackernews.com/2024/09/discord-introduces-dave-protocol-for.html)

**Sep 23, 2024**Ravie LakshmananEncryption / Data Protection

[![End-to-End Encryption](data:image/png;base64... "End-to-End Encryption")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwIMDH5Ttdg8nPhJHywjUPPdok8Br5S_UU9wdeWK1_b6DiESpjKWw67O-k878kGgwBiYmx3qvjyzc9utCn7Z6A1HeVAXwCrP_wH1rNKQQyPhyphenhyphenKh-HD7hx3aSXgj2nApCz1E0IZv6YWVaCrasC_-jm6ICvO7S_mBXBiXoZKuFwmHyz-hjUeKTsUk_EKYhGZ/s790-rw-e365/discord.png)

Popular social messaging platform Discord has [announced](https://discord.com/blog/meet-dave-e2ee-for-audio-video) that it's rolling out a new custom end-to-end encrypted (E2EE) protocol to secure audio and video calls.

The protocol has been dubbed **DAVE**, short for Discord's audio and video end-to-end encryption ("E2EE A/V").

As part of the change introduced last week, voice and video in DMs, Group DMs, voice channels, and Go Live streams are expected to be migrated to use DAVE.

That said, it's worth noting that messages on Discord will remain unencrypted and are subject to its content moderation approach.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"When we consider adding new privacy features like E2EE A/V, we do not do so in isolation from safety," Discord [said](https://discord.com/safety/more-private-and-secure). "That is why safety is integrated across our product and policies, and why messages on Discord are unencrypted."

"Messages will still be subject to our content moderation approach, allowing us to continue offering additional safety protections."

DAVE is [publicly auditable](https://github.com/discord/libdave) and has been reviewed by Trail of Bits, with the protocol leveraging [WebRTC encoded transforms](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms) and Message Layer Security ([MLS](https://thehackernews.com/2023/07/google-messages-getting-cross-platform.html)) for encryption and group key exchange (GKE), respectively.

This allows for media frames, outside of the codec metadata, to be encrypted after they are encoded and decrypted before being decoded on the receiver side.

[![End-to-End Encryption](data:image/png;base64... "End-to-End Encryption")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-Axw3qdOyCa6xB82LoMf_F6AGUJc5iqfzD9fupjV-cy2kKZ6XmHOY9Qgnj_GZ0O3zoH0k4nlIOW1ZgR4xjGhHegyDk0g-lv3kp6O3Eb_SNPqo-qRiuSRvE-0A0nlmFSAy82u7iWGv4AmpsQCeruVkp0fQDlbnlhYkCsqT6DxV3T8MLxO1WmAO1_7MxxCG/s790-rw-e365/encryption.png)

"Each frame is encrypted or decrypted with a per-sender symmetric key," Discord said. "This key is known to all participants of the audio and video session but crucially is unknown to any outsider who is not a member of the call, including Discord."

The use of MLS, on the other hand, makes it possible for users to join or leave a voice or video session on Discord in such a manner that neither new participants can decrypt media sent before they joined nor leaving members can decrypt any media sent in the future.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Discord's existing transport encryption for audio and video between the client and our selective forwarding unit (SFU) is retained, ensuring only audio and video from authenticated call participants is forwarded," it noted.

"While the SFU still processes all packets for the call, audio or video data inside each packet is end-to-end encrypted and undecryptable by the SFU."

The development comes days after the GSM Association (GSMA), the governing body that oversees the development of the Rich Communications Services (RCS) protocol, [said](https://thehackernews.com/2024/09/gsma-plans-end-to-end-encryption-for.html) it's working towards implementing E2EE to secure messages sent between the Android and iOS ecosystems.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[Digital Security](https://thehackernews.com/search/label/Digital%20Security)[encryption](https://thehackernews.com/search/label/encryption)[Online Safety](https://thehackernews.com/search/label/Online%20Safety)[Privacy](https://thehackernews.com/search/label/Privacy)[Social media](https://thehackernews.com/search/label/Social%20media)[technology](https://thehackernews.com/search/label/technology)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI...