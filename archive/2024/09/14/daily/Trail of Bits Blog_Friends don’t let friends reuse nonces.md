---
title: Friends don’t let friends reuse nonces
url: https://blog.trailofbits.com/2024/09/13/friends-dont-let-friends-reuse-nonces/
source: Trail of Bits Blog
date: 2024-09-14
fetch_date: 2025-10-06T18:27:05.914306
---

# Friends don’t let friends reuse nonces

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Friends don’t let friends reuse nonces

Joe Doyle

September 13, 2024

[cryptography](/categories/cryptography/)

If you’ve encountered cryptography software, you’ve probably heard the advice to never use a nonce twice—in fact, that’s where the word **nonce** (**n**umber used **once**) comes from. Depending on the cryptography involved, a reused nonce can reveal encrypted messages, or even leak your secret key! But common knowledge may not cover every possible way to accidentally reuse nonces. Sometimes, the techniques that are supposed to prevent nonce reuse have subtle flaws.

This blog post tells a cautionary tale of what can go wrong when implementing a relatively basic type of cryptography: a bidirectional encrypted channel, such as an encrypted voice call or encrypted chat. We’ll explore how more subtle issues of this type can arise in a network with several encrypted channels, and we’ll describe a bug we discovered in a client’s threshold signature scheme. In that implementation, none of the parties involved ever used the same nonce twice. However, because they used the same sequence of nonce values, two different senders could accidentally use the same nonce as each other. An attacker could have used this issue to tamper with messages, or make honest parties appear malicious.

![](/img/wpdump/335a6210993bcaf6632ff9912d3ed4df.png)

Figure 1: Don’t let your drunk friend drive, or use your nonce!

### How we make encrypted channels

Encrypting messages—making the *meaning* of a message hidden, even to a third party that has full access to the *content* of a message—is probably the oldest activity we’d recognize as “cryptography.” The core structure of today’s message encryption stretches back at least to the polyalphabetic ciphers of the 1500s, and goes as follows:

To encrypt:

* Take the secret message and separate it into regular-sized sections (or “blocks”). The overall data in each section is treated as a single “symbol.”
* Substitute each symbol with a different symbol, depending on the secret, the position in the message, and possibly also on previous symbols in the message.
* Send the now-encrypted message.

To decrypt:

* Take the encrypted message, and separate it into blocks.
* Substitute each symbol using the reverse of the encryption procedure, again using the secret, the position, and possibly the previous symbols.
* Read the now-decrypted message.

The security of this scheme relies on third parties being unable to infer data about the symbol-substitution procedure just by looking at the encrypted data.

Historically, many ciphers have been broken by observing patterns within individual encrypted messages (Alan Turing’s Banburismus technique, which broke the Nazi Navy’s Enigma encryption, is a famous example).

Modern ciphers are designed to completely eliminate these patterns within messages, if properly used. First, our substitution alphabets are *much* larger—two commonly used stream ciphers, AES-CTR and ChaCha20, use block sizes of 128 and 256, respectively. That means the alphabets have 2128 and 2256 symbols, respectively. Next, there are rules used to ensure that every symbol in a message gets a different substitution table. If you treat every symbol in the same way, you risk revealing patterns in the underlying message, as in the classic ECB penguin!

![](/img/wpdump/9358ad591eb8a93ff72ea598fc3a0933.png)

