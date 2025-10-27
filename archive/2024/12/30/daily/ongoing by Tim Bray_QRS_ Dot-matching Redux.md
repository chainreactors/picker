---
title: QRS: Dot-matching Redux
url: https://www.tbray.org/ongoing/When/202x/2024/12/29/Matching-Dot-Redux
source: ongoing by Tim Bray
date: 2024-12-30
fetch_date: 2025-10-06T19:35:51.561125
---

# QRS: Dot-matching Redux

# QRS: Dot-matching Redux

Search

Recently I posted
[Matching “.” in UTF-8](/ongoing/When/202x/2024/12/18/Matching-Dot-in-UTF8), in which I claimed that you could match
the regular-expression “`.`” in a UTF-8 stream with either four or five states in a byte-driven finite automaton,
depending how
you define the problem. That statement was arguably wrong, and you might need three more states, for a total of eight. But you
can make a case that really, only four should be needed, and another case calling for quite a few more.
Because that phrase “depending how you define the problem” is doing a lot of work.

But first, thanks:
[Ed Davies](https://functional.cafe/%40edavies), whose blog contributions
([1](/ongoing/When/202x/2024/12/18/Matching-Dot-in-UTF8#c1734780103.136152),
[2](/ongoing/When/202x/2024/12/18/Matching-Dot-in-UTF8#c1734970677.112348),
[3](/ongoing/When/202x/2024/12/18/Matching-Dot-in-UTF8#c1735151411.984021)) were getting insufficient attention from
me until
[Daphne Preston-Kendal](https://chaos.social/%40dpk) insisted I look more closely.

To summarize Ed’s argument: There are a bunch of byte combinations that look (and work) like regular UTF-8 but are explicitly
ruled out by the Unicode spec, in particular
[Section 3.9.3](https://www.unicode.org/versions/latest/core-spec/chapter-3/#G31703) and
its Table 3.7.

Moar States! ·
Ed posted a nice picture of a corrected 8-state automaton that will fail to match any of these forbidden
sequences.

[![Ed Davies’ corrected UTF-8 state machine](edavies-machine.png "Ed Davies’ corrected UTF-8 state machine")](-big/edavies-machine.jpg.html)

(Original SVG
[here](https://edavies.me.uk/paste/R2XVFXpjcIiVq9FkaZ2u7ZUC/utf8.svg).)

I looked closely at Ed’s proposal and it made sense, so I implemented it and (more important) wrote a bunch of unit tests
exploring the code space, and it indeed seems to accept/reject everything correctly per Unicode 3.9.3.

So, argument over, and I should go forward with the 8-state Davies automaton, right?
Why am I feeling nervous and grumpy, then?

Not all Unicode ·
I’ve already mentioned in this series that your protocols and data structures just gotta support Unicode in the 21st century,
but you almost certainly don’t want to support all the Unicode characters, where by “character” I mean, well… if you care at all
about this stuff, please go read
[Unicode Character Repertoire Subsets](https://www.ietf.org/archive/id/draft-bray-unichars-10.html) (“Unichars for
short), a draft inching
its way through the IETF, with luck an RFC some day. And if you *really* care, dig into
[RFC 3454: PRECIS Framework: Preparation, Enforcement, and Comparison of
Internationalized Strings in Application Protocols](https://datatracker.ietf.org/doc/html/rfc7564). Get a coffee first, PRECIS has multiple walls of text and isn’t
simple at all. But it goes to tremendous lengths to address security issues and other best practices.

If you don’t have the strength, take my word for it that the following things are true:

1. We don’t talk much about abstract characters; instead focus on the numeric “code points” that represent them.
2. JSON, for historical reasons, accepts all the code points.
3. There are several types of code points that don’t represent characters: “Surrogates”, “controls”, and
   “noncharacters”.
4. There are plenty of code points that are problematic because they can be used by phishers and other attackers
   to fool their victims because they look like other characters.
5. There are characters that you shouldn’t use because they represent one or another of the temporary historical hacks
   used in the process of migrating from previous encoding schemes to Unicode.

The consequence of all this is that there are many subsets of Unicode that you might want to restrict users of your protocols
or data structures to:

1. JSON characters: That is to say, all of them, including all the bad stuff.
2. Unichars “Scalars”: Everything except the surrogates.
3. Unichars “XML characters”: Lots but not all of the problematic code points excluded.
4. Unichars “Unicode Assignables”: “All code points that are currently assigned, excluding legacy control codes, or that might in
   future be assigned.”
5. PRECIS “IdentifierClass”: “Strings that can be used to refer to, include, or communicate protocol strings like
   usernames, filenames, data feed identifiers, and chatroom name.”
6. PRECIS “FreeformClass”: “Strings that can be used in a free-form way, e.g., as a password in an authentication exchange
   or a nickname in a chatroom.”
7. Some variation where you don’t accept any unassigned code points; risky, because that changes with every Unicode
   release.

(I acknowledge that I am unreasonably fond of numbered lists, which is probably an admission that I should try harder to
compose smoothly-flowing linear arguments that don’t need numbers.)

You’ll notice that I didn’t provide links for any of those entries. That’s because you really shouldn’t pick one without
reading the underlying document describing why it exists.

What should you accept? ·
I dunno. None of the above are crazy. I’m kind of fond of Unicode Assignables, which I co-invented. The only thing I’m sure
of is that you should *not* go with JSON Characters, because of the fact that its rules make the following chthonic
horror perfectly legal:

> ```
> {"example": "\u0000\u0089\uDEAD\uD9BF\uDFFF"}
> ```

Unichars describes it:

> The value of the “example” field contains the C0 control NUL, the C1 control "CHARACTER TABULATION
> WITH JUSTIFICATION", an unpaired surrogate, and the noncharacter U+7FFFF encoded per JSON rules as two escaped UTF-16 surrogate
> code points. It is unlikely to be useful as the value of a text field. That value cannot be serialized into well-formed UTF-8,
> but the behavior of libraries asked to parse the sample is unpredictable; some will silently parse this and generate an
> ill-formed UTF-8 string.

No, really.

What is Quamina for? ·
If you’re wondering what a “Quamina” is, you probably stumbled into this post through some link and, well, there’s a lot of
history. Tl;dr:
[Quamina](https://github.com/timbray/quamina) is a pattern-matching library in Go with an unusual (and fast)
performance envelope; it can match thousands of Patterns to millions of JSON blobs per second. For much, much more, peruse the
[Quamina Diary](/ongoing/What/Technology/Quamina%20Diary/) series on this blog.

Anyhow, all this work in being correctly restrictive as to the shape of the incoming UTF-8 was making me uncomfortable.
Quamina is about telling you what byte patterns are in your incoming data, not enforcing rules about what
*should* be there.

And it dawned on me that it might be useful to ask Quamina to look at a few hundred thousand inputs per second and tell you
which had ill-formed-data problems. Quamina’s dumb-but-fast byte-driven finite automaton would be happy to do that, and very
efficiently too.

Conclusion ·
So, having literally lain awake at night fretting over this, here’s what I think I’m going to do:

1. I’ll implement a new Quamina pattern called `ill-formed` or some such that will match any field that has
   busted UTF-8 of the kind we’ve been talking about here. It’d rely on an automaton that is basically the inverse of
   Davies’ state machine.
2. By default, the meaning of “`.`” will be “matches the Davies automaton”; it’ll match
   well-formed UTF-8 matching all code points except surrogates.
3. I’ll figure out how to parameterize regular-expression matches so you can change the definition of “`.`” to
   match one or more of the smaller subsets like those in the list above from Unichars and PRECIS.

But who knows, maybe I’ll end up changing my mind again. I already have, multiple times. Granted that implementing regular
expressions is hard, you’d think that matching “`.`” would be the easy part. Ha ha ha.

---

**Updated: 2024/12/30**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing...