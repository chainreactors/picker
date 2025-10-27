---
title: The Scale of Geoblocking by Nation
url: https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html
source: Instapaper: Unread
date: 2024-11-23
fetch_date: 2025-10-06T19:28:58.265296
---

# The Scale of Geoblocking by Nation

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

## The Scale of Geoblocking by Nation

Interesting [analysis](https://www.lawfaremedia.org/article/how-geoblocking-limits-digital-access-in-sanctioned-states):

> We introduce and explore a little-known threat to digital equality and freedom­websites geoblocking users in response to political risks from sanctions. U.S. policy prioritizes internet freedom and access to information in repressive regimes. Clarifying distinctions between free and paid websites, allowing trunk cables to repressive states, enforcing transparency in geoblocking, and removing ambiguity about sanctions compliance are concrete steps the U.S. can take to ensure it does not undermine its own aims.

The paper: “[Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo](https://www.usenix.org/conference/usenixsecurity24/presentation/ablove)”:

> **Abstract**: We present one of the first in-depth and systematic end-user centered investigations into the effects of sanctions on geoblocking, specifically in the case of Cuba. We conduct network measurements on the Tranco Top 10K domains and complement our findings with a small-scale user study with a questionnaire. We identify 546 domains subject to geoblocking across all layers of the network stack, ranging from DNS failures to HTTP(S) response pages with a variety of status codes. Through this work, we discover a lack of user-facing transparency; we find 88% of geoblocked domains do not serve informative notice of why they are blocked. Further, we highlight a lack of measurement-level transparency, even among HTTP(S) blockpage responses. Notably, we identify 32 instances of blockpage responses served with 200 OK status codes, despite not returning the requested content. Finally, we note the inefficacy of current improvement strategies and make recommendations to both service providers and policymakers to reduce Internet fragmentation.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [Cuba](https://www.schneier.com/tag/cuba/), [national security policy](https://www.schneier.com/tag/national-security-policy/), [privacy](https://www.schneier.com/tag/privacy/), [surveillance](https://www.schneier.com/tag/surveillance/)

[Posted on November 22, 2024 at 7:06 AM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html) •
[14 Comments](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html#comments)

### Comments

jnorthon •
[November 22, 2024 12:36 PM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441803)

> U.S. policy prioritizes internet freedom and access to information in repressive regimes.

It’s not hard to see that this is kind of bs, though. Load up Tor Browser and try to view the I.R.S. or F.C.C. web sites, for example: “Access Denied

Luckily, I’m not a U.S. citizen (who’d be required to file U.S. taxes) living in a “repressive regime”. But I’d be curious to see someone file Freedom of Information Act requests for details on why they feel it appropriate to block anonymous viewing of their sites. Heaven forfend someone download a 1040-NR without being tracked by the U.S.A.

Rontea •
[November 22, 2024 1:41 PM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441805)

Sanctions can significantly affect Internet users, predominantly by restricting access to certain digital services and platforms. These measures can limit individuals’ ability to communicate and share information freely, impacting social and professional networks. Internet services such as payment processors and cloud hosting can be affected, disrupting online businesses and freelance work reliant on these services. Moreover, sanctions can create internet fragmentation, with regional services replacing globally popular ones, potentially limiting the availability and quality of information due to language barriers or the lack of certain features. Additionally, the imposition of sanctions can lead to increased censorship and surveillance as governments may attempt to control and monitor online activity as part of their national security plans.

ResearcherZero •
[November 22, 2024 10:56 PM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441807)

It often doesn’t work as they may be next door.

‘https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/

GooseEgg
<https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials/>

ResearcherZero •
[November 23, 2024 6:30 AM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441813)

@jnorthon

It is designed to work that way. Try connecting from a location within the US using a different browser and a VPN.

There are different types of blocking for different purposes. Sometimes censorship, but often for a range of other reasons.

By limiting users on Tor, Geo-blocking reduces attacks that could disrupt services during high usage periods, and other malicious activity. There are also benefits for network management too.

However, if you are not a US citizen, then you do not need to use the service. Most users will be located within the US.

–

What is accountability?

If we don’t understand it, then we cannot have it, or it’s sub-virtue – **justice**.

‘https://euauditors.medium.com/basically-without-accountability-no-democratic-control-203f471137b9

“If you do not speak up for your decision, you should hold your peace and let others run your life.”
[https://medium.com/@danielcfng/abdication-of-responsibility-and-authority-causes-and-consequences-92b0474e5756](https://medium.com/%40danielcfng/abdication-of-responsibility-and-authority-causes-and-consequences-92b0474e5756)

Bob •
[November 23, 2024 1:23 PM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441817)

Any worthwhile infosec/cybersecurity community popping up on Bluesky yet? I miss being able to pull IOCs from Twitter.

Paul Sagi •
[November 26, 2024 9:07 AM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441848)

AFAIK geoblocking is often due to agreements of where certain ads will be shown, also copyright agreements?
I think geoblocking would be easily defeated by a VPN, so I don’t understand why geoblocking exists.

ResearcherZero •
[November 27, 2024 1:00 AM](https://www.schneier.com/blog/archives/2024/11/the-scale-of-geoblocking-by-nation.html/#comment-441871)

The public was given one day to comment.

‘https://www.crikey.com.au/2024/11/25/teen-social-media-ban-inquiry-submissions/

Digital ID cards for proof of age verification....