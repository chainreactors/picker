---
title: Simson Garfinkel on Spooky Cryptographic Action at a Distance
url: https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html
source: Schneier on Security
date: 2024-10-31
fetch_date: 2025-10-06T18:58:15.488854
---

# Simson Garfinkel on Spooky Cryptographic Action at a Distance

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

## Simson Garfinkel on Spooky Cryptographic Action at a Distance

Excellent [read](https://www.linkedin.com/pulse/spooky-data-distance-simson-garfinkel-nrt9e/%20). One example:

> Consider the case of basic public key cryptography, in which a person’s public and private key are created together in a single operation. These two keys are entangled, not with quantum physics, but with math.
>
> When I create a virtual machine server in the Amazon cloud, I am prompted for an RSA public key that will be used to control access to the machine. Typically, I create the public and private keypair on my laptop and upload the public key to Amazon, which bakes my public key into the server’s administrator account. My laptop and that remove server are thus entangled, in that the only way to log into the server is using the key on my laptop. And because that administrator account can do anything to that server­—read the sensitivity data, hack the web server to install malware on people who visit its web pages, or anything else I might care to do­—the private key on my laptop represents a security risk for that server.
>
> Here’s why it’s impossible to evaluate a server and know if it is secure: as long that private key exists on my laptop, that server has a vulnerability. But if I delete that private key, the vulnerability goes away. By deleting the data, I have removed a security risk from the server and its security has increased. This is true entanglement! And it is spooky: not a single bit has changed on the server, yet it is more secure.

Read it all.

Tags: [cryptography](https://www.schneier.com/tag/cryptography/), [quantum cryptography](https://www.schneier.com/tag/quantum-cryptography/)

[Posted on October 30, 2024 at 10:48 AM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html) •
[22 Comments](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html#comments)

### Comments

Royce Williams •
[October 30, 2024 10:56 AM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html/#comment-441400)

Typo: it’s “Simson” (no ‘p’). Maybe this was autocorrect — especially considering it “corrected” me!

(This comment can be deleted once it’s corrected)

Richard H Schwartz •
[October 30, 2024 11:08 AM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html/#comment-441401)

It is more secure, but not necessarily secure unless the private key from your laptop is also entangled with all of its backup copies such that they are all deleted simultaneously.

tfb •
[October 30, 2024 12:34 PM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html/#comment-441403)

No, this is *not* entanglement. And I really, really wish people would actually make the effort to learn what entanglement is before spouting off about it.

Consider the following case: there is a gun and a knife. A bad person has one, I have the other. The bad person is going to do bad things to some other people. You are the police, and the way you deal with a gun threat is very different than the way you deal with a knife threat (maybe it is not in real life, but for the sake of the story let it be so). In particular the method you will use against a gun threat is completely ineffective against a knife threat & vice versa, while each method is completely effective against the threat is was designed for.

You do not know who has which weapon. So your chance of stopping the bad person is 50%. Or, you can persuade me to tell you which weapon I have. Now your chance of stopping the bad person is 100%.

Does that mean the knife is entangled with the gun? That there was spooky action at a distance of which Einstein would not approve? I mean, do you think Einstein was an idiot? Or do you think that, perhaps, spooky action at a distance is a different thing?

Enough already.

Clive Robinson •
[October 30, 2024 1:26 PM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html/#comment-441404)

Hmm,

> *“it’s impossible to evaluate a server and know if it is secure: as long that private key exists on my laptop, that server has a vulnerability.”*

Not actually true.

If either the private key or a way to reconstruct it, exists then the server is not secure.

The laptop could have had the private key stolen from it or the RNG used to generate the primes could be deficient or backdoored in some way.

Which is why this statement is not actually true either,

> *“But if I delete that private key, the vulnerability goes away.”*

But it’s a bit more subtle than just a Private key being available as data via Communication, Storage, or Processing.

In essence it’s to do with the unproven status of “One Way Functions”(OWFs) with “Back doors” or secret “Trap doors” that enable a “secret holder” to reverse the OWF.

There is an old saying about the fact that only three numbers make sense from a philosophical perspective,

1, Zero : There is none of something.

For a true OWF there must be “Zero” back doors.

For a OWF with a Trap Door you hope there is only “One”

But there is no actual proof that OWFs with “Trap Doors” only have one trap door.

[Impossibly Stupid](https://www.impossiblystupid.com) •
[October 30, 2024 1:54 PM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html/#comment-441405)

I would argue that this approach is more “security by obscurity” than any useful analogy to quantum mechanics. Whatever vulnerability that remote access presents does *not* go away when something external to the system changes.

It’s easier to see the flaw in thinking if you consider passwords rather than a complex key pair exchange. If I have a password like ‘sexy123’, anyone who can either guess it or hack my local password database can use it to access the remote system. Deleting it from my local system and acting like the remote system is now secure is extraordinarily short sighted.

> as long that private key exists on my laptop, that server has a vulnerability

It is more correct to say that the server shares the laptop’s vulnerabilities *any time after* that access was set up. Along with all other vulnerabilities that are introduced in the process (e.g., backups, etc.). Nothing “spooky” is happening, and systems *will* get exploited if they are not properly maintained.

Larry •
[October 30, 2024 3:46 PM](https://www.schneier.com/blog/archives/2024/10/simson-garfinkel-on-spooky-cryptographic-action-at-a-distance.html/#comment-441406)

It isn’t spooky action at a distance until the threat goes away faster than the speed of light. If you delete the key on the server. The key...