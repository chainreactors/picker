---
title: Thomas Fitzsimmons: Glove82
url: https://www.fitzsim.org/blog/?p=840
source: Planet Classpath
date: 2026-08-31
fetch_date: 2026-09-01T06:59:37.290857
---

# Thomas Fitzsimmons: Glove82

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Glove82

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [August 30, 2026August 30, 2026](https://www.fitzsim.org/blog/?p=840)
[Leave a comment on Glove82](https://www.fitzsim.org/blog/?p=840#respond)

I have been using the Glove80 keyboard for a few years now, and it suits me very well.

I have some quibbles about the software[1](https://www.fitzsim.org/blog/?p=840#footnote1) and hardware. This blog post is about fixing the hardware.

The keyboard has function keys F1 through F10. This design decision — detailed at [Why are there no F11 and F12 keys?](https://www.moergo.com/pages/faqs) — was to reduce the height of the keyboard for portability. Personally, I wouldn’t mind an extra 12mm in keyboard height; I would prefer to have the extra keys. I wondered if I could add them.

The Glove80 designers cleverly left an [“escape hatch”](https://docs.moergo.com/glove80-user-guide/appendix-more-customizations/) to facilitate extra buttons and other peripherals. I wondered if I could use that to add F6 and F7 keys.

The keyboard is expensive, so I did not want to drill holes or dremel the case or solder directly onto any PCB. My idea was to use the provided GPIO pin header and sneak thin (30 AWG) wires through the power LED case holes such that I could undo everything cleanly if necessary.

For the software side of the modifications, I used the generic ZMK port so I could follow the “west” tool setup instructions verbatim and build the firmware on my own machine (avoiding the recommended proprietary build pipelines). Once I found the right area of the documentation website the instructions were up-to-date and easy-to-follow. I wrote a [ZMK patch](https://www.fitzsim.org/patches/glove82-zmk-1.patch) I thought should work.

Now that the software was ready to test, I bought some supplies:

![Supplies needed to convert Glove80 to Glove82.  Some 30 AWG wire, a 2x6 1.27mm ribbon cable, and two Kailh Low Profile Choc switches.](https://www.fitzsim.org/screenshots/glove82/glove82-supplies.jpg)

Supplies needed to convert Glove80 to Glove82. Some 30 AWG wire, a 2×6 1.27mm ribbon cable, and two Kailh Low Profile Choc switches.

I opened the case, connected the ribbon cable, and performed a test with multimeter probes:

![Hardware setup for probing Glove80 extension pinout.](https://www.fitzsim.org/screenshots/glove82/glove82-probe-test.jpg)

Hardware setup for probing Glove80 extension pinout.

After orienting myself to the pin-numbering scheme,

![Ribbon cable pinouts.](https://www.fitzsim.org/screenshots/glove82/glove82-pin-numbering.jpg)

Ribbon cable pinouts.

I determined the correct pins and connected them. *xev* showed the new F6 key registering!:

![Running xev while probing ribbon cable.](https://www.fitzsim.org/screenshots/glove82/glove82-xev-test.jpg)

Running *xev* while probing ribbon cable.

I started work hacking together a cable (with some soldering help from my son and daughter). Here is the result:

![Glove82 wiring harness installed in chassis.](https://www.fitzsim.org/screenshots/glove82/glove82-harness.jpg)

Glove82 wiring harness installed in chassis.

One more test of shorting the exported wires and I felt confident enough to tape the new harness to the inside of the case. Next, I screwed the cover back on, and routed and secured with Kapton tape the extra wire length I left for further mounting experimentation:

![Routing of wires outside chassis.](https://www.fitzsim.org/screenshots/glove82/glove82-external-wire-routing.jpg)

Routing of wires outside chassis.

To mount the key to the keyboard, I had been conceptualizing something 3D-printed and clip-on. However for the prototype my daughter suggested double-sided sticky tape (“the foam kind”). It turned out to be strong enough to support the key itself and key presses (I use the lightest 35gf switches):

![Key mounting test.](https://www.fitzsim.org/screenshots/glove82/glove82-double-sided-sticky-tape.jpg)

Key mounting test.

I did the second half of the keyboard and… Behold, the final prototype:

![Working Glove82 prototype.](https://www.fitzsim.org/screenshots/glove82/glove82-working-prototype.jpg)

Working Glove82 prototype.

It looks funny because the new keys are raised off the board. It turns out this doesn’t actually bother me or negatively impact usability. The risk of cutting into the case to make the new keys flush *would* bother me!

When making a window fullscreen during testing it was immediately satisfying to mash F11 exactly where I expected it, instead of searching the web for [the layout of the Glove80 lower layer](https://docs.moergo.com/glove80-user-guide/images/lower-layer.png).

#### Potential Future Improvements

Maybe I will find the motivation to design a clip-on 3D-printed mount to replace the tape.

At some point I might create a fork of the official MoErgo firmware with my Glove82 patch, to get back the extra features that the vanilla ZMK port is missing (e.g., LED support). Upstream ZMK and the MoErgo branch have diverged though so this isn’t trivial.

For now though, the keyboard is usable as-is, so I will use it for a while and see how the modifications hold up.

[1](https://www.fitzsim.org/blog/?p=840#reference1). I wish some heroes of the Internet would reverse engineer and re-implement the nRF52840 Bluetooth stack under a [GPL-compatible](https://github.com/qmk/qmk_firmware/issues/18556) license.

*Thank you to [mtegel](https://mtegel.org/), [lexano](https://github.com/lexano-ivs), and my daughter, for reviewing a draft of this post.*

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[August 30, 2026August 30, 2026](https://www.fitzsim.org/blog/?p=840)Posted in[Uncategorized](https://www.fitzsim.org/blog/?cat=1)

## Post navigation

[Previous Post Previous post:
gfx1201 on POWER9](https://www.fitzsim.org/blog/?p=797)

## Leave a comment

### [Cancel reply](/blog/?p=840#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

*The views expressed on this blog are my own and do not reflect the opinions, positions, or policies of my employer.*
[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)