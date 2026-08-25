---
title: Weekly Update 518: IoT Doorlock Nirvana with UniFi
url: https://www.troyhunt.com/weekly-update-518/
source: Troy Hunt's Blog
date: 2026-08-24
fetch_date: 2026-08-25T03:00:36.817884
---

# Weekly Update 518: IoT Doorlock Nirvana with UniFi

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Weekly Update 518: IoT Doorlock Nirvana with UniFi

24 August 2026

I genuinely think I've nailed the IoT door lock situation! Well, Ubiquiti has, but I think I've worked out how to put it all into a residential house and have it make sense. There are a few basic tenets:

1. Main power (never have to rely on batteries)
2. Fail-secure (needs to remain locked on power outage)
3. Local control (no cloud latency to contend with)
4. Manual override ("the house is on fire, let me out")

Which is exactly what we have here in this week's vid (and sorry about the section of rubbish audio; the camera mic started capturing it for a short period there). There are some edge cases I want to validate the impact of, namely the inability to keep the door both closed and unlocked, and some of the assumptions I've made around access methods. The laundry will be our low-impact test case; then, if that's all good, I'll start rolling this approach out much more seriously across the house. Stay tuned, I think this will actually be pretty awesome.

[![Listen on Apple Podcasts](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2018/05/Listen-on-Apple-Podcasts.svg)](https://itunes.apple.com/au/podcast/troy-hunts-weekly-update-podcast/id1176454699?ref=troy-hunt)

[![Watch and Listen on YouTube](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2024/09/Watch-and-Listen-on-YouTube.svg)](https://www.youtube.com/playlist?list=PL7LAAxaabizMAXnJe0s3xjQ30q12EVmjt&ref=troyhunt.com)

[![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2019/10/spotify.svg)](https://open.spotify.com/show/7jMtKFohdrw6qmz8AkLqit?ref=troy-hunt)

[![Download via RSS](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2018/07/Download-via-RSS.svg)](https://omny.fm/shows/troy-hunt-weekly-update/playlists/podcast.rss?ref=troy-hunt)

[Weekly update](/tag/weekly-update/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Weekly%20Update%20518%3A%20IoT%20Doorlock%20Nirvana%20with%20UniFi&url=https://www.troyhunt.com/weekly-update-518/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/weekly-update-518/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/weekly-update-518/)
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

#### This is already the newest post!
[#### Welcoming the Sri Lankan Government to Have I Been Pwned](/welcoming-the-sri-lankan-government-to-have-i-been-pwned/)

[Subscribe](#subscribe)

#### Subscribe Now!

Send new blog posts:

daily

weekly

Hey, just quickly confirm you're not a robot:

Submitting...

Got it! Check your email, click the confirmation link I just sent you and we're done.

###### Copyright 2026, Troy Hunt

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). In other words, share generously but provide attribution.

###### Disclaimer

Opinions expressed here are my own and may not reflect those of others. Unless I'm quoting someone, they're just my own views.

###### Published with Ghost

This site runs entirely on [Ghost](https://ghost.org/) and is made possible thanks to their kind support. Read more about [why I chose to use Ghost](https://www.troyhunt.com/its-a-new-blog/).