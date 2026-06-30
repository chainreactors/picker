---
title: Factoring RSA Keys with Many Zeros
url: https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html
source: Schneier on Security
date: 2026-06-29
fetch_date: 2026-06-30T06:10:11.835424
---

# Factoring RSA Keys with Many Zeros

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

## Factoring RSA Keys with Many Zeros

Interesting research on a [new class](https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/) of weak RSA keys: keys with lots of zeros. It turns out that these keys are out in the wild.

> The badkeys project is an open-source service that checks public keys for known vulnerabilities. While developing this tool, Hanno collected a massive number of real-world keys from public sources, including Certificate Transparency logs, internet-wide TLS and SSH scans, PGP keys, and many others. By searching this dataset for unexpectedly sparse RSA moduli, we uncovered a large number of keys in the wild with the patterns in Figure 1.
>
> Both patterns include several regularly spaced blocks of all zeros interleaved with seemingly random data. Pattern 1 appears in CT logs for certificates issued to several large organizations, including Yahoo and Verizon, and on some devices running NetApp software. Fortunately, these certificates have already expired, but we still shared our findings with these companies. We wanted to learn more about which product could be responsible for generating these keys, but we did not hear back. Pattern 2 appears on SSH hosts running the CompleteFTP software from EnterpriseDT. The underlying vulnerability affects RSA keys generated using versions 10.0.0­12.0.0 (Dec 2016­Mar 2019) and DSA keys generated with v10.0.0­23.0.4 (Dec 2016­Dec 2023).
>
> These vulnerabilities affect a small minority of hosts on the internet, but the more interesting takeaway is that independent cryptographic implementations failed in similar ways. More implementations may include the same bugs, and so it’s worth tailoring cryptanalytic algorithms for this particular type of failure.

The article doesn’t speculate, but I will. This could be a deliberately designed backdoor, of the sort I [wrote about](https://www.schneier.com/essays/archives/2013/10/how_to_design_and_de.html) back in 2013. I could imagine some government agency figuring out how to break this class of RSA keys, and then convincing different providers to hand them out to users.

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [keys](https://www.schneier.com/tag/keys/), [RSA](https://www.schneier.com/tag/rsa/)

[Posted on June 29, 2026 at 12:05 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html) •
[11 Comments](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html#comments)

### Comments

anon •
[June 29, 2026 12:49 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455572)

No, not another butchered RSA implementation. I wonder if all of them are insecure?

lurker •
[June 29, 2026 2:35 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455574)

It’s not the “bias towards many zeroes” that’s the problem: it’s the zeroes turning up in identical sized blocks, identically spaced in the “random” strings. It looks dodgy to the naked eye, as if it could be cracked quickly with an abacus. If somebody gave me a key like those I would send it back and ask for a replacement.
Or use <https://xkcd.com/221/>

Clive Robinson •
[June 29, 2026 4:08 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455575)

@ Bruce, ALL,

With regards,

> “The article doesn’t speculate, but I will.”

We’ve been through this prior to 2013.

With respect to generating certificates on embedded devices such as “network devices”.

It’s very difficult to develop entropy on such devices when they are “first out the box” because they have next to no internal entropy and likewise external entropy[1].

Thus there would be a very high chance that all certificates generated on such devices are very closely related.

Whilst factoring the multiple of two large primes is assumed to be hard… Finding two or more such multiples that share a prime is in comparison trivial, using a simple “Greatest Common Divisor”(GCD) algorithm,

<https://www.cryptool.org/en/posts/rsa-sanity-check/>

As I noted back when I pointed this out, I assume that part of the NSA budget would go on “buying and testing” all edge of network devices looking for weaknesses in such certificate generating devices”

Not technically a “back door” as the NSA did not design or install it. But certainly a nicely exploitable vulnerability almost as good as the one that caused NIST such embarrassment and much to everyone’s suprise turned up on Jupiter Networks high end systems, when it should not have and was still creating issues half a decade back,

<https://checkoway.net/musings/dualec/>

There were other issues with RSA certs which nearly all overlap in time. Thus if the NSA knew about them all could have had access to all RSA PubKey reliant traffic this century…

Which begs the question about why the NSA are twitchy about PQC key establishment protocols…

What do they know that we don’t and is it another bit of NOBUS nonsense again.

[1] It’s one of those “Catch 22” problems… Because the devices have no real human interfaces or electromagnetic moving parts, the device / internal entropy is in the order of one or three bits a minute. Then because the embedded device has no certificate yet, it’s probably got no real external entropy coming in across the network either.

So the “Catch” is to get entropy to make a couple of random numbers of the right size to make a new secure RSA certificate… you either need the certificate already, or known entropy, neither of which is secure…

Not really anonymous •
[June 29, 2026 5:57 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455577)

The NSA is still trying to get people to use pure PQC algorithems rather than hybrids, so something seems to be up with the current PQC proposals.

Weather •
[June 29, 2026 6:20 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455578)

@All

Most algo zero pad, what should be done is 0xaaaa, then each chacter is the value in the area, say 59,60,61,62.

The reason is 0x00 leaks the code book.

CORRUPT ideho •
[June 29, 2026 6:33 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455579)

asking for a friend, if anyone knows who owns a Dodge RAM Truck ideho plates “D RING” please put it right here. They’ve been stalking a friend of mine all day today. They are someone’s FIXERS. Human GARBAGE – WORST OF THE WORST. Thanks a lot.

$H1TH013 Called ideho •
[June 29, 2026 6:45 PM](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html/#comment-455580)

The following Id...