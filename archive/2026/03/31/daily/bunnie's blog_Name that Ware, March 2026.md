---
title: Name that Ware, March 2026
url: https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/
source: bunnie's blog
date: 2026-03-31
fetch_date: 2026-04-01T04:45:14.702810
---

# Name that Ware, March 2026

---

[« Winner, Name that Ware February 2026](https://www.bunniestudios.com/blog/2026/winner-name-that-ware-february-2026/)

## Name that Ware, March 2026

The Ware for March 2026 is below:

[![](https://bunniefoo.com/ntw/ntw_march_2026_sm.jpg)](https://bunniefoo.com/ntw/ntw_march_2026.jpg)

This ware malfunctioned, so I took it apart to see what’s going on and now it’s this month’s Name that Ware. As it would be far too easy to guess if I showed the whole circuit board, this is just a portion of the whole ware. I suspect the nature of the ware will be easy to figure out, but would be impressed if anyone can determine the exact make & model, since these are likely OEM’d by a handful of factories and the same core design is shared among a wide family of devices.

As a *mostly* unrelated side-rant, one side effect of the transition to USB-C that I’ve noticed is that power ratings just aren’t what they used to be. If a power supply said 100 watts on the label, it used to mean 100 watts continuous over a full consumer temperature range. Now, somehow, it seems to have become normalized that it’s 100 watts “briefly”, and maybe two thirds of that continuously on a good day. This is a problem if you use your laptop to do board layout (stressing the discrete GPU) while compiling large Rust programs in the background (stressing the CPU) for hours at a time, while also trying to charge your battery after a long flight. Then again, a 90% efficient regulator at 100 watts is dissipating roughly 10 watts of heat – as much as a small soldering iron – so maybe I shouldn’t be so shocked by this outcome.

This entry was posted on Tuesday, March 31st, 2026 at 3:45 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/feed/) feed.
You can [leave a response](#respond), or [trackback](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/trackback/) from your own site.

### 6 Responses to “Name that Ware, March 2026”

1. ![](https://secure.gravatar.com/avatar/46bc108c16b0286f15f08ab432a20575?s=32&d=mm&r=g) tayken says:

   [March 31, 2026 at 4:09 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/#comment-2754775)

   I’d guess some sort of laptop docking station. Side rant made me think USB-C power supply but the ICs were the big hint.

   The IC in the center is marked as VL817, a USB 3.1 Gen1 4-port hub controller. The one on the right is AG9411, which is a USB-C to HDMI converter.

   [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/?replytocom=2754775#respond)

   * ![](https://secure.gravatar.com/avatar/46bc108c16b0286f15f08ab432a20575?s=32&d=mm&r=g) tayken says:

     [March 31, 2026 at 4:53 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/#comment-2754781)

     Forgot to mention, AG9411 is described as “DisplayPort 1.4 over USB-C to HDMI 2.0 converter with PD 3.0”. The product page mentions that it supports one USB Type-C plug and one USB Type-C receptacle. I believe it’s directly connected to the laptops USB-C port and creates a mixed USB3 + dual lane DP connection. Then it passes the USB3 connection to the USB hub IC. I highly suspect this is the way it’s handled as there is a connector pinout on the right hand side. I think this is where the USB cable of the docking port is soldered. Its labels match with the pins used for DP alt mode:
     \* B5: Vconn
     \* A5: CC
     \* A6: D+
     \* A7: D-
     \* B8: Sideband use 2
     \* A8: Sideband use 1
     \* A4: Vbuc

     Also there seems to be a connector sitting on the other side of AG9411. The shield pins look different compared to the connector on the other side of VL817, or the one of the left of it. Maybe the connector on the other side of the AG9411 is the power input and the others are the USB A ports.

     [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/?replytocom=2754781#respond)
2. ![](https://secure.gravatar.com/avatar/e3943c6f37402b3384a3c5097f1c7860?s=32&d=mm&r=g) Kazriko says:

   [March 31, 2026 at 6:25 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/#comment-2754785)

   Consumer manufacturers have definitely taken the Muntzing of their equipment to an extreme the last couple of decades…

   [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/?replytocom=2754785#respond)
3. ![](https://secure.gravatar.com/avatar/c76732853329bbe35fd81558a42508a1?s=32&d=mm&r=g) Jin says:

   [March 31, 2026 at 8:27 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/#comment-2754787)

   this is a HDMI 2.0 + USB-A dongle just like what tayken explained earlier.

   What I find this interesting is that I suspect this is an Anker brand but china Aigo OEM design board that go for the lower cost market.

   The reason:
   RoHS brand design (export model)
   ENIG solder pad
   Anker style USB-C test pad

   But it have the green soldermask and way more label that the typical high end Anker dongle which usually feature a black PCB board and smaller silkscreen font.

   Also the lack of TVS diode and dirty solder oil mark suggest this is a not a super high quantity assembled product but the tracing of the chip and the ENIG solder pad super similar to Anker design.

   I am very confuse about the origin of this board. Maybe this is what we get from Anker nowadays since all the teardown i saw for anker dongle is not that latest.

   [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/?replytocom=2754787#respond)

   * ![](https://secure.gravatar.com/avatar/f5a247faeba41ba01a510b80a4a87152?s=32&d=mm&r=g) johslarsen says:

     [April 1, 2026 at 9:19 am](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/#comment-2754801)

     The port layout is identical to an Anker 6-in-1 USB-C Hub (<https://www.chargerlab.com/teardown-of-anker-6-in-1-usb-c-hub-a8365/>), but the chip layout is slightly different and the solder mask is green instead of black like you said. Probably a Chinese knock-off.

     I did not have much luck finding OEM branded ones on AliExpress with the same port layout. The closest I found was a UGREEN 7-in-1 adapter (<https://us.ugreen.com/products/7-in-1-multiport-adapter-with-4k-60hz>), but that seems to be a bit wider than the Anker adapter.

     [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/?replytocom=2754801#respond)
4. ![](https://secure.gravatar.com/avatar/1e5c813478ea7293fe81cc28012e738d?s=32&d=mm&r=g) [deadbeef](https://spacehey.com/0xdeadbeef_ayoub) says:

   [March 31, 2026 at 11:08 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/#comment-2754789)

   it feels like a random chinese ali express usb-c multiport adapter (docking station), the pcb model is prob EMA537-2F

   [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-march-2026/?replytocom=2754789#respond)

### Leave a Reply

[Click here to cancel reply.](/blog/2026/name-that-ware-march-2026/#respond)

Name (required)

Mail (will not be published) (required)

Website

Δ

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).