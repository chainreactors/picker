---
title: Winner, Name that Ware May 2024
url: https://www.bunniestudios.com/blog/2024/winner-name-that-ware-may-2024/
source: bunnie's blog
date: 2024-07-01
fetch_date: 2025-10-06T17:38:30.490244
---

# Winner, Name that Ware May 2024

---

[« Formlabs Form 4 Teardown](https://www.bunniestudios.com/blog/2024/formlabs-form-4-teardown/)

[Name that Ware, June 2024 »](https://www.bunniestudios.com/blog/2024/name-that-ware-june-2024/)

## Winner, Name that Ware May 2024

The Ware from May 2024 is a Generac RXSC100A3 100-amp automated load transfer switch. It senses when utility power fails and automatically throws a switch to backup power. Thanks to [Curtis Galloway](https://curtisgalloway.wordpress.com/2024/05/03/diy_battery_backup/) for contributing this ware; he has posted a nice [write-up about his project](https://curtisgalloway.wordpress.com/2024/05/03/diy_battery_backup/) using it. The total function of the ware was a bit difficult to guess because the actual load switch wasn’t shown – the relays don’t do the power switching; they merely control a much larger switch.

A lot of questions in the comments about why a 50/60Hz jumper. I think it’s because as a backup power switch, a deviation of the mains frequency by 10Hz is considered a failure, and thus, backup power should be engaged. I also think the unit does zero-crossing detection to minimize arcing during the switch-over. The system drives a pair of rather beefy solenoids, which can be seen to the left of the load switch in the image below.

![](https://bunniefoo.com/ntw/ntw_may_2024b.jpg)

And this is the inside of the 100-amp load switch itself:

![](https://bunniefoo.com/ntw/ntw_may_2024a.jpg)

For better images hit up [Curtis’ blog](https://curtisgalloway.wordpress.com/2024/05/03/diy_battery_backup/)!

I think Ben got pretty close in his analysis of the ware, noting the 50/60Hz jumper could be for mains failure detection. Congrats, email me for your prize!

*An administrative note*: my ISP upgraded the blog’s database server this past month. Because this blog was created before UTF-8 was widely adopted, the character sets got munged, which required me to muck around with raw SQL queries to fix things up. I think almost everything made it through, but if anyone notices some older posts that are messed up or missing, drop a comment here.

I’m also working on trying to configure a fail-over for my image content server (bunniefoo.com), which is still running on a very power-efficient [Novena](https://en.wikipedia.org/wiki/Novena_%28computing_platform%29) board of my own design from over a decade ago. It’s survived numerous HN hugs of death, but the capacitor electrodes are starting to literally oxidize away from a decade of operating in salty, humid tropical air. So, I think it might be time to prep a fail-safe backup server — a bit like the load switch above, but for bits not amps. However, I think I’m more in my element configuring a 100A load switch than an IP load balancer. The Internet has only gotten more hostile over the past decades, so I’m going to have some learning experiences in the next couple of months. If you see something drop out for more than a day or so, give me a shout!

This entry was posted on Sunday, June 30th, 2024 at 4:25 pm and is filed under [Administrative](https://www.bunniestudios.com/blog/category/administrative/), [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-may-2024/feed/) feed.
Both comments and pings are currently closed.

Comments are closed.

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).