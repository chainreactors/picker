---
title: Security Vulnerabilities in ICEBlock
url: https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html
source: Schneier on Security
date: 2025-07-18
fetch_date: 2025-10-06T23:55:26.453204
---

# Security Vulnerabilities in ICEBlock

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

## Security Vulnerabilities in ICEBlock

The ICEBlock tool has [vulnerabilities](https://www.theverge.com/cyber-security/707116/iceblock-data-privacy-security-android-version):

> The developer of ICEBlock, an iOS app for anonymously reporting sightings of US Immigration and Customs Enforcement (ICE) officials, promises that it “ensures user privacy by storing no personal data.” But that claim has come under scrutiny. ICEBlock creator Joshua Aaron has been accused of making false promises regarding user anonymity and privacy, being “misguided” about the privacy offered by iOS, and of being an Apple fanboy. The issue isn’t what ICEBlock stores. It’s about what it could accidentally reveal through its tight integration with iOS.

Tags: [anonymity](https://www.schneier.com/tag/anonymity/), [iOS](https://www.schneier.com/tag/ios/), [privacy](https://www.schneier.com/tag/privacy/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on July 17, 2025 at 7:06 AM](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html) •
[8 Comments](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html#comments)

### Comments

Clive Robinson •
[July 17, 2025 10:02 AM](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html/#comment-446571)

@ ALL,

The developer Joshua Aaron apparently made claims about the application not storing user details etc. Which it appears are as far as the claims go “true”.

However as I often note especially with secure messaging apps which ICEBlock kind of is. That it’s rather more you need to consider. That is,

“You need to consider the whole system.”

Not just the fun bits like the application. Because it’s been known publicly for a couple of decades at least that an application can not function without,

1, An OS

Any one of which can be “shimmed” to do a “Man In The Middle” attack on the implicit communications paths.

As I’ve pointed out in the past “why attack the apps encryption when you can just watch the I/O at the OS or device driver levels?”

In effect you do a “run around attack”.

I’ve also previously pointed out that,

“Due to the redundancy needed to communicate information, the same redundancy can be used to create a communications channel within the existing communications channel.”

Therefore you can not stop information being leaked either accidently, covertly or even overtly in what is called a “communications side channel”.

Thus to be secure you need very fine control on any communications path be it implicit or explicit.

If there is failures in this area then private or confidential information will be leaked out into other parts of the system. And in turn from there to those observing in the right way.

This is true of all Applications and people who want privacy should seek out ways to mitigate the issues. Methods that I’ve discussed here and other places in the past.

Yes I know my view makes me unpopular with some, but at the end of the day, being honest with people is more important than pleasing people who don’t know what they are talking about, or trying to sell “snake oil”.

lurker •
[July 17, 2025 2:35 PM](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html/#comment-446575)

The Verge headline says it all:

> ICEBlock isn’t ‘completely anonymous’
> But no app is.

The fanbois squabbling on bsk miss the point, Apple or Google, you’re trackable, traceable, and targetable.

Clive Robinson •
[July 17, 2025 4:06 PM](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html/#comment-446577)

@ lurker, ALL,

With regards,

> “The fanbois squabbling on bsk miss the point, Apple or Google, you’re trackable, traceable, and targetable.”

It’s a bit more in-depth than that because it applies to all communications that is not unidirectional like a general broadcast.

The minute communications has a bidirectional element in it or a need to know location then you are pined down like a moth to a cork in a lepidopterist’s display case.

So the obvious question is,

“Why do we have so many non-broadcast communications?”

The answer is in two parts,

1, Control
2, Efficiency

With the first it’s possible to gain a great deal of the second. As well as establishing a tracked master slave relationship where location knowledge is by default.

In practice nearly all multi user shared communications channel systems use a mixture of broadcast and non-broadcast communications.

The remote unit or out-station initiates communications by “broadcasting” the equivalent of “Can Anyone hear me?” On a designated control channel. Known to some as “a CQ Call”[1], the remote continues to call CQ untill it receives a response or a time out happens.

If the remote unit receives an acknowledge from the home/base-station then it sends it’s own ACK back and switches into commanded mode where the base-station becomes the “Master” that commands and controls and the remote becomes the “slave” that is commanded and controlled.

Usually the first thing that happens is a “switch channels” or QSY command to free up the control channel.

At some point identification, location and authorisation information is exchanged either implicitly or explicitly for “billing or logging” purposes.

This can be viewed as the “pinning to a cork” stage at which point the home or base-station knows who you are (or at least the unique ID of the equipment in use).

If you look up the communications stack of all digital based communications you will find this non-broadcast process.

It even happens within software only systems like Operating Systems where processes have not just ID’s but locations in memory. And the semi-equivalent of broadcast setup is done by “signals” and for various reasons get many programmers making “cabalistic signs in the air” to “cast out demons” or equivalent.

[1] In the very early days of radio when transmitters were still of the “spark gap” variety, the need for control protocols became one of the first things recognised. As nearly all modulation was by “Morse Code” the commands in such protocols were letter based. Over time they became known as “International Q-Codes” and they are still in existence and still used as are the protocols they were used for,

<https://www.qsl.net/w5www/qcode.html>

Daniel Popescu •
[July 17, 2025 10:35 PM](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html/#comment-446579)

@Clive – exquisite input, as usual. And I love the lepidopterist touch, haven’t used or heard that word in a looong time :).

Clive Robinson •
[July 18, 2025 2:03 AM](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html/#comment-446586)

@ Daniel Popescu

With regards,

> “And I love the lepidopterist touch”

You can thank Dolly Par...