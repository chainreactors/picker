---
title: QRS: Parsing Regexps
url: https://www.tbray.org/ongoing/When/202x/2024/12/12/QRS-Parsing-Regular-Expressions
source: ongoing by Tim Bray
date: 2024-12-13
fetch_date: 2025-10-06T19:36:42.390836
---

# QRS: Parsing Regexps

# QRS: Parsing Regexps

Search

Parsing regular expression syntax is hard. I’ve written a lot of parsers and,for this one, adopted a couple of new techniques
that I haven’t used before. I learned things that might be of general interest.

I was initially surprised that the problem was harder than it looked, but quickly realized that I shouldn’t have been, because
my brain has also always had a hard time parsing them.

They’re definitely a write-only syntax and just because I’m gleefully
writing this series doesn’t mean I’m recommending you reach for REs as a tool very often.

But I bet most people in my profession
find themselves using them pretty regularly, in the common case where they’re the quickest path from A to B. And I know for
sure that, on a certain number of occasions, they’ve ended up regretting that choice.

Anyhow, I console myself with the thought that the I-Regexp RE dialect has less syntax and fewer footguns than PCREs
generally. Plus, I’ve been having fun implementing them. So knock yourselves out. (Not legal nor investing advice.)

Sample-driven development ·
When I started thinking seriously about the parser, the very first thought in my mind was “How in the freaking hell am I
going to test this?” I couldn’t stand the thought of writing a single line of code without having a plausible answer. Then it
occurred to me that since I-Regexp subsets
[XSD Regular Expressions](https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#regexs), and since XSD (which I
mostly dislike) is widely deployed and used, maybe someone already wrote a test suite? So I stuck my head into an XML
community space (still pretty vigorous after all these years) and asked “Anyone have an XSD regexp test suite?”

And it worked! (I love this profession sometimes.)
[Michael Kay](https://en.wikipedia.org/wiki/Michael_Howard_Kay) pointed at me a few things notably including
[this GitHub repo](https://github.com/qt4cg/xslt40-test/tree/master/tests/misc/regex-syntax). The
`_regex-syntax-test-set.xml` there, too big to display, contains just under a thousand regular expressions, some
valid, some not, many equipped with strings that should and should not match.

The process by which I turned it into a `*_test.go` file, Dear Reader, was not pretty. I will not share the
ugliness, which involved awk and emacs, plus hideous and largely untested one-off Go code.

But I gotta say, if you have to write a parser for any anything, having 992 sample cases makes the job a whole lot less
scary.

Lesson: When you’re writing code to process a data format that’s new to you, invest time, before you start, in looking for samples.

Recursive descent ·
The I-Regexp specification contains a
[complete ABNF grammar](https://www.rfc-editor.org/rfc/rfc9485.html#name-i-regexp-syntax) for the syntax. For writing
parsers I tend to like finite-automaton based approaches, but for a freakishly complicated mini-language like this, I
bowed in the direction of Olympus for that grammar and started recursively descending.

I think at some point I understood the theory of Regular Languages and LL(1) and so on, but not any more. Having said that,
the recursive-descent technique is conceptually simple, so I plowed ahead. And it worked eventually. But there seemed a lot of
sloppy corners where I had to peek one byte ahead or backtrack one. Maybe if I understood LL(1) better it’d have
been smoother.

The “character-class” syntax `[abc0-9]` is particularly awful. The possible leading `-` or
`^` makes it worse, and it has the usual `\`-prefixed stanzas. Once again, I salute the original
specifiers who managed to express this in a usable grammar.

I was tempted, but ended up making no use of Go’s `regexp` library to help me parse REs.

I have to say that I don’t *like* the code I ended up with as much as any of my previous (automaton-based) parsers,
nor as much as the rest of the Quamina code. But it seems to work OK. Speaking of that…

Test coverage ·
When I eventually got the code to do the right thing for each of Michael Kay’s 992 test cases, I was feeling a warm glow. So
then I ran the test-coverage tool, and got a disappointingly-low number. I’m not a 100%-coverage militant generally, but I am for
ultra-low-level stuff like this with a big blast radius.

And here’s the lesson: Code coverage tools are your friend. I went in and looked at the green and red bars; they revealed that while
my tests had passed, I was really wrong in my assumptions about the paths they would make the code take. Substantial
refactoring ensued.

Second, and somewhat disappointingly, there were a lot of coverage misses on Go’s notorious little `if err != nil`
stanza. Which revealed that my sample set didn’t cover the RE-syntax space quite as thoroughly as I’d hoped. In particular,
there was really no coverage of the code’s reaction to malformed UTF-8.

The reason I’m writing this is to emphasize that, even if you’re in a shop where the use of code-coverage tools is
(regrettably) not required, you should use one anyhow, on basically every important piece of code. I have absolutely never
failed to get surprises, and consequently improved code, by doing this.

Sharing the work ·
I don’t know if I-Regexp is going to be getting any uptake, but it wouldn’t surprise me if it did; it’s a nice tractable
subset that hits a lot of use cases. Anyhow, now I have reasonably robust and well-tested I-Regexp parsing code. I’d like to
share it, but there’s a problem.

To do that, I’d have to put it in a separate repo; nobody would want to import all of Quamina, which is a fair-sized library,
just to parse REs. But then that other repo would become a Quamina dependency. And one of my favorite things about Quamina is
that it has
[0 dependencies!](/ongoing/When/202x/2024/09/04/0dependencies)

It’s not obvious what the right thing to do is; any ideas?

---

**Updated: 2024/12/13**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Dirkjan Ochtman](http://https//dirkjan.ochtman.nl/) (Dec 13 2024, at 14:17)

I’ll argue that Dependencies Are Good, Actually.

Assuming you can find high-quality dependencies with maintainers you trust (who will dutifully care about performance and security), you’re better off having dedicated ownership for each of the 5 little sub-problems your project needs to solve instead of worse is better, minimal attention copy/pasta like you find in every C/C++ project — languages which don’t have modern package management tooling to easy the pain of actually reusing modular code.

Reducing dependencies is a good thing, but doesn’t help when your potential dependencies were actually by the same maintainers anyway. 0-dependencies should be more about being careful which maintainers to trust than pushing hard on the dependency counter itself to stick to zero.

(Thus far my semi-impassioned response from the Rust side of the fence, where small dependencies are definitely a thing and where I, as a maintainer of a popular date/time library, am happy to have that library take a dependency on a different library whose sole job it is to find out which timezone the current code is running in across the gajillion platforms that people actually want to run this stuff on.)

*[[link](#c1734128263.780279)]*

From: [Ole Eichhorn](http://w-uh.com) (Dec 13 2024, at 22:58)

I’ve found ChatGPT is amazing at converting English into regex. I could never do it and debugging was impossible, but simply asking for and getting a working expression is supercool.

*[[link](#c1734159528.602312)]*

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

[![picture of the day](/o...