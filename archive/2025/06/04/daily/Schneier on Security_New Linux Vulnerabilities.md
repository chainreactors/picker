---
title: New Linux Vulnerabilities
url: https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html
source: Schneier on Security
date: 2025-06-04
fetch_date: 2025-10-06T22:56:37.946511
---

# New Linux Vulnerabilities

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

## New Linux Vulnerabilities

They’re [interesting](https://thehackernews.com/2025/05/new-linux-flaws-allow-password-hash.html):

> Tracked as [CVE-2025-5054 and CVE-2025-4598](https://www.openwall.com/lists/oss-security/2025/05/29/3), both vulnerabilities are race condition bugs that could enable a local attacker to obtain access to access sensitive information. Tools like Apport and systemd-coredump are designed to handle crash reporting and core dumps in Linux systems.
>
> […]
>
> “This means that if a local attacker manages to induce a crash in a privileged process and quickly replaces it with another one with the same process ID that resides inside a mount and pid namespace, apport will attempt to forward the core dump (which might contain sensitive information belonging to the original, privileged process) into the namespace.”

Moderate severity, but definitely worth fixing.

Slashdot [thread](https://it.slashdot.org/story/25/06/02/0140228/new-moderate-linux-flaw-allows-password-hash-theft-via-core-dumps-in-ubuntu-rhel-fedora).

Tags: [Linux](https://www.schneier.com/tag/linux/), [passwords](https://www.schneier.com/tag/passwords/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on June 3, 2025 at 7:07 AM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html) •
[8 Comments](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html#comments)

### Comments

Clive Robinson •
[June 3, 2025 11:35 AM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445703)

@ Bruce, ALL,

There has always been the question of code size –as well as complexity– against security.

Some parts of the GNU/Linux eco system are shall we put it,

“Way beyond the acceptable limits”

With regards to size and complexity and to give such parts the highest of “security access/control” is frankly unwise.

One such that has caused me concern for quite some time is “SystemD” and apparently I’m not alone in this.

There are several fundamental rules for designing secure systems perhaps the most important is,

“Segregation of function.”

With attendant,

“Strong oversight and minimum privilege.”

Further that you design the system in such a way that for each part,

“You clock the inputs and clock the outputs”

As not only does this knock various forms of “side channel” back it also makes “race conditions” like wise much less of a potential issue.

However with regards SystemD, there appears to be a perverse desire in it’s developer to,

“Extend to, and embrace all.”

To be the master of every thing and certainly way beyond what in all honesty is wise. As SystemD has become what is effectively an impenetrable conglomeration it breaks the basic Secure Design rules.

But it’s not just from a security perspective but also from one of a SysAdmin having to abdicate control to the whims of the developer.

I think it’s safe to say that even though this instance is a “moderate severity” issue… We are going to see increasing issues with SystemD

As I’ve noted in the past there is the issue of,

“Security v. Efficiency”

And whilst it is in manageable modules possible to have a degree of both, it’s usually not going to happen due to the way the industry works currently.

So with any code base like SystemD it would be unwise to assume that any new vulnerabilities are going to be “moderate”…

lurker •
[June 3, 2025 2:06 PM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445705)

@Bruce, ALL

“Interesting” but “Moderate” because of the complexity of pulling it off.

Not really anonymous •
[June 3, 2025 2:25 PM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445706)

At least some parts of systemd are useful. The old shell based init script system was a mess. Systemd provides a nicer interface for doing init type stuff.
The linux kernel is already a mess (not necessarily worse tham ios or windows) and I wouldn’t give local accounts to people I wouldn’t trust to behave. So I don’t think systemd significantly makes things worse in that regard.
Brad Spengler used to regularly find privilege escalations in the linux kernel and had a business based on mitigating the ones he found. He doesn’t post them where I used to see them any more, but I don’t think kernel security has improved so much since then, that it isn’t still a problem.

. •
[June 3, 2025 4:16 PM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445707)

The Leaks Were Right: Mass Layoffs at Microsoft in May, Then Another Wave in June

<https://techrights.org/n/2025/06/03/The_Leaks_Were_Right_Mass_Layoffs_at_Microsoft_in_May_Then_Anot.shtml>

L •
[June 3, 2025 9:57 PM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445709)

First thing I do with Ubuntu Linux is:

> *sudo apt purge apport ubuntu-report whoopsie popularity-contest*

Nothing in there I need or want…

I’ve seen some crazy stuff with Microsoft Windows. Holes you could drive a convoy of trucks through.

This Linux one. Yes, it’s serious and it needs to be patched. A turnkey solution would be a serious threat. But right now, it reads like a mission impossible script…

Joe P •
[June 4, 2025 7:49 AM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445721)

It’s not just the attack surface of SystemD that we need to worry about. It’s also the intent and behind the scenes decisions.

I used Linux Mint years ago and I believe it was Mint 13 which had an update to SystemD (might have been to version 236?) that introduced systemd-resolved. I had previously set up dnsmasq since it allowed two host files. One was goodhosts and one was badhosts. The goodhosts file included lookups to time servers, VPN servers, my bookmarks, trusted dns resolvers and others. The badhosts file was to kill major ad servers, social media buttons, and others.

My dnsmasq was set to use a dnscrypt upstream resolver for when the large host files didn’t have the lookup. Without my knowledge, the update to systemd changed my dns setup to use google for all lookups. When I noticed, the instructions for disabling the systemd resolver did not work as instended. I ended up going back to Debian and since then I have not used systemd.

bye bye M$ •
[June 4, 2025 12:47 PM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445734)

Danish cities drop Microsoft over Trump policies and financial concerns

<https://www.thelocal.dk/20250603/danish-cities-drop-microsoft-over-trump-policies-and-financial-concerns>

Clive Robinson •
[June 4, 2025 12:53 PM](https://www.schneier.com/blog/archives/2025/06/new-linux-vulnerabilities.html/#comment-445735)

@ Joe P,

You probably made the right choice, I won’t give systemd “house room” for the...