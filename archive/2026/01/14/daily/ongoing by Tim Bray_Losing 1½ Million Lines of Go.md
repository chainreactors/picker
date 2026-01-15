---
title: Losing 1½ Million Lines of Go
url: https://www.tbray.org/ongoing/When/202x/2026/01/14/Unicode-Properties
source: ongoing by Tim Bray
date: 2026-01-14
fetch_date: 2026-01-15T03:30:23.135831
---

# Losing 1½ Million Lines of Go

# Losing 1½ Million Lines of Go

![Opens, and navigates to, search input field](/ongoing/misc/smallmag.png)

Confession: My title is clickbait-y, this is really about building on the Unicode Character Database to support
character-property regexp features in
[Quamina](https://github.com/timbray/quamina).
Just halfway there, I’d already got to 775K lines of generated code so I abandoned that particular approach. Thus, this
is about (among other things) *avoiding* those 1½M lines. And really only of interest to people whose
pedantry includes some combination of Unicode, Go programming, and automaton wrangling. Oh, and GenAI, which (\*gasp\*) I
think I should maybe have used.

Character property matching ·
I’m talking about regexp incantations like `[\p{L}\p{Zs}\p{Nd}]`, which matches anything that Unicode classifies
as a letter, a space, or a decimal number. (Of course, in Quamina “`\`” is “`~`”
[for excellent reasons](/ongoing/When/202x/2024/12/12/Quamina-Regular-Expression-Series#p-7), so that reads
`[~p{L}~p{Zs}~p{Nd}]`.)

(I’m writing about this now because I just launched
[a PR](https://github.com/timbray/quamina/pull/465) to enable this feature. Just one more to go before I can
release a new version of Quamina with full regexp support, yay.)

Finding the properties ·
To build an automaton that matches something like that, you have to find out what the character properties are.
This information comes from the
[Unicode Character Database](https://www.unicode.org/ucd/), helpfully provided online by the Unicode consortium.
Of course, most programming languages have libraries that will help you out, and
[that includes Go](https://pkg.go.dev/unicode#pkg-variables), but I didn’t use it.

Unfortunately, Go’s library doesn’t get updated every time Unicode does. As of now, January 2026,
it’s still stuck at Unicode 15.0.0, which
[dates to September 2023](https://www.unicode.org/history/publicationdates.html); the latest version is 17.0.0, last
September. Which means there are plenty of Unicode characters Go doesn’t know about, and I didn’t want Quamina to settle
for that.

So, I fetched and parsed the famous master file from
[www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt](https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt).
Not exactly rocket science, it’s a flat file with `;`-delimited fields, of which I only cared about the first
and third. There are some funky bits, such as the pair of nonstandard lines indicating that the Han characters occur
between U+4E00 and U+9FFF inclusive; but still not really taxing.

The output is, for each Unicode category, and also for each category’s complement (`~P{L}` matches everything
that’s *not* a letter; note the capital `P`), a list of pairs of code points, each pair indicating a subset
of the code space where that category applies. For example, here’s the first line of character pairs with category `C`.

```
    {0x0020, 0x007e}, {0x00a0, 0x00ac}, {0x00ae, 0x0377},
```

How many pairs of characters, you might wonder? There are 37 categories
and it’s all over the place but adds up to a lot. The top three categories
are L with 1,945 pairs, Ll at 664, and M at 563. At the other end are Zl and Zp, both with just 1.
The total number of pairs is 14,811, and the generated Go code is a mere 5,122 lines.

Character-property automata ·
Turning these creations into finite automata was straightforward: I already had the code to handle regexps like
`[a-zA-Z0-9]`, logically speaking the same problem. But, um, it wasn’t fast. My favorite unit test, an exercise in
[sample-driven development](/ongoing/When/202x/2024/12/12/QRS-Parsing-Regular-Expressions#p-1) with 992 regexps,
suddenly started taking multiple seconds, and my whole unit-test suite expanded from around ten seconds to over twelve; since I
tend to run the unit tests every time I take a sip of coffee or scratch my head or whatever, this was painful. And it occurred to
me that it would be painful in practice to people who want for some good reason or another to load up a bunch of
Unicode-property patterns into a Quamina instance.

So, I said to myself, I’ll just precompute all the automata and serialize them into code. And now we
get to the title of this essay; my data structure is a bit messy and ad-hoc and just for the categories, before I got to the
complement versions, I was generating 775K lines of code.

Which worked! But, it was 12M in size and while Go’s runtime is fast, there was a painful pause while it absorbed those data
structures on startup. Also, opening the generated file regularly caused my IDE
([Goland](https://www.jetbrains.com/go/)) to crash. And I was only halfway there. The whole approach was painful to
work with so I went looking for Plan B.

The code that generates the automaton from the code point pairs is pretty well the simplest thing that could possibly work
and it was easy to understand but burned memory like crazy. So I worked for a bit on making it faster and
cheaper, but so far have found no low-hanging fruit.

I haven’t given up on that yet. But in the meantime, I remembered
Computer Science’s general solution for all performance problems, by which I mean caching. So now, any Quamina instance will
compute the automaton for a Unicode property the first time it’s used, then remember it. So now Quamina’s speed at adding
Unicode-property regexps to an instance has increased from 135/second to 4,330, a factor of thirty and Good Enough For
Rock-n-Roll.

It’s worth pointing out that while *building* these automata is a heavyweight process, Quamina can use them to match
input messages at its typical rates, hundreds of thousands to millions per second. Sure, these automata are “wide”, with lots of
branches, but they’re also shallow, since they run on UTF-8 encoded characters whose maximum length is four and average length
is much less. Most times you only have to take one or two of those many branches to match or fail.

Should I have used Claude? ·
This particular segment of the Quamina project included some *extremely* routine programming tasks, for example
fetching and parsing
UnicodeData.txt, computing the sets of pairs, generating Go code to serialize the automata, reorganizing source files that had
become bloated and misshapen, and writing unit tests to confirm the results were correct.

Based on my own
[very limited experience](/ongoing/When/202x/2025/07/01/First-AI-Code) with GenAI code, and in particular after
reading Marc Brooker’s
[On the success of ‘natural language programming’](https://brooker.co.za/blog/2025/12/16/natural-language.html) and
Salvatore (“antirez”) Sanfilippo’s
[Don't fall into the anti-AI hype](https://antirez.com/news/158), I guess I’ve joined the camp that thinks
this stuff is going to have a place in most developers’ toolboxes.

I think Claude could have done all that boring stuff, including acceptable unit tests, way faster than I did.
And furthermore got it right the first time, which I didn’t.

So why didn’t I use Claude? Because I don’t have the tooling set up and I was impatient and didn’t want to invest the time in
getting all that stuff going and improving my prompting skills. Which reminds me of all the times I’ve been trying to evangelize other
developers on a better way to do things and was greeted by something along the lines of “Fine, but I’m too busy right now, I’ll
just going on doing things the way I already know how to.”

Does this mean I’m joining the “GenAI is the future and our investments will pay off!” mob? Not in the slightest. I still
think it’s overpriced, overhyped, and mostly ill-suited to the business applications that “thought leaders” claim for it.
That word “mostly” excludes the domain of code; as I said
[here](/ongoing/When/202x/2025/09/26/GenAI-Predictions#p-5), “It’s pretty obvious that LLMs are better at predicting code
sequences than human language.”

And, as it turns out, the domain of Developer Tools has never been a Big Business by the standards of GenAI’s prom...