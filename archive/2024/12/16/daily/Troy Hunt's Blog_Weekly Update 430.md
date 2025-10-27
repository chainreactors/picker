---
title: Weekly Update 430
url: https://www.troyhunt.com/weekly-update-430/
source: Troy Hunt's Blog
date: 2024-12-16
fetch_date: 2025-10-06T19:37:13.029098
---

# Weekly Update 430

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Weekly Update 430

15 December 2024

I'm back in Oslo! Writing this the day after recording, it feels like I couldn't be further from Dubai; the temperature starts with a minus, it's snowing and there's not a supercar in sight.

Back on business, this week I'm talking about the challenge of loading breaches and managing costs. A breach load immediately takes us from a very high percentage cache hit ratio on Cloudflare to zero. Consequently, our SQL costs skyrocket as the DB scales to support the load. Approximately 28 hours after loading the two breaches I mention in this week's update, we're still running a DB scale that's 350% larger than once we have a high cache hit ratio, and that *directly* hits my wallet. We need to work on this more because as I say in the video, I *really* don't like financial incentives that influence how breaches are handled, such as delaying them and bulking them together to reduce the impact of cache flush events like this. We'll give that more thought, I think there are a few ways to tackle this. For now, here's this week's video and some of the challenges we're facing:

[![Listen on Apple Podcasts](https://www.troyhunt.com/content/images/2018/05/Listen-on-Apple-Podcasts.svg)](https://itunes.apple.com/au/podcast/troy-hunts-weekly-update-podcast/id1176454699?ref=troy-hunt)

[![Watch and Listen on YouTube](https://www.troyhunt.com/content/images/2024/09/Watch-and-Listen-on-YouTube.svg)](https://www.youtube.com/playlist?list=PL7LAAxaabizMAXnJe0s3xjQ30q12EVmjt&ref=troyhunt.com)

[![](https://www.troyhunt.com/content/images/2019/10/spotify.svg)](https://open.spotify.com/show/7jMtKFohdrw6qmz8AkLqit?ref=troy-hunt)

[![Download via RSS](https://www.troyhunt.com/content/images/2018/07/Download-via-RSS.svg)](https://omny.fm/shows/troy-hunt-weekly-update/playlists/podcast.rss?ref=troy-hunt)

### References

1. [Sponsored by: 1Password Extended Access Management: Secure every sign-in for every app on every device.](https://1password.com/xam/extended-access-management?utm_campaign=xam_launch&utm_source=troy_hunt_blog&utm_medium=paid_ad&utm_content=xam_product)
2. [Some people *really* don't like supercars](https://x.com/troyhunt/status/1866441965216366637?ref=troyhunt.com) (although I suspect it's more about not liking to see either the enjoyment others take in them or the success they may have achieved)
3. [Being online means having constant attacks against your online things](https://x.com/troyhunt/status/1867154491499565545?ref=troyhunt.com) (but failed login attempts against my son's and my Microsoft accounts are just that - *failed* attempts)
4. [The German electricity provider Tibber had 50k records breached](https://x.com/haveibeenpwned/status/1867826567885259129?ref=troyhunt.com) (a little one, but newsworthy enough to have hit the media)
5. [And the first-ever Senegalese data breach went into HIBP courtesy of Yonéma](https://x.com/haveibeenpwned/status/1867835332684918873?ref=troyhunt.com) (not exactly a high cross-over with our usual subscribers, but a breach is still a breach)

[Weekly update](/tag/weekly-update/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Weekly%20Update%20430&url=https://www.troyhunt.com/weekly-update-430/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/weekly-update-430/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/weekly-update-430/)
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

[#### Weekly Update 431](/weekly-update-431/)
[#### Weekly Update 429](/weekly-update-429/)

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

This site runs entirely on [Ghost](https://ghost.org/) and is made possible tha...