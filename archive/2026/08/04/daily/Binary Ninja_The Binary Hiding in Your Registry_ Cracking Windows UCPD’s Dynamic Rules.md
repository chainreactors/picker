---
title: The Binary Hiding in Your Registry: Cracking Windows UCPD’s Dynamic Rules
url: https://binary.ninja/2026/08/04/ucpd-dynamic-rules.html
source: Binary Ninja
date: 2026-08-04
fetch_date: 2026-08-05T04:58:18.226799
---

# The Binary Hiding in Your Registry: Cracking Windows UCPD’s Dynamic Rules

[Skip to main content](#main-content)

[![Binary Ninja](/images/binary-ninja-wordmark-light-2tone.svg)](/)

Features

[Features Overview](/features/)
[Enterprise](/enterprise/)

[Sidekick](https://sidekick.binary.ninja)
[Portal](https://portal.binary.ninja/dashboard)
[Training](/training/)

Support

[Support Overview](/support/)
[Extended Support](/support/extended.html)
[Documentation](/support/#documentation)
[License/Installer Recovery](/recover/)
[Renew Current License](/renew/)
[Slack Signup](https://slack.binary.ninja/)
[FAQ](/faq/)
[Sponsorship Information](/sponsorship/)
[Contact Us](/support/)

[Blog](/blog/)
[Gear](https://shop.binary.ninja)

[Try For Free](/free)
[Purchase](/purchase)

Binary Ninja is [10 years old](/10years/)! Catch up on everything from our tenth anniversary.

[Binary Ninja Blog](/blog/)

# The Binary Hiding in Your Registry: Cracking Windows UCPD's Dynamic Rules

By [Xusheng Li](https://github.com/xusheng6)
 2026-08-04

Is Microsoft shipping a hidden binary to your computer â inside the registry?

A few weeks ago I was watching [a YouTube video](https://www.youtube.com/watch?v=xQUYh4iKsB0) that covered my earlier
research on the [UCPD driver](/2025/03/25/default-browser-upcd.html), and for a split second I saw a registry key that I
have been searching for an example of for some time. I contacted the videoâs author and obtained the key from his
machine. It was Base64 encoded and to my surprise, once I decoded it, it started with `MZ`.

Sure enough, itâs a valid Windows executable sitting inside a registry key. This post is the story of both taking it apart
as well as the bug I found that means the whole mechanism is dead anyway.

## A Quick Refresher on UCPD

If you have not read my [earlier post on UCPD](/2025/03/25/default-browser-upcd.html), here is the short version.

UCPD stands for User Choice Protection Driver and its entire job is to protect your default browser choice. On Windows,
setting the default browser used to be a matter of writing a registry key with the correct hash. UCPD put a stop to that:
now, only the Windows Settings app is allowed to do it and the driver specifically blocks a list of Microsoftâs own
utilities like `reg.exe`, `powershell.exe`, `rundll32.exe` that could otherwise be tricked into modifying the setting.

Browser vendors (and spyware/adware authors!) were not thrilled. They found workarounds, Microsoft tightened the driver,
they found new workarounds, and so on. I covered that cat-and-mouse game in the blog post above and in a [lightning talk
at RE//verse 2025](https://youtu.be/TheUdURzFjI) already, so I wonât rehash it here.

There was one loose end from that research, though. Buried in the driver is a code path that loads some configuration
from this registry key:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UCPD\DR
```

Unfortunately, I couldnât analyze it because on every machine and VM I have, the key is empty.

## A PE with No Code

We can see from the FlyTech video
[âMicrosoft Added This Driver to Windows and Said Nothingâ](https://youtu.be/xQUYh4iKsB0?t=381), that on his
machine, `DR` had a value. He read `DR` as âDisaster Recovery,â which, as weâll see below, is probably not the case.

FlyTech is based in Europe, which could explain why he has the key set. The entire UCPD saga grew out of the EU browser
choice rules, so it would not be surprising if Microsoft only pushes these policy blobs to European users. To be clear
though, this is only a guess.

As mentioned earlier, after we Base64 decode it, it is a PE file.

So: is Microsoft running a binary on your machine behind your back?

No. And that relates to the first interesting thing about this file. I opened it in Binary Ninja and there is no
code in it at all. This is not a parsing bug â it only has a tiny `.rdata` section containing
what looks like encrypted data, plus an Authenticode certificate at the end of the file.

```
>>> list(bv.functions)
[]
```

But why wrap data in a PE at all, if nothing is ever going to execute it?

Presumably, by packaging the payload as a signed PE, Microsoft gets to reuse the entire Authenticode code-signing
infrastructure for free and the driver can verify that only Microsoft could have produced this blob before it acts on
the contents. This is actually a very sensible design decision. You really donât want a kernel driver consuming policy
from a registry key that any administrator could overwrite.

Now that I have both halves of the puzzle â the encrypted blob and the code that decrypts it â we can finally figure
out what it does.

## Reversing the Loader

This driver is quite easy to reverse because every stage logs an ETW event with a descriptive tag of the action.
Reading top to bottom, `process_DR` does exactly what you would expect:

| # | log tag | what it does |
| --- | --- | --- |
| 1 | `Base64Decode` | REG\_SZ string to PE bytes |
| 2 | `ParsePEFormat` | locate the `.rdata` blob |
| 3 | `CalculatePEHashInMem` | hash the in-memory PE |
| 4 | `CertificateVerify` | signature gate â only Microsoft-signed policy is accepted |
| 5 | `DecryptData` | decrypt the blob |
| 6 | `DispatcherConfig` | parse and dispatch the decrypted records |

![The driver narrating its own pipeline](/blog/images/ucpd-dr/process-dr-pipeline.png)

Stage 5 is the one I cared about. I asked [Sidekick](https://sidekick.binary.ninja/), our AI assistant, to reverse the
decryption function. Its answer: this is a custom XOR stream cipher. A hash function derives a set of seeds from the
key, those seeds generate a keystream, and the keystream gets XORed against the ciphertext. Nothing exotic.

It also renamed everything as it went: `expand_key_state`, `derive_keystream`, and the two mixing functions. That turned
the wall of `sub_140004xxx` calls into something you can actually read. I had a quick glance at the code and it seemed
correct.

![The code after Sidekick markup](/blog/images/ucpd-dr/code-after-sidekick-markup.png)

## Reimplementing the Cipher

Then I had Sidekick re-implement the whole thing in Python.

Before I could run the code, I noticed that the cipher needs a 32-byte key, but the function doesnât have one baked in.
Thus, it has to come from the data itself.

Looking at the start of `.rdata`, it is not hard to see that it begins with a `u32` schema version of `0x3ec`, followed
by a `u32` of `0x238`, which looks exactly like the length of the ciphertext. If I take the next `0x20` bytes as the encryption key, the
remaining bytes in the section are exactly `0x238`. It all checks out! The layout is shown below:

![The blob layout in .rdata](/blog/images/ucpd-dr/rdata-layout.png)

I handed this to Sidekick and asked it to decrypt the blob. However, despite my high expectations, the result was
garbage:

```
00000000: fe 2a 56 4a e3 ff fb 5b 9f 78 91 bd 2b d0 5c 59  .*VJ...[.x..+.\Y
00000010: 0d 92 1f e9 10 c0 44 8f 0a 2d c5 2d c8 b9 54 7d  ......D..-.-..T}
00000020: be bd 53 65 68 2b b4 08 63 f0 69 89 2e 4c a0 7a  ..Seh+..c.i..L.z
00000030: 2d ca 1c 50 75 00 80 09 f3 ef 41 8e 78 67 7f 49  -..Pu.....A.xg.I
00000040: f5 0a 1e f2 b1 49 05 b5 8e b2 51 2d 27 44 0f 1c  .....I....Q-'D..
00000050: 36 6f bc 39 8f cb 60 49 ee 1c 46 0e 16 a2 b1 91  6o.9..`I..F.....
00000060: 92 40 27 84 64 02 92 41 a2 ec a8 dc d1 4f 54 3f  .@'.d..A.....OT?
```

My first impression was that Sidekick blew it. So I asked Claude Code to redo it with Binary Ninjaâs
[MCP server](https://dev-docs.binary.ninja/guide/mcp.html).
I deliberately only gave it the binary instead of the analysis database, so it could not be affected by Sidekickâs
renaming or type information.

This time it wrote another script, which produced the *exact same* garbage output. When challenged, it even brought
[Unicorn](https://www.unicorn-engine.org/) in and emulated the code to argue that it had done everything correctly.

The chances of two AIs getting it wrong in exactly the same way seemed quite low, so I suspect...