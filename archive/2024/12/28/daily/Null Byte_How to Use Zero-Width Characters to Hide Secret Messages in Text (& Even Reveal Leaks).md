---
title: How to Use Zero-Width Characters to Hide Secret Messages in Text (& Even Reveal Leaks)
url: https://null-byte.wonderhowto.com/how-to/use-zero-width-characters-hide-secret-messages-text-even-reveal-leaks-0198692/
source: Null Byte
date: 2024-12-28
fetch_date: 2025-10-06T19:43:39.188502
---

# How to Use Zero-Width Characters to Hide Secret Messages in Text (& Even Reveal Leaks)

![Header Banner](https://assets.content.technologyadvice.com/null_byte_3840x1800_e4f3abce80.webp)

[![Null Byte Logo](https://assets.content.technologyadvice.com/Logos_Null_Byte_white_b3593aed94.webp)](https://null-byte.wonderhowto.com/)

Null Byte

[WonderHowTo](https://www.wonderhowto.com/)  [Gadget Hacks](https://www.gadgethacks.com/)  [Next Reality](https://next.reality.news/)  [Null Byte](https://null-byte.wonderhowto.com/)

[![wonderhowto.mark.png](https://assets.content.technologyadvice.com/wonderhowto_mark_facd6be46b.webp)](https://null-byte.wonderhowto.com/)

[Cyber Weapons Lab](https://null-byte.wonderhowto.com/collection/cyber-weapons-lab/)  [Forum](https://null-byte.wonderhowto.com/forum)  [Metasploit Basics](https://null-byte.wonderhowto.com/how-to/metasploit-basics/)  [Facebook Hacks](https://null-byte.wonderhowto.com/how-to/facebook-hacks/)  [Password Cracking](https://null-byte.wonderhowto.com/how-to/password-cracking/)  [Top Wi-Fi Adapters](https://null-byte.wonderhowto.com/how-to/buy-best-wireless-network-adapter-for-wi-fi-hacking-2019-0178550/)  [Wi-Fi Hacking](https://null-byte.wonderhowto.com/how-to/wi-fi-hacking/)  [Linux Basics](https://null-byte.wonderhowto.com/how-to/linux-basics/)  [Mr. Robot Hacks](https://null-byte.wonderhowto.com/how-to/mr-robot-hacks/)  [Hack Like a Pro](https://null-byte.wonderhowto.com/how-to/hack-like-a-pro/)  [Forensics](https://null-byte.wonderhowto.com/how-to/forensics/)  [Recon](https://null-byte.wonderhowto.com/how-to/recon/)  [Social Engineering](https://null-byte.wonderhowto.com/how-to/social-engineering/)  [Networking Basics](https://null-byte.wonderhowto.com/how-to/networking-basics/)  [Antivirus Evasion](https://null-byte.wonderhowto.com/how-to/evading-av-software/)  [Spy Tactics](https://null-byte.wonderhowto.com/how-to/spy-tactics/)  [MitM](https://null-byte.wonderhowto.com/how-to/mitm/)  [Advice from a Hacker](https://null-byte.wonderhowto.com/how-to/advice-from-a-hacker/)

[YouTube](https://www.youtube.com/channel/UCgTNupxATBfWmfehv21ym-g/)  [X](https://x.com/NullByte)

Follow Us

Search

  Close Search

Search    Menu

[how to](https://null-byte.wonderhowto.com/how-to/)

# How to Use Zero-Width Characters to Hide Secret Messages in Text (& Even Reveal Leaks)

![](https://assets.content.technologyadvice.com/thumbnail_Logos_Null_Byte_color_light_8d3c214a02.webp)

By [Hoid](https://creator.wonderhowto.com/hoid/)

May 29, 2020, 07:00 PM

May 29, 2020, 10:59 PM

[Cyber Weapons Lab](https://null-byte.wonderhowto.com/collection/cyber-weapons-lab/)[Privacy & Security](https://www.gadgethacks.com/collection/privacy-security/)

![Secret Message](https://assets.content.technologyadvice.com/637263493835297420_24844f6006.webp)

You may be familiar with [image-based](https://null-byte.wonderhowto.com/how-to/steganography-hide-secret-data-inside-image-audio-file-seconds-0180936/) or [audio-based steganography](https://null-byte.wonderhowto.com/how-to/hacks-mr-robot-hide-data-audio-files-0164136/), the art of hiding messages or code inside of pictures, but that's not the only way to conceal secret communications. With zero-width characters, we can use text-based steganography to stash hidden information inside of plain text, and we can even figure out who's leaking documents online.

Image- and audio-based steganography has been covered [several](https://null-byte.wonderhowto.com/how-to/steganography-hide-secret-data-inside-image-audio-file-seconds-0180936/)[times](https://null-byte.wonderhowto.com/how-to/introduction-steganography-its-uses-0155310/)[on Null Byte](https://null-byte.wonderhowto.com/how-to/hacks-mr-robot-hide-data-audio-files-0164136/), which involves changing the least significant digit of individual pixels on a photo or audio file. While plain text characters don't have a least significant digit that we can manipulate in the same fashion, we can still use [Unicode](https://unicode.org/standard/WhatIsUnicode.html) to our advantage. Unicode is the standardized encoding format for text, specifically, UTF-8, that most web browsers use for text.

* **Don't Miss: [How to Hide Payloads Inside Photo Metadata](https://null-byte.wonderhowto.com/how-to/hacking-macos-hide-payloads-inside-photo-metadata-0196815/)**

Because Unicode needs to support almost all written languages in the world, there are some counterintuitive characters such as [zero-width non-joiners](https://en.wikipedia.org/wiki/Zero-width_non-joiner) and [zero-width spaces](https://en.wikipedia.org/wiki/Zero-width_space). For example, the zero-width non-joiner is used in languages such as Persian, where it's needed to display the correct typographic form of words.

![How to Use Zero-Width Characters to Hide Secret Messages in Text (& Even Reveal Leaks)](https://assets.content.technologyadvice.com/637218414490213484_d112822e07.webp)

In that image, notice how the line is no longer continuous? That's what is meant by a non-joiner. However, for our purposes, the most important part about these character types is that they're not needed in English and aren't normally displayed.

That fact allows us to pick two arbitrary zero-width characters and designate them as one and zero. We can then hide any message in plain text by splitting it into single characters and encoding it in binary with zero-width characters acting as the ones and zeros. The best practice is to add the zero-width binary code in the spaces between words. Otherwise, spellcheckers tend to think the word is misspelled.

```
Plain âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âï»¿âtext, nothing to see here
```

To see the concept in action, copy the text "plain text" below and paste it an [online zero-width detention tool](https://www.umpox.com/zero-width-detection/) to see what it says.

## What Can I Use It For?

The ability to hide messages in otherwise ordinary-looking text is useful on its own, but what makes the technique really nifty is the fact that it also...