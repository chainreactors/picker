---
title: Exploding USB Sticks
url: https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html
source: Schneier on Security
date: 2023-03-25
fetch_date: 2025-10-04T10:40:55.200077
---

# Exploding USB Sticks

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

## Exploding USB Sticks

In case you don’t have enough to worry about, people are [hiding explosives](https://www.cbsnews.com/news/news-stations-letter-bombs-ecuador-one-explodes-clear-message-to-silence-journalists/)—actual ones—in USB sticks:

> In the port city of Guayaquil, journalist Lenin Artieda of the Ecuavisa private TV station received an envelope containing a pen drive which exploded when he inserted it into a computer, his employer said.
>
> Artieda sustained slight injuries to one hand and his face, said police official Xavier Chango. No one else was hurt.
>
> Chango said the USB drive sent to Artieda could have been loaded with RDX, a military-type explosive.

[More](https://arstechnica.com/gadgets/2023/03/journalist-plugs-in-unknown-usb-drive-mailed-to-him-it-exploded-in-his-face/):

> According to police official Xavier Chango, the flash drive that went off had a 5-volt explosive charge and is thought to have used RDX. Also known as T4, according to the Environmental Protection Agency ([PDF](https://www.epa.gov/sites/default/files/2017-10/documents/ffrro_ecfactsheet_rdx_9-15-17_508.pdf)), militaries, including the US’s, use RDX, which “can be used alone as a base charge for detonators or mixed with other explosives, such as TNT.” Chango said it comes in capsules measuring about 1 cm, but only half of it was activated in the drive that Artieda plugged in, which likely saved him some harm.

Reminds me of assassination by [cell phone](https://israeled.org/phone-bomb-kills-terrorist-yahya-ayyash/).

Tags: [bombs](https://www.schneier.com/tag/bombs/), [terrorism](https://www.schneier.com/tag/terrorism/), [USB](https://www.schneier.com/tag/usb/)

[Posted on March 24, 2023 at 7:04 AM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html) •
[19 Comments](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html#comments)

### Comments

Winter •
[March 24, 2023 8:09 AM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419752)

> In the port city of Guayaquil, journalist Lenin Artieda of the Ecuavisa private TV station received an envelope containing a pen drive which exploded when he inserted it into a computer, his employer said.

86 journalists were killed in 2022. Remember that people rarely get murdered for lying. When people get killed, it is for speaking the truth.

‘https://news.un.org/en/story/2023/01/1132507

‘https://rsf.org/en

Mack •
[March 24, 2023 9:13 AM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419755)

@Bruce

Now that is interesting. Can cell phones normally be made to explode remotely or was that some weird “government replaced” version? Should this be a concern for “regular” people?

Hans •
[March 24, 2023 9:36 AM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419757)

@Mack
From the article:

> A Hamas informant who reportedly received $1 million and refuge in the United States
> helped the Shin Bet smuggle Ayyash’s phone out of and back into Gaza so it could be
> turned into a bomb.

So it should only be a concern to you if your death is worth $1 million to someone.

Andy •
[March 24, 2023 10:12 AM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419758)

Also note that the cell phone for 1M$ was in 1996…

Kent Brockman •
[March 24, 2023 12:23 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419763)

Putting a strange pen drive in one’s computer is rather a dumb move even if you’re not worried about being blown to hell. Aquiring a virus or trojan payload is a good possibility.

Chelloveck •
[March 24, 2023 12:42 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419764)

This is going to lead to not being able to carry thumb drives on airplanes, isn’t it? Or maybe we’ll have to separate thumb drives out in clear plastic bags, and no single drive over 3.5 GB will be allowed…

ALT •
[March 24, 2023 2:17 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419769)

@Kent Brockman
Journalists may need to do this with confidential sources, and the computer *might* have been air gapped with no writable storage – would not be too dumb.

Leonid •
[March 24, 2023 2:17 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419770)

@Kent Brockman: “Putting a strange pen drive in one’s computer is rather a dumb move even if you’re not worried about being blown to hell. Aquiring a virus or trojan payload is a good possibility.”

This is complete nonsense, because a virus/trojan is a program that needs to be executed to do harm. So… don’t execute anything from untrusted media (and don’t use OS that does so automatically).

Even rubber-ducky type attacks can be thwarted if you plug an untrusted drive into a device and login to the latter remotely, or use an environment that won’t take input from an unknown device (e.g. MacOS has protection against such attacks).

iAPX •
[March 24, 2023 2:37 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419771)

@Leonid

You put too much trust into OS level security and behaviours, USB controller firmware security, and generally modern computing platforms security.

And also the inability of your attacker to not have insider informations, for example for the exact model of USB keyboard that is available at your job (for example).

In fact if Stuxnet was so efficient, and was also detected on other devices that those targeted, it’s because people were putting trust in the wrong place.
They trusted the USB controllers, they trusted their OSes, theyr trusted their antivirus, and so on…

It’s very difficult to read a USB Key safely, it involves using low-tech and burner devices.

ALT •
[March 24, 2023 3:44 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419773)

@iAPX

Yes, firmware is a problem – I should have written “would not be *too* dumb”.

So, maybe it’s harder to make an exploding CD/DVD?

iAPX •
[March 24, 2023 4:09 PM](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html/#comment-419775)

@ALT

In fact you need low-tech and burner devices (plural is not an error).

Attacks could come from the USB high-level protocol (and physical too if firmware is backdoored at this level!) targeting firmware and OS, and encapsulated protocols (say keyboard for example) targeting their support on the OS (or a backdoor on USB firmware), so this is at least one step, and a burner device.

Then with full data contained on the USB Key (all blocks), you might still have a Boot-record MBR/GPT/etc. attack, an UFI/UEFI attack, a filesystem attack.
You need a burner at this point.

Then you have files, including one containing all the blocks of the initial U...