---
title: New Serious PHP Vulnerabilities Released and Patched
url: https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html
source: Schneier on Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:40.742932
---

# New Serious PHP Vulnerabilities Released and Patched

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

## New Serious PHP Vulnerabilities Released and Patched

PHP maintainers have [released](https://www.php.net/archive/2026.php#2026-10-20-1) fixes for two critical vulnerabilities:

> PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately.
>
> Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod\_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod\_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs.
>
> The vulnerabilities:
>
> * RCE via OOM corruption, CVE-2026-109618 ([GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)): out-of-memory handling can interrupt PHP while internal request data is only partially initialized. Request cleanup may then treat the invalid data as valid.* RCE via stale global state, CVE-2026-109619 ([GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)): request-owned internal state can survive after its backing memory has been freed. A later request handled by the same worker may use that stale state before normal initialization resets it.

Updating PHP is the only way to regain security. Do it now.

More [news](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html).

[Good](https://www.wired.com/story/this-is-not-a-drill-2-php-vulnerabilities-are-setting-the-internet-on-fire/) [explanations](https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation).

Tags: [patching](https://www.schneier.com/tag/patching/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on October 22, 2026 at 9:26 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html) •
[14 Comments](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html#comments)

### Comments

Clive Robinson •
[October 22, 2026 10:07 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459163)

Sent in parts due to auto-mod at 14:00UTC

Part 1,

@ Bruce, ALL,

A search Gave the following information,

> “The critical PHP vulnerabilities were discovered by the cybersecurity firm Calif … and independently by researchers at Wiz”

If this is correct then the vulnerabilities were found by the use of AI systems.

Clive Robinson •
[October 22, 2026 10:09 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459164)

Part 2,

I could list another series of “AI Vulnerability Discoveries” but the list would be fairly lengthy…

Many have been dismissed as “slop” but sufficient have not to be of considerable concern.

These non slop AI findings have the feeling of being found at a rapid rate that is outstripping developers ability to fix them in a timely fashion.

I don’t know if anyone is keeping figures on this but it appears to be rattling lots of people including UK politicians (which is not good).

Thus I’m worried that ill advised precipitous political actions will be taken and we will suffer for a considerable period because of them.

Perry •
[October 22, 2026 10:28 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459165)

“Updating PHP is the only way to regain security.”

Updating PHP is the only way to mitigate these vulnerabilities, but doing so does NOT make PHP “secure.”

In fact, that train of thought borders on magical thinking. Because beyond on a shadow of doubt there exist other severe issues in PHP that have simply not been discovered.

Clive Robinson •
[October 22, 2026 10:36 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459166)

@ ALL,

The BBC is running a news “live update” on the PHP issue,

<https://www.bbc.co.uk/news/live/ckgel5xp2xv9t>

It reports that 32 UK Gov sites are effected but as of yet, nobody has reported being attacked in the UK…

I would take that with a grain of salt about the size of Lott’s Wife …

There is however other news that is equally as worrying…

Indian Certificate Authority eMudhra has used rediculous signing key values for it’s top level certificates.

Thus something like 60million certificates are now garbage and it will be easily possible for anyone to fake certs that most browsers will accept untill the browsers and other Apps have been correctly updated (which they may never ve in the case of embedded systems such as consumer Routers and IoT devices…

You can read an Outraged at this article,

<https://arstechnica.com/security/2026/10/the-internet-goes-on-high-alert-after-discovery-of-8-compromised-tls-certs/>

There is however an ironically funny side to it… One of the PK cert values was “4” which many probably remember from a XKCD joke on a random number generator.

Have a look on the Current Friday squid for more on this,

<https://www.schneier.com/blog/archives/2026/10/friday-squid-blogging-squid-before-the-chicxulub-meteor-impact.html/#comment-459121>

So two very serious security issues this week, and as the old saying has it,

“It’s not even over yet…”

Smooth Operator •
[October 22, 2026 10:46 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459167)

@ Perry • October 22, 2026 10:28 AM,

Amen brother,

there are very trivial ways around PHP “safeguards” that I have discovered a very, very long time ago (almost 20 years ago) and that “gift” keeps on giving to this day.
Some “bugs” you just keep for your own use, and that goes not only for php but any other OO Language. Personally, I’d never use it but I do love the sites/servers who have it implemented, because it opens many doors that only appear to be closed, and are supposed to be closed. Cheers.

Smooth Operator •
[October 22, 2026 10:51 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459168)

FFS clive f@gg07$0n, get a life lady, linking to your own past comments, yes I said this, I did this, blah blah blah – yaaayyyyyy – here’s Nobel Prize 4 u – boo hoo.
Grow up lady.

wiredog •
[October 22, 2026 11:40 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html/#comment-459169)

It sounds like the cert issue was caused by training, or at least not intended for public use, certs being used. Sort of like if your corporate example.corporate.com accidentally got routed.

Also, xkcd is on top of it: <https://m.xkcd.com/3314/>

Rontea •
[October 22, 2026 12:56 PM](https://...