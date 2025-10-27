---
title: Weekly Update 426
url: https://www.troyhunt.com/weekly-update-426/
source: Troy Hunt's Blog
date: 2024-11-18
fetch_date: 2025-10-06T19:15:18.178505
---

# Weekly Update 426

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Weekly Update 426

17 November 2024

I have absolutely no problem at all talking about the code I've screwed up. Perhaps that's partly because after 3 decades of writing software (and doing some meaningful stuff along the way), I'm not particularly concerned about showing my weaknesses. And this week, I screwed up a bunch of stuff; database queries that weren't resilient to SQL database scale changes, partially completed breach notifications I didn't notice until it was too late to easily fix, and some queries that performed so badly they crashed the entire breach notification process after loading the massive DemandScience incident. Fortunately, none of them had any impact of note, we fixed them all and re-ran processes, and now we're more resilient than ever 😄

Oh - and if you like this style of content, this coming Friday, Stefan and I will do a joint live stream on all sorts of other bits about how now HIBP runs.

[![Listen on Apple Podcasts](https://www.troyhunt.com/content/images/2018/05/Listen-on-Apple-Podcasts.svg)](https://itunes.apple.com/au/podcast/troy-hunts-weekly-update-podcast/id1176454699?ref=troy-hunt)

[![Watch and Listen on YouTube](https://www.troyhunt.com/content/images/2024/09/Watch-and-Listen-on-YouTube.svg)](https://www.youtube.com/playlist?list=PL7LAAxaabizMAXnJe0s3xjQ30q12EVmjt&ref=troyhunt.com)

[![](https://www.troyhunt.com/content/images/2019/10/spotify.svg)](https://open.spotify.com/show/7jMtKFohdrw6qmz8AkLqit?ref=troy-hunt)

[![Download via RSS](https://www.troyhunt.com/content/images/2018/07/Download-via-RSS.svg)](https://omny.fm/shows/troy-hunt-weekly-update/playlists/podcast.rss?ref=troy-hunt)

### References

1. [Sponsored by: 1Password Extended Access Management: Secure every sign-in for every app on every device.](https://1password.com/xam/extended-access-management?utm_campaign=xam_launch&utm_source=troy_hunt_blog&utm_medium=paid_ad&utm_content=xam_product)
2. [Elon Musk is right](https://twitter.com/troyhunt/status/1856940146169434556?ref=troyhunt.com) (I hate cookie warnings, but I'm entertained by people losing their minds "because Elon")
3. [The Hot Topic breach went into HIBP](https://au.pcmag.com/security/107921/hacker-may-have-breached-hot-topic-stolen-data-on-millions?ref=troyhunt.com) (that's another 57M email addresses right there)
4. [There are also now 122M more records in HIBP courtesy of the DemandScience breach](https://www.troyhunt.com/inside-the-demandscience-by-pure-incubation-data-breach/) (it's publicly aggregated data, but it's still a breach)

[Weekly update](/tag/weekly-update/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Weekly%20Update%20426&url=https://www.troyhunt.com/weekly-update-426/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/weekly-update-426/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/weekly-update-426/)
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

[#### Closer to the Edge: Hyperscaling Have I Been Pwned with Cloudflare Workers and Caching](/closer-to-the-edge-hyperscaling-have-i-been-pwned-with-cloudflare-workers-and-caching/)
[#### Inside the DemandScience by Pure Incubation Data Breach](/inside-the-demandscience-by-pure-incubation-data-breach/)

[Subscribe](#subscribe)

#### Subscribe Now!

Send new blog posts:

daily

weekly

Hey, just quickly confirm you're not a robot:

Submitting...

Got it! Check your email, click the confirmation link I just sent you and we're done.

###### Copyright 2025, Troy Hunt

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). In other words, share generously but provide attribution.

###### Disclaimer

Opinions expressed here are my own and may not reflect those of others. Unless I'm quoting someone, they're just my own views.

###### Published with Ghost

This site runs entirely on [Ghost](https://ghost.org/) and is made possible thanks to their kind support. Read more about [why I chose to use Ghost](https://www.troyhunt.com/its-a-new-blog/).