---
title: Quickpost: The Electric Energy Consumption Of A Wired Doorbell
url: https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/
source: Didier Stevens
date: 2024-11-04
fetch_date: 2025-10-06T19:13:52.379543
---

# Quickpost: The Electric Energy Consumption Of A Wired Doorbell

# [Didier Stevens](https://blog.didierstevens.com/)

## Sunday 3 November 2024

### Quickpost: The Electric Energy Consumption Of A Wired Doorbell

Filed under: [Hardware](https://blog.didierstevens.com/category/hardware/),[Quickpost](https://blog.didierstevens.com/category/quickpost/) — Didier Stevens @ 0:00

I have a classic [wired doorbell](https://en.wikipedia.org/wiki/Doorbell#Wired_doorbells) at home: the 230V powered [transformer](https://en.wikipedia.org/wiki/Transformer) produces 12V on its secondary winding. The circuit on that secondary winding powers an electromechanical doorbell via a pushbutton. The bell rings (“ding-dong”) when the button is pushed (closing the circuit).

Since losses occur in all transformers, I wanted to know how much my doorbell transformer consumes in standby mode (doorbell not ringing). The primary winding is always energized, as the pushbutton (normal-open switch) is on the circuit of the secondary winding.

I made the measurements on the primary winding: 3,043 Watt. That’s more than I expected, so I double-checked, and noticed I had forgotten this:

![](https://blog.didierstevens.com/wp-content/uploads/2024/11/image.png)

There’s a small incandescent light-bulb in the doorbell button. That consumes power too!

Second set of measurements after removing the light-bulb: 1,475 Watt.

So with light-bulb, my doorbell consumes 3 Watt 24/7, and 1,5 Watt without light-bulb.

1,5 Watt is very similar to the standby consumption of [linear power supplies](https://blog.didierstevens.com/2022/10/08/quickpost-standby-power-consumption-of-an-old-linear-power-supply/). As energy experts here in Europe advice to replace linear power supplies in favor of switched-mode power supplies, I wonder why they never mention doorbells … Replacing your doorbell would not be as easy as replacing a (USB) charger though (it would best be done by an electrician), so that might explain it, but on the other hand, there are enough energy experts proposing impractical solutions.

3 Watt is 26,28 kWh for a whole year. In my case, that’s a cost of €5,89 (that’s total cost: electricity plus taxes). I could reduce this by half, just by removing the incandescent light-bulb.

Should I do this? Well, the decision has already been taken for me: I dropped the light-bulb while it was still hot, and the impact broke the filament …

For comparison: 3 Watt is at least three times higher than the individual standby consumption of our appliances like TV, fridge, freezer, …

Yet another comparison: asking an [LLM to write an email](https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/) requires less (< 0,3 Wh) than my doorbell over a period of an hour (3 Wh).

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/?share=x)

### *Related*

[Comments (4)](https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/#comments)

## 4 Comments [»](#postcomment "Leave a comment")

1. lol

   Comment by Anonymous — Wednesday 6 November 2024 @ [12:32](#comment-629492)
2. A doorbell uses a simple electromagnetic coil to pull in the plunger. That electromagnetic doesn’t know the difference between AC and DC. As a test, I tried ringing my 24VAC doorbell with a DC power supply and got a good ding at 5V DC. Then why not replace the lossy transformer with an efficient USB power supply that produces 5V DC?

   Another thought: how did you measure 1.5 watts of wasted energy? Did you take into account the fact that an unloaded transformer will consume current but that current will be out-of-phase with the voltage? This is called low power-factor. Because current and voltage are out of phase, you can’t simply multiply one number for measured current with one number for measured voltage. A good power meter will do this correctly, but even a very expensive ampmeter will not do this.

   Comment by Anonymous — Monday 9 June 2025 @ [14:33](#comment-630313)
3. I won’t change to a more efficient power supply, because that would not only require making the change, but also documenting it and having my electrical installation re-certified. And that complete process is way too expensive compared with the cost of the light.
   I made the measurements with a good bench power meter. It can also measure harmonics. Don’t know the model from the top of my head, by I reference it in other blog posts.

   Comment by [Didier Stevens](https://didierstevens.wordpress.com/) — Monday 9 June 2025 @ [21:21](#comment-630315)
4. Correction: I remember now, I did the measurements with a professional energy multimeter: a Metrahit Energy.
   It takes the power factor into account.

   Comment by [Didier Stevens](https://didierstevens.wordpress.com/) — Monday 9 June 2025 @ [21:30](#comment-630316)

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](htt...