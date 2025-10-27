---
title: Unicode Scalar Value
url: https://www.tbray.org/ongoing/When/202x/2023/08/14/Unicode-Scalar-Value
source: ongoing by Tim Bray
date: 2023-08-15
fetch_date: 2025-10-04T12:01:13.298391
---

# Unicode Scalar Value

# Unicode Scalar Value

Search

Suppose you’re writing code (or defining a protocol) that involves interchanging messages, and those messages include
text for humans to read. You owe it to the world to make any such text Unicode, so that the humans can
use Korean or Arabic or whatever else they live in. It turns out to be non-obvious how to say
“do Unicode right.” Today’s
ongoing piece exists to tell you how.

Here’s the rule ·

> The text must consist of a sequence of
> [Unicode scalar values](https://www.unicode.org/versions/Unicode10.0.0/ch03.pdf#G7404), i.e integers in the
> inclusive ranges 0-0xD7FF and 0xE000-0x10FFFF.
>
> The text must be encoded in UTF-8.
>
> If the messages are packaged in JSON, they must conform to the I-JSON Message Format
> ([RFC7493](https://www.rfc-editor.org/rfc/rfc7493.html)).

You can stop here; do this and you’ll be OK, and fortunately plenty of software libraries will help you do the right thing.

Here’s a bit of back story.

What’s a “Unicode character”? ·
You could read the
[Unicode standard](https://www.unicode.org/versions/Unicode15.0.0/), or you start at the bottom of my
[Technology/Coding/Text](https://www.tbray.org/ongoing/What/Technology/Coding/Text/) blog category and read forward
in time.

Programmers don’t need to stress out over what a Unicode character is. All you really need to know is that they’re
identified by numbers in the range 0-0x10FFFF, called “Code points”.
There are 1,114,112 code points, but last time I looked, less than
150K are assigned. Which, yes, leaves lots of empty space, but if an unassigned value creeps into your text that doesn’t
seem to break anything in practice.

In an ideal world, in the rule above you could just say “Code points”, but unfortunately there is a cursed block of 2048 code
points (0xD800-0xDFFF inclusive) called
[surrogates](https://en.wikipedia.org/wiki/UTF-16#U+D800_to_U+DFFF_(surrogates)) that are leftovers from a historical
mistake, can only occur in constrained pairs, and that in 2023 nobody should ever have to think about. The rule above says
“any code point that’s not a surrogate”.

UTF-8 ·
The second part of the rule above requires UTF-8. There are lots of
different ways to encode a list of codepoints into bytes in computer storage. For use on the Internet, UTF-8 is always the right
choice and any other choice is wrong.

If you want more, all these years later I still think my 2003 blog piece,
[Characters vs Bytes](/ongoing/When/200x/2003/04/26/UTF), is a good backgrounder.

JSON and I-JSON ·
Ever since its first-ever description at
[json.org](https://json.org), JSON has specified that strings are made up of codepoints, not excluding
surrogates. This can create a variety of problems, which you can avoid simply by never using any surrogates.

The JSON spec also allows several other dumb practices, for example duplicate object keys.
(I can say that because I was the editor of that RFC.)
I-JSON is an RFC that’s just JSON only with all that dumb stuff forbidden; among other things, text has to be
UTF-8 and surrogates are forbidden. Adopting it is a good way to signal to users of your technology that textual data will be
clean and sane.

Thank you for your attention ·
Fortunately, doing the right thing is easy.

---

**Updated: 2023/08/14**

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

[August](/ongoing/When/202x/2023/08/) [14](/ongoing/When/202x/2023/08/14/), [2023](/ongoing/When/202x/2023/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [Text](/ongoing/What/Technology/Text) (5 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!