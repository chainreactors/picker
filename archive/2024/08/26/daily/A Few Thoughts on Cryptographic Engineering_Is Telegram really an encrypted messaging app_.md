---
title: Is Telegram really an encrypted messaging app?
url: https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/
source: A Few Thoughts on Cryptographic Engineering
date: 2024-08-26
fetch_date: 2025-10-06T18:00:49.236412
---

# Is Telegram really an encrypted messaging app?

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# Is Telegram really an encrypted messaging app?

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/ "Posts by Matthew Green")
in [messaging](https://blog.cryptographyengineering.com/category/messaging/)
August 25, 2024August 25, 2024
2,290 Words

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

* [Is Telegram really an encrypted messaging app?](https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/)
* [Kerberoasting](https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [Why the FBI can’t get your browsing history from Apple iCloud (and other scary stories)](https://blog.cryptographyengineering.com/2021/03/25/whats-in-your-browser-backup/)
* [Useful Cryptography Resources](https://blog.cryptographyengineering.com/useful-cryptography-resources/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Let's talk about PAKE](https://blog.cryptographyengineering.com/2018/10/19/lets-talk-about-pake/)
* [What's the deal with RC4?](https://blog.cryptographyengineering.com/2011/12/15/whats-deal-with-rc4/)
* [Three questions about Apple, encryption, and the U.K.](https://blog.cryptographyengineering.com/2025/02/23/three-questions-about-apple-encryption-and-the-u-k/)

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

This blog is reserved for more serious things, and ordinarily I wouldn’t spend time on questions like the above. But much as I’d like to spend my time writing about exciting topics, sometimes the world requires a bit of what [Brad Delong](https://braddelong.substack.com/) calls “Intellectual Garbage Pickup,” namely: correcting wrong, or mostly-wrong ideas that spread unchecked across the Internet.

This post is inspired by the recent and concerning news that [Telegram’s CEO Pavel Durov has been arrested by French authorities](http://app is accused of failure to cooperate with law enforcement over drug trafficking, child sexual content and fraud.) for its failure to sufficiently moderate content. While I don’t know the details, the use of criminal charges to coerce social media companies is a pretty worrying escalation, and I hope there’s more to the story.

But this arrest is not what I want to talk about today.

What I do want to talk about is one specific detail of the reporting. Specifically: the fact that nearly every news report about the arrest refers to Telegram as an “encrypted messaging app.” Here are [just a](https://www.politico.eu/article/telegram-app-ceo-pavel-durov-reportedly-arrested-at-french-airport/) [few](https://abcnews.go.com/Technology/wireStory/french-authorities-arrest-telegram-ceo-pavel-durov-paris-113132319) [examples](https://www.france24.com/en/live-news/20240825-telegram-chief-pavel-durov-arrested-at-french-airport):

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2024/08/image-1.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2024/08/image-1.png)

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2024/08/image-2.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2024/08/image-2.png)

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2024/08/image-3.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2024/08/image-3.png)

This phrasing drives me nuts because in a very limited technical sense it’s *not wrong.* Yet in every sense that matters, it fundamentally misrepresents what Telegram is and how it works in practice. And this misrepresentation is bad for both journalists and particularly for Telegram’s users, many of whom could be badly hurt as a result.

Now to the details.

### Does Telegram have encryption or doesn’t it?

Many systems use encryption in some way or another. However, when we talk about encryption in the context of modern private messaging services, the word typically has a very specific meaning: it refers to the use of default [end-to-end](https://en.wikipedia.org/wiki/End-to-end_encryption) encryption to protect users’ message content. When used in an industry-standard way, this feature ensures that every message will be encrypted using encryption keys that are only known to the communicating parties, and not to the service provider.

From your perspective as a user, an “encrypted messenger” ensures that each time you start a conversation, your messages will only be readable by the folks you intend to speak with. If the operator of a messaging service tries t...