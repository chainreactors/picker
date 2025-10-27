---
title: Q Numbers Redux
url: https://www.tbray.org/ongoing/When/202x/2024/08/28/Q-Numbers-2
source: ongoing by Tim Bray
date: 2024-08-29
fetch_date: 2025-10-06T18:03:02.841629
---

# Q Numbers Redux

# Q Numbers Redux

Search

Back in July I wrote about
[Q numbers](/ongoing/When/202x/2024/07/09/Q-Numbers), which make it possible to compare numeric values using a finite
automaton. It represented a subset of numbers as 14-hex-digit strings. In a
remarkable instance of BDD (Blog-Driven Development, obviously) Arne Hormann and Axel Wagner figured out a way to represent
*all 64-bit floats* in at most ten bytes of UTF-8 and often fewer. This feels nearly miraculous to
me; read on for heroic bit-twiddling.

Numbits ·
Arne Hormann worked out how to rearrange the sign, exponent and mantissa that make up a float’s 64 bits into a
big-endian integer that you probably couldn’t do math with but you can compare for equality and ordering. Turn that into sixteen
hex digits and you’ve got automaton fuel which covers all the floats at the cost of being a little bigger.

If you want to admire Arne’s awesome bit-twiddling skills, look at
[numbits.go](https://github.com/timbray/quamina/blob/main/numbits.go). He explained to me how it works in some chat
that I can’t find, and to be honest I can’t quite look at this and remember the explanation.

```
    u := math.Float64bits(f)
    // transform without branching
    // if high bit is 0, xor with sign bit 1 << 63,
    // else negate (xor with ^0)
    mask := (u>>63)*^uint64(0) | (1 << 63)
    return numbits(u ^ mask)
```

*[Update: Arne wrote it up! See
[Q Numbers Redux Explained](/ongoing/When/202x/2024/08/31/QNum-Redux-Explained).]*

Even when I was puzzled, I wasn’t worried because the unit tests are good; it
works.

Arne called these “numbits” and wrote a nice complete API for them, although Quamina just needs `.fromFloat64()`
and `.toUTF8()`.
I and Arne both thought he’d invented this, but then he discovered that the same trick was being used in the DB2 on-disk data
format years and years ago. Still, damn clever, and I’ve urged him to make numbits into a standalone library.

We want less! ·
We care about size; Among other things, the time an automaton takes to match a value is linear (sometimes worse) in its
length.
So the growth from 14 to 16 bytes made us unhappy. But, no problemo! Axel Wagner pointed out that if you use base-128, you
can squeeze those 64 bits into ten usable bytes of UTF-8. So now we’re *shorter* than the previous iteration of Q numbers
while handling all the float64 values…

But wait, there’s more! Arne noticed that for purposes of equality and comparison, trailing zeroes (`0x0`, not
`‘0’`) in those 10-byte strings
are entirely insignificant and can just be discarded. The final digit only has 1/128 chance of being zero, so maybe no big
deal. But it turns out that you do get dramatic trailing-0 sequences in positive integers, especially small ones,
which in my experience are the kinds of numbers you most often want to match. Here’s a chart of the length of the lengths the of
numbits-based Q numbers for the integers zero through 100,000 inclusive.

| Length | Count |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 3 | 115 |
| 4 | 7590 |
| 5 | 92294 |

They’re all shorter than 5 until you get to 1,000.

Unfortunately, none of my benchmarks prove any performance increase because they focus on corner cases and extreme numbers;
the benefits here are to the world’s most boring numbers, namely small non-negative integers.

Here I am, well past retirement age, still getting my jollies from open-source bit-banging. I hope other people manage to
preserve their professional passions into later life.

---

**Updated: 2024/09/01**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Michael Kay](http://www.saxonica.com) (Sep 09 2024, at 15:59)

I was aware that the Oracle database used a similar technique for representing numeric values - I've no idea how similar.

Saxon tackles the problem a different way. Numeric values are held using native representations (such as IEEE floating point) so that we can use native hardware operations for arithmetic. But when we have to compare a string to a number, as is common in XPath, then rather than immediately converting the string to a number, we quickly compute its order of magnitude (as a power of ten) and its first signfiicant digit, and use those to return false if the values obviously don't match; only after this prefiltering do we perform the normal string-to-number conversion.

*[[link](#c1725922799.688107)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/ongoing/misc/Tim) ·
[Dad](http://www.textuality.com/BillBray/)
[colophon](/ongoing/misc/Colophon) ·
[rights](/ongoing/misc/Copyright)

[![picture of the day](/ongoing/potd.png)](/ongoing/goto-potd/)

[August](/ongoing/When/202x/2024/08/) [28](/ongoing/When/202x/2024/08/28/), [2024](/ongoing/When/202x/2024/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [Quamina Diary](/ongoing/What/Technology/Quamina%20Diary) (19 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!