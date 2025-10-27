---
title: Stream Automator
url: https://buaq.net/go-151989.html
source: unSafe.sh - 不安全
date: 2023-03-05
fetch_date: 2025-10-04T08:43:20.928248
---

# Stream Automator

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

![](https://8aqnet.cdn.bcebos.com/d691c8058fc82ada3034b7b8d31baf4e.jpg)

Stream Automator

I have a problem, and I think I’m not alone: Getting TV is too complicated and too expensive. I
*2023-3-4 04:0:0
Author: [www.tbray.org(查看原文)](/jump-151989.htm)
阅读量:22
收藏*

---

I have a problem, and I think I’m not alone: Getting TV is too
complicated and too expensive. I know what a solution might look like, and if
someone can build it and charge just a little bit for access, they might become very wealthy.

![Apple TV+](https://www.tbray.org/ongoing/When/202x/2023/03/03/apple-tv.png "Apple TV+")

Alternatively, if someone could build an
open-protocol-based co-operative tool to fix the problem, they’d be a benefactor of humanity.

Let’s call the thing I want a “Stream Automator”, Automator for short. I thought of “Streamplex” but there are
already a few things named that; none of them look likely to be significant in the long-term but oh well.

![Crave TV](https://www.tbray.org/ongoing/When/202x/2023/03/03/crave.png "Crave TV")

Let’s make it personal ·
My family still has dumb-cable TV. It’s absurdly expensive and all anyone watches on it are live sports. We
subscribe to a couple of streaming services, which give us access to maybe 20% of the really happening shows that people are
talking about.

So, I want to dump dumb-cable and still watch the sports I like and the TV that matters.

![DAZN](https://www.tbray.org/ongoing/When/202x/2023/03/03/dazn.png "DAZN")

Axiom: Subscribing to everything is not a sane option. *There has to be a better way.*

**Complication**: Sports coverage.
In Canada where we are, there are two national sports streamers, one of which is a subsidiary of the other, but which offer
disjoint packages. Then there are global services like
[DAZN](https://en.wikipedia.org/wiki/DAZN).

![Disney+](https://www.tbray.org/ongoing/When/202x/2023/03/03/disney.png "Disney+")

It’s unreasonably difficult to discover exactly which games you can watch
on which channels. For example, in recent seasons I’ve enjoyed watching the Toronto Blue Jays. For years I’d been an MLB.tv
subscriber, but I dropped it because the Jays are blocked since they’re my “local” team (three timezones away), which is OK
I guess because I can get them on one of those sports networks that happens to be included with our current dumb-cable package,
but maybe not because we pay for some extra sports, and the dumb-cable company makes it really hard to figure out what exactly you’re
subscribing for.

![ESPN](https://www.tbray.org/ongoing/When/202x/2023/03/03/espn.png "ESPN")

**Complication**: VPN. A member of my family (also in Canada) is an NFL fan and boasts that he watches any game he wants
without paying a penny, via VPN magic.

**Complication**: National borders. Here in Canada, if you want to watch HBO you subscribe to something called “Crave
TV”, which gets you most of (all of?) the HBO stuff and some Paramount. Except for, you might do better going upstream with a
VPN. But some of the streamers are smart about blocking them.

![HBO max](https://www.tbray.org/ongoing/When/202x/2023/03/03/hbo.png "HBO max")

The point isn’t “Canada is hard”; it’s that every country is going to have its own streaming-provider weirdness.

**Complication**: Your hardware. We have Roku but no AppleTV hardware. It doesn’t seem like that matters, I can
ChromeCast Apple TV+, is that weird?

![MLB.tv](https://www.tbray.org/ongoing/When/202x/2023/03/03/mlb.png "MLB.tv")

Also, one of the many irritants about our dumb-cable service is that it’s 720p with no upgrade path.
We have a nice LG 4K screen but I’ve watched ballgames where the picture looked like my grandparents’ big console Color TV
in the Sixties.

Speaking of that LG TV, it runs on
[WebOS](https://en.wikipedia.org/wiki/WebOS), with loads of stream-provider apps, except for it’s really
hard to turn any of that on without becoming a part of LG’s data-farming operation. Ewww.

![Netflix](https://www.tbray.org/ongoing/When/202x/2023/03/03/netflix.png "Netflix")

Also, I haven’t figured out how to
route the TV audio outfit back into the A/V receiver; this involves something called “eARC” which the TV and the receiver
both claim to support but does not Just Work.

Oh, and our neighbor has a digital TV antenna up on his roof and he gets a whole bunch of mainstream channels free off the
air with an absolutely fabulous picture, including marquee events like the Olympics and so on. Hmmm.

![Paramount+](https://www.tbray.org/ongoing/When/202x/2023/03/03/paramount.png "Paramount+")

**Complication**: Streaming networks offer you lower prices if you sign up for a whole year. But if I want to watch
Ted Lasso and Succession and Russian Doll and Star Trek: Strange New Worlds
and The Rings of Power
over the next year, it becomes rational to switch subscriptions every month or two. At what cost? I dunno, I want someone to
tell me.

The problem ·
It’s really freaking complicated and time-consuming and error-prone to discover what’s available from what providers at what
cost. Also, the picture likely changes at least once per year. I have
better things to do with my time than figure that shit out.

![Prime Video](https://www.tbray.org/ongoing/When/202x/2023/03/03/prime.png "Prime Video")

The Automator ·
In my dreams, I tell it where I am, what shows and what teams I want to watch and what hardware
I have  — in
natural language, forsooth, what are Big ML Models for if they can’t grok TV tastes?

It makes me a plan
that lists the services I should subscribe to and when I should switch between them. I suppose it would be too much to hope for
a tool that actually manages the subscriptions for me, but I would totally pay for one.

![Roku](https://www.tbray.org/ongoing/When/202x/2023/03/03/roku.png "Roku")

Side trip ·
At home, we’re currently watching Babylon Five because smart people told us it was good and a lot like
Deep Space 9. We’re doing this by taking the Blu-Rays out of the local public library. So the Automator would get
extra credit for knowing about that resource. A lot of classics are in libraries, which are apparently easy to talk to, check out the wonderful
[Libby](https://libbyapp.com/) app (for books).

![TSN](https://www.tbray.org/ongoing/When/202x/2023/03/03/tsn.png "TSN")

I’m optimistic ·
Something’s gotta give, because the current economic structure for digital entertainment is just broken. Nobody’s willing to
subscribe to all the channels.

Hey, I have another idea: Micropayments for watching individual games or shows. *[Enough with the crazy talk, Tim!
-Ed.]* *[\*sigh\* -T.]*

*[Thanks to Lauren for pointing out several complications I hadn’t thought of.]*

---

文章来源: https://www.tbray.org/ongoing/When/202x/2023/03/03/Streamplex
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)