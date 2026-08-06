---
title: Fiddler in 2026
url: https://textslashplain.com/2026/08/05/fiddler-in-2026/
source: text/plain
date: 2026-08-05
fetch_date: 2026-08-06T05:01:30.010817
---

# Fiddler in 2026

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Fiddler in 2026

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-052026-08-05](https://textslashplain.com/2026/08/05/fiddler-in-2026/)Posted in[fiddler](https://textslashplain.com/category/fiddler-2/), [life](https://textslashplain.com/category/life/), [storytelling](https://textslashplain.com/category/storytelling/)

I’ve shared the stories behind the Fiddler Web Debugger a fair bit over the years, in the [Fiddler Book](https://fiddlerbook.com/), in [a talk](https://github.com/ericlaw1979/CodeMash2015/tree/master/LuckingIn) at the CodeMash conference in 2015, and [on this blog](https://textslashplain.com/2024/11/24/fiddler-my-mistakes/). It features prominently in my [to-be-completed (some day?) memoir](https://bluebadgebook.com/bbb/), and I’ve enjoyed telling Fiddler stories to folks who ask over the years. (I’ve also written a ton of content about [*using* Fiddler](https://textslashplain.com/category/fiddler-2/).)

Over two decades, what was once a little side project came to influence a very meaningful percentage of my life, including where I live today and so many of my life’s experiences.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-45.png?resize=299%2C268&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-45.png?ssl=1)

Receiving the Engineering Excellence Award for Fiddler, circa 2007

On Monday morning, I got a ping from someone from Progress Software, acquirers of Telerik in 2014, after Telerik acquired Fiddler (and for a few years, me) back in 2012. They asked for an email address to which they could send a note.

“*This isn’t gonna be good*“, I assumed. Correctly.

After I [left Telerik for Google in 2016](https://textslashplain.com/2015/12/23/my-next-adventure/), development on the “Fiddler Classic” application had stagnated as the owners put their investments into a series of products they could monetize.

To be fair, this pivot was not unexpected. Initially, Telerik had purchased Fiddler largely for the community attention — the tool had a huge userbase of the exact developers the company was courting — we always expected that eventually we’d have a *cross-platform* version of the product that could be sold like Telerik’s other professional tools.

### Fiddler: Free Forever?

Telerik had loudly promised that Fiddler would remain “free forever” to avoid expected [community outrage](https://weblog.west-wind.com/posts/2011/Mar/19/The-Red-Gate-and-NET-Reflector-Debacle) about commercializing a previously-free tool. *Before Telerik, I had spoken to one potential acquirer who estimated the brand damage of their commercializing another previously-free tool at 25x their acquisition price, meaning they’d likely never turn a profit.*

Telerik’s blog post announcing the change was explicit:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-42.png?resize=750%2C250&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-42.png?ssl=1)

… but even that wasn’t enough, so a follow-up post was made shortly after:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-43.png?resize=750%2C327&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-43.png?ssl=1)

The unambiguous clarity of this promise had somewhat painted Telerik into a corner– they’d either need to find new ways to 1) monetize the technology behind Fiddler (we had several solid ideas), or 2) pivot to a new cross-platform product they could sell, or 3) renege on their promise and start charging for Fiddler for Windows.

While I was at Telerik, I worked a little on #1 — we created a licensable version of FiddlerCore, the core engine inside Fiddler, with the idea that other companies could sell products based on it. They had used FiddlerCore inside Telerik’s Test Studio product (that’s how I came to their attention to start with), and we figured other companies might need similar technology. Interest was… not very high.

Very frustratingly and humiliatingly, my former employer wanted to use FiddlerCore inside their [Message Analyzer](https://en.wikipedia.org/wiki/Microsoft_Network_Monitor) product. *But they didn’t want to pay for it*. So instead, a juggernaut worth hundreds of billions of dollars wrote code to *prompt the end-user to pirate FiddlerCore*:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-44.png?resize=400%2C184&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-44.png?ssl=1)

This is the sort of behavior then most often seen from shady apps trying to avoid paying MP3 patent fees. To this day, I remain *shocked* that the lawyers from both companies allowed this experience to ship. (*The fact that Microsoft-ecosystem developers made up virtually all of Telerik’s customers probably had something to do with Telerik not suing their pants off)*.

I had also started work on strategy #2 (build a cross-platform version) shortly after I started at Telerik. I spent months trying to get Fiddler running on [Mono](https://en.wikipedia.org/wiki/Mono_%28software%29), an early cross-platform version of the .NET Framework. It didn’t go great. I built a *serviceable* version for Linux, but the UI port for MacOS would crash constantly. A hybrid strategy, using Mono for FiddlerCore, and building a new front-end on Electron, seemed plausible though. Alas, this vision had been put on pause in 2014 when Telerik conducted wide US-based layoffs in advance of an expected IPO on the US stock market. After its acquisition by Progress, Telerik eventually restarted this strategy, eventually shipping [Fiddler Everywhere](https://www.telerik.com/fiddler/fiddler-everywhere), a product that had a few key advantages over Fiddler Classic (cross platform! some team features!) and a lot of downsides (no extensibility model).

I’d hoped that Progress/Telerik might open-source Fiddler Classic at some point to grow the ecosystem (things like the Fiddler SAZ format would get even more popular and create the possibility of sellable synergies) but this never happened. Instead, Fiddler just quietly *decayed*. As browsers adopted new standards (e.g. http2, h3, GREASE, tls1.3, `zstd` content compression), Fiddler Classic required more and more caveats for use. However, Fiddler’s rich extensibility model means that I could keep [building new capabilities](https://textslashplain.com/2025/05/16/fiddler-in-2025/) [in](https://gist.github.com/ericlaw1979) [and on](https://textslashplain.com/2022/01/08/debug-native-messaging/) Fiddler in the ten years since I’ve been able to commit updates to Fiddler itself.

I still use Fiddler almost every single day, but in many cases I’m not even using Fiddler to *capture* traffic anymore, instead just using it as a viewer for traffic [captured natively by Chromium](https://textslashplain.com/2020/04/08/analyzing-network-traffic-logs-netlog-json/), or to use its TextEncoder and inspectors, or even as a [frontend for other tools](https://textslashplain.com/2022/01/08/debug-native-messaging/#:~:text=Tampering%20with%20Messages).

Telerik periodically added surveys and ads to the Fiddler Classic UI, and even if they were gratingly [misleading](https://textslashplain.com/2025/05/16/fiddler-in-2025/#:~:text=Add%20a%20SingleBrowserMode%20button%20to%20Fiddler%E2%80%99s%20toolbar), they weren’t *too* annoying.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-48.png?resize=391%2C159&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-48.png?ssl=1)

Other changes of [dubious value](https://textslashplain.com/2025/03/31/runtime-signature-checking-threat-model/) were also mildly annoying at worst.

## This Week’s Rug Pull

Opening Fiddler on Monday, I was presented with a FiddlerUpdate ...