---
title: Weekly Update 423
url: https://www.troyhunt.com/weekly-update-423/
source: Troy Hunt's Blog
date: 2024-10-27
fetch_date: 2025-10-06T18:53:16.424535
---

# Weekly Update 423

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Weekly Update 423

27 October 2024

Firstly, my apologies for the minute and a bit of echo at the start of this video, OBS had somehow magically decided to start recording both the primary mic and the one built into my camera. Easy fix, moving on...

During the livestream, I was perplexed as to why the HIBP DB was suddenly maxing out. Turns out that this aligned with *dropping* a constraint on the table of domains which appears to have caused the table to reindex and massively slow down the queries for breached email addresses. Further, we simultaneously started having problems related to MAXDOP (the maximum degree of parallelism for the stored procedure running the query), which was only resolved after we forced it to *not* run on multiple CPUs by setting it to 1 (weirdly, 2 is also fine but 3 or higher completely killed perf). Fun times, running a service like this.

[![Listen on Apple Podcasts](https://www.troyhunt.com/content/images/2018/05/Listen-on-Apple-Podcasts.svg)](https://itunes.apple.com/au/podcast/troy-hunts-weekly-update-podcast/id1176454699?ref=troy-hunt)

[![Watch and Listen on YouTube](https://www.troyhunt.com/content/images/2024/09/Watch-and-Listen-on-YouTube.svg)](https://www.youtube.com/playlist?list=PL7LAAxaabizMAXnJe0s3xjQ30q12EVmjt&ref=troyhunt.com)

[![](https://www.troyhunt.com/content/images/2019/10/spotify.svg)](https://open.spotify.com/show/7jMtKFohdrw6qmz8AkLqit?ref=troy-hunt)

[![Download via RSS](https://www.troyhunt.com/content/images/2018/07/Download-via-RSS.svg)](https://omny.fm/shows/troy-hunt-weekly-update/playlists/podcast.rss?ref=troy-hunt)

### References

1. [Sponsored by: 1Password Extended Access Management: Secure every sign-in for every app on every device.](https://1password.com/xam/extended-access-management?utm_campaign=xam_launch&utm_source=troy_hunt_blog&utm_medium=paid_ad&utm_content=xam_product)
2. [The Internet Archive's Zendesk was accessed and replies sent to a bunch of tickets](https://x.com/troyhunt/status/1847919775302750422?ref=troyhunt.com) (it's just gone from bad to bad for them, and still no disclosure to individuals...)
3. [Basically everyone thinks unauthorised access should result in breach notifications being sent to impact individuals](https://x.com/troyhunt/status/1849348747047706667?ref=troyhunt.com) (I mean, it's a predictable outcome, but there were still some wacky arguments against it)
4. [I'm feeling pretty damn exasperated about the lack of breach disclosure lately](https://x.com/troyhunt/status/1849905006293680518?ref=troyhunt.com) (multiple incidents this year have included my own personal data, and I'm pissed)

[Weekly update](/tag/weekly-update/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Weekly%20Update%20423&url=https://www.troyhunt.com/weekly-update-423/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/weekly-update-423/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/weekly-update-423/)
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

[#### Weekly Update 424](/weekly-update-424/)
[#### Weekly Update 422](/weekly-update-422/)

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