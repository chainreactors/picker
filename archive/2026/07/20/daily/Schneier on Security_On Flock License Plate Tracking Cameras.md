---
title: On Flock License Plate Tracking Cameras
url: https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html
source: Schneier on Security
date: 2026-07-20
fetch_date: 2026-07-21T05:03:10.486013
---

# On Flock License Plate Tracking Cameras

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

## On Flock License Plate Tracking Cameras

A recent story of a writer who was [mistakenly](https://www.thedrive.com/news/how-flock-cameras-wrongly-tracked-me-for-days-over-stolen-plates-and-sent-police-after-me) identified, tracked, and arrested using data from Flock cameras has gone viral.

> The New Jersey plates that were allegedly stolen from the LA dealer were **34 03 DTM**, not **34 10 DTM**. But when the police report was created and the plate was entered into Flock’s system, it was just recorded as **34 DTM**. Just the five large characters, no little number in the middle. And Flock’s AI tech wasn’t registering that non-standard little number when it began picking up the Range Rover around town. It just saw **34 DTM** in large type and started alerting the local police.
>
> As we all stood there shaking our heads, including my wife, who was finally allowed to join me, I connected the final dot. A lot of vehicles in JLR’s media fleet have a New Jersey manufacturer plate with the same alphanumeric structure­34 ## DTM­and Officer Ganshyn observed that meant it was now a nationwide issue. Anywhere a police department has a partnership with Flock, any other JLR-owned car with the same plate structure is going to get flagged as stolen. In fact, four other **34 ## DTM** cars were being tracked around Minnesota that week, according to Officer Ganshyn. I was just the first one to get nabbed. The only way to stop it would be for the LAPD to correct their initial report and update Flock’s system, which Jaguar Land Rover was now racing to make happen following the phone call.

Flock has responded to the bad press. First, they [affirmed](https://www.thedrive.com/news/inside-the-flock-dragnet-how-systemic-errors-led-to-police-ambushing-me-for-no-reason) that their systems were working correctly, and blamed the police:

> The obvious question was that Flock cameras were looking for 34 DTM, and the plate on the car I was driving was 34 10 DTM. Why was that flagged as a match?
>
> “The way that the ML [machine learning] works is it correctly read what it was supposed to read. It was fed those characters that you said, 34 DTM, and it spit back out [a result] with the characters, 34 DTM,” Thomas said. “It was asked, can you find this? And it did find that. It just didn’t say if there’s more here, then don’t do it. It just simply said, is it there? And the answer was yes.”
>
> He explained that even if the 10 was normal size, Flock would still have flagged it as a match, because that’s how they’ve set it up according to law enforcement’s requests. Sometimes partial plates are all they have to go on at first.
>
> “The way that law enforcement likes to use these tools is, if any of the characters that they have put into these hot lists get read, they want to get those alerts,” he said. “Now, what we try to train officers to do is to do what you said, which is to verify that 34 DTM is what I’m looking for, and what I’m seeing is 34 10 DTM.”

Second, Flock’s CEO has [apologized](https://gizmodo.com/flocks-ceo-is-sorry-for-calling-privacy-activists-terrorists-2000787247) for calling privacy advocates terrorists:

> The CEO of Flock Safety, the company that runs an enormous network of cameras used by police departments across the U.S., hasn’t been shy about taking on Flock’s critics. Last year, he even called one group that tracks the location of Flock cameras “terrorists.” But he’s had a change of heart. Or, at the very least, a change in PR strategy.

Meanwhile, the police are [using](https://www.404media.co/how-cops-use-flock-to-track-people-not-cars/) (alternate [source](https://archive.ph/k4E8q)) the Flock camera network to track people in addition to cars:

> Police departments around the country have used Flock cameras at least hundreds of times to search for specific people, not cars, using searches such as “heavy-set male with a black and white hat,” “person on skateboard,” and “person wearing orange vest and construction hat,” according to data reviewed by 404 Media. Sometimes searches reference a target’s race or signs of their political affiliation.

And, like all police surveillance technologies, there are [abuses](https://www.cleveland.com/news/2026/07/ohio-audit-flags-unusual-police-database-searches.html).

Tags: [cameras](https://www.schneier.com/tag/cameras/), [cars](https://www.schneier.com/tag/cars/), [law enforcement](https://www.schneier.com/tag/law-enforcement/), [tracking](https://www.schneier.com/tag/tracking/)

[Posted on July 20, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html) •
[7 Comments](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html#comments)

### Comments

wiredog •
[July 20, 2026 8:10 AM](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html/#comment-456103)

About 30 years ago, pre-cellphone, I was driving on I-15 in southern Utah on a Sunday morning and saw a pickup weaving across both lanes. I got a partial plate, and the make of the pickup, hopped off at the New Harmony exit, and called 911. Got back on the road and long about Hurricane saw the truck on the shoulder with the driver failing the sobriety test. So the use case for partial plate plus vehicle make is pretty obvious. Flock is correct that *in this case* it’s an issue of how the police used the system.

In Ye Olden Days of the 1990s if a nationwide alert had gone out for a stolen Range Rover with that partial plate the same thing could have happened, it just would have been more difficult for the police as they would have needed to have it all written down. And, probably, the alert wouldn’t have gone out of California because of the overhead involved in sending it. Might not have left LA.

All of this is entirely separate from the privacy issues that Flock raises.

anon •
[July 20, 2026 10:53 AM](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html/#comment-456105)

If the police are searching for a short person with tan-coloured skin and black hair wearing blue denim pants, a white long sleeved shirt, and a red baseball cap, why should they have to leave out the ‘tan-coloured skin’ from the query? Wouldn’t that be the same, if they were looking for a vehicle, to leave out the body style?

KC •
[July 20, 2026 12:59 PM](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html/#comment-456106)

Re: tracking *people* in addition to cars

404’s article pulled together some actual – and *remarkably* vague – search terms.

> eg, Florence SC PD looking for “person with gun” across 61 cameras

In the comments, the CDT’s Tom Bowman links to some policy recommendations. Sill reading thru. Someone replied that these policy recommendations “do not address the problem of mass surveillance by corporations acti...