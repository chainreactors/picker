---
title: Why encrypted backup is so important
url: https://blog.cryptographyengineering.com/2022/12/07/apple-icloud-and-why-encrypted-backup-is-the-only-privacy-issue/
source: A Few Thoughts on Cryptographic Engineering
date: 2022-12-08
fetch_date: 2025-10-04T00:51:28.448425
---

# Why encrypted backup is so important

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# Why encrypted backup is so important

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/ "Posts by Matthew Green")
in [Apple](https://blog.cryptographyengineering.com/category/apple/)
December 7, 2022December 8, 2022
2,335 Words

![](https://matthewdgreen.files.wordpress.com/2016/08/matthew-green.jpg?w=200&h=300)

# Matthew Green

I'm a cryptographer and professor at Johns Hopkins University. I've designed and analyzed cryptographic systems used in wireless networks, payment systems and digital content protection platforms. In my research I look at the various ways cryptography can be used to promote user privacy.

[My academic website](https://matthewgreen.io)
[BlueSky](https://bsky.app/profile/did%3Aplc%3Axvgztewzbfh7bpnklayrsvds)
[Mastodon](https://ioc.exchange/%40matthew_d_green)
[Twitter](https://twitter.com/matthew_d_green)
[Top Posts](https://blog.cryptographyengineering.com/top-posts/)
[Useful crypto resources](https://staging.cryptographyengineering.com/useful-cryptography-resources/)
[Bitcoin tipjar](https://blog.cryptographyengineering.com/p/bitcoin-tipjar.html)
[Cryptopals challenges](http://cryptopals.com/)
[Applied Cryptography Research: A Board](https://acrab.isi.jhu.edu/)

[Journal of Cryptographic Engineering
(not related to this blog)](http://www.springer.com/computer/security%2Band%2Bcryptology/journal/13389)

Search for:

# Top Posts & Pages

* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [Is Telegram really an encrypted messaging app?](https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/)
* [Kerberoasting](https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [EUF-CMA and SUF-CMA](https://blog.cryptographyengineering.com/euf-cma-and-suf-cma/)
* [The Many Flaws of Dual\_EC\_DRBG](https://blog.cryptographyengineering.com/2013/09/18/the-many-flaws-of-dualecdrbg/)
* [Attack of the week: RC4 is kind of broken in TLS](https://blog.cryptographyengineering.com/2013/03/12/attack-of-week-rc4-is-kind-of-broken-in/)
* [What is Differential Privacy?](https://blog.cryptographyengineering.com/2016/06/15/what-is-differential-privacy/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Useful Cryptography Resources](https://blog.cryptographyengineering.com/useful-cryptography-resources/)

*Banner image by Matt Blaze*

# Archives

Archives

Select Month
 September 2025  (1)
 June 2025  (1)
 March 2025  (1)
 February 2025  (5)
 January 2025  (1)
 August 2024  (1)
 April 2024  (1)
 January 2024  (1)
 November 2023  (1)
 October 2023  (1)
 August 2023  (1)
 May 2023  (2)
 April 2023  (1)
 March 2023  (1)
 December 2022  (1)
 October 2022  (1)
 June 2022  (1)
 January 2022  (1)
 August 2021  (1)
 July 2021  (1)
 March 2021  (1)
 November 2020  (1)
 August 2020  (1)
 July 2020  (1)
 April 2020  (1)
 March 2020  (1)
 January 2020  (1)
 December 2019  (1)
 October 2019  (1)
 September 2019  (1)
 June 2019  (1)
 February 2019  (1)
 December 2018  (1)
 October 2018  (1)
 September 2018  (1)
 July 2018  (2)
 May 2018  (1)
 April 2018  (3)
 February 2018  (1)
 January 2018  (2)
 December 2017  (1)
 November 2017  (1)
 October 2017  (2)
 September 2017  (1)
 July 2017  (1)
 March 2017  (1)
 February 2017  (1)
 January 2017  (1)
 November 2016  (1)
 August 2016  (2)
 July 2016  (1)
 June 2016  (1)
 March 2016  (2)
 December 2015  (1)
 November 2015  (1)
 October 2015  (1)
 September 2015  (1)
 August 2015  (1)
 July 2015  (1)
 May 2015  (1)
 April 2015  (2)
 March 2015  (1)
 February 2015  (3)
 January 2015  (1)
 December 2014  (1)
 November 2014  (1)
 October 2014  (3)
 September 2014  (1)
 August 2014  (1)
 July 2014  (1)
 April 2014  (2)
 March 2014  (1)
 February 2014  (1)
 January 2014  (1)
 December 2013  (4)
 October 2013  (1)
 September 2013  (4)
 August 2013  (1)
 July 2013  (1)
 June 2013  (2)
 May 2013  (1)
 April 2013  (2)
 March 2013  (2)
 February 2013  (3)
 January 2013  (2)
 December 2012  (1)
 November 2012  (1)
 October 2012  (4)
 September 2012  (3)
 August 2012  (4)
 July 2012  (2)
 June 2012  (3)
 May 2012  (5)
 April 2012  (6)
 March 2012  (4)
 February 2012  (7)
 January 2012  (8)
 December 2011  (11)
 November 2011  (13)
 October 2011  (7)
 September 2011  (8)

You might have seen the news today that Apple is announcing a [raft of improvements](https://www.apple.com/newsroom/2022/12/apple-advances-user-security-with-powerful-new-data-protections/) to Macs and iOS devices aimed at improving security and privacy. These include FIDO support, improvements to iMessage key verification, and a much anticipated announcement that the company is [abandoning their plans](https://www.macrumors.com/2022/12/07/apple-abandons-icloud-csam-detection/) for (involuntary) photo scanning.

While every single one of these is exciting, one announcement stands above the others. This is Apple’s decision to roll out (opt-in) end-to-end encryption for iCloud backups. While this is only one partial step in the right direction, it’s still a huge and decisive step — one that I think will substantially raise the bar for cloud security across the whole industry.

If you’re looking for precise details on all of these features, see Apple’s [description](https://www.apple.com/newsroom/2022/12/apple-advances-user-security-with-powerful-new-data-protections/) here or [their platform security guide](https://support.apple.com/guide/security/advanced-data-protection-for-icloud-sec973254c5f/web). Others will no doubt have the time to do deep-dive explanations on each one. (I was given a short presentation by Apple today, and was provided the opportunity to ask a bunch of questions that their representative answered thoughtfully. But this is no substitute for a detailed look at the technical specs.)

In the rest of this post I want to zero in on end-to-end encrypted iCloud backup, and why I think this announcement is such a big deal.

### Smartphones and cloud backup: the biggest consumer privacy compromise you never heard of

If you’re the typical smartphone or tablet user, your devices have become the primary repository for your private papers, photos and communications. Imagine some document that your grandparents would have kept on a shelf or inside of a locked drawer in their home. Today the equivalent document probably resides in one of your devices. This data is the most personal stuff in a human life: your private family photos, your mail, your financial records, even a history of the books you read and which pages you found meaningful. Of course, it also includes new types of information that are *unimaginably* more [valuable](https://www.howtogeek.com/437871/how-to-find-your-location-history-on-iphone-or-ipad/) [and](https://support.apple.com/en-us/HT204351) [invasive](https://recoverit.wondershare.com/phone-recovery/find-deleted-history-on-google-chrome-android.html) than anything your grandparents could have ever imagined.

But this is only half the story.

If you’re the typical user, you don’t *only* keep this data in your device. An exact duplicate exists in a data center hundreds or thousands of miles away from you. Every time you snap a photo, each night while you sleep, this doppelganger is scrupulously synchronized through the tireless efforts of cloud backup software — usually the default software built into your device’s operating system.

It goes without saying that *you*, dear reader, might not be the typical user. You might be one of the vanishingly small fraction of users who chang...