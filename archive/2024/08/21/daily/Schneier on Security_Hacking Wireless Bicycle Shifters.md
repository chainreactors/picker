---
title: Hacking Wireless Bicycle Shifters
url: https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html
source: Schneier on Security
date: 2024-08-21
fetch_date: 2025-10-06T18:05:18.367747
---

# Hacking Wireless Bicycle Shifters

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

## Hacking Wireless Bicycle Shifters

This is yet another insecure Internet-of-things [story](https://arstechnica.com/security/2024/08/researchers-hack-electronic-shifters-with-a-few-hundred-dollars-of-hardware/), this one about wireless gear shifters for bicycles. These gear shifters are used in big-money professional bicycle races like the Tour de France, which provides an incentive to actually implement this attack.

Research [paper](https://www.usenix.org/system/files/woot24-motallebighomi.pdf). Another [news story](https://jalopnik.com/hackers-are-targeting-tour-de-france-riders-fancy-elec-1851622950).

Slashdot [thread](https://it.slashdot.org/story/24/08/15/2019206/researchers-hack-electronic-shifters-with-a-few-hundred-dollars-of-hardware).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [firmware](https://www.schneier.com/tag/firmware/), [hacking](https://www.schneier.com/tag/hacking/), [Internet of Things](https://www.schneier.com/tag/internet-of-things/), [patching](https://www.schneier.com/tag/patching/)

[Posted on August 20, 2024 at 7:08 AM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html) •
[17 Comments](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html#comments)

### Comments

Clive Robinson •
[August 20, 2024 10:54 AM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html/#comment-440124)

@ Bruce, ALL,

Whilst a patch might solve one aspect of the problem it won’t stop others.

There is such a thing as “jamming margin” which is always going to be present in radio based systems.

Put simply if I increase my on frequency energy above that of the user at the receiver antenna their signal becomes lost as the demodulator in the receiver demodulates my signal not that of the user.

Even with complex modulation schemes such as Spread Spectrum the same thing applies just more power is required by my transmitter…

Believe it or not one of the reasons such radio systems are used is because it’s less expensive than using wire as well as being less weight etc.

Eriadilos •
[August 20, 2024 11:29 AM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html/#comment-440125)

It at least seems like Shimano thought a little about the security of their solution, although it is obviously not perfect.

However, I don’t see how the DoS can be prevented, it is inherent to wireless technologies. In the case of Tour de France an other professional riders I see 2 solutions :
– The tech savy teams will switch back to mechanical, which is improbable
– Once an attack is carried out and has serious consequences on performance or rider health, they will switch back to mechanical

I get that wireless is attractive to manufacturers as it avoids them cable routing, but what is wrong with simple cables ? As a user having to recharge your (leg operated) bike seems unnecessary

Aaron •
[August 20, 2024 11:53 AM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html/#comment-440127)

Wireless Bicycle Shifters
Another technological tale of “just because you can, doesn’t mean you should”

dorian •
[August 20, 2024 11:58 AM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html/#comment-440128)

The researchers wrote “Modern bicycles are cyber-physical systems”, but it’s not really true. Bruce has it right: this affects “big money” bicycles. The Dura-Ace Di2 costs around $4,000 (USD), whereas the “[affordable](https://bikerumor.com/shimano-105-di2/)” 105 Di2 is about half that.

A non-racer can get a pretty nice bicycle for under $1,000; possibly well under, with end-of-season and rental-bike sales during the next 60 days or so. It’ll include quite a lot of modern technology, but nothing “cyber”. (Indexed shifting was apparently invented in 1969, for example, but only become common during the 1990s. And there are reasons why bicycles themselves didn’t become popular till the 1890s.) The vast majority come with no electrical or electronic components whatsoever.

lurker •
[August 20, 2024 2:42 PM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html/#comment-440132)

Blutooth Bites Again …
I can understand the incentive on racing bikes to eliminate the weight and wind resistance of physical wiring, but the “designers” of these systems seem to have assumed that “wireless” is some magic sauce that simply replaces wires. The ability to complicate things by linking with wearable body function monitors must have been irresistable. And of course to keep costs down they don’t hire anybody who understands “wireless” communications and security.

Years ago I had a bike odometer, mechanical, mounted on the front fork, with a five toothed cog which was turned one tooth (1/5th of a turn) when struck by a pin screwed onto one of the wheel spokes. There were specific devices for the two popular wheel sizes. Nowadays with many wheel sizes used, a one-size-fits-all electronic gadget uses a magnet on the spoke which excites a Hall effect sensor, wired to a tiny computer on the handlebar which can be set for any wheel size, calculate speed, trip distance, total distance, &c. The wire between sensor and counter is now being replaced by blutooth connection, even for commuter shopping bikes. The basic reason seems to be “just because.”

finagle •
[August 20, 2024 3:55 PM](https://www.schneier.com/blog/archives/2024/08/hacking-wireless-bicycle-shifters.html/#comment-440133)

Not disputing their results, but when SRAM first mooted wireless shifters as a response to issues over them launching a competitor to the wired Di2 Shimano system there were immediate concerns over security and whether a bike could be hacked. Quite a lot of conversations ensued.
How the SRAM security was described to me at the time was wireless signals would use AES256 encryption, with the components needing to be paired in advance to setup a unique shared secret across the components. Once the parts were paired then signals would be unique to the components on the bike. Replay attacks were mentioned and I think a simple single use token was incorporated in each message, to ensure playback attacks were impossible. A wired connection to a laptop was needed to change the pairing. They weren’t Bluetooth at that time either, as Bluetooth was higher battery consumption, and range was severely limited, so interception required you to be really close to a moving bike.
Shimano implemented their wireless more recently, so I would have expected it to be more secure, but clearly not.
For those that don’t build or maintain bikes, or maybe even ride them who are scratching their heads as to why wireless shifting is even a thing, electronic shifting is smooth and less susceptible to wear. Wireless systems don’t need to run rel...