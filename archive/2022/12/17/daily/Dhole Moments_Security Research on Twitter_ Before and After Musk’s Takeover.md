---
title: Security Research on Twitter: Before and After Musk’s Takeover
url: https://soatok.blog/2022/12/16/security-research-on-twitter-before-and-after-musks-takeover/
source: Dhole Moments
date: 2022-12-17
fetch_date: 2025-10-04T01:47:00.892897
---

# Security Research on Twitter: Before and After Musk’s Takeover

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[(Anti-)Social Media](https://soatok.blog/category/social-media/)

# Security Research on Twitter: Before and After Musk’s Takeover

I got banned for criticizing Twitter’s security, as I’ve done often in the past without repercussion.

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [December 16, 2022](https://soatok.blog/2022/12/16/security-research-on-twitter-before-and-after-musks-takeover/)
* [3 Comments on Security Research on Twitter: Before and After Musk’s Takeover](https://soatok.blog/2022/12/16/security-research-on-twitter-before-and-after-musks-takeover/#comments)

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/BlogHeader-TwitterSecurity.png?fit=1200%2C675&ssl=1)

This is going to be a bit less polished than my usual writing, because I’m hammering it out before a busy day at work.

My Twitter account was suspended last night, around the same time that a wave of prominent journalists being suspended for criticizing Elon Musk.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/goodbye-elon.png?resize=670%2C454&ssl=1)

My account suspension was a bit less egregious than how journalists were treated, but it’s still remarkable because I have several comparable data points from before Musks’s takeover.

## Why Did @SoatokDhole Get Suspended?

It’s important to emphasize, for background, that Elon Musk claims to be a “Free Speech” absolutist.

> Comedy is now legal on Twitter
>
> — Elon Musk (@elonmusk) [October 28, 2022](https://twitter.com/elonmusk/status/1586104694421659648?ref_src=twsrc%5Etfw)

> It’s insane! I’m just fighting for free speech in America.
>
> — Elon Musk (@elonmusk) [November 26, 2022](https://twitter.com/elonmusk/status/1596323842246545409?ref_src=twsrc%5Etfw)

Yesterday, Musk banned the @ElonJet Twitter account, [after explicitly promising not to](https://www.theverge.com/2022/12/14/23508898/elonjet-twitter-ban-elon-musk-jet-tracker). So much for free speech.

> musk's pledge (lol) was to bring twitter's free speech policy in line with what is legal. the jet account was reposting public information, perfectly legal to do. he changed the rules to ban legal speech that was allowed before he took over
>
> — Shaun (@shaun\_vids) [December 16, 2022](https://twitter.com/shaun_vids/status/1603673062787932160?ref_src=twsrc%5Etfw)

But his team took it a step further: They also blocked Twitter users from linking to the @ElonJet account on Mastodon.

They also banned the @joinmastodon account, shortly before adding the filter. [**Twitter’s going great, really!**](https://twitterisgoinggreat.com/)

Elon’s remaining Twitter staff apparently didn’t include any security experts, because it’s completely trivial to bypass their rule that prohibits posting a link to ElonJet on Mastodon:

* Capitalize any letter in the URL
* Append a query string (i.e. `?t=1`)

![Facepaw](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-facepaw.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

Naturally, [I pointed this out](https://archive.ph/qkPtU). And when I woke up the next morning, my account had been suspended.

## Security Research Before the Age of Ruin

Being suspended by Twitter isn’t exactly a remarkable feat. It surely isn’t, by itself, worthy of blogging about.

What is more interesting, however, is I have a history of criticizing Twitter’s security.

1. My first real blog post here was about how, in April 2020, you could [bypass Twitter’s client-side validation to make your Gender field hold a megabyte of data](https://soatok.blog/2020/04/27/why-server-side-input-validation-matters/).

   This was publicly disclosed and widely exploited by trans people in protest of being misgendered by Twitter’s automation.

   No account suspension.
2. I was a [loud critic of the Birdwatch feature](https://soatok.blog/2021/01/27/twitters-birdwatch-is-fundamentally-flawed/) when it was first announced. I even tracked down the employees that worked on Birdwatch and sent them DMs to notify them of my critique.

   No account suspension.
3. I’ve been a loud critic of Twitter features that use dark patterns to be user-hostile, such as Twitter Spaces. In fact, my article on [how to remove Twitter Spaces](https://soatok.blog/2022/01/07/how-to-remove-twitter-spaces/) was a top search result for relevant queries ever since I wrote it.

   No account suspension.

But criticizing their failed attempts to block people from posting a link to ElonJet? Banned.

> "im not owned! im not owned!!", i continue to insist as i slowly shrink and transform into a corn cob
>
> — wint (@dril) [November 11, 2011](https://twitter.com/dril/status/134787490526658561?ref_src=twsrc%5Etfw)

Twitter’s Remaining Security Team

My interpretation of this shift in response to security researcher criticism is that Elon Musk is an absolute pissbaby and the remaining Twitter employees are sycophants and/or afraid of another Musk tantrum.

## Takeaways

As [predicted](https://soatok.blog/2022/11/07/contemplating-the-future/), Twitter has gone to shit. It’s only going to get worse from here.

You can find me on Mastodon at [@soatok@furry.engineer](https://furry.engineer/%40soatok).

I don’t intend to rejoin Twitter, even if my suspension is reversed.

## Epilogue

Shortly after I published this blog post, Twitter’s UI updated to inform me that my account suspension is permanent.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/permabanned.png?resize=665%2C413&ssl=1)

Rest in piss, Muskrat.

## Update (2022-12-18)

Apparently permanent doesn’t mean what I thought it does, in this age of newspeak.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/private-information.png?resize=696%2C702&ssl=1)

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/thinkens.png?resize=678%2C629&ssl=1)

My appeal, for the record, was a link to this blog post with the accompanying text, “Your boss needs to get over himself”.

Twitter responded is a predictably stupid manner:

![Hello,  We’re writing to let you know that your account features will remain limited for the allotted time for violating the Twitter Terms of Service, specifically the Twitter Rules against posting another person’s private and confidential information.  Violations of of this policy may include: publishing people’s private information without consent; threatening to hack Twitter or other platforms in order to obtain someone's private information; and/or posting intimate photos or videos taken or distributed without the subject's consent.  Please note that continued abusive behavior may lead to the suspension of your account. To avoid having your account suspended, please only post content that abides by the Twitter Rules.  You can learn more about our rules against posting another person’s private and confidential information.  Thanks,  Twitter](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/twitter-dumb.png?resize=637%2C858&ssl=1)

What’s funny about this is:

1. I didn’t post anyone’s private information, full stop.
2. I didn’t threaten to hack *anything*. I did imply that competent security professionals wouldn’t have implemented a filter as badly as Elon Musk’s Twitter did. But that’s not threatening to hack anything.
3. I haven’t posted any photos or videos. You can see the tweet they flagged has no media attached to it.

The only reasonable way to interpret what I did as posting “private information” is to assume ...