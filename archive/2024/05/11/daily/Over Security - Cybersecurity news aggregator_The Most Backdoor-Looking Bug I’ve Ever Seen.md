---
title: The Most Backdoor-Looking Bug I’ve Ever Seen
url: https://words.filippo.io/dispatches/telegram-ecdh/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-11
fetch_date: 2025-10-06T17:18:45.535864
---

# The Most Backdoor-Looking Bug I’ve Ever Seen

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

10 Jan 2021

# The Most Backdoor-Looking Bug I’ve Ever Seen

This is the story of a bug that was discovered and fixed in Telegram’s self-rolled cryptographic protocol about seven years ago. The bug didn’t get any press, and no one seems to know about it, probably because it was only published in Russian.

To this day, it’s the most backdoor-looking bug I’ve ever seen.

Google Translate does a good enough job on the [original article](https://habrahabr.ru/post/206900/), which is still available on Habr, but I’m going to walk you through it along with some context.

Telegram is a popular chat app that uses its own… bizarre protocol to encrypt chats, called MTProto. The protocol is used both to encrypt all messages to the Telegram server, and to encrypt opt-in 1:1 end-to-end “Secret Chats”.[1](#fn:default) In text I can’t do justice to the facial expressions of cryptographers when you mention Telegram’s protocol, so just believe me that it’s *weird*.

The current consensus seems to be that the latest version is not broken in known ways that are severe or relevant enough to affect end users, assuming the implementation is correct. That is about as safe as leaving exposed wires around your house because they are either not live or placed high enough that no one should touch them.

The original version was, however, completely broken, in the most puzzling of ways.

End-to-end Telegram chat sessions use [finite-field Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)[2](#fn:ffdhe) to establish a shared key between the two participants. The negotiation happens through messages relayed by the Telegram server. Diffie-Hellman is a fundamental building block of many cryptosystems, and it allows two parties to establish a shared secret that any eavesdroppers can’t derive. It is however only one part of a secure key exchange, because an attacker capable of intercepting the messages could simply establish two separate sessions with the two parties, carrying out a [Person-in-the-Middle](https://en.wikipedia.org/wiki/Person-in-the-middle_attack) attack. The parties need some way to verify they derived the same secret. In TLS, they use a signature from a certificate. In most secure chat apps, there is a fingerprint (“Safety Numbers” in Signal) that the two parties can compare out-of-band.[3](#fn:fingerprint) What’s important is that if the two sides derived the same secret, they can be sure no one else has access to it.

The Telegram key exchange is described in [the “Key Generation” section of Telegram’s end-to-end API docs](https://web.archive.org/web/20131220000537/https%3A//core.telegram.org/api/end-to-end#key-generation). Concretely, Alice requests the DH parameters `(p, g)` from Telegram, painstakingly verifies them, computes a random `a` value, and sends `g^a mod p` to Telegram. Bob receives `(p, g, g^a mod p)`, similarly computes `b` and `g^b mod p`, and sends the latter back (along with a truncated hash of the derived key, for some reason).

Now, normally the two sides would compute the shared key as `(g^a)^b mod p` and `(g^b)^a mod p`. Instead, the original version of MTProto computed it as

```
(g^a)^b mod p XOR nonce
```

where `nonce` was an arbitrary, supposedly random value sent by the server along with the peer’s public contribution.

This was a completely non-standard and useless addition, and all it did was let the server perform an undetected Person-in-the-Middle attack. Let’s see how.

In a normal PitM, the server negotiates two separate Diffie-Hellman sessions with Alice and Bob, who end up with different shared keys, which they could detect by comparing fingerprints.

```
Alice                     Telegram              Bob

a = random()
A = g^a mod p       ->
                        t = random()
                        T = g^t mod p ->
                                          b = random()
                                      <-  B = g^b mod p
                                          key = T^b mod p
                    <-  T
key = T^a mod p

                    T^a mod p != T^b mod p
```

With the nonce addition, however, the server could “fix” Alice’s key to match Bob’s by manipulating Alice’s nonce. The two parties would end up with the same fingerprint, and couldn’t tell that an attack happened, but the server (and no one else) would know the shared key, allowing it to decrypt all messages.

```
nonce_bob = random()
key_bob = T^b mod p  XOR  nonce_bob

nonce_alice = A^t mod p  XOR  B^t mod p  XOR  nonce_bob
key_alice = T^a mod p  XOR  nonce_alice =
  T^a mod p  XOR  (A^t mod p  XOR  B^t mod p  XOR  nonce_bob) =
  B^t mod p  XOR  nonce_bob = key_bob
```

Why do I say this addition was useless? Because it literally had no purpose! Indeed, the vulnerability was [fixed by silently removing the nonce step from the docs](https://web.archive.org/web/diff/20131220000537/20131225140924/http%3A//core.telegram.org/api/end-to-end).[4](#fn:ia) [A later API revision](https://core.telegram.org/constructor/encryptedChatRequested?layer=11) removed the nonce parameter with the caption “Improve secret chats”. All [the original API reference](https://web.archive.org/web/20131028041748/http%3A//core.telegram.org/constructor/encryptedChatRequested) said about the nonce is “Random server sequence for calculation of key”.

I never heard a plausible explanation for why the designers of MTProto went out of their way to add useless complexity to their protocol, with the only outcome of making undetectable interception possible.

**Edit (2021-01-11)**: [@asdofindia linked me on Twitter](https://twitter.com/asdofindia/status/1348491279798128641) to [an official statement by Telegram about this](https://telegram.org/blog/crowdsourcing-a-more-secure-future) that I couldn’t find anymore. It claims the nonce was there to protect clients with weak random number generators. Here’s what I had buried into a footnote when I couldn’t find a citation to attribute that explanation to Telegram:

> This doesn’t make sense for a number of reasons: 1) clients with weak randomness are likely to be toast anyway, because Telegram’s bizarro not-a-MAC relies on randomness in the payload to avoid an offline decryption oracle (there is a plaintext hash of the payload on the wire, I told you this was weird!); 2) the API also allows clients to request random bytes from the server to XOR with their secret share; and 3) defending against weak randomness by relying on a server contribution defends against everything but the server, which is the relevant attacker in the end-to-end setting. (Said another way, anyone that can intercept client-server messages can see the extra randomness, making it moot.) Non-practitioners might think this is a reasonable defense in depth, belts and suspenders kind of thing, but in cryptography engineering adding complexity to defend against scenarios that lead to compromise anyway is simply pointless.

Anyway, it’s been a while, the world is a different place now, and maybe [Hanlon’s razor](https://en.wikipedia.org/wiki/Hanlon%27s_razor) cuts deeper than I thought. I think there are better reasons not to use Telegram today than this old bug[1](#fn:default), but it’s still what I think about every time people talk about far-fetched “bugdoors”. The bar is high!

## The picture

In other news, this newsletter is going to pivot into Rome photoblogging. (Not really, if you made it this far and like cryptography engineering, you should [subscribe](https://buttondown.email/cryptography-dispatches?tag=header) or [follow me on Twitter](https://twitter.com/FiloSottile).)

![St. Peter's reflecting in the Tevere](https://assets.buttondown.email/images/ee618b89-a8fa-45a2-af01-6f9955d2c99a.jpeg)

---

1. By the way, aside from all the cryptographic weirdness and the unexplained backdoor-looking bug, the real reason you should...