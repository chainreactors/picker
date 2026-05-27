---
title: Identifying People Using Wi-Fi Routers
url: https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html
source: Schneier on Security
date: 2026-05-26
fetch_date: 2026-05-27T06:12:44.564195
---

# Identifying People Using Wi-Fi Routers

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

## Identifying People Using Wi-Fi Routers

Not identifying people based on their use of Wi-Fi routers, but identifying people [using Wi-Fi signals](https://gizmodo.com/researchers-issue-warning-about-tech-that-could-turn-every-router-into-a-potential-means-for-surveillance-2000763181).

> This is accomplished through what is known as [WiFi sensing](https://wballiance.com/wi-fi-sensing-101-an-introduction/), or the use of WiFi signals to infer information about a physical environment. When radio signals like WiFi travel through a space, they interact with the objects and people around them. Those signals can be reflected, scattered, or absorbed. By analyzing how the signal is expected to behave compared with how it is actually received, researchers can infer details about the surrounding environment.
>
> “By observing the propagation of radio waves, we can create an image of the surroundings and of persons who are present,” said Thorsten Strufe, a KIT professor and study co-author, in a [press release](https://www.kit.edu/kit/english/pi_2025_069_the-spy-who-came-in-from-the-wifi-beware-of-radio-network-surveillance.php). “This works similar to a normal camera, the difference being that in our case, radio waves instead of light waves are used for the recognition.”

Tags: [identification](https://www.schneier.com/tag/identification/), [privacy](https://www.schneier.com/tag/privacy/), [surveillance](https://www.schneier.com/tag/surveillance/), [Wi-Fi](https://www.schneier.com/tag/wi-fi/)

[Posted on May 26, 2026 at 11:02 AM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html) •
[10 Comments](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html#comments)

### Comments

Clive Robinson •
[May 26, 2026 12:31 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454659)

@ ALL,

Sensing people and how they move with any EM signal above a couple of GHz is not exactly new.

Back in the 1980’s when involved with Pirate Radio, we realised that the UK Authorities (still Home Office back then) when trying to “direction find” the studio link gave away the fact they were in the area due to the way the DF antenna was rotated thus some stations would just “switch studio”.

The problem with getting an “image” has always been “resolution”.

In theory you can work to about 1/16th of a wavelength so 2.5GHz WiFi has a wavelength of 300/2500 meters or 12cm so the resolution is at best a little less than 1cm quite close in (ie a couple of meters).

To give you an idea of how bad that is the average human eye can see 1mm at 2000mm… Some people like Australian Aboriginals are known to have a lot better vision.

Yes there are tricks you can do that effectively use multiple paths but things start getting a little interesting.

[Fazal Majid](https://majid,ingo) •
[May 26, 2026 12:51 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454660)

This is not completely new, there is an IEEE standard 802.11bf for WiFi sensing, which has features like detecting if a senior person has fallen (to call emergency services).

<https://en.wikipedia.org/wiki/WiFi_Sensing>

The new thing here is that not only can it sense people, but also identify them.

Clive Robinson •
[May 26, 2026 1:05 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454661)

@ ALL,

To understand what modern WiFi can give in terms of “tricks” imagine a dark room with many flashing EM sources and lots of receivers that act as sensors.

The sensors do not give range or bearing information, but do report “Received Signal Strength” by broadcasting it in plain text back to the WiFi base unit. Which as it’s a broadcast means any passive unot in range will get the equivalent of many multiple beams information.

This information can be deconvolved and the effect is to receive many imprecise range indicators.

Get enough even poor range information and you can effectively average it up. Thus you get a more precise image.

Read the paper for the nitty gritty of this.

But remember the paper is not so much a technical rabbit hole dive, as opposed to a Big Red Flag waving excercise.

The information being used is publicly available because,

“It’s not encrypted”

And the authors quite rightly feel it should be.

Zaphod •
[May 26, 2026 1:43 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454662)

Too late but was about to mention that (as often) Clive has excellent insight into this topic and I was looking forward to his comments. Others too of course.

Z

Weather •
[May 26, 2026 2:12 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454663)

@All

A electric field, which a Rf source is most dominant in ,in close proximity to a antenna, has a time variable but is deffinrial based on distance.

If you have a signal, a voltage will max be produced at X distance, changing the frequency, changes the distance.

Theres E and M and EM(rf) ,take a 1m2 metal plate as a antenna and scan the frequency range looking for peaks, the peaks will be distance based on 1^4 .

lurker •
[May 26, 2026 3:07 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454665)

This should have been expected by anyone who watches StarTrek. But note that even ST devices could only distinguish human or non-human lifeforms, and required the target to carry some tracking device for more precise identification.

Moving animals (or vegetables) will cause disturbances in a complex RF field. As @Clive said

This BFI method avoids having to do some of the math involved in previous CSI analyses. Encrypting the information will only force them to hone their algorithms and buy a bigger computer. You cannot hide.

Expose the CANCER, The FILTH In Our Society •
[May 26, 2026 4:37 PM](https://www.schneier.com/blog/archives/2026/05/identifying-people-using-wi-fi-routers.html/#comment-454667)

s h or t u r l . a t / x9q9k

BOISE, IDAHO:
The following Boise Police Department Officers (current or former)

Matt Hudson,
Edward Pieczonka,
Trent Schneider,
Chad Wigington,
Damir Subasic,

as well as their two former, (both TERMINATED) Chiefs:

Bill Bones and
Ryan Lee,

AS WELL AS THE @D@ COUNTY PR0SECUT0RS:
Jan Bennetts and
Brittany Ford,

as well as the Public Defenders:
Jonathan D. Loschi and
Kendra Nagy,

as well as the PRIVATE LAWYERS THAT THE INNOCENT AMERICAN CITIZEN HAD RETAINED:
these private lawyers COLLECTED THE MONEY FROM AN INNOCENT MAN TO DEFEND HIM
BUT THEY DID NOT EVEN FILE AN APPEAL EVEN THOUGH THE MAN WHO PAID THEM SPECIFICALLY
ASKED THEM TO CLEAR HIS NAME OF ALL FAKE CHARGES WHICH HAVE DESTROYED HIM AND
HIS FAMILY.

Raymond D. ...