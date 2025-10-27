---
title: Hacks at Pwn2Own Vancouver 2023
url: https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html
source: Schneier on Security
date: 2023-03-28
fetch_date: 2025-10-04T10:55:20.576143
---

# Hacks at Pwn2Own Vancouver 2023

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

## Hacks at Pwn2Own Vancouver 2023

An impressive array of hacks were demonstrated at the [first day](https://www.bleepingcomputer.com/news/security/windows-11-tesla-ubuntu-and-macos-hacked-at-pwn2own-2023/) of the Pwn2Own conference in Vancouver:

> On the first day of Pwn2Own Vancouver 2023, security researchers successfully demoed Tesla Model 3, Windows 11, and macOS zero-day exploits and exploit chains to win $375,000 and a Tesla Model 3.
>
> The first to fall was Adobe Reader in the enterprise applications category after Haboob SA’s Abdul Aziz Hariri ([@abdhariri](https://twitter.com/abdhariri)) used an exploit chain targeting a 6-bug logic chain abusing multiple failed patches which escaped the sandbox and bypassed a banned API list on macOS to earn $50,000.
>
> The STAR Labs team ([@starlabs\_sg](https://twitter.com/starlabs_sg)) demoed a zero-day exploit chain targeting Microsoft’s SharePoint team collaboration platform that brought them a $100,000 reward and successfully hacked Ubuntu Desktop with a previously known exploit for $15,000.
>
> Synacktiv ([@Synacktiv](https://twitter.com/Synacktiv)) took home $100,000 and a Tesla Model 3 after successfully executing a TOCTOU (time-of-check to time-of-use) attack against the Tesla-Gateway in the Automotive category. They also used a TOCTOU zero-day vulnerability to escalate privileges on Apple macOS and earned $40,000.
>
> Oracle VirtualBox was hacked using an OOB Read and a stacked-based buffer overflow exploit chain (worth $40,000) by Qrious Security’s Bien Pham ([@bienpnn](https://twitter.com/bienpnn)).
>
> Last but not least, Marcin Wiązowski elevated privileges on Windows 11 using an improper input validation zero-day that came with a $30,000 prize.

The con’s [second](https://www.bleepingcomputer.com/news/security/windows-11-hacked-again-at-pwn2own-tesla-model-3-also-falls/) and [third](https://www.bleepingcomputer.com/news/security/windows-ubuntu-and-vmware-workstation-hacked-on-last-day-of-pwn2own/) days were equally impressive.

Tags: [Adobe](https://www.schneier.com/tag/adobe/), [cars](https://www.schneier.com/tag/cars/), [hacking](https://www.schneier.com/tag/hacking/), [Windows](https://www.schneier.com/tag/windows/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on March 27, 2023 at 7:03 AM](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html) •
[12 Comments](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html#comments)

### Comments

modem phonemes •
[March 27, 2023 9:11 AM](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html/#comment-419881)

How instructive these tour-de-force are ! They inspire hope that security engineering principles may one day be really used routinely in software and hardware design.

Plumbing the big tinkertoy box and seeing around the corner next after this.

Clive Robinson •
[March 27, 2023 12:51 PM](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html/#comment-419883)

@ Bruce,

> “The con’s second and third days were equally impressive.”

Which raises all sorts of questions…

Firstly the “reward” for these financially are very low compared to what we know can be obtained from spurces that do not have public disclosure.

Which begs the question,

“Are there more impressive attacks out there, being ‘locked and loaded’ if not launched at those considered ‘inconvenient people’?”

But it also raises, along with the rapidly rising CVE count,

“Just how bad is the ICT Industry?”

Followed by,

“Why is it this bad?”

And I don’t mean just on the technical level…

We all have a part to play in what could best be described as the “ICTsec Disaster” especially as we know much if not most of it can be avoided, by relatively simple measures.

Developing high quality code is not just possible, surprisingly to many it is not done by some impossibly difficult methods.

Which begs the question,

“Why some half century or more since the fundementals of these attacks were found and starkly described are they still happening?”

Take that “Time-Of-Check to Time-Of-Use”(TOCTOU)[1] attack. Despite the fancy name it’s been widely known with file systems for a third of q century.

But it is more general. As I explained with a way to get code siging to fail, all you need to find is,

1, A serial process where,

With the solution being “make authentication and transaction atomic throughout the transaction”.

But as always, but still rarely done properly, handle “errors and exceptions” where they need to be handled. Not push them as far to the left as you can effectively outside the business logic where they are actually needed when dealing with an “active adversary”.

If the system environment you have to work in does not support atomic operations of the form you need. Then have a look at how “multiple phase commits”[2] on databases or “eXtended Architecture”(XA) Protocol works on transactions[3]. As they should tell you how to “shrink the hole” (though actually closing it may need a few other skills not so well known).

[1] <https://en.m.wikipedia.org/wiki/Time-of-check_to_time-of-use>

[2] See Jim Gray’s book,

“Transaction Processing : Concepts and Techniques”

ISBN:1558601902

Published in 1992 by Morgan Kaufmann as part of their “Series in Data Management Systems”.

Or similar work that deecribes “the reasoning” for the method, rather than just the method.

[3] The “eXtended Architecture”(XA) Protocol is an extention to “Two Phase Commit”(2PC) and is used not just for replicated databases but distributed transaction systems. You can get an indicator “overview” of method from,

<https://blog.sofwancoder.com/two-phased-commit-and-extended-architecture-the-basics>

Confused •
[March 27, 2023 1:45 PM](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html/#comment-419889)

Is this conference special? There are lots of conferences where zero days are presented (after responsible disclosure), is this one different?

Less confused •
[March 28, 2023 6:04 AM](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html/#comment-419942)

@Confused

It’s not normal conference, it’s a hacking contest.

Gert-Jan •
[March 28, 2023 7:05 AM](https://www.schneier.com/blog/archives/2023/03/hacks-at-pwn2own-vancouver-2023.html/#comment-419945)

Very good that these events are held. It offers white hat hackers (“security researchers”) legit payment for successful work. The argument that they could get more money by selling them to “security companies” is only relevant to hackers with a corrupt moral compass.

And because of the mandatory fix without 90 days, any exploitable vulnerability they find will soon get removed from the toolbox of all the evil regimes and cybercriminals.
We’ll have to accept that there is increased risk of abuse after the d...