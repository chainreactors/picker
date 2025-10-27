---
title: Diving into RFID Protocols with Flipper Zero
url: https://blog.flipper.net/rfid/
source: Instapaper: Unread
date: 2023-08-04
fetch_date: 2025-10-04T12:04:15.384747
---

# Diving into RFID Protocols with Flipper Zero

[![Flipper Blog](https://blog.flipper.net/content/images/2022/07/orange_text_transpar-2.png)](https://blog.flipper.net)

* [Home](https://flipperzero.one/)
* [Shop](https://shop.flipperzero.one/)
* [Docs](https://docs.flipper.net/)
* [Downloads](https://flipperzero.one/downloads)
* [Community](https://flipperzero.one/community)

Subscribe to notifications of new posts:

You're subscribed

Oops! Please try again

Subscribe

[Classroom](https://blog.flipper.net/tag/classroom/)

# Diving into RFID Protocols with Flipper Zero

* [![Anna Oake](/content/images/size/w100/2022/04/3I6A4842_F-copy.jpg)](/author/koteeq/)

#### [Anna Oake](/author/koteeq/)

Sep 22, 2021

![Flipper Zero RFID protocols 13.56 MHz and 125 kHz](/content/images/size/w2000/2021/09/Untitled-183831--1-.jpg)

RFID is a contactless radio-tag technology. It is quite common and you may see it in a lot of places: intercoms, bank cards, public transport passes, office passes, they are used to track domestic animals, for toll collection, etc. The two main RFID tag types are high frequency and low frequency.

* **Low-Frequency tags** (125 kHz) — work at a higher range. Despite being insecure and dumb, they are still used in primitive access control systems: in building intercoms, offices, sports facilities, museums.
* **High-Frequency tags** (13.56 MHz) — have a lower effective range when compared with the low-frequency ones but have more complex protocols. They support encryption, authentication, and cryptography. These tags are commonly used in contactless bank cards, to pay for public transport, and in high-security access control systems.

Here we will compare these two types of tags, take a look at the main protocols and learn to work with them using Flipper Zero — we will read, emulate, save and clone them. You will see how you will be able to save your office, sports, home whatever RFID keys you have and we'll take a glimpse at what Flipper can read from a bank card.

## How RFID Tags Work

![](https://habrastorage.org/webt/vz/f6/_a/vzf6_a87tdtfu2xyk33nosvk-ms.gif)

RFID chip turns on when it receives power from the reader's RF field

Most RFID tags are passive tags with no internal power source. The chip inside is completely turned off until the tag is exposed to a reader's electromagnetic field. As soon as it comes within range, the tag's antenna begins absorbing energy from the reader's EM field and the chip receives power. The chip then turns on and begins communicating with the reader. It's worth mentioning, that a tag's antenna is tuned to a specific frequency, so the tag can only activate when it is inside a suitable electromagnetic field.

## RFID Tag Types

On the outside RFID tags can be quite different: cards both fat or thin, key fobs, bracelets, coins, rings, or even stickers. Judging by the visuals alone it's almost impossible to distinguish the frequency or protocol the tag operates on.

![](https://habrastorage.org/r/w1560/webt/aa/m6/jx/aam6jxqe9ktqlldlvrvr1yhrjwy.jpeg)

On the outside RFID tags can be quite different

Quite often manufacturers use similar plastic cases for different types of RFID fobs operating on different frequencies. Two absolutely visually similar tags might be totally different inside. It is worth considering when you try to distinguish the type of tag you have. In this article, we will be looking at the two most popular types of RFID tags that are used in access control systems. Flipper Zero supports both their frequencies.

> There is a variety of RFID protocols working on other frequencies. UHF for example uses the 840-960 MHz range. They are used for tracking assets in warehouses, paying for toll roads, tracking wild animals during their migration and so forth. These tags may have a battery and work from a couple of meters to kilometers. They are quite rare though, and you may not encounter them unless you go looking for them specifically. We will omit them entirely for the purpose of this article.

### 125 kHz & 13.56 MHz – Which is Which?

The easiest way to understand what range of the RFID tag is operating on is to look at the antenna. Low-frequency tags (125 kHz) have an antenna made of a very thin wire, literally thinner than a hair. But such antennas have a large number of turns, therefore, such an antenna looks like a solid piece of metal. High-frequency cards (13.56 MHz) have a significantly smaller number of thicker turns, with visible gaps between them.

![](https://habrastorage.org/r/w1560/webt/hi/dc/ki/hidckijb-wsscmuqutxmkeeuama.jpeg)

With enough backlight, you can guess the card's operating frequency

You can shine some light through an RFID card to see an antenna inside. If the antenna has only a few large turns, it is most likely a high-frequency antenna. If the antenna looks like a solid piece of metal with no gaps between the turns, it is a low-frequency antenna.

![](https://habrastorage.org/r/w1560/webt/iq/yw/gp/iqywgpjwwkoweffxdockmhwhajy.jpeg)

Low-frequency antennas have a thin wire for their turns, while high-frequency use a thicker one

**Low-frequency tags** are often used in systems that do not require high security: building access, intercom keys, gym membership cards, etc. Due to their higher range, they are convenient to use for paid car parking: the driver does not need to bring the card close to the reader, as it is triggered from further away. At the same time, low-frequency tags are very primitive, they have a low data transfer rate. For that reason, it's impossible to implement complex two-way data transfer for such things as keeping balance and cryptography. Low-frequency tags only transmit their short ID without any means of authentication.

**High-frequency tags** are used for a more complex reader-tag interaction when you need cryptography, a large two-way data transfer, authentication, etc.
It's usually found in bank cards, public transport, and other secure passes.

![](https://habrastorage.org/r/w1560/webt/ci/q6/qz/ciq6qzytjmw78hgkvymz-lslhq8.jpeg)

125 kHz & 13.56 MHz RFID tag comparison

### Low-Frequency 125 kHz Tags

* **Long Range** — lower frequency translates to higher range. There are some EM-Marin and HID readers, which work from a distance of up to a meter. These are often used in car parking.
* **Primitive protocol** —  due to the low data transfer rate these tags can only transmit their short ID. In most cases, data is not authenticated and it's not protected in any way. As soon as the card is in the range of the reader it just starts transmitting its ID.
* **Low security** — These cards can be easily copied, or even read from somebody else's pocket due to the protocol's primitiveness.

### High-Frequency 13.56 MHz Tags

* **Low range** — high-frequency cards are specifically designed so that they would have to be placed close to the reader. This also helps to protect the card from unauthorized interactions. The maximum read range that we managed to achieve was about 15 cm, and that was with custom-made high-range readers.
* **Advanced protocols** — data transfer speeds up to 424 kbps allow complex protocols with full-fledged two-way data transfer. Which in turn allows cryptography, data transfer, etc.
* **High security** — high-frequency contactless cards are in no way inferior to smart cards. There are cards that support cryptographically strong algorithms like AES and implement asymmetrical cryptography.

## RFID in Flipper Zero

![](https://habrastorage.org/r/w1560/getpro/habr/post_images/2cc/938/53a/2cc93853ab4aed7cc4ad5ebeeadafe12.png)

How RFID antenna works in Flipper Zero

Flipper supports both high-frequency and low-frequency tags. To support both frequencies we developed a dual-band RFID antenna that is situated on the bottom part of the device.

A separate NFC controller (ST25R3916) is used for high-frequency protocols (NFC). It takes care of everything related to hardware interaction with the cards: reading and emulation. Low-frequency 125 kHz protocols are implemented program...