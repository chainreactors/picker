---
title: 3D Printer Surveillance
url: https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html
source: Instapaper: Unread
date: 2026-02-12
fetch_date: 2026-02-13T04:18:53.088426
---

# 3D Printer Surveillance

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

## 3D Printer Surveillance

New York is [contemplating](https://blog.adafruit.com/2026/02/03/new-york-wants-to-ctrlaltdelete-your-3d-printer/) a bill that adds surveillance to 3D printers:

> New York’s 2026­2027 executive budget bill (S.9005 / A.10005) includes language that should alarm every maker, educator, and small manufacturer in the state. Buried in Part C is a provision requiring all 3D printers sold or delivered in New York to include “blocking technology.” This is defined as software or firmware that *scans every print file* through a “firearms blueprint detection algorithm” and refuses to print anything it flags as a potential firearm or firearm component.

I get the policy goals here, but the solution just won’t work. It’s the same problem as DRM: trying to prevent general-purpose computers from doing specific things. Cory Doctorow [wrote about it](https://boingboing.net/2018/03/22/yellow-dots-cubed.html) in 2018 and—more generally—[spoke about it](https://github.com/jwise/28c3-doctorow/blob/master/transcript.md) in 2011.

Tags: [3d printers](https://www.schneier.com/tag/3d-printers/), [guns](https://www.schneier.com/tag/guns/), [laws](https://www.schneier.com/tag/laws/), [privacy](https://www.schneier.com/tag/privacy/), [surveillance](https://www.schneier.com/tag/surveillance/)

[Posted on February 12, 2026 at 7:01 AM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html) •
[15 Comments](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html#comments)

### Comments

BCS •
[February 12, 2026 9:50 AM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html/#comment-452063)

Would the world be better off or worse off if the lawmakers actually understood what they were trying to regulate?

On the one hand, there would be fewer laws proposed that will never have any chance of being anything more than expensive virtue signaling. On the other, it will be harder to measure the hubris of the law makers.

Also, I think xkcd had a nice concise take on this: <https://xkcd.com/1425/>

RightToComputeRightToPrint •
[February 12, 2026 10:20 AM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html/#comment-452064)

The maker community ought to get a lot more vocal about this, remind the legislators that a 3d printer can be cobbled together from basic parts by just about anyone. Any printer infected\* with this sort of “DRM” can have its control board ripped out and replaced by an arduino with a couple of stepper dual h bridge boards which can run existing freedom-respecting firmware. There’s no need for advanced firmware hacking to rewrite a DRM-infected machine’s existing firmware, just a full transplant of the circuit board. The community needs to make it very clear that this sort of tyranny will not be obeyed. If lawmakers want to clamp down on gun violence they should target the supply of ammunition for restriction. Printed plastic isn’t a suitable material for something which has to survive as harsh an environment as the chamber of a gun must cope with, but whereas people have occasionally printed items which they call guns (but which are frankly more dangerous to the maniac firing them than to any intended target), nobody has ever or will ever print the bullet-plus-propellant combination required for a round of ammo. If the crooks running New York (and the crooks running Washington state too, they are trying the same thing, I doubt it is a coincidence, the pro planned obsolescence lobby must have gotten at both legislatures at once) want to push for this, they need to find themselves being frustrated at every turn by people who are cleverer than them in every way. I wonder if New York will soon be home to shops selling three entirely separate products,each of which definitely isn’t supposed to be bolted to another even though the holes would line up perfectly, one of which is a handheld plastic extrusion 3d pen, another is a hotplate and the other of which is an x-y-z linear stage assembly (core-xy, bedslinger, whatever). If I was in that benighted state, no way would I ever obey, this, along with protecting the right to general purpose computing (another Doctorow talking point) is a hill to die upon. The right to be able to make little plastic trinkets (ok, there’s a lot more use than trinkets but everything one makes is still a plastic item, plastic is great for little brackets and adaptors and household modifications and small hobby projects. NYC tyrants, please understand, plastic is still no good for guns) is more important than the supposed authority of a government.

\*infected really is the right word, because the only way anything like that can happen is by a printer uploading every file to the cloud to ask for permission whether that file is ok, and it won’t be able to stop people making bad thinga, all it will do is prevent people making repair and replacement parts for shoddily made consumer items with planned obsolescence

Rontea •
[February 12, 2026 10:39 AM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html/#comment-452065)

Requiring 3D printers to include “blocking technology” for firearm components is a classic example of security theater that risks far more than it solves. Once you embed surveillance and control mechanisms into general-purpose fabrication devices, you are sliding toward the same brittle, easily bypassed model that DRM imposed on computers. The danger isn’t just that it won’t stop people determined to print weapons—it’s that it creates a framework for monitoring and restricting all forms of 3D printing, chilling innovation and personal freedom. Security controls that are invasive and unenforceable ultimately weaken trust without meaningfully improving safety.

Tony •
[February 12, 2026 12:05 PM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html/#comment-452067)

Isn’t there already a precedent. Colour copiers won’t make a copy of something they identify as “currency”. [Not that this is any kind of good reason to mess with 3-D printers].

Agammamon •
[February 12, 2026 12:23 PM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html/#comment-452069)

Do these people not know that there are plans for easy building from base parts some pretty capable 3d printers? To the point that if you can assemble legos and manage a pre-built 3d printer you have the skills to build and operate your own.

<https://vorondesign.com/>

That’s just one of the options.

Worst case, you buy a shitty 3d printer to print out the plastic parts for your really good build-your-own printer – no gun check necessary.

And what are they going to do about desktop CNC?

Clive Robinson •
[February 12, 2026 12:26 PM](https://www.schneier.com/blog/archives/2026/02/3d-printer-surveillance.html/#comment-452070)

@ BCS, ALL,

You ask,

>...