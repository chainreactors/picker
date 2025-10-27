---
title: Sustaining Snowflake operations
url: https://blog.torproject.org/snowflake-daily-operations/
source: Tor Project blog
date: 2023-02-08
fetch_date: 2025-10-04T06:03:56.484005
---

# Sustaining Snowflake operations

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Sustaining Snowflake operations

by [dcf](/author/dcf)
| February 7, 2023

![](/snowflake-daily-operations/lead.png)

The team that runs the primary Snowflake bridge is raising funds to pay for server operating expenses such as bandwidth, hardware, and maintenance..
You can help the project by donating to the project on Open Collective:

[Snowflake Daily Operations â Open Collective](https://opencollective.com/censorship-circumvention/projects/snowflake-daily-operations)

What follows is [an update originally posted on the Open Collective project](https://opencollective.com/censorship-circumvention/projects/snowflake-daily-operations/updates/2022-year-in-review).

The year 2022 was transformative for the [Snowflake](https://snowflake.torproject.org/) censorship circumvention system. The year saw a massive increase in the number of Snowflake users, fueled by some significant censorship events where Snowflake was one of few systems that worked to keep people connected. At the end of 2022, something around 2% of all Tor users used Snowflake to access the Tor network and the uncensored Internet. The Snowflake team has had to invest in powerful server hardware and a fast network connection in order to keep up with demand. Servers and bandwidth don't come for free, which is why we have started [an Open Collective project](https://opencollective.com/censorship-circumvention/projects/snowflake-daily-operations). We aim to collect funds to sustain current operational needs and support future upgrades.

The first major event affecting Snowflake usage actually happened at the end of 2021. Snowflake is deployed as a circumvention system (a pluggable transport) alongside the [Tor](https://www.torproject.org/) anonymity system. People use Snowflake and other pluggable transports when direct access to the Tor network is blocked. On December 1, 2021, some Internet service providers in Russia suddenly [blocked access](https://blog.torproject.org/tor-censorship-in-russia/) to most ways of accessing Tor, including, briefly, Snowflake. With the help of people in Russia, Snowflake developers [found](https://bugs.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/40014#note_2765074) and [fixed](https://github.com/pion/dtls/pull/410) the protocol flaw that was being used to discover and block Snowflake connections, and Snowflake began working again in Russia. But because other ways of accessing Tor remained blocked, [more and more people in Russia](https://bugs.torproject.org/tpo/community/support/40050#note_2826459) began using Snowflake.

All the new users started to overwhelm the resources of the server that was then hosting the Snowflake bridge. There were times when the system was barely usable because off all the people trying to use it at once. We had to [innovate a new way to deploy a Tor bridge](https://forum.torproject.net/t/tor-relays-how-to-reduce-tor-cpu-load-on-a-single-bridge/1483) to remove a performance bottleneck; then, when that had taken us as far as it could, we [started looking for a more powerful server](https://forum.torproject.net/t/tor-project-more-resources-required-for-snowflake-bridge/2353). We [moved to better hardware](https://bugs.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/40110#note_2791036) in March, which enabled the Snowflake bridge to meet demand. The situation remained stable for about the next six months.

On September 21, 2022, Internet service providers in Iran began imposing [even more severe censorship](https://ooni.org/post/2022-iran-blocks-social-media-mahsa-amini-protests) than usual, in response to mass protests. Evidently, many people in Iran turned to Snowflake to circumvent the blocks, as the number of users quadrupled in a matter of days. This began a few days of [intense performance and optimization work](https://lists.torproject.org/pipermail/anti-censorship-team/2022-October/000270.html) because the greatly increased load was straining even the upgraded server hardware.

The performance work was ultimately successful, and the bridge started handling its new load of users smoothly. Then, about two weeks after the protests began, Snowflake traffic from Iran [dropped off precipitously](https://github.com/net4people/bbs/issues/131). The cause turned out to be an oversight in the implementation of Snowflake, a [TLS fingerprint](https://bugs.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/40207#note_2849437) that has been blocked. When a fix for that problem was deployed, the number of users began to grow again, faster than ever.

Over the course of 2022, Snowflake scaled from 5,000 to 75,000 users. It has been made possible by a dedicated team and investment in hardware infrastructure. As you can see from the user graph, demand for Snowflake continues to grow. It seems likely that there is [additional blocking in Russia](https://bugs.torproject.org/tpo/anti-censorship/censorship-analysis/40030#note_2823140) that has not yet been addressed; and when it is, it is likely to increase usership further.

* [circumvention](/category/circumvention)
* [fundraising](/category/fundraising)
* [metrics](/category/metrics)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/snowflake-daily-operations/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/snowflake-daily-operations/&text=Snowflake%20bridge%20operators%20are%20raising%20funds%20to%20keep%20infrastructure%20running)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/snowflake-daily-operations/&text=Snowflake%20bridge%20operators%20are%20raising%20funds%20to%20keep%20infrastructure%20running)
[Bluesky](https://bsky.app/intent/compose?text=Snowflake%20bridge%20operators%20are%20raising%20funds%20to%20keep%20infrastructure%20running%0Ahttps%3A//blog.torproject.org/snowflake-daily-operations/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/author/boklm)
| September 22, 2025

Tor Browser 15.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.0](/new-release-tails-7_0/)

by [tails](/author/tails)
| September 18, 2025

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

## [New Release: Tor Browser 14.5.7](/new-release-tor-browser-1457/)

by [ma1](/author/ma1)
| September 16, 2025

Tor Browser 14.5.7 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####...