---
title: What We Do in the /etc/shadow – Cryptography with Passwords
url: https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/
source: Dhole Moments
date: 2022-12-30
fetch_date: 2025-10-04T02:44:53.773733
---

# What We Do in the /etc/shadow – Cryptography with Passwords

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/)

# What We Do in the /etc/shadow – Cryptography with Passwords

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [December 29, 2022](https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/)
* [13 Comments on What We Do in the /etc/shadow – Cryptography with Passwords](https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/#comments)

![What We Do in the /etc/shadow Cryptography with Passwords](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/BlogHeader-2022-Passwords.png?fit=1200%2C675&ssl=1)

Ever since the famous “Open Sesame” line from *One Thousand and One Nights*, humanity was doomed to suffer from the scourge of passwords.

![Something you know. Password. Something you have. RSA token. Something you are. Fingerprint.  Something you pretend to be. Happy.](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/swiftonsecurity-something.png?resize=600%2C312&ssl=1)

Courtesy of [SwiftOnSecurity](https://twitter.com/SwiftOnSecurity/status/512081783643320320)

Even in a world where we use hardware tokens with asymmetric cryptography to obviate the need for passwords in [modern authentication protocols](https://webauthn.guide/), we’ll still need to include “something you know” for legal and political reasons.

In the United States, we have the Fifth Amendment to the US Constitution, which prevents anyone from being forced to testify against oneself. This sometimes includes revealing a password, so it is imperative that passwords remain a necessary component of some encryption technologies to prevent prosecutors from side-stepping one’s Fifth Amendment rights. (Other countries have different laws about passwords. I’m not a lawyer.)

If you’ve ever read anything from [the EFF](https://www.eff.org/), you’re probably keenly aware of this, but the US government *loves* to side-step citizens’ privacy rights in a court of law. They do this not out of direct malice towards civil rights (generally), but rather because it makes their job easier. *Incentives rule everything around me.*

Thus, even in a passwordless future, anyone who truly cares about civil liberties will not want to dispense with them entirely. Furthermore, we’ll want these password-based technologies to pass [the Mud Puddle test](https://blog.cryptographyengineering.com/2012/04/05/icloud-who-holds-key/), so that we aren’t relying on large tech companies to protect us from government backdoors.

Given all this, most security professionals will agree that **passwords suck**. Not only are humans bad sources of randomness, but we’re awful at memorizing a sequence of characters or words for every application, website, or operating system that demands a password.

None of what I’ve written so far is the least bit novel or interesting. But here’s a spicy take:

The only thing that sucks worse than passwords is the messaging around password-based cryptographic functions.

## Password-Based Cryptographic Functions

That isn’t a term of the art, by the way. I’m kind of coining it as a superset that includes both **Password-Based Key Derivation Functions** and **Password Hashing Functions**.

You might be wondering, “Aren’t those two the same thing?” No, they are not. I will explain in a moment.

The intersection of human-memorable secrets (passwords) and cryptographic protocols manifests in a lot of needless complexity and edge-cases that, in order to sufficiently explain anything conversationally, will require me to sound either drunk or like a blue deck player in *Magic: The Gathering*.

![Drakeposting No Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-07.png?resize=512%2C512&ssl=1)

Counterspell!
Art: [CMYKat](https://cmykatgraphics.carrd.co/)

To that end, what I’m calling **Password-Based Cryptographic Functions** (PBCFs) includes all of the following:

* Password-Hashing Functions
  + Bcrypt
* Password-Based Key Derivation Functions
  + Scrypt
  + Argon2
  + PBKDF2
  + [bscrypt](https://github.com/Sc00bz/bscrypt)
* Balanced Password Authenticated Key Exchanges
  + CPace
* Augmented Password Authenticated Key Exchanges
  + SRP
  + AuCPace
  + [BS-SPEKE](https://gist.github.com/Sc00bz/e99e48a6008eef10a59d5ec7b4d87af3)
* Doubly-Augmented Password Authenticated Key Exchanges
  + OPAQUE
  + [Double BS-SPEKE](https://gist.github.com/Sc00bz/a57c07a83f16bb78683425be60a65718)

If you tried to approach categorization starting with simply “Key Derivation Functions”, you’d quickly run into a problem: What about [HKDF](https://soatok.blog/2021/11/17/understanding-hkdf/)? Or any of the NIST SP 800-108 KDFs for that matter?

If you tighten it to “Password-Based KDFs” or “Key-stretching functions”, that doesn’t include bcrypt. Bcrypt is a password hashing function, but [it’s not suitable for deriving secret keys](https://news.ycombinator.com/item?id=22028143). I’ve discussed [these nuances previously](https://soatok.blog/2021/08/24/programmers-dont-understand-hash-functions/#password-hashing-functions).

And then you have some password KDF and/or hashing algorithms that are memory-hard, some that are *cache-hard*.

And then some Password Authenticated Key Exchanges (PAKEs) are quantum-annoying, while others are not.

![Blue Screen of Death Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-10.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

To make heads or tails of the different algorithms, their properties, and when and where you should use them, you’d either need to secure postdoc funding for cryptography research or spend a lot of time reading and watching passwords-focused conference talks.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/defcon30-sc00bz-soatok-quantumvillage.png?resize=768%2C576&ssl=1)

It helps if you’re friends with a [Password Hashing Competition](https://www.password-hashing.net/) judge.
(Selfie taken by Sc00bz (left) at DEFCON 30 in the Quantum Village.)

So let’s talk about these different algorithms, *why* they exist to begin with, and some of their technical details.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-cooking.png?resize=512%2C470&ssl=1)

Art: [Harubaki](https://harubaki.carrd.co/)

## Why Does Any of This Matter?

The intersection of passwords and cryptography is one of the foundations of modern society, and one that most Internet users experience everywhere they go.

You’ll know you have succeeded in designing a cryptographic algorithm when the best way to attack it is to try every possible key. This is called an exhaustive search, or a brute-force attack, depending on the disposition of the author.

Remember earlier when I said passwords suck because humans are bad at creating or remembering strong, unique passwords for every website they visit?

Well, it turns out, that [some passwords are extremely common](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt). And even worse, people who choose common passwords tend to reuse them everywhere.

This presented a challenge to early web applications: In order to have authenticated users, you need to collect a password from the user and check it on subsequent visits. If you ever get hacked, then it’s likely that all of your users will be impacted on other websites they used the same passwords for.

Including their bank accou...