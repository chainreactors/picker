---
title: Kerberoasting
url: https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/
source: A Few Thoughts on Cryptographic Engineering
date: 2025-09-11
fetch_date: 2025-10-02T19:57:14.526261
---

# Kerberoasting

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# Kerberoasting

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/ "Posts by Matthew Green")
in [attacks](https://blog.cryptographyengineering.com/category/attacks/), [Microsoft](https://blog.cryptographyengineering.com/category/microsoft/), [passwords](https://blog.cryptographyengineering.com/category/passwords/)
September 10, 2025September 11, 2025
1,591 Words

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

* [Kerberoasting](https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/)
* [Is Telegram really an encrypted messaging app?](https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [Attack of the week: RC4 is kind of broken in TLS](https://blog.cryptographyengineering.com/2013/03/12/attack-of-week-rc4-is-kind-of-broken-in/)
* [Let's talk about PAKE](https://blog.cryptographyengineering.com/2018/10/19/lets-talk-about-pake/)
* [EUF-CMA and SUF-CMA](https://blog.cryptographyengineering.com/euf-cma-and-suf-cma/)
* [How to prove false statements? (Part 3)](https://blog.cryptographyengineering.com/2025/02/19/how-to-prove-false-statements-part-3/)
* [How to choose an Authenticated Encryption mode](https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)

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

I learn about cryptographic vulnerabilities all the time, and they generally fill me with some combination of jealousy (“oh, why didn’t I think of that”) or else they impress me with the brilliance of their inventors. But there’s also another class of vulnerabilities: these are the ones *that can’t possibly exist* in important production software, because *there’s no way anyone could still do that in 2025.*

Today I want to talk about one of those ridiculous ones, something Microsoft calls “low tech, high-impact”. This vulnerability isn’t particularly new; in fact the worst part about it is that it’s *[had a name](https://www.redsiege.com/wp-content/uploads/2020/08/Kerberoastv4.pdf)* for over a decade, and it’s existed for longer than that. I’ll bet most Windows people already know this stuff, but I only happened to learn about it today, after seeing a [letter from Senator Wyden to Microsoft](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_microsoft_kerberoasting_ransomwarepdf.pdf), describing how this vulnerability was used in the May 2024 [ransomware attack on the Ascension Health hospital system](https://www.hipaajournal.com/ascension-cyberattack-2024/).

The vulnerability is called [Kerberoasting](https://www.irongeek.com/i.php?page=videos%2Fderbycon4%2Ft120-attacking-microsoft-kerberos-kicking-the-guard-dog-of-hades-tim-medin), and TL;DR it relies on the fact that Microsoft’s Active Directory is *very, very old*. And also: RC4. If you don’t already know where I’m going with this, please read on.

**A couple of updates:** *The [folks on HN](https://news.ycombinator.com/item?id=45196437) pointed out that I was using some incorrect terms in here (sorry!) and added some good notes, so I’m updating below. Also, Tim Medin, who discovered and named the attack, has a great post on it [here](https://redsiege.com/blog/2025/09/kerberoasting-microsoft-and-a-senator/).*

### What’s Kerberos, and what’s Active Directory?

Microsoft’s Active Directory (AD) is a many-tentacled octopus that controls access to almost every network that runs Windows machines. The system uses centralized authentication servers to determine who gets access to which network resources. If an employee’s computer needs to access some network Service (a file server, say), an Active Directory server authenticates the user and helps them get securely connected to the Service.

This means that AD is also the main barrier ensuring that attackers can’t extend their reach deeper into a corporate network. If an attacker somehow gets a toehold inside an enterprise (for example, because [an employee clicks on a malicious Bing link](https://www.audacy.com/wwjnewsradio/news/local/worker-who-clicked-bogus-link-led-to-ascension-cyber-attack)), they should absolutely not be able to move laterally and take over critical network services. That’s because any such access would require the employee’s machine to have access to specialized accounts (called “Service accounts”) with privileges to fully control those machines. A well-managed network obviously won’t allow this. This ...