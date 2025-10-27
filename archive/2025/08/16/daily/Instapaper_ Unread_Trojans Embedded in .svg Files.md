---
title: Trojans Embedded in .svg Files
url: https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html
source: Instapaper: Unread
date: 2025-08-16
fetch_date: 2025-10-07T00:49:48.916385
---

# Trojans Embedded in .svg Files

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

## Trojans Embedded in .svg Files

Porn sites are [hiding code](https://arstechnica.com/security/2025/08/adult-sites-use-malicious-svg-files-to-rack-up-likes-on-facebook/) in .svg files:

> Unpacking the attack took work because much of the JavaScript in the .svg images was heavily obscured using a custom version of “JSFuck,” a technique that uses only a handful of character types to encode JavaScript into a camouflaged wall of text.
>
> Once decoded, the script causes the browser to download a chain of additional obfuscated JavaScript. The final payload, a known malicious script called Trojan.JS.Likejack, induces the browser to like a specified Facebook post as long as a user has their account open.
>
> “This Trojan, also written in Javascript, silently clicks a ‘Like’ button for a Facebook page without the user’s knowledge or consent, in this case the adult posts we found above,” Malwarebytes researcher Pieter Arntz wrote. “The user will have to be logged in on Facebook for this to work, but we know many people keep Facebook open for easy access.”

This isn’t a new trick. We’ve seen Trojaned .svg files before.

Tags: [malware](https://www.schneier.com/tag/malware/), [pornography](https://www.schneier.com/tag/pornography/)

[Posted on August 15, 2025 at 7:07 AM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html) •
[12 Comments](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html#comments)

### Comments

James N. Kennett •
[August 15, 2025 8:40 AM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447195)

Come back Flash! All is forgiven!

Santana •
[August 15, 2025 9:52 AM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447197)

Hiding code in .svg files is not a problem. But Facebook having CSRF vulnerabilities is.

[Mexaly](http://xkcd.com/722) •
[August 15, 2025 11:40 AM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447201)

Facebook is not for me, so, meh.

lurker •
[August 15, 2025 1:32 PM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447204)

As detestable as JavaScript is, and as evil as obfuscated .js is, this hack relies on the sucker having a valid FB account open while browsing porn. Surely that’s a deathwish …

Clive Robinson •
[August 15, 2025 3:00 PM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447205)

@ Bruce, ALL,

With regards,

> “This isn’t a new trick. We’ve seen Trojaned .svg files before.”

Not just SVG files… Which set off a thought…

We’ve seen so many vulnerabilities in different graphics files from BMP, PDF, JPEG, etc, etc, I could not think of any graphics file formats that had not been abused in some way.

Often the weakness is the interpreter in the application used to take the compressed image format and in the process of expanding it to a display format to display it gets abused.

In fact a little more thought gave rise to the realisation that either the more compression in a file or the more compression formats decoded by the application the more likely it is to have exploitable vulnerabilities.

Especially in libraries of code that have high code reuse.

Clive Robinson •
[August 15, 2025 3:20 PM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447206)

@ ALL,

The end of the article closes with two statments,

> *“Facebook regularly shuts down accounts that engage in these sorts of abuse. The scofflaws regularly return using new profiles.”*

Facebook is a private corporate site, thus it’s quite legal to “shut down” accounts it considers objectionable, provided they are not discriminating for some reason.

How ever using the word “scofflaws” is technically and legally incorrect. That is opening a new account is not unlawful / illegal even though the Facebook Terms Of Service might imply it is.

Also consider, the graphic file is “pulled by the user”, not “pushed by the service” thus quote a bit of legislation about malware effectively gets negated …

Thus raising the question of if quite a bit of current anti-malware legislation is actually effective…

cb •
[August 15, 2025 6:38 PM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447208)

What kind of ever-loving idiot writes his browser to load and execute JavaScript (or any executable) from a graphic file? Do all browsers do this? What possible benefit could it have, ever?

Clive Robinson •
[August 16, 2025 3:13 AM](https://www.schneier.com/blog/archives/2025/08/trojans-embedded-in-svg-files.html/#comment-447220)

@ cb, ALL,

With regards,

> “What kind of ever-loving idiot writes his browser to load and execute JavaScript (or any executable) from a graphic file? Do all browsers do this? What possible benefit could it have, ever?”

The answer to your three questions in short are,

1, Someone who uses a second parties graphics code library.
2, If the application uses the same second parties graphics code library then very probably.
3, Using a second parties graphics code library takes a lot of heavy lift out for the first party thus “reducing time to market”.

The real issue is,

“Being all things to all men”

Along with

“Highly complex interpretive functionality”.

We’ve seen this before with “log4j” and the vulnerability called “log4shell” back at the end of 2021,

<https://www.ibm.com/think/topics/log4j>

The underlying issue is similar to the

“Publish or be dammed”

Of academic progression. To get the benefits your name has to be well known.

In Open Source this means getting as many people to use your code as you can. To do this it has to work seamlessly for as many people as possible. Thus you put in everything anyone could possibly want behind a simple interface this has three side effects

1, Covers many edge cases
2, Large often disparate code base
3, High complexity

Which frequently results in hidden or unpredictable vulnerabilities.

But the point to note is that the more disparate edge cases you cover the more likely it is that your program logic for “ease and flexibility” to be implemented as an interpreter of some kind that is “Turing Complete” thus introduces variations on the “Halting Problem” and Kurt Gödel’s “undecidability” theorems. Which is dangerous enough when acting on “controlled tested input” but is open to all sorts of issues when it acts on “uncontrolled untested input” such as files downloaded from the Internet

In some graphics files they are actually programs… See PDF which is based on PostScript. Which is described by some as

> *“The language Postscript is what computer scientists call a “back-assward” programming language.”*

Of a similar type to the Forth “Stack Based Reverse Polish Notation” Programming...