---
title: Jurisdiction Is Nearly Irrelevant to the Security of Encrypted Messaging Apps
url: https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/
source: Dhole Moments
date: 2025-07-10
fetch_date: 2025-10-06T23:26:07.146753
---

# Jurisdiction Is Nearly Irrelevant to the Security of Encrypted Messaging Apps

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

[Software Security](https://soatok.blog/category/technology/software-security/)

# Jurisdiction Is Nearly Irrelevant to the Security of Encrypted Messaging Apps

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [July 9, 2025](https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/)

![Jurisdiction Is Nearly Irrelevant to the Security of Encrypted Messaging Apps](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/07/BlogHeader-2025-Jurisdiction.png?fit=1200%2C675&ssl=1)

Every time I lightly touch on this point, I always get someone who insists on arguing with me about it, so I thought it would be worth making a dedicated, singular-focused blog post about this topic without worrying too much about tertiary matters.

Here’s the TL;DR: **If you actually built your cryptography properly, you shouldn’t give a shit which country hosts the ciphertext for your messaging app.**

The notion of some apps being somehow “more secure” because they shovel data into Switzerland rather than a US-based cloud server is [laughable](https://en.wikipedia.org/wiki/Crypto_AG).

But this line of argument sometimes becomes sinister when people evangelize *storing plaintext* instead of using end-to-end encryption, and then try to justify not using cryptography by appealing to jurisdiction instead.

That more extreme argument is patently stupid. That is all I will say about it, lest this turn into a straw man argument. But if I didn’t bring it up somewhere, someone would tell me I “forgot” about it, so I’m mentioning it for completeness.

> I’m going to state up front an important nuance that several commentators overlooked when responding to this post.
>
> I am **only** talking about the jurisdiction of “where ciphertext is stored”. That is the entire relevant scope. Nothing more, nothing less.

Let’s start with the premise of the TL;DR.

What does “actually [building] your cryptography properly” mean?

## Properly Built Cryptography

An end-to-end encrypted messaging app isn’t as simple as “I called AES\_Encrypt() somewhere in thee client-side code. Job done!”

If you’ve implemented the cryptography properly, you might even be a contender for [a real alternative to Signal](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/). This isn’t an exercise for the faint of heart.

To begin with, you need to solve key management. This means both client-side, secret-key management (and deciding whether or not to pass [The Mud Puddle Test](https://blog.cryptographyengineering.com/2012/04/05/icloud-who-holds-key/#:~:text=do%20it%20anyway.-,The%20mud%20puddle%20test,-You%20don%E2%80%99t%20have)) and providing some mechanism for validating that the public key vended by the server is the correct one for the other conversation participant.

The cryptography community tried for over three decades to make “key fingerprints” happen, but I know professional cryptographers who have almost never verified a PGP key fingerprint or Signal safety number in practice. I’m working on a project to provide [Key Transparency for the Fediverse](https://github.com/fedi-e2ee/public-key-directory-specification). This is much a better starting point. Feel free to let power users do whatever rituals they want, but don’t count on most people bothering.

Separately, the app that ships the cryptography should itself strictly adhere to [reproducible builds](https://reproducible-builds.org/) and binary transparency (i.e., [SigStore](https://www.sigstore.dev/)).

### What’s This About Transparency?

Both “Key Transparency” and “Binary Transparency” are specific instances of a general notion of using a Transparency Log to keep a privileged system honest.

Also, Key Transparency is an abbreviated term. The thing that you’re being incredibly transparent about is a user’s **public keys**. If that wasn’t the case, key transparency would be a dangerous and scary idea.

> If you don’t know what a public key is, this blog post might be too technical for you right now.
>
> If that’s the case, [start here](https://old.reddit.com/r/explainlikeimfive/comments/qsljvr/eli5_what_is_public_key_encryption/) to get a sense for how people try to explain it simply.

Separate to both of those topics, **Certificate Transparency** is already being used to keep the Certificate Authorities that secure Internet traffic honest.

But either way, they’re just specific instances of using a transparency log to provide some security property to an ecosystem.

#### What’s a Transparency Log?

A transparency log is a type of log or ledger that uses an append-only data structure, such as a Merkle tree.

They’re designed such that anyone can verify the integrity and consistency of the log’s entries. See [this web page](https://certificate.transparency.dev/logs/) for more info.

Sometimes you’ll hear cryptographers talk about a “secure bulletin board” in a protocol design. What they almost always mean is a transparency log, or something fancier built on top of one.

> If this vaguely sounds blockchainy to you, you would be correct: Every cryptocurrency ledger is a consensus protocol (often “proof-of-work”) stapled onto a transparency log, and from there, they build fancier features like smart contracts and zero-knowledge virtual machines.

#### Independent Third-Party Monitors Are Essential

There is little point in running any sort of transparency log if you do not have independent third parties that monitor the log entries.

Even better if you take [a page out of Sigsum’s book](https://www.sigsum.org/docs/) and implement witness co-signatures as a first class feature.

### What Does Transparency Give You?

If you’re wondering, “Okay, so what?” then let me try to connect the dots.

If you want to surreptitiously compromise a messaging app, you might try to:

1. **Backdoor the client-side software.**

   But binary transparency and reproducible build verification will make this extremely easy to detect–or even worse, mitigate.
2. **Compromise the server to distribute the wrong public keys.**

   But key transparency prevents the server from successfully lying about the public keys that belong to a given user. Additionally, it prevents the server from changing history without being detected.

For a more detailed treatment, refer to [the threat model I wrote](https://github.com/fedi-e2ee/public-key-directory-specification/blob/main/Specification.md#threat-model) for the public key directory project.

### What Else Is Needed for Proper Implementations?

Once you have reproducible builds, binary transparency, secret-key management (which may or may not include secure backups), and public key transparency, you next need to actually ship a secure end-to-end encryption protocol.

The two games in town are MLS and the Signal Protocol. My previous blog post [compared the two](https://soatok.blog/2025/07/07/checklists-are-the-thief-of-joy/#signal-mls). They provide different subtly different security properties, serve slightly different use cases, and have similar but not identical threat models.

If you want to go with a third option, it **MUST NOT** tolerate plaintext transmission at all. Otherwise, it doesn’t qualify.

If your use case is to focus on scaling up group chats to large numbers of participants, efficiently, and don’t care about obfuscating metadata or social graphs, you might find MLS a more natural fit for your application.

Cryptographers use formal notions t...