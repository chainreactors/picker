---
title: No-Fly List Exposed
url: https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html
source: Schneier on Security
date: 2023-01-24
fetch_date: 2025-10-04T04:40:29.690476
---

# No-Fly List Exposed

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

## No-Fly List Exposed

I can’t remember the last time I thought about the US no-fly list: the list of people so dangerous they should never be allowed to fly on an airplane, yet so innocent that we can’t arrest them. Back when I thought about it a lot, I realized that the TSA’s practice of giving it to every airline meant that it was not well protected, and it certainly ended up in the hands of every major government that wanted it.

The list is back in the news today, having been [left exposed](https://www.dailydot.com/debug/no-fly-list-us-tsa-unprotected-server-commuteair/) on an insecure airline computer. (The airline is CommuteAir, a company so obscure that I’ve never heard of it before.)

This is, of course, the problem with having to give a copy of your secret list to lots of people.

EDITED TO ADD (2/14): The 23 yo researcher who found NOFLY.csv [wrote](https://maia.crimew.gay/posts/how-to-hack-an-airline/) a blog post about it. This is [not the first time](https://www.linkedin.com/pulse/americas-secret-terrorist-watchlist-exposed-web-report-diachenko) the list has become public.

Tags: [air travel](https://www.schneier.com/tag/air-travel/), [hacking](https://www.schneier.com/tag/hacking/), [no-fly list](https://www.schneier.com/tag/no-fly-list/), [TSA](https://www.schneier.com/tag/tsa/)

[Posted on January 23, 2023 at 7:02 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html) •
[29 Comments](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html#comments)

### Comments

[Chris](https://chriswells.io) •
[January 23, 2023 8:07 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416367)

Good thing taxpayer IDs weren’t in the file or the TSA would be on the hook for a free year of credit monitoring.

What’s the appropriate level of responsibility for leaking personal data of suspected criminals never charged with a crime?

Thomas M •
[January 23, 2023 8:18 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416369)

Well the question is, is this list even valid? I read it contains 1.5 million entries!

Andy •
[January 23, 2023 8:28 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416370)

I wonder how related it is to OFAC’s list <https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists> . That one is public and has birthdays as well.

Snarki, child of Loki •
[January 23, 2023 8:59 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416371)

The “no-fly list” was a stupid idea, implemented by deeply stupid people.

Unfortunately, such ideas seem to have a very long lifespan.

Ted •
[January 23, 2023 9:15 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416373)

@Andy

> I wonder how related it is to OFAC’s list

Good question. Apparently Viktor Bout, who was the only person listed by name in the article, is also on the OFAC list.

Victor Bout is, of course, the Russian arms dealer who was swapped in a prisoner exchange for Brittney Griner on Dec 8, 2022.

David in Toronto •
[January 23, 2023 9:59 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416376)

Frankly, I’m surprised it took this long to leak publicly.

Brian •
[January 23, 2023 10:07 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416377)

I wouldn’t mind the no-fly list so much if it were like an expanded version of the FBI’s Most Wanted list: people who should be arrested if we notice them trying to board an airplane.

Winter •
[January 23, 2023 10:20 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416378)

The No-Fly list contains so many names that have nothing at all to do with terrorism that I doubt it actually prevents any terrorists from boarding.

‘https://edition.cnn.com/2015/12/07/politics/no-fly-mistakes-cat-stevens-ted-kennedy-john-lewis/index.html

> Sen. Ted Kennedy told the Senate Judiciary Committee in 2004 that he had been stopped and interrogated on at least five occasions as he attempted to board flights at several different airports. A Bush administration official explained to the Washington Post that Kennedy had been held up because the name “T. Kennedy” had become a popular pseudonym among terror suspects.

The oldies under us will remember Cat Stevens, the singer who converted to Islam. He flew to the US and the No-Fly list kicked in for all passengers:

> In 2004, a Washington-bound United Airlines flight from London was diverted to Maine after officials discovered Yusuf Islam, the singer formerly known as Cat Stevens, was on board. Islam was denied entry into the U.S. and made to return to the U.K.
>
> “Celebrity or unknown, our job is to act on information that others have given us,” Homeland Security Secretary Tom Ridge said at the time. “And in this instance, there was some relationship between the name and the terrorists’ activity with this individual’s name being on that no-fly list, and appropriate action was taken.”
>
> But there was no further formal explanation and Islam was allowed in 2006 to enter the U.S. without incident.

jeadly •
[January 23, 2023 10:23 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416379)

Have I missed some legitimate reason that this list needs to be kept secret? Yes, the public outrage of such a stupid idea would surely have shuttered it long ago had it been exposed early on; though I’m not sure that should be considered legitimate.

Micah •
[January 23, 2023 10:30 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416381)

> This is, of course, the problem with having to give a copy of your secret list to lots of people.

I don’t see why they’d “have to”. That’s just another badly designed aspect of a bad idea. They could force the airlines to give them passenger lists for approval instead. Or, just have the TSA agents check the names when people are going through security. (Sure, it would feel like arbitrary harassment to be turned away at that point, but isn’t that the point of the list in practice?)

David in Toronto •
[January 23, 2023 11:08 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416389)

Famously lampooned in a Boston Legal Episode “Nuts” <https://www.youtube.com/watch?v=A1g10DBQfWE>

Winter •
[January 23, 2023 11:16 AM](https://www.schneier.com/blog/archives/2023/01/no-fly-list-exposed.html/#comment-416390)

@Micah

> They could force the airlines to give them passenger lists for approval instead.

That would mean checking the list would weight on the budget of the TSA or whomever. Now the cost of checking the names is paid for by the airlines....