---
title: Processing 630 Million More Pwned Passwords, Courtesy of the FBI
url: https://www.troyhunt.com/processing-630-million-more-pwned-passwords-courtesy-of-the-fbi/
source: Troy Hunt's Blog
date: 2025-12-12
fetch_date: 2025-12-13T03:16:21.847215
---

# Processing 630 Million More Pwned Passwords, Courtesy of the FBI

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Processing 630 Million More Pwned Passwords, Courtesy of the FBI

13 December 2025

The sheer scope of cybercrime can be hard to fathom, even when you live and breathe it every day. It's not just the volume of data, but also the extent to which it replicates across criminal actors seeking to abuse it for their own gain, and to our detriment.

We were reminded of this recently when the FBI reached out and asked if they could send us 630 million more passwords. For the last four years, [they've been sending over passwords found during the course of their investigations](https://www.troyhunt.com/open-source-pwned-passwords-with-fbi-feed-and-225m-new-nca-passwords-is-now-live/) in the hope that we can help organisations block them from future use. Back then, we were supporting 1.26 *billion* searches of the service each month. Now, it's... more:

Just as it's hard to wrap your head around the scale of cybercrime, I find it hard to grasp that number fully. On *average*, that service is hit nearly 7 thousand times per second, and at peak, it's many times more than that. Every one of those requests is a chance to stop an account takeover. But the real scale goes well beyond the API itself. Because the data model is open source and freely available, many organisations use the [Pwned Passwords Downloader](https://github.com/HaveIBeenPwned/PwnedPasswordsDownloader?ref=troyhunt.com) to take the entire corpus offline and query it directly within their own applications. That tool alone calls the API around a million times during download, but the resulting data is then queried… well, who knows how many times after that. Pretty cool, right?

This latest corpus of data came to us as a result of the FBI seizing multiple devices belonging to a suspect. The data appeared to have originated from both the open web and Tor-based marketplaces, Telegram channels and infostealer malware families. We hadn't seen about 7.4% of them in HIBP before, which might sound small, but that's 46 million vulnerable passwords we weren't giving people using the service the opportunity to block. So, we've added those and bumped the prevalence count on the other 584 million we already had.

We're thrilled to be able to provide this service to the community for free and want to also quickly thank Cloudflare for their support in providing us with the infrastructure to make this possible. Thanks to their edge caching tech, all those passwords are queryable from a location just a handful of milliseconds away from wherever you are on the globe.

If you're hitting the API, then all the data is already searchable for you. If you're downloading it all offline, go and grab the latest data now. Either way, go forth and put it to good use and help make a cybercriminal's day just that much harder 😊

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Processing%20630%20Million%20More%20Pwned%20Passwords%2C%20Courtesy%20of%20the%20FBI&url=https://www.troyhunt.com/processing-630-million-more-pwned-passwords-courtesy-of-the-fbi/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/processing-630-million-more-pwned-passwords-courtesy-of-the-fbi/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/processing-630-million-more-pwned-passwords-courtesy-of-the-fbi/)
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
[#### Weekly Update 481](/weekly-update-481/)

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

This site runs entirely on [Ghost](https://ghost.org/) and is made possible thanks to their kind support. Read more about [why I chose to u...