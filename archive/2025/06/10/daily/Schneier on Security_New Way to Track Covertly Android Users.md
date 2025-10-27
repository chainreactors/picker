---
title: New Way to Track Covertly Android Users
url: https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html
source: Schneier on Security
date: 2025-06-10
fetch_date: 2025-10-06T22:57:27.245730
---

# New Way to Track Covertly Android Users

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

## New Way to Covertly Track Android Users

Researchers have [discovered](https://localmess.github.io/) a new way to covertly track Android users. Both Meta and Yandex were using it, but have suddenly stopped now that they have been caught.

The [details](https://arstechnica.com/security/2025/06/meta-and-yandex-are-de-anonymizing-android-users-web-browsing-identifiers/) are interesting, and worth reading in detail:

> Tracking code that Meta and Russia-based Yandex embed into millions of websites is de-anonymizing visitors by abusing legitimate Internet protocols, causing Chrome and other browsers to surreptitiously send unique identifiers to native apps installed on a device, [researchers have discovered](https://localmess.github.io/). Google says it’s investigating the abuse, which allows Meta and Yandex to convert ephemeral web identifiers into persistent mobile app user identities.
>
> The covert tracking—­implemented in the [Meta Pixel](https://www.facebook.com/business/tools/meta-pixel/) and [Yandex Metrica](https://ads.yandex/metrica) trackers­—allows Meta and Yandex to bypass core security and privacy protections provided by both the Android operating system and browsers that run on it. [Android sandboxing](https://source.Android.com/docs/security/app-sandbox), for instance, isolates processes to prevent them from interacting with the OS and any other app installed on the device, cutting off access to sensitive data or privileged system resources. Defenses such as [state](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/State_Partitioning) [partitioning](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/State_Partitioning) and [storage partitioning](https://privacysandbox.google.com/cookies/storage-partitioning), which are built into all major browsers, store site cookies and other data associated with a website in containers that are unique to every top-level website domain to ensure they’re off-limits for every other site.

*Washington Post* [article](https://www.washingtonpost.com/technology/2025/06/06/meta-privacy-facebook-instagram/).

Tags: [Android](https://www.schneier.com/tag/android/), [Meta](https://www.schneier.com/tag/meta/), [smartphones](https://www.schneier.com/tag/smartphones/), [tracking](https://www.schneier.com/tag/tracking/)

[Posted on June 9, 2025 at 6:54 AM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html) •
[20 Comments](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html#comments)

### Comments

george •
[June 9, 2025 8:12 AM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html/#comment-445836)

I think I’ve reached a state of permanent cyncicism regarding big tech.

Nothing they’ve done has ever had any real consequences for them. Users should be disgusted; instead we’re shrugging it off because surveillance capitalism has long been normalized and completely accepted. After all, the only viable alternative is throwing our devices into the trash, which we can’t do because we’re all hopelessly addicted.

Meta should be sued into oblivion for this, in fact they should never be able to recover. And yet, it’s just another Tuesday.

I’m deeply convinced that things will get even worse because of AI. The insane investments must be recouped, and they will be recouped.

/rant

InveigledParsimony •
[June 9, 2025 12:30 PM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html/#comment-445841)

Welcome to the Cynic’s Club, George. You aren’t wrong. Per the WarGames prophecy:

“The only winning move is not to play.”

InveigledParsimony •
[June 9, 2025 12:32 PM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html/#comment-445842)

Welcome to the Cynic’s Club, George. You aren’t wrong. Per the WarGames prophecy:

“The only winning move is not to play.”

Clive Robinson •
[June 9, 2025 12:37 PM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html/#comment-445843)

@ ALL,

The problem…

When putting information in secure containers it is effectively useless as it can not be reached.

When you add a communications channel to the container so the information can be reached / used, by information theory you,

1, Add Redundance.

And further where you have “redundancy” by information theory you,

2, Add a communications channel.

Whilst it might be of a much lower bandwidth, and difficult to see information is still leaked…

And you have in effect,

3, Added a covert side channel.

The first question that comes up is,

“Why don’t we encrypt it?”

Well that might,

A, Hide the “data” in the side channel.

But encryption usually,

B, Won’t hide any “meta-data”

And further usually,

C, Won’t hide any “meta-meta-data”

At the end of the day there is always one piece of information that get’s leaked,

“The channel exists by it being used”

How you lock down or dilute meta-data and meta-meta-data all different but in one respect they are all the same,

“The strongly reduce the efficiency of the system.”

Which is why the known methods of dealing with the leakage of meta-daya and meta-meta-data are almost never used in consumer or commercial products, systems, or software.

As the old saying has it,

“You make your bed and you sleep in it.”

So if you throw down your bed roll on ground you have not taken the time or effort to clear, expect not to wake feeling the way you would like.

Whilst it is possible to design secure systems, the basic rule of thumb that says,

“Efficiency v. Security”

Applies and almost all ways security looses at some point in the system.

In short,

“Modern smart devices can not be secure due to the way they are designed.”

Which is what Google has at best underestimated and Meta and Yandax have exploited.

But ask yourself a question,

“As Google are one of the worst offenders on collecting Personal and Private Information from users and abusing it, was this really accidental?”

not important •
[June 9, 2025 5:39 PM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html/#comment-445844)

@Clive asked ‘“As Google are one of the worst offenders on collecting Personal and Private Information from users and abusing it, was this really accidental?”

Nope. They working very closely with deep state and provide any cooperation authorized or not by law. Lawyers could always provide ‘legend’ to cover or exonerate ITs to get them free ride on that.

NO NETWORKING •
[June 9, 2025 7:26 PM](https://www.schneier.com/blog/archives/2025/06/new-way-to-track-covertly-android-users.html/#comment-445848)

Buy *OLD* hardware and software now, I’m talking about the hardware which used 5″ floppies and had *ZERO* networking loaded when you popped in a disk to use a word processor, for ex...