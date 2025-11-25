---
title: Counter Galois Onion: Improved encryption for Tor circuit traffic
url: https://blog.torproject.org/introducing-cgo/
source: Tor Project blog
date: 2025-11-24
fetch_date: 2025-11-25T03:13:26.034183
---

# Counter Galois Onion: Improved encryption for Tor circuit traffic

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Counter Galois Onion: Improved encryption for Tor circuit traffic

by [nickm](/author/nickm)
| November 24, 2025

![](/introducing-cgo/lead.png)

It's always a good day when we can talk about cryptography.
Especially when we are sunsetting one of the oldest and most important
encryption algorithms in Tor
and replacing it with a research-backed new design,
called Counter Galois Onion.

This overhaul will defend users against a broader class of online attackers
(described below), and form the basis for more encryption work in the future.

## Which cryptography are we talking about here?

The algorithm in question is Tor's *relay encryption*.
While Tor uses the standard TLS protocol
for communication between relays,
and between clients and relays,
it needs a specialized algorithm for encrypting user data as it traverses
multiple relays in a circuit.[1](#fn-nested)

That's the relay encryption algorithm.
The client shares a symmetric key with each relay on its circuit,
and encrypts an outgoing message, or "relay cell" with each one of those keys.
Each relay can remove a single layer of encryption,
until the client's cell reaches the exit relay.

Of course, we need to make sure that the data isn't modified
on the way from the client.
For that, we include a cryptographic digest in the cell.
The digest covers not only the cell itself,
but also *all previous cells sent through the circuit*
(to prevent re-ordering)
and another secret shared key
(to make the digest unpredictable).

So with the digest added, clients behave as follows:
they calculate and set the digest,
then they use a stream cipher
(AES-128-CTR in Tor's case) multiple times
to encrypt the cell for each relay.

If we simplify *a lot*,
then a relay cell looks a little like this:

| Field | Width |
| --- | --- |
| Zero | 2 bytes |
| Digest | 4 bytes |
| Other stuff | ... |

The "zero" field is there so that nodes other than the exit
can avoid checking the digest:
If a relay gets a cell with a value other than zero,
then it can tell that it isn't the recipient of that cell,
so it doesn't need to check the digest:
it just decrypts the cell and forwards it to the next relay.

When we designed this algorithm,
we didn't give it a name.
Now that we're replacing it,
it helps to have some way to identify it,
so we're calling it "tor1".

![A diagram of the Tor1 encryption algorithm](./cgo-tor1.svg)

Figure 1. The tor1 encryption algorithm, as used at a middle layer.

The input is a message M.
A counter CTR is expanded via a psueodrandom function (PRF, instantiated with
AES-128-CTR), to produce a stream of bytes.
These bytes are xored with M to produce a ciphertext C.

![A diagram of the Tor1 encryption algorithm](./cgo-tor1-originate.svg)

Figure 2: The tor1 encryption algorithm, as used to originate a message.

The message M is mixed with the hash state HS, and a portion of the digest
is appended to the message. The whole thing is then xored with the PRF
(AES-128-CTR) to produce our ciphertext C.

### Wait, that design looks funny!

Yeah, you wouldn't build it that way nowadays, would you?
That's why we're replacing it.

In today's world of [high-quality online courses](https://www.coursera.org/learn/crypto) and
[excellent introductory material](https://nostarch.com/serious-cryptography-2nd-edition),
it's easy to forget the [general state](http://www.faqs.org/faqs/cryptography-faq/)
of accessible [cryptography resources](https://www.schneier.com/books/applied-cryptography/)
when Tor was getting started.
[AES was brand new](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process),
and [authenticated](https://eprint.iacr.org/2001/045) [encryption](https://homes.cs.washington.edu/~yoshi/papers/SSH/ssh-acmccs.pdf)
as a separate [field of study](https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/proposed-modes/eax/eax-spec.pdf)
had just started to emerge.

Existing designs weren't suitable for Tor's needs.
The original [onion routing paper](https://www.onion-router.net/Publications/IH-1996.pdf)
didn't specify a means for authentication.
Designs like [mixmaster](https://mixmaster.sourceforge.net/) and [mixminion](https://www.mixminion.net/)
were optimized for larger message sizes,
and required a separate full digest
for every *possible* layer of encryption.
(For example, Mixmaster supported up to 20 remailers,
so had to reserve space for 20 digests (and other stuff)
in *every message*.)

Some of the "weird things" in the current tor1 design
are outdated, but not *awful*;
others are things that are more valuable to resolve.

### So, what *are* the problems with the tor1 design?

There are a few. First the big one:

#### Problem 1: Tagging attacks

Tagging attacks enable an active adversary to trace traffic
by modifying it in one place on the network,
and observing predicatable changes in another.
Even when tagging attacks don't succeed immediately,
their side effects can give the attacker more and more
opportunities to retry.

> This is the most important attack we're solving with CGO.
> Even without the other problems below,
> this one would be worth fixing on its own.

The main version of this attack arises
because tor1's use of AES-CTR encryption
with no hop-by-hop authentication
means that the relay encryption is [malleable](https://en.wikipedia.org/wiki/Malleability_%28cryptography%29).
Since [counter mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)) derives its ciphertext C
by XORing a secret key stream S
with the plaintext P (C = S â P),
an attacker who can XOR their own pattern M in to the ciphertext
will produce C' = (S â P) â M = S â (P â M) â that is,
a valid encryption of (P â M).

An attacker can use this attack
to ensure that they control both ends of the circuit.
They XOR a pattern onto a cell at one end,
and then see if any garbled cells at the other end
become clear when whey remove that same pattern.
Any circuits with an honest endpoint will fail (and not be deanonymized),
but the client will retry them until they eventually
choose a malicious endpoint.

If the attacker chooses a known-plaintext portion of the relay cell for their marker
(such as the header or slack zero space),
then they can use their marker to communicate an identifier across the circuit,
by retrieving it at the end:

```
 M = (P â M) â P.
```

M can then be used to transmit an IP address or unique identifier for the user.

In comparison to probabilistic traffic correlation,
this attack provides definite results immediately,
with a strength multiplier:
it also allows the attacker to ensure that all the traffic
they successfully carry is fully deanonymized,
before the circuit is used for any application traffic at all.

The downside for the attacker is that the resulting failure rate of circuits
can be detected by the client.
Currently, Tor clients emit log notices and warnings when circuit failure rates
are excessively high.
Unfortunately, as vigilant users have noticed,
when the DDoS attacks on Tor become severe, these detectors give false alarms.

This class of attacks
(where an adversary is able to abuse the Tor Protocol
to transmit information between relays *before* application activity)
is known as [Internal Covert Channel attacks](https://spec.torproject.org/proposals/344-protocol-info-leaks.html#11-highly-severe-internal-covert-channel-vectors).
Tor is in the process of [updating its threat model](https://gitlab.torproject.org/tpo/core/torspec/-/issues/318)
to cover these attack vectors explicitly,
along with [two other categories](https://spec.torproject.org/proposals/344-protocol-info-leaks.html) of attack vectors.

#### Problem 2: Forward secrecy ...