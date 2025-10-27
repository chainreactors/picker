---
title: Clever Social Engineering Attack Using Captchas
url: https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html
source: Schneier on Security
date: 2024-09-21
fetch_date: 2025-10-06T18:34:41.242854
---

# Clever Social Engineering Attack Using Captchas

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

## Clever Social Engineering Attack Using Captchas

[This](https://isc.sans.edu/diary/rss/31282) is really interesting.

It’s a phishing attack targeting GitHub users, tricking them to solve a fake Captcha that actually runs a script that is copied to the command line.

Clever.

Tags: [captchas](https://www.schneier.com/tag/captchas/), [malware](https://www.schneier.com/tag/malware/), [social engineering](https://www.schneier.com/tag/social-engineering/)

[Posted on September 20, 2024 at 11:32 AM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html) •
[11 Comments](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html#comments)

### Comments

erna •
[September 20, 2024 12:08 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440658)

That link just gives me a blank page, and the HTML contains little other than “script src=/\_Incapsula\_Resource”. Am I supposed to run that script? Seems ironic.

The Wayback Machine can’t even get those hundred-or-so bytes; it spends a couple of minutes trying to save the page, then fails entirely.

Andrew •
[September 20, 2024 12:56 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440660)

Saw this earlier today in Brian Kerbs’s blog.

The Intuition there was that developers have a good chance to catch and avoid this. Most of the regular users probably have very slim chance against attack like that.

Who? •
[September 20, 2024 4:23 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440668)

I fail to see why JavaScript have access to the operating system’s clipboard. It does not need this feature. We need to rethink the basic concepts of Internet and write browsers with a small subset of current features (support for basic HTML (1.0, 2.0, 3.2, 4.01 and 5), CSS and perhaps a small subset of JavaScript (why not?) restricted to safe and well-proved features only.

A browser should fit on a floppy disk!

Anything outside this subset (e.g. PDF readers and video players) should be external —and, again, simple— tools, just like it was on an X11 environment in the nineties.

Perhaps it is time to consider dropping support for ancient web features no one uses these days (after all, it has passed a long time since the first web pages were removed from anything but archive.org). W3C **requirement** of supporting all technologies developed in the last decades, including old bugs, for compatibility is an error that we are paying on a daily basis.

We need an “updated” Mosaic, simple, fast, auditable and based on modern standards (HTML 5, CSS, and a small and safe subset of JavaScript), not the current swiss-army knifes that have more than one hundred gigabytes of dependencies no one is able to track.

Zerolagtime •
[September 20, 2024 6:41 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440673)

DISA hardening STIGs block this exact script which tries to write to a temporary folder by not allowing programs to be executed from $Env:TEMP. In Linux, they also try to get /tmp mounted as a dedicated mount point with “noexec” for the same effect.

Winter •
[September 21, 2024 1:45 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440684)

I wonder how many users actually perform the verification steps in the challenge screen. They look quite involved.

I would be very wary to do anything unexpected in a terminal on the suggestion of a website. But maybe others look at this differently?

Dude •
[September 22, 2024 11:20 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440696)

To me asking people to run a Powershell command doesn’t seem so clever, especially when the target is developers.

lurker •
[September 22, 2024 11:43 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440697)

@Who?
I see nobody has yet warned you that HTML5 is an instrument of the devil. But no, there are some useful features in it. The problem as you say is the browsers who think they must fit Monty Python’s Flying Circus into the Palace of Versailles.

My perfect browser would ask the user for permission to open any odd file type in a suitable external application; no setting up humungous lists of mimetypes vs applications. This is another aspect of why IE was never a good browser, it choked on any filetype that wasn’t in the secret seven hardwired list of suffixes that could be opened by Office. And note, the present attack is against Windows systems …

Daniel Popescu •
[September 23, 2024 6:52 AM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440700)

@Who? – Good points, thanks.

Clive Robinson •
[September 23, 2024 9:52 PM](https://www.schneier.com/blog/archives/2024/09/clever-social-engineering-attack-using-captchas.html/#comment-440713)

**This attack is a half century or so old.**

Yup seriously.

Back in the 1970’s the old mechanical KSR and ASR Teletypes were being replaced with “Visual Display Units”(VDUs).

With VDU’s and the “screen clear” command came the notion of “screens” that gave “menus” and the like.

These menus quickly gave rise to the idea of “function keys” that could be programmed by the software running on the central “main frame”.

Because the length of the serial lines could be 1000ft or more, VDU’s could be in offices anywhere on University Campus and frequently were as they had “status symbol” value.

Around this time Unix was becoming popular and with it came a couple of useful things,

1, “shell scripting”,
2, A program called “write”

(Write was more famously known among admins as “wall” which enabled admin messages to be sent to all logged in users and still is. Write became more structured with “talk”, which was the forerunner of IRC).

It did not take someone too long to work out how to use “write” to put a “shell script” in a function key on another users VDU and get the user to press it.

Which if you think about it is the same as putting a PowerShell script in the browser clipboard and getting the user to execute it.

As I note from time to time, the ICT Industry appears condemned to never learn from it’s history… So here we are a half century later falling for the same old attacks.

And so… I will bet that this is not the last time we see some idiot putting in a buffer that can,

1, Hold a command / script / executable.
2, Be easily written to by an attacker for a user to execute.

Heck I developed such an attack on AT&T Sys V 4 back in the early 90’s due to the terminal-mux pr...