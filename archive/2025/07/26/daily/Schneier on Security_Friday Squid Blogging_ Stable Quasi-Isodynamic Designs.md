---
title: Friday Squid Blogging: Stable Quasi-Isodynamic Designs
url: https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html
source: Schneier on Security
date: 2025-07-26
fetch_date: 2025-10-06T23:54:54.251010
---

# Friday Squid Blogging: Stable Quasi-Isodynamic Designs

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

## Friday Squid Blogging: Stable Quasi-Isodynamic Designs

Yet another SQUID acronym: “[Stable Quasi-Isodynamic Design](https://www.ipp.mpg.de/5457187/SQulD_Stellarator).” It’s a [stellarator](https://en.wikipedia.org/wiki/Stellarator) for a fusion nuclear power plant.

Tags: [squid](https://www.schneier.com/tag/squid/)

[Posted on July 25, 2025 at 5:00 PM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html) •
[28 Comments](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html#comments)

### Comments

Ismar •
[July 25, 2025 5:48 PM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446704)

A Premium Luggage Service’s Web Bugs Exposed the Travel Plans of Every User—Including Diplomats | WIRED

<https://www.wired.com/story/luggage-service-web-bugs-exposed-travel-plans-users-diplomats-airportr/>

not important •
[July 25, 2025 7:22 PM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446707)

“Data is like garbage. You’d better know what you are going to do with it before you

@ALL Have a good weekend!

Clive Robinson •
[July 25, 2025 10:19 PM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446711)

@ Bruce,

When you lookup “stellarator” on Wikipedia you get,

> *“It is one of many types of magnetic confinement fusion devices. The name “stellarator” refers to stars because fusion mostly occurs in stars such as the Sun.”*

There is a little bit of irony there… Because “stars” achieve and maintain the conditions for “fusion” not by “magnetic confinement” but by the constriction effects of “gravity”.

The fun thing to note is that “magnetic confinement” has never achieved sustainable fusion.

Some think it never will because it is not stable. That is magnetic confinement is an external force that “pushes in”. Rather than gravity which is effectively an internal force that “pulls in” which is stable.

I suspect none of us reading this today will be around when sustainable stable fusion goes into commercial production of electricity or other way to efficiently transmit energy to the home etc.

So up there in the Unobtainium stakes along with AGI, Quantum Computing, World Peace and day trips to Mars 😉

lurker •
[July 26, 2025 1:28 AM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446713)

@Clive

When you lookup “stellarator” on Wikipedia you see –

pictures of star-shaped objects, surely difficult to contain magnetic fields within. And further irony, they should have known back then, that such magnetic containment as exists in the sun is unstable and leaks frequently, hurling blobs of solar material at us, causing pretty lights in the sky and comms and nav blackouts …

pattimichelle •
[July 26, 2025 1:18 PM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446721)

Heh. Humans cannot even safely handle fission tech.

Clive Robinson •
[July 26, 2025 4:12 PM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446725)

@ Bruce, ALL,

**Another attack on RAM secrets.**

I suspect some remember the tales of times distant past when DRAM would get frozen with something quite cold. Such that the contents of memory could be read out.

Some called it a “Cold Boot” attack and the solution used was to store secrets in SRAM in the chip thus making it nearly impossible to get at.

Or so many thought… Welcome to a new attack “Volt Boot” that exploits design failings in “System on a Chip”(SoC) devices power busses. Or as the Communications of the ACM article,

<https://cacm.acm.org/research-highlights/sram-has-no-chill-exploiting-power-domain-separation-to-steal-on-chip-secrets/>

Puts it,

> *“A Volt Boot attack leverages a vulnerability of on-chip volatile memories due to the physical separation common to modern system-on-chip power distribution networks.”*

So another fun hardware exploit and it’s not even Xmas.

Put simply SRAM “being static” retains what is written to it as long as power is maintained to it in various ways.

As the article indicates “embedded systems” are vulnerable. This includes most Internet of Things”(IoT) and network infrastructure and edge devices.

However it will probably work against some “Smart Devices” such as Pads and Mobiles.

In the distant past I gave methods of protecting “root of trust” KeyMat by using evolving “data shadows” that should still work today.

Clive Robinson •
[July 27, 2025 2:08 AM](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-stable-quasi-isodynamic-designs.html/#comment-446728)

@ pattimichelle,

With regards,

> “Heh. Humans cannot even safely handle fission tech.”

The way we currently do it is kind of,

1, Start a nuclear bomb
2, Get the heat in to a pressure cooker bomb
3, Vent off pressure into turbines
4, Hope that the turbines and generators they drive wont lock up or fly apart under changeable rotational forces.

What could possibly go wrong, with that?

That has not already happened one place or another…

Oh and why such power stations are only useful for,

“Constant base load that is resistive”

Which is so 20th century…

The problem being in our drive to being not wasteful this century our loads have become highly reactive and very variable.

Which can sort of be averaged out and power factor corrected if all the loads act as though they are independent within about five times the averaging time.

Even back last century that was not true, with very few entertainment channels on TV and radio and a National Sporting Event the load would go up and down like an express elevator. But it was possible for the skilled technicians in the National Grid to predictively act as part of the control loop and spin up and spin down for peak loads. Such as at half time when everyone put the kettle on…

The recent Iberian Peninsula Peninsular “black out” that took Spain, Portugal and quite a few other parts of Western Europe “off the European grid” is still a bit of a mystery…

Back last century the national grids got fast damping from “inertial load” from the “mechanical” rotational mass in the generators and turbines acting like a “fly wheel”.

Highly efficient Green power sources such as Solar has no moving parts so no mechanical storage for fast damping.

Thus you need less efficient wind or wave systems that do have mechanical storage, or you need something else.

Wind is very far from predictable enough to give grid sized fly wheel damping. And whilst wave is more predictable it has a cyclic pattern that does not match the human power require...