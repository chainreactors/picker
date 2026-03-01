---
title: The Mystery of Skype
url: https://clevcode.org/the-mystery-of-skype/
source: ClevCode
date: 2026-02-28
fetch_date: 2026-03-01T04:26:54.856980
---

# The Mystery of Skype

[Skip to content](#page)

[ClevCode](https://clevcode.org/)

Vulnerability Research, Exploit Development, Reverse-Engineering

### Recent Posts

* [The Mystery of Skype](https://clevcode.org/the-mystery-of-skype/)
* [Ashley Madison Post-Mortem](https://clevcode.org/ashley-madison-post-mortem/)
* [Android HID device forwarding](https://clevcode.org/android-hid-device-forwarding/)
* [Low-latency VR desktop with Immersed](https://clevcode.org/low-latency-vr-desktop-with-immersed/)
* [31C3 CTF: Maze write-up](https://clevcode.org/31c3-ctf-maze-write-up/)

### Categories

* [Ashley Madison](https://clevcode.org/category/ashley-madison/) (1)
* [Codegate](https://clevcode.org/category/codegate/) (1)
* [CTF](https://clevcode.org/category/ctf/) (13)
* [Exploit Development](https://clevcode.org/category/exploit-development/) (7)
* [GCHQ](https://clevcode.org/category/gchq/) (3)
* [Mentorship](https://clevcode.org/category/mentorship/) (1)
* [Plaid CTF](https://clevcode.org/category/plaidctf/) (12)
* [Research](https://clevcode.org/category/research/) (4)
* [Reverse-Engineering](https://clevcode.org/category/reverse-engineering/) (1)
* [Team](https://clevcode.org/category/team/) (3)
* [Uncategorized](https://clevcode.org/category/uncategorized/) (1)
* [VR/XR/MR](https://clevcode.org/category/vr-xr-mr/) (2)
* [Work](https://clevcode.org/category/work/) (1)
* [Writeup](https://clevcode.org/category/ctf/writeup/) (15)

### People

* [Gynvael Coldwind](http://gynvael.coldwind.pl/)
* [Halvar Flake](http://addxorrol.blogspot.com/)
* [j00ru](http://j00ru.vexillium.org/)
* [Joshua J. Drake](http://twitter.com/jduck)
* [Michal Zalewski](http://lcamtuf.blogspot.com/)
* [Rolf Rolles](http://twitter.com/rolfrolles)
* [Sean Heelan](http://seanhn.wordpress.com/)

### Tools

* [BinaryNinja](https://binary.ninja/)
* [GDB](http://www.gnu.org/software/gdb/)
* [Ghidra](https://ghidra-sre.org/)
* [IDA Pro](http://www.hex-rays.com/idapro/)
* [Neovim](https://neovim.io/)
* [OllyDbg](http://www.ollydbg.de/)
* [Vim](http://www.vim.org/)
* [x64dbg](https://x64dbg.com/)

Expand Menu

* [ClevCode](https://clevcode.org/)
* [About](https://clevcode.org/about/)
* [Team](https://clevcode.org/team/)
* [Solving Cicada 3301](https://clevcode.org/cicada-3301/)
* [GCHQ](https://clevcode.org/canyoucrackit-co-uk-gchq-challenge-solution/)
* [pCTF](https://clevcode.org/pctf/)
* [Contact](https://clevcode.org/contact/)

![](https://clevcode.org/wp-content/uploads/2022/10/profile.jpg)

Joel Eriksson

Vulnerability researcher, exploit developer and reverse-engineer. Have spoken at BlackHat, DefCon and the RSA conference. CTF player. Puzzle solver (Cicada 3301, Boxen)

# The Mystery of Skype

2026-02-28
[0](https://clevcode.org/the-mystery-of-skype/#respond)
[Joel Eriksson](https://clevcode.org/author/je/ "Posts by Joel Eriksson")
[Uncategorized](https://clevcode.org/category/uncategorized/)

End of an era. Skype is finally shutting down for good.

What happens when you press that glowing blue call button? For most of Skype’s users—once numbering in the hundreds of millions—this question never crossed their minds. The magic just worked. A connection formed across continents, through firewalls, past corporate security systems, delivering crystal-clear encrypted communication when other technologies failed.

But for some of us, these black boxes of technology are irresistible puzzles begging to be solved.

## The Man Behind the Keyboard

“What is it that you actually do?” It’s a question I’ve fielded countless times, even from family members, and one I can rarely answer completely.

Some of you may know me through my work on the Cicada 3301 puzzles in 2012—those cryptic internet mysteries that captivated the world’s brightest minds. Others might recognize me from my public-facing security research: speaking about kernel exploitation techniques at BlackHat and Defcon, presenting “Hacking the Hacker” at the RSA conference, or perhaps from my appearance in a Netflix documentary about the Ashley Madison hack, where I led the technical investigation.

My team and I have traveled the world competing in the finals of international hacking competitions—from Codegate in South Korea to DefCamp in Romania and Defcon in Las Vegas. I’ve turned down more speaking opportunities than I can remember.

But these public endeavors, as challenging as they might seem, have always been child’s play compared to the projects I’ve been involved with where matters of national security were at stake. That work—the truly thrilling work—remains largely classified, existing only as redacted sections in unseen reports.

The significance of this hidden work hasn’t gone unnoticed by adversaries. Just a few years ago, I became a target of North Korean state-sponsored hackers, not once but twice, during their coordinated campaigns against security researchers in late 2020 and again in 2021. Fortunately, both attempts proved futile.

What I’m about to share is a rare glimpse into this other world—the one that exists in the shadows of technology. Like Cicada 3301, this journey had many layers, twists, and turns. Unlike those puzzles, however, this challenge demanded far more technical ability and persistence, with real-world implications that extended far beyond intellectual curiosity.

For obvious reasons, many details must remain secret. But what follows is perhaps the closest answer I can provide to that persistent question: “What is it that you actually do?”

## First Contact

In 2004, Skype was revolutionary: a communication system that seemed to defy the conventional rules of networking. It could establish connections between computers that shouldn’t have been able to reach each other, it promised encryption that nobody could break, and it guarded its secrets behind layers of sophisticated protection.

This used to be top-secret, but at this point I would assume it doesn’t really matter anymore. At least not when it comes to the technical aspects related to why I became very intimately familiar with Skype.

I initially started reverse-engineering Skype in 2004, slightly more than 20 years ago. They had a proprietary supposedly encrypted protocol, and they were using various techniques to make life significantly more difficult for anyone who wanted to take a peek inside.

What drew me to Skype wasn’t just technical curiosity. There was something almost defiant about how thoroughly they had locked their system down—as if issuing a challenge to those of us who believe that understanding how our technology works is a fundamental right. In a world increasingly built on closed systems, Skype represented a fortress of code that millions entrusted with their most private communications without knowing what was happening beneath the surface.

Every time I heard that distinctive Skype ringtone, I couldn’t help but wonder: what’s really happening behind that friendly interface? What mechanisms were at work, shuttling voices and messages across the digital expanse? And perhaps most importantly—was it as secure as everyone believed?

Little did I know that pulling on this thread would unravel a technological tapestry more intricate and ingenious than I had imagined. One that would consume countless hours over years of exploration, leading me deep into the heart of what was then the world’s most sophisticated peer-to-peer communication system.

This is the story of how I cracked open one of the internet’s most closely-guarded secrets, one assembly instruction at a time.

## Breaking Through the First Layer

My first encounter with Skype’s internals felt like opening a Russian nesting doll. Each layer revealed another, more intricate challenge beneath.

As with most protected software, Skype’s exterior defenses came in the form of a custom “packer”—a program that compresses and encrypts the actual executable code, unfolding itself only at runtime. It’s digital camouflage, designed to thwart curious eyes like mine.

The packer used self-modifying code...