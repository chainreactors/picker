---
title: Weekly Update 390
url: https://www.troyhunt.com/weekly-update-390/
source: Troy Hunt's Blog
date: 2024-03-11
fetch_date: 2025-10-04T12:08:34.389954
---

# Weekly Update 390

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Weekly Update 390

10 March 2024

Let me begin by quoting Stefan during the livestream: "​​Turns out having tons of data integrity is expensive". Yeah, and working with tons of data in a fashion that's both fast *and* cost effective is bloody painful. I'm reminded of the old "fast, good and cheap - pick 2" saying, but there's a lot more nuance to it than that, of course. I mean Table Storage was all 3 of those, just so long as we never needed to restore *at all*, let alone to a point in time. Or geo-replicate. Or do ad hoc queries and do on and so forth. Mind you, I think that with a combination of Azure SQL in Hyperscale mode, some better index optimisation, and a willingness to scale up more aggressively when processing large breaches, we might be able to find a happy balance. Literally as I'm writing this, we're upgrading to Hyperscale so hopefully when I do next week's video from Tokyo, there'll be a happy story to tell (or I'll be drowning my sorrows in sake).

[![Listen on Apple Podcasts](https://www.troyhunt.com/content/images/2018/05/Listen-on-Apple-Podcasts.svg)](https://itunes.apple.com/au/podcast/troy-hunts-weekly-update-podcast/id1176454699?ref=troy-hunt)

[![Get it on Google Play](https://www.troyhunt.com/content/images/2018/05/Get-it-on-Google-Play.svg)](https://playmusic.app.goo.gl/?ibi=com.google.PlayMusic&%3B%3Bisi=691797987&%3B%3Bius=googleplaymusic&%3B%3Bapn=com.google.android.music&%3B%3Blink=https%3A%2F%2Fplay.google.com%2Fmusic%2Fm%2FIf3tw7npymckucxq4q76762ncny%3Ft%3DTroy_Hunt%27s_Weekly_Update_Podcast%26pcampaignid%3DMKT-na-all-co-pr-mu-pod-16&%3B%3Bref=troy-hunt&%3Bref=troy-hunt&ref=troyhunt.com)

[![](https://www.troyhunt.com/content/images/2019/10/spotify.svg)](https://open.spotify.com/show/7jMtKFohdrw6qmz8AkLqit?ref=troy-hunt)

[![Download via RSS](https://www.troyhunt.com/content/images/2018/07/Download-via-RSS.svg)](https://omny.fm/shows/troy-hunt-weekly-update/playlists/podcast.rss?ref=troy-hunt)

### References

1. [Sponsored by: Kolide ensures that if a device isn't secure, it can't access your apps. It's Device Trust for Okta. Watch the demo today!](https://kolide.com/troyhunt?ref=troyhunt.com)
2. [The German government has become the 35th national gov to be granted access to all their gov domains in HIBP](https://www.troyhunt.com/welcoming-the-german-government-to-have-i-been-pwned/) (and one more to come next week)
3. [WoTLabs got very pwned](https://web.archive.org/web/20240303062156/http%3A//forum.wotlabs.net/) (site defacement on top of leaked data is never a good look)
4. [The Онлайн Трейд (Online Trade) breach was an oldie, but it's helping us tune the import process as part of the RDBMS rollover](https://xakep.ru/2022/09/21/new-leaks/?ref=troyhunt.com) (which is... painful)
5. [Speaking of RDBMS rollover, most of the ideas I had during this video have proven to be completely useless, so we're now rolling to Hyperscale as well](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tier-hyperscale?view=azuresql&ref=troyhunt.com) (it's actually only very slightly more expensive)
6. [We're still contributing to the HIBP UX rebuild repo](https://github.com/haveibeenpwned/ux-rebuild/?ref=troyhunt.com) (consider it a "soft launch" for now, I'll blog about it in more detail after I get back from Japan)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Weekly%20Update%20390&url=https://www.troyhunt.com/weekly-update-390/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/weekly-update-390/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/weekly-update-390/)
 Email
 [RSS](https://feeds.feedburner.com/TroyHunt)

Troy Hunt's Picture

##### Troy Hunt

Hi, I'm Troy Hunt, I write this blog, create courses for Pluralsight and am a Microsoft Regional Director and MVP who travels the world speaking at events and training technology professionals

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

#### Troy Hunt

Hi, I'm Troy Hunt, I write this blog, run "Have I Been Pwned" and am a Microsoft Regional Director and MVP who travels the world speaking at events and training technology professionals

#### Upcoming Events

I often run [private workshops](/workshops) around these, here's upcoming events I'll be at:

#### Must Read

* [Data breach disclosure 101: How to succeed after you've failed](/data-breach-disclosure-101-how-to-succeed-after-youve-failed/)
* [Data from connected CloudPets teddy bears leaked and ransomed, exposing kids' voice messages](/data-from-connected-cloudpets-teddy-bears-leaked-and-ransomed-exposing-kids-voice-messages/)
* [Here's how I verify data breaches](/heres-how-i-verify-data-breaches/)
* [When a nation is hacked: Understanding the ginormous Philippines data breach](/when-nation-is-hacked-understanding/)
* [How I optimised my life to make my job redundant](/how-i-optimised-my-life-to-make-my-job/)

Don't have Pluralsight already? [How about a 10 day free trial?](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fbilling.pluralsight.com%2Findividual%2Fcheckout) That'll get you access to thousands of courses amongst which are dozens of my own including:

1. [OWASP Top 10 Web Application Security Risks for ASP.NET](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fowasp-top10-aspdotnet-application-security-risks)
2. [What Every Developer Must Know About HTTPS](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fhttps-every-developer-must-know)
3. [Hack Yourself First: How to go on the Cyber-Offense](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fhack-yourself-first)
4. [The Information Security Big Picture](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Finformation-security-big-picture)
5. [Ethical Hacking: Social Engineering](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fethical-hacking-social-engineering)
6. [Modernizing Your Websites with Azure Platform as a Service](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fmodernizing-websites-microsoft-azure)
7. [Introduction to Browser Security Headers](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fbrowser-security-headers)
8. [Ethical Hacking: SQL Injection](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fethical-hacking-sql-injection)
9. [Web Security and the OWASP Top 10: The Big Picture](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fweb-security-owasp-top10-big-picture)
10. [Ethical Hacking: Hacking Web Applications](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fethical-hacking-web-applications)

[#### Welcoming the Liechtenstein Government to Have I Been Pwned](/welcoming-the-liechtenstein-government-to-have-i-been-pwned/)
[#### Welcoming the German Government to Have I Been Pwned](/welcoming-the-german-government-to-have-i-been-pwned/)

[Subscribe](#subscribe)

#### Subscribe Now!

Send new blog posts:

daily

weekly

Hey, just quickly confirm you're not a robot:

Submitting...

Got it! Check your email, click the confirmation link I just sent you and we're done.

###### Copyright 2025, Troy Hunt

This work is licensed under a [Creative Commons Attribution 4.0 International License...