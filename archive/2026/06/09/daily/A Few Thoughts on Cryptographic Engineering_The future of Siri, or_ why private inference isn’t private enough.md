---
title: The future of Siri, or: why private inference isn’t private enough
url: https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/
source: A Few Thoughts on Cryptographic Engineering
date: 2026-06-09
fetch_date: 2026-06-10T06:15:11.085082
---

# The future of Siri, or: why private inference isn’t private enough

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# The future of Siri, or: why private inference isn’t private enough

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/)
in [Apple](https://blog.cryptographyengineering.com/category/apple/), [privacy](https://blog.cryptographyengineering.com/category/privacy/)
June 9, 2026June 9, 2026
2,854 Words

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

* [The future of Siri, or: why private inference isn’t private enough](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/)
* [Let's talk about encrypted reasoning](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [Is Telegram really an encrypted messaging app?](https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/)
* [WhatsApp Encryption, a Lawsuit, and a Lot of Noise](https://blog.cryptographyengineering.com/2026/02/02/whatsapp-encryption-a-lawsuit-and-a-lot-of-noise/)
* [Attack of the week: RC4 is kind of broken in TLS](https://blog.cryptographyengineering.com/2013/03/12/attack-of-week-rc4-is-kind-of-broken-in/)
* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [How to choose an Authenticated Encryption mode](https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/)
* [Anonymous credentials: an illustrated primer](https://blog.cryptographyengineering.com/2026/03/02/anonymous-credentials-an-illustrated-primer/)

*Banner image by Matt Blaze*

# Archives

Archives

Select Month
 June 2026  (1)
 May 2026  (1)
 April 2026  (1)
 March 2026  (1)
 February 2026  (1)
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

Yesterday Apple announced a big step towards [deploying real AI in their Siri ecosystem.](https://www.wired.com/story/apples-new-siri-ai-is-ready-to-get-personal/) In most ways this is good and inevitable: Siri is one of the world’s most widely-used voice agents, and it would be good if it didn’t suck. The idea that Apple would boost its capabilities with frontier models wasn’t so much a matter of *if*, but a question of *when* and *who*.

The who turns out to be Google: Apple looks like it will use some combination of Google Gemini models, combined with Google’s [Confidential Inference](https://blog.google/innovation-and-ai/products/google-private-ai-compute/) and Apple’s own [Private Cloud Compute](https://security.apple.com/blog/expanding-pcc/) for private hosting. These systems will process both your queries *and* evaluate private data from your devices. Apple’s marketing [pitches the advantages](https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/) as follows:

1. First, since your phone already has *context* about you — meaning, your private information, schedules, email, text messages — an AI-enabled Siri can potentially offer more useful answers to your practical requests than external LLMs. Want to schedule a reservation for next week’s birthday party? In theory, a future Siri-AI might already know who’s coming, and what kind of cake they like.
2. Of course, what Apple calls “*context*” is also the raw data of your life. This is deeply private data from all of your apps, and that data can’t just be shipped to random adtech companies (or Sam Altman) for processing. Your context needs to be protected, and Apple bills itself as a privacy company.

There’s some tension between these goals. Apple has addressed this by marketing a service it calls [Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/), or PCC. PCC was introduced in 2024 as a private model inference system that ran entirely on Apple Silicon, using a set of “trusted” hardware security modules running in Apple’s datacenters. The goal of this system is to ensure that your data never leaves Apple’s hardware: it’s encrypted from your phone to a dedicated server, and then it disappears once a response reaches your phone. The stateless design of PCC ensures (in theory) that your data doesn’t linger, and the design of the hardware prevents even Apple from seeing the inputs.

Apple has since “expanded” PCC to encompass Google’s hardware as well. I will confess that I find the details of [the new “expanded” PCC](https://security.apple.com/blog/expanding-pcc/) just a bit vague. It sounds a lot like Apple is primarily going to rely on Google’s existing [confidential compute (running in Google datacenters)](https://blog.google/innovation-and-ai/products/goo...