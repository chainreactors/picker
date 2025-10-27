---
title: 1965 Cryptanalysis Training Workbook Released by the NSA
url: https://www.schneier.com/blog/archives/2025/09/1965-cryptanalysis-training-workbook-released-by-the-nsa.html
source: Schneier on Security
date: 2025-09-03
fetch_date: 2025-10-02T19:34:43.578414
---

# 1965 Cryptanalysis Training Workbook Released by the NSA

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

## 1965 Cryptanalysis Training Workbook Released by the NSA

In the early 1960s, National Security Agency cryptanalyst and cryptanalysis instructor Lambros D. Callimahos coined the term “Stethoscope” to describe a diagnostic computer program used to unravel the internal structure of pre-computer ciphertexts. The term appears in the newly declassified September 1965 document *[Cryptanalytic Diagnosis with the Aid of a Computer](https://www.governmentattic.org/59docs/NSAlDCCDAC1965.pdf)*, which compiled 147 listings from this tool for Callimahos’s [course](https://ia601207.us.archive.org/22/items/Legacy_Callimahos-nsa/Legacy_Callimahos.pdf), [CA-400: NSA Intensive Study Program in General Cryptanalysis](https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cryptologic-spectrum/Callimahos_Course.pdf).

The listings in the report are printouts from the Stethoscope program, run on the NSA’s Bogart computer, showing statistical and structural data extracted from encrypted messages, but the encrypted messages themselves are not included. They were used in NSA training programs to teach analysts how to interpret ciphertext behavior without seeing the original message.

The listings include elements such as frequency tables, index of coincidence, periodicity tests, bigram/trigram analysis, and columnar and transposition clues. The idea is to give the analyst some clues as to what language is being encoded, what type of cipher system is used, and potential ways to reconstruct plaintext within it.

Bogart was a special-purpose electronic computer tailored specifically for cryptanalytic tasks, such as statistical analysis of cipher texts, pattern recognition, and diagnostic testing, but not decryption per se.

Listings like these were revolutionary. Before computers, cryptanalysts did this type of work manually, painstakingly counting letters and testing hypotheses. Stethoscope automated the grunt work, allowing analysts to focus on interpretation, and cryptanalytical strategy.

These listings were part of the Intensive Study Program in General Cryptanalysis at NSA. Students were trained to interpret listings without seeing the original ciphertext, a method that sharpened their analytical intuitive skills.

Also mentioned in the report is Rob Roy, another NSA diagnostic tool focused on different cryptanalytic tasks, but also producing frequency counts, coincidence indices, and periodicity tests. NSA had a tradition of giving codebreaking tools colorful names—for example, DUENNA, SUPERSCRITCHER, MADAME X, HARVEST, and COPPERHEAD.

Tags: [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [history of cryptography](https://www.schneier.com/tag/history-of-cryptography/), [NSA](https://www.schneier.com/tag/nsa/)

[Posted on September 2, 2025 at 7:08 AM](https://www.schneier.com/blog/archives/2025/09/1965-cryptanalysis-training-workbook-released-by-the-nsa.html) •
[7 Comments](https://www.schneier.com/blog/archives/2025/09/1965-cryptanalysis-training-workbook-released-by-the-nsa.html#comments)

### Comments

KC •
[September 2, 2025 10:33 AM](https://www.schneier.com/blog/archives/2025/09/1965-cryptanalysis-training-workbook-released-by-the-nsa.html/#comment-447506)

From Mr. Callimahos’ “Invitation to Learning”:

“Errors (but nonduplicative!) are encouraged, as they are particularly instructive to the entire class; without errors, there is no assurance of complete understanding. In other words, if you breeze through problems, you are on the wrong problems, or in the wrong course […]

You can now look forward to 18 weeks of sheer delight!”

Some lessons are timeless

Clive Robinson •
[September 2, 2025 10:34 AM](https://www.schneier.com/blog/archives/2025/09/1965-cryptanalysis-training-workbook-released-by-the-nsa.html/#comment-447507)

@ ALL,

@ Bruce notes,

> “In the early 1960s, National Security Agency cryptanalyst and cryptanalysis instructor Lambros D. Callimahos coined the term “Stethoscope” to describe a diagnostic computer program used to unravel the internal structure of pre-computer ciphertexts.” … “Bogart was a special-purpose electronic computer tailored specifically for cryptanalytic tasks, such as statistical analysis of cipher texts, pattern recognition, and diagnostic testing, but not decryption per se.”

Seymour Cray’s Bogart was indeed a not just special-purpose it was large, power hungry and very expensive. But quickly became less expensive and a version was sold to others not just the NSA.

You can read more,

<https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/history-today-articles/10%202018/05OCT2018%20SEYMOUR%20CRAY%20and%20NSA.pdf?ver=P3xsKeHprvcBBChHKi77Gw%3d%3d>

However in a little over a decade Bogart was effectively redundant, as the clever use of 8 bit computer chips had out paced it. And smart kids with access to Apple ][ computers with dual floppy drives were developing their own programs based on what had become public knowledge by the end of the 1970’s.

[Frode Weierud](https://cryptocellar.org) •
[September 5, 2025 1:55 AM](https://www.schneier.com/blog/archives/2025/09/1965-cryptanalysis-training-workbook-released-by-the-nsa.html/#comment-447558)

@ ALL,

If you are interested in cryptodiagnosis, three historical texts come to mind; alas, they are still classified. They and other cryptanalytical texts were presented to the readers of the NSA Cryptolog, Vol. XVI, No. 1, 1st Issue, 1989, Page 13–14 in an article entitled ”One Cryptanalyst’s One-Foot Shelf.” <https://media.defense.gov/2021/Jul/01/2002754974/-1/-1/0/CRYPTOLOG_114.PDF>

The first text is historical for many reasons, but most importantly because it is written by the British mathematician Irving J. Good. If any of these texts should be declassified and published, this is the one.

**STANDARD REAGENTS AND DIAGNOSTICIAN’S DICTIONARY by. I. J. Good (Blue Ribbon Series, Monograph No. 11)**

This most valuable tome, unfortunately, is out of print, and no reissue is planned for the near future. If you do not have a copy, make friends with someone who does, especially if he is about to retire. Meanwhile, there’s a copy in the CA library that you can read.

The subsequent text is L. D. Callimahos’ well-known
**ARS CONJECTANDI: THE FUNDAMENTALS OF CRYPTODIAGNOSIS by L. D. Callimahos (Blue Ribbon Series, Monograph No. 18)**
It’s neatly put in the foreword by Dr. Tordella: ”This monograph represents a milestone in cryptologic literature: it is the first detailed and comprehensive exposition of the fundamentals of cryptodiagnosis, treating the techniques and procedures of manipulating data and recognizing and interpreting phenomena. Broadly theoretical in its treatment of the principles of diagnosis, it is applicable to both manual and machine cryptosystems, whether the diagnostic examination is performed by manual methods or with machine aids.

”Any cryptanalyst,...