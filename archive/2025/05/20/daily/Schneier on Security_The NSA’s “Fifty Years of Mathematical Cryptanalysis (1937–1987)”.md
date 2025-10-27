---
title: The NSA’s “Fifty Years of Mathematical Cryptanalysis (1937–1987)”
url: https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html
source: Schneier on Security
date: 2025-05-20
fetch_date: 2025-10-06T22:28:38.194847
---

# The NSA’s “Fifty Years of Mathematical Cryptanalysis (1937–1987)”

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

## The NSA’s “Fifty Years of Mathematical Cryptanalysis (1937–1987)”

In response to a FOIA request, the NSA released “[Fifty Years of Mathematical Cryptanalysis (1937-1987)](https://www.governmentattic.org/58docs/NSA50YrsMathCrypt1988.pdf),” by Glenn F. Stahly, with a lot of redactions.

Weirdly, this is the second time the NSA has declassified the document. John Young got a [copy](https://archive.org/details/NSAFiftyYearsOfMathematicalCryptanalyisis) in 2019. This one has a few less redactions. And nothing that was provided in 2019 was redacted here.

If you find anything interesting in the document, please tell us about it in the comments.

Tags: [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [mathematics](https://www.schneier.com/tag/mathematics/), [NSA](https://www.schneier.com/tag/nsa/), [reports](https://www.schneier.com/tag/reports/)

[Posted on May 19, 2025 at 7:06 AM](https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html) •
[13 Comments](https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html#comments)

### Comments

Clive Robinson •
[May 19, 2025 9:04 AM](https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html/#comment-445343)

@ Bruce,

You have two copies of the same document with redactions.

If might be interesting to see in effect “what has become shown” in the latest version that was not shown in the previous version.

Then do a couple of things with it,

Firstly, to compare to advancements in academic and industry to what has become revealed.

Secondly, by “patchworking” get an insight into other areas the NSA was methodically investigating at the time.

Thirdly, by analysing the size, shape and location of still redacted sections make “educated” guesses about the possible areas of mathematics that are within.

Fourthly, get a feel for areas that the NSA was not investigating for various reasons, thus by inference see why they followed some areas of investigation not others.

Fifthly, having do this potentially come up with new FOI requests.

I’m sure others will be able to add to the list 😉

Geoffrey Nicoletti •
[May 19, 2025 10:11 AM](https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html/#comment-445345)

I thought the document was especially useful in the argument over who has the advantage…cryptanalyst? cryptographer? Instead of being outside of the process, you are listening from the inside on the matter. All conclusions by we, the readers, is salted by the fact that Stahly’s report pre-dates hacking impact of the Internet and current staggering impact of AI.

AlexT •
[May 19, 2025 5:20 PM](https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html/#comment-445351)

Not my field of expertise but can we really assume that there are groundbreaking concepts / findings that would still need to be classified almost 40 years later ?

Clive Robinson •
[May 19, 2025 7:24 PM](https://www.schneier.com/blog/archives/2025/05/the-nsas-fifty-years-of-mathematical-cryptanalysis-1937-1987.html/#comment-445354)

@ Alex T,

You ask,

> “… can we really assume that there are groundbreaking concepts / findings that would still need to be classified almost 40 years later ?”

The simple answer is yes, but it’s getting less so as academia and industry see the worth of Privacy and Security.

Not sure how old you are but the early history of DES was a bit of an eye opener.

The “public responses” to the request were often little more than upgraded paper and pencil ciphers.

The IBM cipher was designed by some of the best outside of the Puzzle Palace and initially had some quite critical weaknesses. The basic idea was to build a “mixing function” and ended up based on a system for “Information Friend or Foe”(IFF) designed for aircraft. The idea behind it came from Horst Feistel and subsequently became known as the Feistel Round (and is the basis for most block ciphers).

However it has some issues that were not known even to the NSA at the time. However one of the IBM team Don Coppersmith realised that it was there and found a way to “design it out”. The idea and the method remained classified for many years. In fact even when the method was discovered by others the NSA kept quiet untill someone demonstrated that it must have been used during the DES design process.

Do I need to mention the embarrisment of the “Dual Eliptic Curve Digital Random Bit Generator”(Dual\_EC\_DRBG)?

How long do you think that would have remained secret if not realised by someone who was working at Microsoft?

I’ve mentioned before that the design of “Mechanical Cipher Systems” that got used for “field ciphers” had an interesting issue. When you look at their “key space” you find the keys have varying strengths some secure by WWII standards and some ridiculously weak.

The person behind this stratagem was working at the private research “Riverbank Laboratory” by the name of William Friedman. He probably thought it up during WWI.

The idea is that any field cipher machine is going to fall into the hands of the enemy one way or another, it can not be avoided.

Thus depending on the enemies skills they might decide for several reasons to copy it (The WWII German Enigma and British Typex were logically the same).

If they were not very skilled or had a thought to get around certain “Key Material”(KeyMat) that the Germans had with Enigma, they could end up using on a random basis a mixture of strong and weak keys.

The thing is if a weak key gets broken the message gets discovered with some effort. However if the message gets built into a “card index” then you end up with sufficient “probable plaintext” that can make breaking even the strong keys fairly trivial.

Now the way around this if you know which are strong keys and which are weak is to issue “Key Tables” that were strong from a central “Key Management”(KeyMan) system. If the enemy were less adept then they would either issue weak keys or use a key generation method that would throw up weak keys based on probability.

This led onto William Friedman and his students coming up with such weak key strong key systems and it was not till something like a century later with Crypto AG in Zug Switzerland that the idea of different key strength systems became clear.

The lesson from this was “random was not the way to go” when designing parts of your cipher system like the wiring intervals one rotor wheels. A lesson that still is not much talked about.

Another area where things were kept secret even long after it was known in academia was “Linear Feedback Shift Registers”(LFSR). Yes they can produce very long sequences but they are actually almost as easy to predict as XORing t...