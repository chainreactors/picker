---
title: We have proof automation now
url: http://www.imperialviolet.org/2026/07/26/zstd-lean.html
source: ImperialViolet
date: 2026-07-26
fetch_date: 2026-07-27T05:42:40.690986
---

# We have proof automation now

# [ImperialViolet](https://www.imperialviolet.org)

### [We have proof automation now](/2026/07/26/zstd-lean.html) (26 Jul 2026)

I've long had a soft spot for dependently-typed languages like ~~Coq~~ Rocq and Lean.
They offer the possibility of a type system capable of encoding and enforcing
arbitrarily subtle invariants. The sort of thing that, in regular languages, ends
up (at best) as a comment, and which quickly gets lost as the size of the team grows.
Then you get subtle misunderstandings and components that don't quite
fit together. It's often the case that those components have grown to a
sufficient size that, when the problem is noticed, aligning either of them is a wearying prospect. Perhaps, say
dependent types seductively, you could write those invariants formally and have
a machine check them.

(p.s. Coq changed its name! I remember many years ago at a Coq conference in
Princeton, I tried suggesting that,
in an English-speaking world, having a programming language called Coq was an
impediment. I don't think the audience agreed at the time. I also joked that many of the talks there sounded like a speech by
Tyrion Lannister, there being so many Coqs and Hoares. A joke
that was hilarious and timely, even though it fell completely flat, coming as
it did before the final season of that show and our collective memory-holing of
it.)

The problem has always been that with great type-system power comes great
proof effort. I can certainly attest to entire days spent proving
really quite simple things. Doing proofs is actually quite fun: it's
challenging, interactive, and there's a clear goal. But gosh, does it take a lot
of time, especially if, like me, you don't know what you're doing. There's also the
periodic, galling experience, at the end of many hours of effort, where you realise that the goal
that you're trying to prove is, in fact, *false*. The classic [result](https://trustworthy.systems/publications/nicta_full_text/7371.pdf) here is the
retrospective from the seL4 effort that found that, even though the project was
large enough for the engineers to develop considerable experience, they
spent about 10 times as much time proving as they did designing and
implementing. They ended up with more than 20 times as many lines of proof code as they
did C code.

That overhead has made programming in dependently-typed languages extremely niche. It has also spurred people to try and automate
it away. The attempt I'm passingly familiar with is F\*, where the
system tries to have an SMT solver automatically discharge the obligations.
That certainly works for simple cases, but it's very easy to craft something
that causes the SMT solver to go off into space and run for hours, leaving you
wondering whether it's ever going to finish. I've seen that people who use
these languages a lot have to develop a sixth sense for what is going to make
the solver happy, and then craft everything around that. It can help,
but to an extent it converts the problem into mysticism: you end up
serving a complex and fickle god.

A critical fact is that, at least in theory, once the statement is correct, the contents of its proof
are irrelevant: only its existence matters. This is not entirely true
because of two complicating factors: first, what the seL4 group called “proof
engineering”: the need to structure proofs so that the effort of realigning them
after code changes is reduced. And, second, sufficiently complicated
proofs can cause even type checkers to blow up and consume vast amounts of
memory.

We now have LLMs which, combined with proof irrelevance, promise to be
an extremely capable form of proof automation. With sufficient amounts of
automation perhaps you don't need to worry about proof engineering nearly so much. You
still need to avoid blowing up the type checker but, in my limited tests, LLMs can avoid that. Potentially, LLMs suddenly make dependent-type systems dramatically
more practical. I wanted to play around with this so built a Zstandard decompressor
in Lean, mostly because I was also curious about Zstandard.

Zstandard seems like it's winning the competition to replace gzip as the
canonical compression utility. It's another LZ77-style compressor, but it offers
better entropy coding and a careful design that allows it to achieve very
impressive decompression speeds. It will never be as beautiful as bzip2, but
the shining elegance of the Burrows–Wheeler transform doesn't count for too
much in the face of significant practical advantages:

zstd

bzip2

gzip

lzma (XZ/LZMA2)

50
100
200
500
1000
2000
zstd
bzip2
gzip
lzma (XZ/LZMA2)

70
72
74
76
78
80
82
84
86
Compression tradeoff on 64 MiB of Lean/mathlib source
Space saved (%) — farther right is more compression
Decompression throughput (MiB/s, log scale) — higher is faster

(Measurements taken on the standard reference computer, i.e. whatever the author was using at the time. And note the log scale on the y-axis: gzip and Zstandard are in their own speed class. This is an Apple machine and Apple's gzip is especially optimised; expect gzip to be slower elsewhere.)

Zstandard (by Yann Collet, building on the seminal [ANS](https://en.wikipedia.org/wiki/Asymmetric_numeral_systems) work by Jarek Duda) has [an RFC](https://www.rfc-editor.org/rfc/rfc8878),
but it is quite terse. It contains all the information you need to implement a
decompressor, but unless you're already quite familiar with compression, I
think you'll need to re-read it a few times to understand what's going on. I,
at least, had to read section 4.1 half a dozen times before I felt that I
had a decent grasp of it. Too late into this process, I
discovered that my colleague, Nigel Tao, has written [a better
write-up of Zstandard](https://nigeltao.github.io/blog/2022/zstandard-part-1-concepts.html) than I was going to manage anyway. So, if you want to
understand Zstandard, you should read that. I'm just going to give an explanation of the most interesting bit,
the entropy encoder, and mix that in with some evangelism about Lean.

The job of an entropy encoder is, given a set of symbols with non-uniform
probabilities, to encode a sequence of those symbols using the fewest number of
bits. The classic entropy coder is a Huffman encoder. Huffman encoders build a
binary tree with symbols at the leaf nodes, and Huffman showed that a very
simple algorithm produces an optimal prefix-tree: you take the list of symbols, you
find the two with the least probability, and you form a tree node with them as
children. That tree node then has a probability that is the sum of its two
children, and then you repeat the algorithm with two fewer symbols,
but now with a tree node in the mix. Obviously each step of this
algorithm reduces the size of the set of elements by one, so it terminates, and
it also produces an optimal tree. Huffman trees are very fast because you can
build a table indexed by the next *n* bits (where *n* is the length of the longest code).
The table entry tells you what symbol you've decoded and
how many bits to unread. The drawback of Huffman trees is that they can
only use a whole number of bits for each symbol: if you have a symbol where -log2(p) = 2.3 then ideally you want to use 2.3 bits to
encode it. But Huffman forces you either to round up to 3 bits or to round
down, which will force some other symbols to consume more bits.

Zstandard uses Huffman trees, but it also has a higher-compression
entropy encoder called FSE. FSE is a state machine. There
are more states than symbols, and each symbol gets a fraction of the states
that mirrors its probability of occurrence in the stream. So if there's some
symbol that is expected to appear 50% of the time, it gets ~50% of the states.
Each state has three values: the symbol for that state, a number of bits to
read from the bitstream when in that state, and a baseline state number that is
added to those bits to get the next state. Now, if you recall, the problem with
Huffman trees was that they co...