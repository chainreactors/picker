---
title: On the Security of Password Managers
url: https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html
source: Schneier on Security
date: 2026-02-23
fetch_date: 2026-02-24T04:12:14.560725
---

# On the Security of Password Managers

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## On the Security of Password Managers

[Good article](https://arstechnica.com/security/2026/02/password-managers-promise-that-they-cant-see-your-vaults-isnt-always-true/) on password managers that secretly have a backdoor.

> New research shows that these claims aren’t true in all cases, particularly when account recovery is in place or password managers are set to share vaults or organize users into groups. The researchers reverse-engineered or closely analyzed Bitwarden, Dashlane, and LastPass and identified ways that someone with control over the server­—either administrative or the result of a compromise­—can, in fact, steal data and, in some cases, entire vaults. The researchers also devised other attacks that can weaken the encryption to the point that ciphertext can be converted to plaintext.

This is where I plug my own [Password Safe](https://www.pwsafe.org/). It isn’t as full-featured as the others and it doesn’t use the cloud at all, but it’s actual encryption with no recovery features.

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [Password Safe](https://www.schneier.com/tag/password-safe/), [passwords](https://www.schneier.com/tag/passwords/)

[Posted on February 23, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html) •
[14 Comments](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html#comments)

### Comments

bw •
[February 23, 2026 7:35 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452342)

I self hold vaultwarden, as far as I can tell has all of the features of bitwarden… you can use the bitwarden extension AND I can self host behind multiple layers of security as well.

I feel like “defense in depth” has been forgotten…

TimH •
[February 23, 2026 8:29 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452343)

@bw “I feel like “defense in depth” has been forgotten…”

Also, don’t store your secrets on somebody else’s computer, no matter what assurances they give.

Chris Becke •
[February 23, 2026 8:39 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452344)

Wish there was a product that was as secure as PasswordSafe but simple enough for my grandparents to safely use.

Reinhold •
[February 23, 2026 9:10 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452345)

My father-in-law with 89 still used Password Safe. I love it since many years.

Clive Robinson •
[February 23, 2026 9:37 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452346)

@ Bruce,

With regards,

> “This is where I plug my own Password Safe. It isn’t as full-featured as the others and it doesn’t use the cloud at all, but it’s actual encryption with no recovery features.”

1, Not full-featured = lower attack surface.

As for “it’s actual encryption” there are always risks with encryption in the modes, protocols and standards that it’s used within. However much of that should not apply and that which does can usually be mitigated against.

@ ALL,

With regards password managers there is an issue that is not much talked about…

Some services store all user data in an encrypted form with the key derived from the user password.

Sensible selection of the password can mitigate the risk of it being cracked and the encryption key recovered by a hostile third party.

However… Backups of the encrypted user data on a cloud or similar server can usually be acquired by a hostile third party who keeps it untill either,

A, They get a copy of the password.
B, The potential for Quantum Computing arises.

But there is more to it, with passwords stored in a file even though encrypted the chances are a user has a mixture of password strengths and once one is found the others are easier to find (especially if the encryption is not properly implemented).

Thus any password strategy needs to take these issues into account.

Also all communications encryption these days should be via a hybrid of strong pre-quantum and strong post-quantum crypto.

All file encryption should use the strongest encryption with the largest bit size that is secure, because Quantum Computing effectively halves the number of bits of key size of conventional encryption.

One mitigation is not to use “passwords” but other forms of “root of trust, shared secret” where proof of knowledge systems can be used where the “shared secret” gets checked by “zero knowledge encryption” etc but never put out over the wire.

Such systems can be built into “Hardware Security Modules”(HSMs) that can be built using “smart cards” in devices small enough to slide into a wallet.

But apparently these are not considered worth designing, building, and putting on the market…

nessuno •
[February 23, 2026 9:48 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452347)

“Wish there was a product that was as secure as PasswordSafe but simple enough for my grandparents to safely use.”

There is: pen and paper, stored within a safe with a mechanical lock.

TTS •
[February 23, 2026 10:36 AM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452349)

@TimH
*Also, don’t store your secrets on somebody else’s computer, no matter what assurances they give.*

Amen.

On another hand, will the entire login ecosystem be soon broken?

<https://www.securityweek.com/nists-quantum-breakthrough-single-photons-produced-on-a-chip/>

Quantum computers will upend current cryptology by using Shor’s algorithm to rapidly negate the current public/private key secure encryption methods. This has largely been solved by NIST’s post quantum cryptology (PQC) algorithms.
NIST has developed Superconducting Nanowire Single-Photon Detectors (SNSPDs) which would allow single photons to be reliably sent and received over longer distances – up to 600 miles.

The second big advance is that NIST can do this on a single chip, which means such chips could be in mass production by the end of next year. Traditionally, NIST develops standards and industry rapidly adopts them. While the QKD market is likely to be relatively small (limited to areas that require very strong security), separate applications will quickly follow.

M Haden •
[February 23, 2026 12:34 PM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452350)

How do you handle or recommend people document passwords in a way that people can access things once you pass from this realm?

Steve •
[February 23, 2026 1:10 PM](https://www.schneier.com/blog/archives/2026/02/on-the-security-of-password-managers.html/#comment-452355)

@**M Haden**: *How do you handl...