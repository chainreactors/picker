---
title: Weekly Retro 2024-W36
url: https://0xda.de/blog/2024/09/weekly-retro-2024-w36/
source: Blogs  dade
date: 2024-09-10
fetch_date: 2025-10-06T18:25:20.877988
---

# Weekly Retro 2024-W36

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/09/weekly-retro-2024-w36/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

3 minutes

# [Weekly Retro 2024-W36](https://0xda.de/blog/2024/09/weekly-retro-2024-w36/)

---

* [Elgato Key Lights, Control Center, and Stream Deck](#elgato-key-lights-control-center-and-stream-deck)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

It’s going to be a bit of a short week again this week. I am working on several projects in parallel right now but I’m not ready to announce any of them just yet. Trying this new thing where I actually complete the work before I milk the dopamine from it. Once I have the details worked out, I’m hoping to announce at least one of the projects in the near future. It would be cool if it is this week, but I’m not sure yet.

I did pick up a [HackRF One](https://hackerwarehouse.com/product/hackrf-one-kit/) finally, after telling myself I’ve been meaning to for years. I also got the PortaPack H2 to use the HackRF without connecting it to my computer. It arrived this past week but I haven’t put it together yet. I’m excited to try it out, though. Radio in general is an area where my skillset and knowledge has been lacking.

## Elgato Key Lights, Control Center, and Stream Deck

I have been annoyed by my Elgato Key Lights for some time. They would randomly get disconnected and become unreachable over the network. I would then stand up, unplug each of them, and plug them back in, and they’d get fixed. There are no firmware updates available, so I thought maybe my units were just faulty. But after complaining to a friend, we compared WiFi settings and he said his don’t have this problem at all. I looked at the connection logs for my lights and it appeared that the lights were roaming between my two access points, and at some point during roaming, it would just stop being reachable. So in the Unifi Network app, I just pinned each Key Light to the access point nearest to my office, and the disconnecting problem has completely gone away.

I also found out that the Elgato Control Center, which I use to control the Elgato Key Lights on my desk, is hella inefficient and my lights, even when basically idle 99% of the time, are using hundreds of megabytes of data transfer per day. Why is that? Apparently it’s because the Elgato Control Center just spams them with requests to make sure they are still there. So I replaced Control Center with Home Assistant, which I’ve been running for some time now. Setting up the Home Assistant integration with my Stream Deck took a little effort but it was pretty straightforward.

```
{
  "brightness_step_pct": {{ ticks }}
}
```

This is how I had to configure the knobs on my stream deck so that they could turn the light brightness up and down for each light. When I turn left, `ticks` is a negative number so lights get dimmer. When I turn right, it’s a positive number, and lights get brighter. I also can press the knob down to turn on/off the light, and I have a shortcut to touch the screen of the Stream Deck to immediately turn each light on at full brightness.

My only complaint now is that the icons on the screen look like garbage. But hopefully at least getting rid of the Control Center Windows application will reduce the spam on my network.

## Interesting Links

* I don’t recall a single link I clicked on last week. Is this what it feels like to be free???

## Upcoming Projects

* A conference that wishes to remain nameless currently has it’s CFP open. I am exploring a few ideas for talks to submit. (Due: 2024-10-01)

---

Share this page

`https://0xda.de/blog/2024/09/weekly-retro-2024-w36/`

[weekly retro](https://0xda.de/tags/weekly-retro)

573 Words

Date Published

2024-09-09 00:23 +0000

fc092bc @ 2024-09-09

---

[芒聠聬
Weekly Retro 2024-W37](https://0xda.de/blog/2024/09/weekly-retro-2024-w37/)

[Weekly Retro 2024-W35
芒聠聮](https://0xda.de/blog/2024/09/weekly-retro-2024-w35/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/09/weekly-retro-2024-w36/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.json "JSON Feed")