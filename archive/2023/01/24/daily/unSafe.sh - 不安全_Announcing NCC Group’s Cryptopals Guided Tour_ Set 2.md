---
title: Announcing NCC Group’s Cryptopals Guided Tour: Set 2
url: https://buaq.net/go-146547.html
source: unSafe.sh - 不安全
date: 2023-01-24
fetch_date: 2025-10-04T04:36:58.937020
---

# Announcing NCC Group’s Cryptopals Guided Tour: Set 2

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Announcing NCC Group’s Cryptopals Guided Tour: Set 2

Hello and welcome to NCC Group’s Cryptopals guided tour! This post is the second in a series of
*2023-1-23 22:0:0
Author: [research.nccgroup.com(查看原文)](/jump-146547.htm)
阅读量:19
收藏*

---

Hello and welcome to NCC Group’s Cryptopals guided tour! This post is the second in a series of eight installments ([previously](https://research.nccgroup.com/2021/12/10/announcing-ncc-groups-cryptopals-guided-tour/)) covering the solutions to the [Cryptopals Crypto Challenges](https://cryptopals.com/).

For those who don’t know, Cryptopals is a series of eight sets of challenges covering common cryptographic constructs and common attacks on them. You can read more about Cryptopals at <https://cryptopals.com/>.

There’s a lot of practical knowledge wrapped up in these challenges, and working through them is an excellent way for programmers to learn more about cryptography – or for cryptographers to learn more about programming. We strongly encourage you to give them a try and to see how far you can get on your own.

These videos are here for you to check your work after completing a challenge, or to see how else you might’ve solved it – or for when you get stuck, can’t get yourself unstuck, and are looking for a nudge in the right direction. We *strongly* encourage you to try “learning by doing” before watching the videos. You’ll get more out of them that way!

Rather than just giving you a walkthrough that rushes you to the finish line, with this guided tour we’ve tried to encourage you to slow down and see the sights. That’s why, for set two, we’ve added a section to the start of each video where we discuss the problem in detail, with visual aids, *before writing any code.* The idea is that before putting a single line into the editor, we should know exactly what we’re trying to do, cryptographically speaking – so that we can focus on how we’re going to do it.

Each video comes with a timestamped index of content so you can skip around as desired. Many of the videos also contain lists of links for further reading.

Oh, and by the way: if you just want to see the finished solution code, you can find that [here](https://github.com/nccgroup/cryptopals-py). The videos are also available as a playlist [here](https://www.youtube.com/playlist?list=PLWvDpnCcem1P6i8pZm2x7KHp5iaxwrK_P).

Now, without further ado, here are the videos for Cryptopals Set 2. We hope you find them helpful, and we look forward to sharing the videos for the following challenge sets as soon as they’re ready.

## Set 2, Challenge 9: Implement PKCS#7 padding

Challenge link: <https://cryptopals.com/sets/2/challenges/9>

00:00 – Intro

Further reading:
<https://www.rfc-editor.org/rfc/rfc2898#section-6.1.1><https://www.rfc-editor.org/rfc/rfc5652#section-6.3><https://www.rfc-editor.org/rfc/rfc1321#section-3.1><https://bearssl.org/constanttime.html#cbc-padding>

Note: The discussion of SIV is intended to refer to GCM-SIV ([RFC 8452](https://www.rfc-editor.org/rfc/rfc8452.html), not to be confused with [RFC 5297](https://www.rfc-editor.org/rfc/rfc5297)).

## Set 2, Challenge 10: Implement CBC mode

Challenge link: <https://cryptopals.com/sets/2/challenges/10>

00:00 – Intro
00:30 – Start of discussion
01:15 – Construction of CBC
02:00 – Alternate diagrams
02:30 – Motivation: IV
03:25 – Motivation: chaining step
04:08 – Detour: CTS
06:41 – Limitations of CBC
07:05 – Problem 1: performance
07:45 – Problem 2: impossible differentials
09:07 – Problem 3: IV reuse
10:19 – Start of screencast
11:00 – Implementing aes\_cbc\_dec()
14:30 – Writing main block
15:30 – Playing that funky music

Further reading:
<https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation><https://en.wikipedia.org/wiki/Ciphertext_stealing><https://bearssl.org/speed.html#symmetric-encryption>

## Set 2, Challenge 11: An ECB/CBC detection oracle

Challenge link: <https://cryptopals.com/sets/2/challenges/11>

00:00 – Intro
00:25 – Defining “oracle”
01:08 – Problem statement
02:00 – Comparison to challenge 8
02:22 – Solution strategy (high-level)
03:22 – Solution strategy (detailed)
04:00 – Checking our work
04:15 – What about IVs?
05:00 – Second solution
06:06 – Start of screencast
06:30 – Discussing get\_encryption\_oracle()
09:08 – Discussing detector()
10:15 – Discussing main block

Further reading:
<https://www.dcc.fc.up.pt/~acm/turing-phd.pdf><https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation>

## Set 2, Challenge 12: Byte-at-a-time ECB decryption (Simple)

Challenge link: <https://cryptopals.com/sets/2/challenges/12>

00:00 – Intro
00:40 – Determining block length
01:00 – Determining padding length
01:40 – Determining suffix length
02:03 – Detecting ECB mode
02:20 – Solution strategy (first block)
04:20 – What about the 17th byte?
04:55 – Solution strategy (full)
05:20 – Optimizing for oracle queries
06:02 – Revealing the message
06:52 – Start of screencast
07:17 – Discussing make\_oracle()
08:05 – Discussing find\_block\_size\_and\_postfix\_len()
09:40 – Shilling for Big Static Analysis
09:56 – Discussing detect\_ecb()
10:15 – Discussing guess\_byte()
11:35 – Discussing main block
12:40 – Explaining the transpose-and-flatten construct
15:45 – “Hollywood-style” decryption
16:55 – “Now this is how hacking is supposed to look”

## Set 2, Challenge 13: ECB cut-and-paste

Challenge link: <https://cryptopals.com/sets/2/challenges/13>

00:00 – Intro
00:25 – Discussing chosen-ciphertext attacks
01:06 – Token format
01:36 – Adding admin block
02:12 – Visualizing the attack
02:37 – Start of screencast
02:50 – Discussing profile\_parse()
04:02 – Discussing profile\_build()
04:32 – Discussing profile\_for()
05:27 – Big detour: dictionary iteration order
07:21 – Discussing enc\_profile() & dec\_profile()
07:30 – Discussing do\_evil()
08:23 – Discussing main block

## Set 2, Challenge 14: Byte-at-a-time ECB decryption (Harder)

Challenge link: <https://cryptopals.com/sets/2/challenges/14>

00:00 – Intro
00:48 – Comparison to challenge 11
01:25 – Finding the prefix length
02:50 – Deducing the oracle’s plaintext layout
04:05 – Start of screencast
04:25 – Implementing find\_prefix\_length()
07:55 – Implementing wrap\_oracle()
11:00 – Refactoring challenge 12
13:30 – Retesting challenge 12
13:50 – Writing main block
15:50 – Troubleshooting
16:25 – Running the attack

## Set 2, Challenge 15: PKCS#7 padding validation

Challenge link: <https://cryptopals.com/sets/2/challenges/15>

00:00 – Intro
00:16 – Callback to challenge 9
00:48 – Reviewing strip\_pkcs7()
01:30 – Copying in test vectors
03:08 – Refactoring
04:02 – Running the tests
04:10 – Discussing unpadding in context (BearSSL example)

Further reading:
<https://bearssl.org/constanttime.html#cbc-padding>[BearSSL code pointer](https://www.bearssl.org/gitweb/?p=BearSSL;a=blob;f=src/ssl/ssl_rec_cbc.c;h=c0806049e3cdc8b7135ea4c9968b60e99a7f4770;hb=5f045c759957fdff8c85716e6af99e10901fdac0#l97)

## Set 2, Challenge 16: CBC bitflipping attacks

Challenge link: <https://cryptopals.com/sets/2/challenges/16>

00:00 – Intro
01:20 – Reviewing CBC mode
01:45 – Propagation of XOR differentials
02:22 – Problem statement
03:05 – Strategizing
04:03 – Solution strategy
04:39 – Dealing with junk bytes
05:43 – Start of screencast
06:47 – Too Much Crypto vs Not Enough Crypto
07:27 – Generating global parameters
08:12 – Writing wrap\_userdata()
08:45 – Showing how to look up URL-escaping codes
09:30 – Writing check\_for\_admin()
10:45 – Writing make\_admin()
13:20 – Writing main block
13:57 – Testing the script

Further reading:
<https://eprint.iacr.org/2019/1492.pdf>

## Thank you!

Before wrapping ...