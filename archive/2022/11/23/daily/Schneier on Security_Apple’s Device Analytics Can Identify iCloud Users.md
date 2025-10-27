---
title: Apple’s Device Analytics Can Identify iCloud Users
url: https://www.schneier.com/blog/archives/2022/11/apples-device-analytics-can-identify-icloud-users.html
source: Schneier on Security
date: 2022-11-23
fetch_date: 2025-10-03T23:34:57.824561
---

# Apple’s Device Analytics Can Identify iCloud Users

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

## Apple’s Device Analytics Can Identify iCloud Users

Researchers [claim](https://www.macrumors.com/2022/11/21/apple-device-analytics-identifying-user/) that supposedly anonymous device analytics information can identify users:

> On [Twitter](https://twitter.com/mysk_co/status/1594515229915979776?s=61&t=rpR_X8V52MjKkTSK1fwzZg), security researchers Tommy Mysk and Talal Haj Bakry have found that Apple’s device analytics data includes an iCloud account and can be linked directly to a specific user, including their name, date of birth, email, and associated information stored on iCloud.

Apple has long claimed otherwise:

> On Apple’s device analytics and privacy [legal page](https://www.apple.com/legal/privacy/data/en/device-analytics/), the company says no information collected from a device for analytics purposes is traceable back to a specific user. “iPhone Analytics may include details about hardware and operating system specifications, performance statistics, and data about how you use your devices and applications. None of the collected information identifies you personally,” the company claims.

Apple was [just sued](https://www.theregister.com/2022/11/14/apple_data_collection_lawsuit/) for tracking iOS users without their consent, even when they explicitly opt out of tracking.

Tags: [Apple](https://www.schneier.com/tag/apple/), [cloud computing](https://www.schneier.com/tag/cloud-computing/), [courts](https://www.schneier.com/tag/courts/), [identification](https://www.schneier.com/tag/identification/), [iOS](https://www.schneier.com/tag/ios/), [privacy](https://www.schneier.com/tag/privacy/), [tracking](https://www.schneier.com/tag/tracking/)

[Posted on November 22, 2022 at 10:28 AM](https://www.schneier.com/blog/archives/2022/11/apples-device-analytics-can-identify-icloud-users.html) •
[3 Comments](https://www.schneier.com/blog/archives/2022/11/apples-device-analytics-can-identify-icloud-users.html#comments)

### Comments

Winter •
[November 22, 2022 11:13 AM](https://www.schneier.com/blog/archives/2022/11/apples-device-analytics-can-identify-icloud-users.html/#comment-412834)

Cardinal Richelieu has been quoted as saying he only needs six lines of the most honest man to condemn him to death.

That might not be as easy nowadays. And you do not need even three lines to get death threats.

But six data points on any person could very well be enough to identify any person, honest or not. 6 location + time stamps would be more than enough to identify anyone.

There are 8 billion people in the world, so 33 bit should suffice. Time stamps already give a lot of information about the person doing a task.

Winter •
[November 22, 2022 11:35 AM](https://www.schneier.com/blog/archives/2022/11/apples-device-analytics-can-identify-icloud-users.html/#comment-412835)

And here are the numbers on re-identifyability:

‘https://www.nature.com/articles/s41467-019-10933-3/

> Using our model, we find that 99.98% of Americans would be correctly re-identified in any dataset using 15 demographic attributes.

Example:

> ZIP code, date of birth, gender, and number of children would also identify 79.4% of the population in Massachusetts with high confidence

It is now common practice to never include a date of birth in any published data set. Age, or even age bracket (in decades) is now SOP. ZIP codes below city level are also banned. I have never seen number of children in any data set not specifically related to family structure.

But then, these practices were all designed after Latanya Sweeney’s ground breaking work.

Still, most people are re-identifed because they post everything on social media. It used to be pretty easy to track Russian Oligarchs by following Instagram posts of their children.

Clive Robinson •
[November 23, 2022 8:55 AM](https://www.schneier.com/blog/archives/2022/11/apples-device-analytics-can-identify-icloud-users.html/#comment-412860)

@ ALL,

The answer to the question of if tracking is possible is “it depends”…

We glibly talk of “Data Points”(DPs) and to a lesser extent “Signal to Noise Ratio”(SNR).

But the SNR to what?

1, Individual DPs.

Apple talks about “Individual” DPs from their “Chosen Group” of DPs.

This process is covered under,

“Lies, damn lies, and statistics.”

And the easy way to give an analog of the process is to talk about “jigsaws”.

Each piece has a SNR but also that SNR is relative to adjacent pieces in the completed puzzle. It consits of an easy SNR –from the shape– and a variable SNR (from the image).

What most people know is most jigsaws are a rectangle and usually cut on a grid. This tells us there are three basic groups,

1, Cornor pieces.
2, Edge pieces.
3, Inside pieces.

As a rule of thumb this tells us further information, when we apply a “locking mechanism” to the shapes. This is,

4, Each piece is aproximately a rectangle and thus has two axis
5, On each axis there will be two lock features unless “cut”.
6, A lock feature,can be a,”lug” or a hole.

The “cut” rules are based on having straight edges so,

7, A Corner piece has two cuts thus only two lock features.
8, An Edge piece has one cut thus three lock features.
9, An Inside piece usually has no cuts so has four lock features

Further we know that for a cut axis there are only two lock features combinations “lug” or “hole”. For uncut axis there are four “l,l”, “l,h”, “h,l”, “h,h”. We can apply further logic to come up with sixteen shapes for the Internal pieces and so on, into which they can be sorted. However there is ambiguity and what,

10, The actual shape a piece is, is only 100% known when the jigsaw is compleated.

But is the inversion of that statment true?

Actually it’s not. And for that a bit of further information is required. For most pictures they come in one of two orientations painters traditionally call “landscape” or “portrait” what artists and some mathamaticians know is that the shapes of these is defined by optomising the cut of materials[1].

If you assume that the pieces are cut on a square grid, then you can know from the number of pieces the size of the puzzel or vice veser. Thus you know that of your Edge pieces break down into four groups where the groups have only two sizes you can easily calculate…

Further by looking at the types of groups of Inner pieces you have, you can work out further information which is how the grid cut to locking mechanism is applied by the manufacturer. I won’t go into those details as the explanation whilst simple, is also long winded. All you need to know is that more often than not the cut pattern is “determanistic” not actually “random” though it might be a simple pseudo random sequence that is both linear and of short length (for material and cutting die strength).

The “take away” is that for any given piece there is a limited number of places it can be in, which in turn is fixed by the pieces around it forming a larger regul...