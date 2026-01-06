---
title: Analysis of PPPP “encryption”
url: https://palant.info/2026/01/05/analysis-of-pppp-encryption/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-05
fetch_date: 2026-01-06T03:27:58.909049
---

# Analysis of PPPP “encryption”

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Analysis of PPPP âencryptionâ

2026-01-05
 [Security](/categories/security/)/[IoT](/categories/iot/)
 8 mins
 [0 comments](/2026/01/05/analysis-of-pppp-encryption/#comments)

My first article on the PPPP protocol already [said everything there was to say about PPPP âencryptionâ](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/#the-encryption):

* Keys are static and usually trivial to extract from the app.
* No matter how long the original key, it is mapped to an effective key thatâs merely four bytes long.
* The âencryptionâ is extremely susceptible to known-plaintext attacks, usually allowing reconstruction of the effective key from a single encrypted packet.

So this thing is completely broken, why look any further? There is at least one situation where you donât know the app being used so you cannot extract the key and you donât have any traffic to analyze either. Itâs when you are trying to [scan your local network for potential hidden cameras](https://github.com/pmarrapese/iot/tree/master/p2p/lansearch).

This script will currently only work for cameras using plaintext communication. Other cameras expect a properly encrypted âLAN searchâ packet and will ignore everything else. How can this be solved without listing all possible keys in the script? By sending all possible ciphertexts of course!

TL;DR: What would be completely ridiculous with any reasonable protocol turned out to be quite possible with PPPP. There are at most 157,092 ways in which a âLAN searchâ packet can be encrypted. Iâve opened a [pull request](https://github.com/pmarrapese/iot/pull/6) to have the PPPP device detection script adjusted.

*Note*: Cryptanalysis isnât my topic, I am by no means an expert here. These issues are simply too obvious.

#### Contents

* [Mapping keys to effective keys](#mapping-keys-to-effective-keys)
* [Redundancies within the effective key](#redundancies-within-the-effective-key)
* [ASCII to the rescue](#ascii-to-the-rescue)
* [How large is n?](#how-large-is-n)
* [How many ciphertexts is that?](#how-many-ciphertexts-is-that)
* [Understanding the response](#understanding-the-response)

## Mapping keys to effective keys

The key which is specified as part of the appâs âinit stringâ is not being used for encryption directly. Nor is it being fed into any of the established key stretching algorithms. Instead, a key represented by the byte sequence b1,b2,â¦,bnb\_1, b\_2, \ldots, b\_n is mapped to four bytes k1,k2,k3,k4k\_1, k\_2, k\_3, k\_4 that become the effective key. These bytes are calculated as follows (âxâ\lfloor x \rfloor means rounding down, â\otimes stands for the bitwise XOR operation):

k1=(b1+b2+â¦+bn)modââ256k2=(âb1+âb2+â¦+âbn)modââ256k3=(âb1Ã·3â+âb2Ã·3â+â¦+âbnÃ·3â)modââ256k4=b1âb2ââ¦âbn
\begin{aligned}
k\_1 &= (b\_1 + b\_2 + \ldots + b\_n) \mod 256\\
k\_2 &= (-b\_1 + -b\_2 + \ldots + -b\_n) \mod 256\\
k\_3 &= (\lfloor b\_1 \div 3 \rfloor + \lfloor b\_2 \div 3 \rfloor + \ldots + \lfloor b\_n \div 3 \rfloor) \mod 256\\
k\_4 &= b\_1 \otimes b\_2 \otimes \ldots \otimes b\_n
\end{aligned}

In theory, a 4 byte long effective key means 2564=4,294,967,296256^4 = 4{,}294{,}967{,}296 possible values. But that would only be the case if these bytes were independent of each other.

## Redundancies within the effective key

Of course the bytes of the effective key are not independent. This is most obvious with k2k\_2 which is completely determined by k1k\_1:

k2=(âb1+âb2+â¦+âbn)modââ256=â(b1+b2+â¦+bn)modââ256=âk1modââ256
\begin{aligned}
k\_2 &= (-b\_1 + -b\_2 + \ldots + -b\_n) \mod 256\\
&= -(b\_1 + b\_2 + \ldots + b\_n) \mod 256\\
&= -k\_1 \mod 256
\end{aligned}

This means that we can ignore k2k\_2, bringing the number of possible effective keys down to 2563=16,777,216256^3 = 16{,}777{,}216.

Now letâs have a look at the relationship between k1k\_1 and k4k\_4. Addition and bitwise XOR operations are very similar, the latter merely ignores carry. This difference affects all the bits of the result but the lowest one, no carry to be considered here. This means that the lowest bits of k1k\_1 and k4k\_4 are always identical. So k4k\_4 has only 128 possible values for any value of k1k\_1, bringing the total number of effective keys down to 256â256â128=8,388,608256 \cdot 256 \cdot 128 = 8{,}388{,}608.

And thatâs how far we can get considering only redundancies. It can be shown that a key can be constructed resulting in any combination of k1k\_1 and k3k\_3 values. Similarly, it can be shown that any combination of k1k\_1 and k4k\_4 is possible as long as the lowest bit is identical.

## ASCII to the rescue

But the keys we are dealing with here arenât arbitrary bytes. These arenât limited to alphanumeric characters, some keys also contain punctuation, but they are all invariably limited to the ASCII range. And that means that the highest bit is never set in any of the bib\_i values.

Which in turn means that the highest bit is never set in k4k\_4 due to the nature of the bitwise XOR operation. We can once again rule out half of the effective keys, for any given value of k1k\_1 there are only 64 possible values of k4k\_4. We now have 256â256â64=4,194,304256 \cdot 256 \cdot 64 = 4{,}194{,}304 possible effective keys.

## How large is n?

Now letâs have a thorough look at how k3k\_3 relates to k1k\_1, ignoring the modulo operation at first. We are taking one third of each byte, rounding it down and summing that up. What if we were to sum up first and round down at the end, how would that relate? Well, it definitely cannot be smaller than rounding down in each step, so we have an upper bound here.

âb1Ã·3â+âb2Ã·3â+â¦+âbnÃ·3ââ¤â(b1+b2+â¦+bn)Ã·3â
\lfloor b\_1 \div 3 \rfloor + \lfloor b\_2 \div 3 \rfloor + \ldots + \lfloor b\_n \div 3 \rfloor \leq \lfloor (b\_1 + b\_2 + \ldots + b\_n) \div 3 \rfloor

How much smaller can the left side get? Each time we round down this removes at most two thirds, and we do this nn times. So altogether these rounding operations reduce the result by at most nâ2Ã·3n \cdot 2 \div 3. This gives us a lower bound:

â(b1+b2+â¦+bnânâ2)Ã·3ââ¤âb1Ã·3â+âb2Ã·3â+â¦+âbnÃ·3â
\lceil (b\_1 + b\_2 + \ldots + b\_n - n \cdot 2) \div 3 \rceil \leq \lfloor b\_1 \div 3 \rfloor + \lfloor b\_2 \div 3 \rfloor + \ldots + \lfloor b\_n \div 3 \rfloor

If nn is arbitrary these bounds donât help us at all. But nn isnât arbitrary, the keys used for PPPP encryption tend to be fairly short. Letâs say that we are dealing with keys of length 16 at most which is a safe bet. If we know the sum of the bytes these bounds allow us to narrow down k3k\_3 to â16â2Ã·3â=11\lceil 16 \cdot 2 \div 3 \rceil = 11 possible values.

But we donât know the sum of bytes. What we have is k1k\_1 which is that sum modulo 256, and the sum is actually iâ256+k1i \cdot 256 + k\_1 where ii is some nonnegative integer. How large can ii get? Remembering that we are dealing with ASCII keys, each byte has at most the value 127. And we have at most 16 bytes. So the sum of bytes cannot be higher than 127â16=2032127 \cdot 16 = 2032 (or 7F0 in hexadecimal). Consequently, ii is 7 at most.

Letâs write down the bounds for k3k\_3 now:

â(iâ256+k1ânâ2)Ã·3ââ¤jâ256+k3â¤â(iâ256+k1)Ã·3â
\lceil (i \cdot 256 + k\_1 - n \cdot 2) \div 3 \rceil \leq j \cdot 256 + k\_3 \leq \lfloor (i \cdot 256 + k\_1) \div 3 \rfloor

We have to consider this for eight possible values of ii. Wait, do we really?

Once we move into modulo 256 space again, the iâ256Ã·3i \cdot 256 \div 3 part of our bounds (which is the only part dependent on ii) will assume the same value after every three ii values. So only three values of ii are really relevant, say 0, 1 and 2. Meaning that for each value of k1k\...