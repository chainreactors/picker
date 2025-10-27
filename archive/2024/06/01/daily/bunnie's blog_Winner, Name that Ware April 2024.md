---
title: Winner, Name that Ware April 2024
url: https://www.bunniestudios.com/blog/2024/winner-name-that-ware-april-2024/
source: bunnie's blog
date: 2024-06-01
fetch_date: 2025-10-06T16:55:09.664146
---

# Winner, Name that Ware April 2024

---

[« Name that Ware, April 2024](https://www.bunniestudios.com/blog/2024/name-that-ware-april-2024/)

[Name that Ware, May 2024 »](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/)

## Winner, Name that Ware April 2024

Last month’s ware was a “Z16 AI Voice Translator”. The name doesn’t really tell you much, so here’s some photos that give a better idea of what the device is about.

[![](https://bunniefoo.com/ntw/ntw_april_2024_soln_c_sm.jpg)](https://bunniefoo.com/ntw/ntw_april_2024_soln_c.jpg)

Above are the main parts of the device. The construction is simple and straightforward: big battery, screen with captouch, a rear-facing camera, and a speaker in a large chamber. The speaker chamber is the portion of the plastic mid-case that has the words “XP-Z6” emblazoned on it.

As many contestants observed, the device is based on a Mediatek chip that features a now mostly-obsolete 3G modem. Some correctly picked out that despite the potential for a cellular connection, it only has a wifi antenna.

![](https://bunniefoo.com/ntw/ntw_april_2024_sm.jpg)

This board design was almost certainly adapted by deleting parts from a reference design with 3G functionality, as evidenced by the footprint of the RF shielding containing blank areas that are just large enough to accommodate the [analog front-end (AFE) companion chip](http://bunniefoo.com/fernvale/fernvale-afe-top_sm.jpg) required for 3G. You can see some images of such an AFE in a decade-old post I did about [reverse engineering an MT6260A](https://www.bunniestudios.com/blog/2014/from-gongkai-to-open-source/), a distant ancestor of the SoC in this device.

![](https://bunniefoo.com/ntw/ntw_april_2024_soln.jpg)

The OS is basically a stripped down Android phone that runs some real-time voice and image translation software, which feels descended from Google Translate, or possibly “borrowed” from [Rabbit OS](https://en.wikipedia.org/wiki/Rabbit_r1). Above is a snapshot of the home screen UI. I’m not sure who pays for the back-end service for the on-line translation — it doesn’t require a subscription or registration of any kind for the device to operate (I can almost hear the howls of pain from VCs from all the way across the Pacific) — but more importantly, the device is capable of offline translation.

I was initially highly suspicious of the offline claim, so I purchased a sample to try it out. In fact, the device works as advertised with no internet connection at all (although you do need to initially provision it with some translation dictionaries).

![](https://bunniefoo.com/ntw/ntw_april_2024_soln_b.jpg)

It does a surprisingly good job of picking up and translating voice in real-time, and it can also translate text from photos as well in offline mode (although not in real-time: you have to shoot, crop and wait a couple seconds).

The device is exactly what it needs to be and no more — from the oversized speaker (so you can hear the synthesized voice output in a noisy saloon) to the minimal rear-facing camera, to the pair of buttons on the side used by each speaker to toggle the language recognition mode. Personally, I’d prefer if the device had no on-line capability at all; perhaps I’ll strip out the wifi antenna entirely. The UI is similarly minimal, full of quirks that I’m fine “learning through” but any trendy tech reviewer would rip it apart in disgust: “ugh, the icon design is soooo last generation and the menu navigation require *two* swipes. This work is so *derivative*“.

At \$40, it’s cheap enough to carry around as a backup translator when I’m on the road or for lending to local guides; I don’t lose sleep if it gets nicked at the bar or left in a taxi. On close inspection, some of the parts look like they were recycled (which imho is not a bad thing that old silicon is finding new life), and the fit and finish is pretty good for \$40 but nowhere near the standard of thousand-dollar smartphones. But, like most shanzhai products it has already been cloned and is available in a wide variety of form factors and price points. I’m pretty sure the ones that sell for hundreds of dollars aren’t materially different from this one — maybe they use better quality parts, but more likely than not they are simply charging more for the same BOM because Western consumers expect a device like this to cost much more than it does. Smartphone advertising has done an amazing job of programming consumers to accept higher prices for minor differences.

I wonder how it does all of its processing offline – my guess is the small Mali GPU included on the 3G chipset is just powerful enough to do real-time audio inference, and/or some amount of character recognition processing on images. The fact that it can do this processing offline, and so cheaply, further implies that it’s now easy to embed highly effective speech-to-text listening devices in every kiosk and hallway, which makes mass surveillance/real-time ad targeting a lot more bandwidth efficient. It’s small enough to Trojan into a wall power adapter, and with 3G functionality you can efficiently exfiltrate text conversations over SMS after screening for key words. Without a screen or battery, the cost overhead would be just a few dollars per surveillance endpoint. A power adapter listening device would be super easy to bundle into almost any off the shelf consumer product, giving it a free pass into conference rooms, homes and hotel rooms around the world.

Ah yes, I should also probably pick a winner. This ware suffers from the “every contemporary gadget looks like a cell phone” problem, so it was tough to guess (but also tough to image search). For no particularly strong reason, I’ll pick AZeta as the winner – the response did identify the device is wifi only, and highlighted the computational potential of the SoC; and a baby monitor is a kind of surveillance device. Congrats, email me for your prize!

This entry was posted on Friday, May 31st, 2024 at 2:38 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-april-2024/feed/) feed.
Both comments and pings are currently closed.

Comments are closed.

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).