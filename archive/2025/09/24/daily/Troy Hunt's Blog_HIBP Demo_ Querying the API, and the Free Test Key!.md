---
title: HIBP Demo: Querying the API, and the Free Test Key!
url: https://www.troyhunt.com/hibp-demo-querying-the-api-and-the-free-test-key/
source: Troy Hunt's Blog
date: 2025-09-24
fetch_date: 2025-10-02T20:36:43.694978
---

# HIBP Demo: Querying the API, and the Free Test Key!

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# HIBP Demo: Querying the API, and the Free Test Key!

24 September 2025

One of the most common use cases for HIBP's API is querying by email address, and we support hundreds of millions of searches against this endpoint every month. Loads of organisations use this service to understand the exposure of their customers and provide them with better protection against account takeover attacks. Many also use it to support customers who've already fallen victim - "hey, did you know HIBP says you're in 7 data breaches, any chance you've been reusing passwords?" Some companies even use it to help establish the legitimacy of an email address; we're all so pwned that if an address isn't pwned, [maybe it isn't even real](https://www.troyhunt.com/pwned-or-bot/).

The latest video demo walks you through how to use this API and introduces something new that has been requested for *years:* a test API key. We've had this request so many times, and my response has usually been something to the effect of "mate, a key is a few bucks, just get a cheapie and start writing code". However, even if it were just a few *cents*, it would still pose a burden to some for various reasons. So, [today we're also launching a test key](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#TestAPIKey):

```
hibp-api-key: 00000000000000000000000000000000
```

The test key can only be used for queries against [the test accounts](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#TestAccounts) (and we've had those for many years now), but it allows developers to start immediately writing code against the real live APIs. The technical implementation is identical to the key you get when you have a paid subscription, so this should help a bunch of people really fast-track their development and remove that one little barrier we previously had. Here's how it all works:

So, that's the breached account API, and it comes off the back of [last week's first demo, showing how domain searches work](https://www.troyhunt.com/have-i-been-pwned-demos-are-now-live/). We've got a heap more to add yet and I'd love to hear about and others you feel would help you get the most out of the service.

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20HIBP%20Demo%3A%20Querying%20the%20API%2C%20and%20the%20Free%20Test%20Key!&url=https://www.troyhunt.com/hibp-demo-querying-the-api-and-the-free-test-key/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/hibp-demo-querying-the-api-and-the-free-test-key/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/hibp-demo-querying-the-api-and-the-free-test-key/)
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

[#### Weekly Update 471](/weekly-update-471/)
[#### Weekly Update 470](/weekly-update-470/)

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