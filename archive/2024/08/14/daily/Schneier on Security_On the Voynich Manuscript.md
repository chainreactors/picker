---
title: On the Voynich Manuscript
url: https://www.schneier.com/blog/archives/2024/08/on-the-voynich-manuscript.html
source: Schneier on Security
date: 2024-08-14
fetch_date: 2025-10-06T18:05:52.014904
---

# On the Voynich Manuscript

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## On the Voynich Manuscript

Really interesting [article](https://www.theatlantic.com/magazine/archive/2024/09/decoding-voynich-manuscript/679157/?gift=YFkW3a8mqv4T0YBMneIYIuIiYZJAqQJorEylZzhFIOw&utm_source=copy-link&utm_medium=social&utm_campaign=share&fbclid=IwY2xjawEhtldleHRuA2FlbQIxMQABHdyEbPaL8wyhs9wMtkGXHfevH3pYDJ2kW9Oax8-NaxAEyKrmldht_ShcSg_aem_gPeUGAVQrTw8m61YZhwgig) on the ancient-manuscript scholars who are applying their techniques to the Voynich Manuscript.

No one has been able to understand the writing yet, but there are some new understandings:

> Davis presented her findings at the medieval-studies conference and [published them in 2020](https://muse.jhu.edu/pub/56/article/754633/pdf) in the journal *Manuscript Studies*. She had hardly solved the Voynich, but she’d opened it to new kinds of investigation. If five scribes had come together to write it, the manuscript was probably the work of a community, rather than of a single deranged mind or con artist. Why the community used its own language, or code, remains a mystery. Whether it was a cloister of alchemists, or mad monks, or a group like the medieval Béguines—a secluded order of Christian women—required more study. But the marks of frequent use signaled that the manuscript served some routine, perhaps daily function.
>
> Davis’s work brought like-minded scholars out of hiding. In just the past few years, a Yale linguist named Claire Bowern had [begun performing sophisticated analyses](https://campuspress.yale.edu/clairebowern/voynich/) of the text, building on the efforts of earlier scholars and on methods Bowern had used with undocumented Indigenous languages in Australia. At the University of Malta, computer scientists were figuring out how to analyze the Voynich with tools for natural-language processing. Researchers found that the manuscript’s roughly 38,000 words—and 9,000-word vocabulary—had many of the statistical hallmarks of actual language. The Voynich’s most common word, whatever it meant, appeared roughly twice as often as the second-most-common word and three times as often as the third-commonest, and so on—a touchstone of natural language known as Zipf’s law. The mix of word lengths and the ratio of unique words to total words were similarly language-like. Certain words, moreover, seemed to follow one another in predictable order, a possible sign of grammar.
>
> Finally, [each of the text’s sections](https://www.voynich.nu/illustr.html)—as defined by the drawings of plants, stars, bathing women, and so on—had different sets of overrepresented words, just as one would expect in a real book whose chapters focused on different subjects.
>
> Spelling was the chief aberration. The Voynich alphabet—if that’s what it was—appeared to have a conventional 20-odd letters. But compared with known languages, too many of those letters repeated in the same order, both within words and across neighboring words, like a children’s rhyme. In some places, the spellings of adjacent words so converged that a single word repeated two or three times in a row. A rough English equivalent might be something akin to “She sells sea shells by the sea shore.” Another possibility, Bowern told me, was something like pig Latin, or the Yiddishism—known as “shm-reduplication”—that begets phrases such as *fancy shmancy* and *rules shmules*.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [history of cryptography](https://www.schneier.com/tag/history-of-cryptography/)

[Posted on August 13, 2024 at 7:04 AM](https://www.schneier.com/blog/archives/2024/08/on-the-voynich-manuscript.html) •
[9 Comments](https://www.schneier.com/blog/archives/2024/08/on-the-voynich-manuscript.html#comments)

### Comments

jelo 117 •
[August 13, 2024 8:38 AM](https://www.schneier.com/blog/archives/2024/08/on-the-voynich-manuscript.html/#comment-439974)

> If five scribes had come together to write it, the manuscript was probably the work of a community, rather than of a single deranged mind or con artist.

… was probably the work of a community of deranged minds or con artists, rather than of a single deranged mind or con artist.

[Torsten Timm](https://independent.academia.edu/TorstenTimm) •
[August 13, 2024 9:46 AM](https://www.schneier.com/blog/archives/2024/08/on-the-voynich-manuscript.html/#comment-439975)

The article from the atlantic does not provide an accurate description of what we know about the Voynich manuscript.

For instance the article states “The mix of word lengths and the ratio of unique words to total words were similarly language-like.” The contrary is true. The word length distribution matches almost perfectly a binomial distribution and is therefore not language like (see Stolfi 2000 <https://www.ic.unicamp.br/~stolfi/voynich/00-12-21-word-length-distr/>). Jürgen Hermes states “When looking at word lengths the text of the VMS is astonishingly uniform (hardly any words have less than 3 or more than 10 characters). Even more surprising is the similar behaviour of type lengths and token lengths. Although Voynichese tokens are also slightly shorter on average than types, the word length distributions of both, types and tokens, is almost binomial” [Jürgen Hermes 2022, p. 2 <https://ceur-ws.org/Vol-3313/paper7.pdf%5D>.

The article also states: “Certain words, moreover, seemed to follow one another in predictable order, a possible sign of grammar.”

The article further states “Finally, each of the text’s sections—as defined by the drawings of plants, stars, bathing women, and so on—had different sets of overrepresented words, just as one would expect in a real book whose chapters focused on different subjects.”
However in natural languages the most frequent words “are distributed equally over the entire text, the so-called function words (like conjunctions, articles etc.). They do not appear contextual, but rather serve to implement grammatical structures, and they normally do not have co-occurring similar words of comparable frequency. In the VMS frequently used tokens differ from page to page” [Timm & Schinner 2020, p. 6].

Clive Robinson •
[August 13, 2024 9:53 AM](https://www.schneier.com/blog/archives/2024/08/on-the-voynich-manuscript.html/#comment-439976)

@ Bruce,

Let us assume it does make sense in a spoken language form.

It’s known that before Shakespear’s time although spoken words were consistent, the spelling of written words and what some might call grammar in the written form was not, and few cared.

Going back long prior to that, written language was used in a similar way to George Orwell’s various “New Speaks” to keep people segregated.

Further we know that “hiding text within text” in simple ways was also used to form hierarchies of people.

Such documents were used in hierarchies such as religions and have been found around the world.

The us...