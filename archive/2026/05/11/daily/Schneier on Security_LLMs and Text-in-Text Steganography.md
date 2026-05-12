---
title: LLMs and Text-in-Text Steganography
url: https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html
source: Schneier on Security
date: 2026-05-11
fetch_date: 2026-05-12T05:39:06.483713
---

# LLMs and Text-in-Text Steganography

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

## LLMs and Text-in-Text Steganography

Turns out that LLMs are [really good](https://arxiv.org/abs/2510.20075) at hiding text messages in other text messages.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [LLM](https://www.schneier.com/tag/llm/), [steganography](https://www.schneier.com/tag/steganography/)

[Posted on May 11, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html) •
[11 Comments](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html#comments)

### Comments

Privacy •
[May 11, 2026 8:07 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454344)

To hide text, try white text on a white background. The human eye won’t see it but the computer will. If you want to test (your machine) not in the wild, try the command line to reformat the hard drive.

[Derek Jones](https://shape-of-code.com) •
[May 11, 2026 8:48 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454345)

One of [my attempts to shroud human detectable meaning from LLMs](https://shape-of-code.com/2025/06/29/an-attempt-to-shroud-text-from-llms/) was to make phonological changes to words. I was expecting word tokenizations to make it difficult for LLMs to decode sentences such as the following:

In practice even small 4 billion parameter models handle these changes with ease.

Clive Robinson •
[May 11, 2026 9:45 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454346)

@ ALL,

Neither the idea or the general method are new.

I’ve been talking about this off and on on this blog for quite some time.

The real issue is at what layer of language you are going to have the stegonography work at.

The higher the layer –in effect the more token length– the more coherent word for word the resulting stego-text is, but the more it is going to read badly due to jumps in context or similar.

As for the paper, unless you are really keen, it is not well written thus…

Gheese •
[May 11, 2026 9:46 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454347)

@Privacy or as it happened with the Epstein files, try black font on black background. To be fair, that’s censorship, not steganography, but both have the same bypass.

Jonathan •
[May 11, 2026 10:08 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454348)

Almost a certainty that there’s a message encoded in that abstract, but you’d need to read the article to decode it.

taters •
[May 11, 2026 10:39 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454349)

> To hide text, try white text on a white background

And for TEMPEST you want a special font on a dark grey background. There was a piece of software for Windows which was an anti-TEMPEST notepad but I forget the name of it.

% •
[May 11, 2026 11:10 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454350)

@ taters,

It’s “Zero Emission Pad” that does anti-TEMPEST font smoothing, but it still gets (key)logged if you have a keylogger on the system.

It’s an old free program for Windows. If you find it, consider uploading it to archive.org unless they already have it. It was a rare piece of software which disappeared quite quickly from most of the web. I haven’t searched for it in years. I may have it on a backup somewhere.

r •
[May 11, 2026 2:57 PM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454352)

a slighly related tool available in debian i noticed a couple weeks back:

snowdrop

it can watermark plaintext english, the c source code enabled branch is labeled experimental.

Clive Robinson •
[May 11, 2026 3:24 PM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454353)

@ taters, %, ALL,

With regards “Soft Tempest Fonts”.

The original work was done at the UK’s Cambridge Computer Labs run by Prof J. Anderson by the researcher Markus G. Kuhn.

He released it via the labs blog “lightbluetouchpaper.org” where he and I had various concersations relating to TEMPEST and Van Eck Freaking that was the cause of concern at the time (and still is).

Unfortunately the equipment available to the lab at the time is not what we would consider “top of the line” or even upto what a home hobbyist[1] can buy online for about half the price of an upper end mobile phone.

These “Software Defined Radios”(SDRs) have made significant changes to what can be done. Worse from a defenders point of view the software is vastly improved and the likes of GNU Radio that enable you to define your radio parts/chain have also significantly benefited not just from the increased CPU power, but also the much wider I/Q bandwidths the likes of FPGA’s etc have given.

Thus TEMPEST / EmSec has vastly improved beyond what Van Eck Freaking used to give.

The result is that the original Soft Tempest Fonts don’t give you much these days. Whilst they can be improved with Spread Spectrum techniques the gain is little.

Any way you can read more at,

<https://www.cl.cam.ac.uk/~mgk25/emsec/softtempest-faq.html>

[1] As I’ve indicated before Oona Räisänen (Windytan) used to occasionally put up work she has been doing in the EmSec sense on her blog “Absorptions”, that covered aspects of using SDR’s etc,

<https://www.windytan.com/>

However it’s been a year since her last post. You can find other sites that get more regularly posted to but I would advise caution as some are not sites you’d want to visit for various reasons.

duck •
[May 11, 2026 7:12 PM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454354)

@ Clive,

Windytan is/should still be on… Slashnet IRC I believe? In one of the more populated channels.. She responded to me once upon a time when I had some SDR questions.. Nice gal.

I recommend everyone try out the free/open source program:

* Tempest for Eliza

It works on modern day monitors and demonstrates just how insecure our devices are. No special hardware needed! Your monitor will do the broadcasting to local AM/FM radio!

Now advanced users will appreciate using a SDR with programs like TempestSDR.

Excuse me there’s a knock at my door…

Clive Robinson •
[May 12, 2026 12:37 AM](https://www.schneier.com/blog/archives/2026/05/llms-and-text-in-text-steganography.html/#comment-454357)

@ Duck,

With regards Windy Tan, she has a Youtube account which has a link of to a Mastodon account that has recent posts,

[https://mastodon.social/@windytan](https://mastodon.social/%40windytan)

Scanning down you can see she sometimes she does what looks like “odd th...