Figure 2: The original image ([source](https://en.wikipedia.org/wiki/File%3ATux.svg))

![](/img/wpdump/d4801b71a45f2c4fb5e5d3fe270274ac.png)

Figure 3: The image after encryption with ECB mode ([source](https://en.wikipedia.org/wiki/File%3ATux_ECB.png))

Finally, and most importantly for this story, you need to ensure that every message is treated differently—which is where nonces come in.

### Numbers, but only once

The AES-CTR and ChaCha20 stream ciphers are both “counter-mode” stream ciphers. Counter-mode ciphers use a very simplistic type of substitution table: map the ith block, with the value `x_i to x_i XOR F(i)`, where F is a a so-called “pseudorandom function” derived from the secret key1. To see how this works, let’s start again with our trusty image of Tux, and an image generated from AES-CTR’s pseudorandom function:

![](/img/wpdump/34e27bb2d42f6b63a32ae9d104e1bc1a.png)

Figure 4: The original image again

![](/img/wpdump/8941498074bae8229f7e91f3cd7f1f4d.png)

Figure 5: Image generated from AES-CTR’s pseudorandom function

When we XOR the pseudorandom image with Tux, Tux vanishes in the noise:

![](/img/wpdump/67272e70cf9cf421ac38c70097f1e0d4.png)

Figure 6: XOR of the pseudorandom image with Tux

It might not be obvious that this actually still has Tux in it—but if you closely watch the animation below, you can see the outline of Tux as it switches from the original noise to the encrypted version of Tux:

![](/img/wpdump/c244214fc349f9abc6f68c4df8f4d32a.gif)

Figure 7: Animation of mixing Tux with the AES-CTR output; notice the visible outline of Tux

And if we XOR this with the noise again, Tux returns!

![](/img/wpdump/34e27bb2d42f6b63a32ae9d104e1bc1a.png)

Figure 8: Tux visible again after XOR

This lets us both encrypt and decrypt data, so long as you know the function F used to generate the pseudorandom data.

But if we aren’t careful, we might reveal too much. Let’s start with a different image, but the same noise:

![](/img/wpdump/2b5a536aee29425b9d8404c7f24208df.png)

Figure 9: A different example: Beastie ([source](https://en.wikipedia.org/wiki/BSD_Daemon#/media/File:Daemon-phk.svg))

![](/img/wpdump/8941498074bae8229f7e91f3cd7f1f4d.png)

Figure 10: Same noise

If we XOR the image and the noise together, Beastie, like Tux, vanishes:

![](/img/wpdump/d4d74fbcaa4894a516f945e62a5ac067.png)

Figure 11: Beastie disappears in noise

But if we now XOR these two encrypted messages, suddenly we can tell what they originally were!

![](/img/wpdump/8719cc4ebb22783d5af6fcdb3799fa88.png)

Figure 12: Beastie and Tux reappear when the two encrypted messages are XORed

What went wrong? Well, we used the *exact* same noise in each encrypted message. In real encrypted channels, the pseudorandom function F we use to generate our noise gets an extra parameter, called the “nonce,” or “number used once.” As the name suggests, that number should be unique for each message. If you ever reuse a nonce, a third party who sees two encrypted messages can learn the XOR of the plaintext. However, so long as you never reuse a nonce, a good pseudorandom function will generate completely different noise given two different nonces2. By tweaking the above experiment to use the nonce `1` for Tux and the nonce `2` for the Beastie, the XOR of the two messages is still incomprehensible noise:

![](/img/wpdump/175d0cf5790aaa937d3307a112f1d660.png)

Figure 13: Encrypted Tux

![](/img/wpdump/4614a0d26d786e99c4b3c2bc022bee28.png)

Figure 14: Encrypted Beastie

![](/img/wpdump/176dd908580f00f59467dfc29fdf5916.png)

Figure 15: XOR of the previous two images

Which brings us to the bug.

### The bug

Our client was implementing a threshold signature scheme. The signing process in a threshold signature scheme requires a lot of communication between all parties. Some communication is broadcast, and some is peer-to-peer. For security, the peer-to-peer communication needs to be both private and tamper-resistant, so the implementation uses an authenticated encryption scheme called ChaCha20-Poly1305, which combines the ChaCha20 stream cipher with Poly1305, a Polynomial Message Authentication Code.

Let’s consider a three-party example with Alice, Bob, and Carol. To create her peer-to-peer channels, Alice establishes two different shared secrets, s\_B and s\_C, with Bob and with Carol respectively, via Diffie-Hellman key exchange. Then, Alice sets up a global “nonce counter”: every time Alice sends a message, she send...