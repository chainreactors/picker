---
title: Conversation Index Analysis in Email Forensics — Part 2
url: https://www.metaspike.com/conversation-index-analysis-email-forensics/
source: Instapaper: Unread
date: 2026-07-30
fetch_date: 2026-07-31T05:31:20.867826
---

# Conversation Index Analysis in Email Forensics — Part 2

[Skip to main content](#ajax-content-wrap)

[![Metaspike Cloud Digital Forensics Software](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Dark_Sm.png)![Metaspike Cloud Digital Forensics Software](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Light_Sm.png)![Metaspike Cloud Digital Forensics Software](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Dark_Sm.png)](https://www.metaspike.com)

[0](https://www.metaspike.com/cart/)

[Menu](#slide-out-widget-area)

* [Software](https://www.metaspike.com/software/)
* [Training](https://www.metaspike.com/product-category/training/)
* [Blog](https://www.metaspike.com/blog/)
* [FAQ](https://www.metaspike.com/faq/)
* [Resources](https://www.metaspike.com/resources/)
* [Community](https://community.metaspike.com)
* [Resellers](https://resellers.metaspike.com)
* [Contact](https://www.metaspike.com/contact/)
* [BUY NOW](https://www.metaspike.com/product-category/software/)

* [twitter](https://twitter.com/MetaspikeHQ) [bluesky](https://bsky.app/profile/metaspike.bsky.social) [linkedin](https://www.linkedin.com/company/metaspike/) [youtube](https://www.youtube.com/Metaspike)
* [0](https://www.metaspike.com/cart/)

  was successfully added to your cart.
* [Menu](#slide-out-widget-area)

![Metaspike](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Dark_Sm.png)

*Press enter to begin your search*
Search

Close Search

![](https://www.metaspike.com/wp-content/uploads/2026/07/conversation-index2.jpg)

# Conversation Index Analysis in Email Forensics — Part 2

By [Arman Gungor](https://www.metaspike.com/author/agungor/ "Posts by Arman Gungor")July 28, 2026July 30th, 2026[Articles](https://www.metaspike.com/category/articles/)

[No Comments](https://www.metaspike.com/conversation-index-analysis-email-forensics/#respond)

The Conversation Index MAPI property piqued my interest long ago as a potentially valuable digital forensics artifact. I wrote a blog about it in 2013, and have been happy to hear that the artifact has been instrumental in solving numerous cases.

What we know about Conversation Index has changed since then. This article is intended as a follow-up to my original blog to discuss how newer Conversation Indices (I will call these “modern”) differ from the original, “classic” Conversation Indices. If you have not read the **[original blog](https://www.meridiandiscovery.com/how-to/e-mail-conversation-index-metadata-computer-forensics/)**, I recommend doing so before you proceed.

## Thread Index vs. Conversation Index

Contents of the Conversation Index MAPI property are often Base64 encoded and transmitted in a MIME header named “Thread-Index”. Here is what a Thread-Index header may look like:

```
Thread-Index: Ac3pCr/g148OQoCCQSCy8dDjwH7QBwAAzLowAAARRGA=
```

When encoded in Base64, the “classic” Thread Index values typically start with “Ab”, “Ac”, “Ad”, or “Ae” while the “modern” ones typically start with “AQH”.

## Layout

Let’s take a look at the following Conversation Index:

```
0101DCCE985315F83A00F6984B6C8FF8236D5A0B3BCDB5E39A588080000048808000020F2F8004467680800022E6808000074A80
```

As in the classic version, the Conversation Index comprises a 22-byte header block and 0 or more 5-byte child blocks. The last 16 bytes of the header block is a GUID. So, we can organize the Conversation Index as follows:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Timestamp | GUID | Child Block 1 | Child Block 2 | Child Block 3 | Child Block 4 | Child Block 5 | Child Block 6 |
| 0101DCCE9853 | 15F83A00-F698-4B6C-8FF8-236D5A0B3BCD | B5E39A5880 | 8000004880 | 8000020F2F | 8004467680 | 800022E680 | 8000074A80 |

## Header Timestamp

In classic Conversation Indices, there is no wasted byte in the header timestamp. The initial 01 byte and the following 5 bytes form the first 6 bytes of a FILETIME value, which we pad with two bytes of zeros. In the modern version, there is an extra 01 byte prefix which is dropped, and the remainder forms the first 5 bytes of a FILETIME value, to be padded with three bytes of zeros. The side effect of this change is precision loss. In the classic variant, we were missing the precision from the dropped 2 bytes, which left us with ~0.0066-second precision. In the modern version, we are missing the last three bytes, which gives us ~1.68-second precision (2^24 100-nanosecond units = 1,677,721.6 microseconds = ~1.677 seconds).

In any case, the header timestamp calculation is straightforward. We drop the first 01 byte, take the 01DCCE9853 part, pad it to 01DCCE9853000000, and treat that as a hexadecimal FILETIME value in big-endian. In human readable form, this decodes to 2026-04-17 18:30:53.7132032 UTC.

Counterintuitively, we must also calculate the header timestamp the “wrong” way, by treating it as if this were a classic Conversation Index. In that scenario, we start with 0101DCCE9853, pad it with two bytes of zeros to 0101DCCE98530000, and calculate the timestamp as 1831-01-02 18:28:09.1588608. This corresponds to 72581848891588608 100-nanosecond units since the start of January 1, 1601. Let’s call this the “base timestamp”.

## Child Block 1

Here is where things start to get interesting. In a modern Conversation Index, the first child block’s time difference is not calculated from the header timestamp, but from the base timestamp.

Our child block looks as follows: B5E39A58 80

The first four bytes contain the 1-bit Delta Code (DC) and 31 bits of Time Difference.

The last byte (0x80) represents the Random Number and Sequence Count. Notably, MS-OXOMSG 2.2.1.3 identifies this byte as “*Random (8 bits): Random value generated by using an implementation-specific algorithm.*”

In this case, the DC is 1. Which means, per [Microsoft’s spec](https://learn.microsoft.com/en-us/office/client-developer/outlook/mapi/tracking-conversations), the high 10 bits and the low 23 bits were discarded. Because the high 10 bits are discarded, the time difference value has a maximum capacity of 54 bits (64 – 10), which allows it to at most represent 2^54 100-nanosecond units. This is 18014398509481984 100-nanosecond units in decimal, and corresponds to approximately **57 years**. To refresh our memory, MS-OXOMSG 2.2.1.3 states the following:

:   > *DC (Delta code) (1 bit) and Time Delta (31 bits): Calculated based on TimeDiff, a 64-bit value representing the difference between the current time and the time stored in the conversation index header:*

* > *If the difference is less than 1.7 years (high order part of the delta file time bitwise AND with 0x00FE0000 resulting in “0”), the Delta Code field is 0 and the Time Delta field is the least significant 31 bits of the TimeDiff value remaining after the 18 least significant bits are excluded.*
* > *If the difference is greater than or equal to 1.7 years (high order part of the delta file time bitwise AND with 0x00FE0000 resulting in nonzero), the Delta Code field is 1 and the Time Delta field is the least significant 31 bits of the TimeDiff value remaining after the 23 least significant bits are excluded.*

Note that, since the time difference in modern Conversation Indices is calculated from the base timestamp, the time difference is expected to be greater than 1.7 years and DC is expected to be always 1.

One might think that 57 years is eternity in the context of email communications, and that this would have no practical effect. But, because the child block time difference is calculated from the base timestamp, not the header timestamp, the time difference exceeds 57 years–multiple times. When it does, the time difference value silently wraps (i.e., overflows). To account for this, we add the dropped ~57 year time periods until we pass the header timestamp.

Let’s do the math:

* First, let’s calculate the time difference for this child block. We remove the first bit (1), which takes us from 0xB5E39A58 to 0x35E39A58 (904108632 in decimal). Consi...