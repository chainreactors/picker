---
title: Real-World Steganography
url: https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html
source: Schneier on Security
date: 2023-01-21
fetch_date: 2025-10-04T04:31:27.459534
---

# Real-World Steganography

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

## Real-World Steganography

From an [article](https://www.bbc.com/news/world-asia-china-64206950) about Zheng Xiaoqing, an American convicted of spying for China:

> According to a Department of Justice (DOJ) indictment, the US citizen hid confidential files stolen from his employers in the binary code of a digital photograph of a sunset, which Mr Zheng then mailed to himself.

EDITED TO ADD (2/14): The 2018 [criminal complaint](https://www.courtlistener.com/docket/14983061/1/united-states-v-zheng/) has a “Steganography Egress Summary” that spends about 2 pages describing Zheng’s steps (p 6-7). That document has some really good detail.

Tags: [China](https://www.schneier.com/tag/china/), [espionage](https://www.schneier.com/tag/espionage/), [steganography](https://www.schneier.com/tag/steganography/)

[Posted on January 20, 2023 at 7:25 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html) •
[38 Comments](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html#comments)

### Comments

PaulBart •
[January 20, 2023 8:12 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416217)

So what makes this stolen technology, American? Does GE only allow US citizens to be on board of directors and executive officers? Aren’t we all one big diverse, inclusive, and equitable bunch of peoples? Or do nation states, beholden to their elites, think differently?

TimH •
[January 20, 2023 10:05 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416219)

I doubt that the stenography was just “found”. There’s much more to the story.

Q •
[January 20, 2023 10:07 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416220)

Using images for steganography is not good. The statistics of the image get all messed up and it becomes obvious which images have hidden data. If that “hidden” data is not encrypted then you just lost your freedom. And sometimes even if it is encrypted you still lose your freedom, check with the laws of the country you are in.

Andy •
[January 20, 2023 10:23 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416221)

Still amazed by the crude methods used by these so called “spies” to supposedly steal corp or gov secrets. Or perhaps those are the ones caught or publicized. Pretty much anybody knows that most activities on an enterprise network are recorded, fairly cheaply. So why would someone e-mail themselves anything? Or do the other silly things we hear super spies from Russia/Iran/China are doing – using thumb drives, uploading files or printing? Don’t these people receiving even a basic briefing from their handlers? Maybe it’s a dragnet designed to catch low hanging fruit.

Peter A. •
[January 20, 2023 10:30 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416222)

Theorizing about image steganography: how easy or hard it would be to hide a message in “sensor noise”, i.e. lowest significant bits of pixels’ luminosity values. I realize that sensor noise is uneven throughout the 2D matrix of pixels, so a special encoding scheme would have to be used to mimic spatial and statistical distribution of noise.

Chelloveck •
[January 20, 2023 10:38 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416223)

@TimH: I don’t know what happened, but I like to think they got suspicious when an 800×600 JPEG of a kitten weighed in at over 900 MB.

yet another bruce •
[January 20, 2023 10:53 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416224)

RAW FTW

Clive Robinson •
[January 20, 2023 11:55 AM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416226)

@ TimH, ALL,

Re : There has to be more to it.

> “I doubt that the stenography was just “found”. There’s much more to the story.”

Stenography is neither coding or ciphering it’s just hiding.

As @Q has noted anyone with any knowledge which “should” include a spy, would these days pre-encrypt the data such that “finding it” reveled nothing but high strength cryptography at best.

Importabtly most PC’s come with such tools built in if you know how to access it (again not particularly hard). Heck a lot of \*nix come with “Command Line Tools” by default.

But as @Andy has noticed, there is a considerable gap between what is alledged and the very basics, hence his surprise.

For those reading along it’s “not new” for the FBI to “invent/manufacture” “Chinese Spys” they have done it before when the US executive has been banging the drum about how unfair it is that China are now doing what the US used to do…

But encryption is insufficient as @Peter A. Has noted because whilst the bottom bits of an image superficially appear random, they are not. You can find utilities written to demonstrate this from back last century.

Thus you have to analyse the sensor not just in 2D but actually more dimentions to pull out the offset biases that apply at that level of sensor illumination. And apply the bias.

How this can be done with “Spread Spectrum”(SS) techniques was discussed adnausium in the mid 1990’s with “Digital watermarking”(DW). All of which came to a fairly dramatic end, when the UK Cambridge Lab released a utility that provided minor distortion to inages that whilst not noticeably chwnging the picture to “hunan perception” totally Ban-Jaxed the DW system.

However the fact is that the SS DW did quite successfully hide small amounts of data in images that could not be “pulled out” thus has a degree of viability.

But note the “small amounts” we are talking maybe 1% or so of the image size.

Which brings us to the next point that @Chelloveck raised, we are not talking about a small amount of data.

A simple look at the file meta-data would tell even a non proffessional that there was something wrong with the file…

I’m sure “all these alledged suspect mistakes” will convince a non technical jury, but in my head just as it would appear every person who has posted sofar there is lets be polite, a distinct suspicion that there is,

“A lot we’ve not been told”

And unlike the alledged suspect the FBI sure has previous experience on creating “fall guys” when it’s politically expedient to have a few…

I’m not going to say what I think other than so far it smells like the cats breakfast has been left in the sun… So I for one would like to see a lot lot more.

Diplomacy is still good •
[January 20, 2023 12:34 PM](https://www.schneier.com/blog/archives/2023/01/real-world-steganography.html/#comment-416227)

in my opinion:

Use of either “S” word is unfair and controversial and advertises to the wrong recipients. The other troublesome word is the “T” word.

“it is not not yet a secure time for me to substantiate...