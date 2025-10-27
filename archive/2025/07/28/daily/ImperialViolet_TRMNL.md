---
title: TRMNL
url: http://www.imperialviolet.org/2025/07/27/trmnl.html
source: ImperialViolet
date: 2025-07-28
fetch_date: 2025-10-06T23:22:22.030288
---

# TRMNL

# [ImperialViolet](https://www.imperialviolet.org)

### [TRMNL](/2025/07/27/trmnl.html) (27 Jul 2025)

The [TRMNL](https://usetrmnl.com/) is an 800×600, 1-bit e-ink display connected to a battery and a microcontroller, all housed in a nice but unremarkable plastic case. Because the microcontroller spends the vast majority of the time sleeping, and because e-ink displays don't require power unless they're updating, the battery can last six or more months. It charges over USB-C.

When the microcontroller wakes up, it connects to a Wi-Fi network and communicates with a pre-configured server to fetch an 800×600 image to display, and the duration of the next sleep. You can flash your own firmware on the device, or point the [standard firmware](https://github.com/usetrmnl/trmnl-firmware) at a custom server. The company provides an [example server](https://github.com/usetrmnl/byos_hanami), although you can implement the (HTTP-based) protocol in whatever way you wish.

I considered running my own server, but thought I would give the easy path a try first to see if it would suffice. The default service lets you split the display into several tiles, and there are a number of pre-built and community-built things that can display in each. None of them worked well for me, but that's okay because you can create your own private ones. They get data either by polling a given URL, or by having data posted to a webhook. The layout is rendered using the [Liquid](https://shopify.github.io/liquid/) templating system, which I had not used before, but it's reasonably straightforward.

I wrote a Go program hosted on [Cloud Run](https://cloud.google.com/run) which fetches the family shared calendar and converts events from the next week into a JSON format designed to make it trivial to render in the templating system.

With a [3D-printed holder](https://makerworld.com/en/models/1045586-trmnl-magnetic-fridge-mount#profileId-1031360), super glue, and some [magnets](https://www.amazon.com/dp/B0DXSF9JJJ), it's now happily stuck to the fridge where it displays the current date and the family events for the next week.

The most awkward part of the default service is managing the refreshes. The device has a sleep schedule, and so do the tiles, which are only updated periodically. So the combination can easily leave the wrong day showing. It would be helpful if the service told you when the device would next update, and when a given tile would next update. But it's not a huge deal and, after a little bit of head scratching, I managed to configure things such that the device updates in the early hours of the morning and the tiles are ready for it.

The price has gone up a bit since I ordered one, and you have to pay an extra $20 for the Developer Edition to do interesting things with it. So it ends up a little expensive for something that's neat, but hardly life-changing. But maybe you'll figure out something interesting for it! (Or you can [repurpose an old Kindle](https://usetrmnl.com/guides/turn-your-amazon-kindle-into-a-trmnl) into a TRMNL device.)