---
title: My First GenAI Code
url: https://www.tbray.org/ongoing/When/202x/2025/07/01/First-AI-Code
source: ongoing by Tim Bray
date: 2025-07-02
fetch_date: 2025-10-06T23:49:24.333215
---

# My First GenAI Code

# My First GenAI Code

Search

At the moment, we have no idea what the impact of genAI on software development is going to be. The impact of
*anything* on coding
is hard to measure systematically, so we rely on anecdata and the community’s eventual consensus.
So, here’s my anecdata. Tl;dr: The AI was not useless.

The problem ·
My current work on
[Quamina](/ongoing/What/Technology/Quamina%20Diary/) involves dealing with collections of finite-automata states,
which, in the Go programming language, are represented as slices of pointers to state instances:

> `[]*faState`

The problem I was facing was deduping them, so that there would be only one instance corresponding to any particular
collection. This is what, in Java, the `intern()` call does with strings.

The algorithm isn’t rocket science:

1. Dedupe the states, i.e. turn the collection into a set.
2. For each set of states, generate a key.
3. Keep a hash table of sets around, and use the key to see whether you’ve already got such a set, and if so return
   it. Otherwise, make a new entry in the hash table and return that.

I’m out of touch with the undergrad CS curriculum, but this feels like a second-year assignment or thereabouts? Third?

Enter Claude ·
So I prompted Claude thus:

> I need Go code to provide a "intern"-like function for lists of pointers. For example, if I have several
> different []\*int arrays, which may contain duplicates, I want to call intern() on each of them and get back a single canonical
> pointer which is de-duplicated and thus a set.

Claude did pretty well. It got the algorithm right, the code was idiomatic and usefully commented, and it also provided a
decent unit test (but in a `main()` stanza rather than a proper Go test file).
I didn’t try actually running it.

The interesting part was the key computation. I, being lazy, had just done a Go `fmt.Sprintf("%p")`
incantation to get a hex string representing each state’s address, sorted them, joined them, and that was the key.

Claude worked with the pointers more directly.

```
	// Sort by pointer address for consistent ordering
	sort.Slice(unique, func(i, j int) bool {
		return uintptr(unsafe.Pointer(unique[i])) < uintptr(unsafe.Pointer(unique[j]))
	})
```

Then it concatenated the raw bytes of the map addresses and lied to Go by claiming it was a string.

```
	// Create key from pointer addresses
	key := make([]byte, 0, len(slice)*8)
	for _, ptr := range slice {
		addr := uintptr(unsafe.Pointer(ptr))
		// Convert address to bytes
		for i := 0; i < 8; i++ {
			key = append(key, byte(addr>>(i*8)))
		}
	}
	return string(key)
```

This is an improvement in that the keys will be half the size of my string version.
I didn’t copy-paste Claude’s code wholesale, just replaced ten or so lines of key construction.

Take-away ·
I dunno. I thought the quality of the code was fine, wouldn’t have decomposed the functions in the same way but wouldn’t have
objected on review. I was pleased with the algorithm, but then I would be since it was the same one I’d written, and, having
said that, quite possibly that’s the only algorithm that anyone has used. It will be *super* interesting if someone
responds to this write-up saying “You and Claude are fools, here’s a much better way.”

Was it worth fifteen minutes of my time to ask Claude and get a slightly better key computation?
Only if this ever turns out
to be a hot code path and I don’t think anybody’s smart enough to know that in advance.

Would I have saved time by asking Claude first? Tough to tell; Quamina’s data structures are a bit non-obvious and I would
have had to go to a lot of prompting work to get it to emit code I could use directly.
Also, since Quamina is low-level performance-critical infrastructure code, I’d be nervous about having any volume of code
that I didn’t really *really* understand.

I guess my take-away was that in this case, Claude knew the Go idioms and APIs better than I did; I’d never looked at the
[unsafe](https://pkg.go.dev/unsafe) package.

Which reinforces my
suspicion that genAI is going to be especially useful at helping generate code to talk to big complicated
APIs that are hard to remember all of. Here’s an example: Any moderately competent Android developer could add a feature to an
app where it strobes the flash and surges the vibration in sync with how fast you’re shaking the device back and forth,
probably in an afternoon. But it would require a couple of dozen calls into the dense forest of Android APIs, and I suspect a
genAI might get you there a lot faster by just filling the calls in as prompted.

Reminder: This is just anecdata.

---

**Updated: 2025/07/01**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Pascal Costanza](http://p-cos.net) (Jul 01 2025, at 12:24)

I believe the Claude code is incorrect. While the current Go garbage collector is not a moving or copying collector, there is no guarantee it stays that way. For example, <https://pkg.go.dev/runtime#Pinner.Pin> hints at the possibility that objects might be moved in memory. So comparing uintptr(unsafe.Pointer(...)) with < can be problematic in the long run. (Note also that actual pointer types in Go are not ordered and can only be compared with == and !=.)

A nitpick: Your statement "Claude did pretty well." is incorrect. LLMs don't "do" anything, they just repeat what they have seen elsewhere.

*[[link](#c1751397848.101858)]*

From: [Tim](https://www.tbray.org/ongoing/) (Jul 01 2025, at 12:35)

Hey @Pascal, I'm pretty sure I don't need to worry about objects moving, there are pointers to these things scattered all over the place and I can't see how they could be moved without breaking the whole finite automaton that they're part of.

But suppose you're right and it isn't safe to use these things. How would you go about constructing a key corresponding to a set of pointers?

*[[link](#c1751398533.991718)]*

From: [Pascal Costanza](http://p-cos.net) (Jul 01 2025, at 16:28)

The typical way to implement interning, to the best of my knowledge, is with hashtables. In languages like Java whose garbage collector can move objects around, this is not an issue because the runtime system ensures that hash codes remain consistent. This works for == and !=, but not for < etc. in the general case.

The sorting code in Go that you have shown will access pointers several times in the general case, so any ordering between pointers is not guaranteed to be stable in the presence of a copying collector.

*[[link](#c1751412526.811053)]*

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

[July](/ongoing/When/202x/2025/07/) [01](/ongoing/When/202x/2025/07/01/), [2025](/ongoing/When/202x/2025/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [AI](/ongoing/What/Technology/AI) (8 more)

 · · [Software](/ongoing/What/Technology/Software) (89 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!