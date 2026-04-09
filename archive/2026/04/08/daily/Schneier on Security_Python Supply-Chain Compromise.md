---
title: Python Supply-Chain Compromise
url: https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html
source: Schneier on Security
date: 2026-04-08
fetch_date: 2026-04-09T04:32:23.255172
---

# Python Supply-Chain Compromise

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

## Python Supply-Chain Compromise

This is [news](https://www.truesec.com/hub/blog/malicious-pypi-package-litellm-supply-chain-compromise):

> A malicious supply chain compromise has been identified in the Python Package Index package litellm version 1.82.8. The published wheel contains a malicious .pth file (litellm\_init.pth, 34,628 bytes) which is automatically executed by the Python interpreter on every startup, without requiring any explicit import of the litellm module.

There are a lot of really boring things we need to do to help secure all of these critical libraries: SBOMs, SLSA, SigStore. But we have to do them.

Tags: [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [malware](https://www.schneier.com/tag/malware/), [supply chain](https://www.schneier.com/tag/supply-chain/)

[Posted on April 8, 2026 at 6:25 AM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html#comments)

### Comments

wiredog •
[April 8, 2026 7:31 AM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html/#comment-453446)

Oblig. XKCD: <https://xkcd.com/2347/>

Python User •
[April 8, 2026 9:29 AM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html/#comment-453453)

If you wanna screw somebody – just use python – I do it all the time. And mutual satisfaction is guaranteed every single time! After all – imagine penetration testing or the penetration without testing, sans python? Much better with python. Thing is, it’s free to boot.

Anselm •
[April 8, 2026 12:19 PM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html/#comment-453457)

The problem here is with .pth files, which are used in Python to tell the Python interpreter about the location of various resources. These can, in principle, contain arbitrary Python code and are sourced by the Python interpreter whenever it starts up. Apparently a more declarative approach that functions without arbitrary Python is in the works, in order to counter such attacks in the future.

Ray Dillinger •
[April 8, 2026 1:42 PM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html/#comment-453458)

I have been avoiding most “modern” programming languages because each program tends to come with a transitive closure of dependencies imported from so many sources all over the Internet that it seems flatly impossible that these sources are all trustworthy and flatly impossible that there is any unified team trying to make sure that they are all trustworthy.

And that dependency tree can change after the program is written. Usually these dependencies, if missing, get dynamically loaded from some random Internet site, and run without so much as a notification to the user that this is happening. Some library maintainer decides it’s okay to change their dependencies, and suddenly the project you wrote three years ago and haven’t changed is now downloading and running code that’s entirely outside the set of things you have accepted the risk to run, from a source you have no idea whether to trust or not, without your permission.

And these libraries are for the most part undocumented – or at least undocumented in any way that would be discoverable and verifiable by any standard procedure or by someone who’s not already downloading and using them. I mean, oh, yeah, there’s a website somewhere. But all these websites are organized in different ways and may omit crucial information or hide it six levels down in a click-random-things hierarchy most of which doesn’t have much to do with the crucial information you’re after.

The organization or hosting of these websites can change on somebody’s whim, the URLs are random hosts you never heard of, any of them could be run by anybody including attackers, and neither the libraries nor their documentation is even signed (other than some which is “trust me bro” self-signed by the authors). None of it is resident on your system where you’ll know if it has changed. None of it is resident on my system where I could use it in places or circumstances where I do not want the machine connected to the internet. None of it is even resident on my system where I could rely on being notified if it had been changed.

Just, no. I try building a program and watch, aghast, as the machine goes and downloads code from a thousand different completely unknown and unvetted hosts, fails to install locally resident documentation for any of it, fails to provide any uniform interface to whatever documentation exists, and spits out something I am expected to run.

There is not even an accepted stable specification for all these libraries, and nobody who is testing new versions of each to see that it meets any such specification. Nor is there a central repository with a gatekeeper and a unified bugtracker for all of this stuff. Finally none of it is even packaged for, signed by, and served by for any consistent identifiable signing authority like a distro maintainer that tracks and announces security issues and bugs. Therefore no distribution maintainer is even testing new specific versions of it in combination with specific versions of other things accepted into the same distro as dependencies.

Nobody other than the packager/author is tracking bugs or security issues or signing new releases, so each one basically all comes down to “trust me bro” with no reference to anybody whose work depends (and the value of whose signature depends) on all of it being tested and clean.

No fecking way am I ever going to take the having all that on my own system to develop software. And if I did build software that way I’d wind up with a program I could not in good conscience ask any client, user, or customer to ever trust.

[Seth Wells](https://xer0trust.com) •
[April 8, 2026 5:48 PM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html/#comment-453463)

The dependency problem is also an authority problem. Every layer in the chain that can interpret, authorize, or execute becomes a trust surface. I’ve been working on a constraint architecture where the intermediary layer is stateless, holds no secrets, makes no decisions, and has zero dependencies — 1.7KB total. It just binds and forwards. Authority stays at the provider boundary mechanically, not by policy. Live demo under sustained adversarial load: challenge.xer0trust.com

Kent Brockman •
[April 8, 2026 11:33 PM](https://www.schneier.com/blog/archives/2026/04/python-supply-chain-compromise.html/#comment-453465)

<https://dev.to/alanwest/why-your-open-source-dependencies-are-a-ticking-time-bomb-and-how-to-defuse-them-k32>

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](...