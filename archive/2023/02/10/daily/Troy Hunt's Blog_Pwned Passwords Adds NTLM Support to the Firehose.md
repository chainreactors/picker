---
title: Pwned Passwords Adds NTLM Support to the Firehose
url: https://www.troyhunt.com/pwned-passwords-adds-ntlm-support-to-the-firehose/
source: Troy Hunt's Blog
date: 2023-02-10
fetch_date: 2025-10-04T06:16:06.828088
---

# Pwned Passwords Adds NTLM Support to the Firehose

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Pwned Passwords Adds NTLM Support to the Firehose

09 February 2023

I think I've pretty much captured it all in the title of this post but as of about a day ago, Pwned Passwords now has full parity between the SHA-1 hashes that have been there since day 1 and NTLM hashes. We always had both as a downloadable corpus but as of just over a year ago with [the introduction of the FBI data feed](https://www.troyhunt.com/open-source-pwned-passwords-with-fbi-feed-and-225m-new-nca-passwords-is-now-live/), we stopped maintaining downloadable behemoths of data.

A little later, [we added the downloader](https://www.troyhunt.com/downloading-pwned-passwords-hashes-with-the-hibp-downloader/) to make it easy to pull down the latest and greatest complete data set directly from the same API that so many of you have integrated into your own apps. But because we only had an API for SHA-1 hashes, the downloader couldn't grab the NTLM versions and increasingly, we had 2 corpuses well out of parity.

I don't know exactly why, but just over the last few weeks we've had a marked uptick in requests for an updated NTLM corpus. Obviously there's still a demand to run this against local Active Directory environments and clearly, the more up to date the hashes are the more effective they are at blocking the use of poor passwords.

So, [Chief Pwned Passwords Wrangler Stefán Jökull Sigurðarson](https://www.troyhunt.com/expanding-the-have-i-been-pwned-volunteer-community/) got to work and just went ahead and built it all for you. For free. In his spare time. As a community contribution. Seriously, have a look through [the public GitHub repos](https://github.com/HaveIBeenPwned?ref=troyhunt.com) and it's all his work ranging from the API to the Cloudflare Worker to the downloader so if you happen to come across him say, [at NDC Oslo in a few months' time](https://ndcoslo.com/speakers/stefn-jkull-sigurarson?ref=troyhunt.com), show your appreciation and buy the guy a beer 🍺

Lastly, every time I look at how much this tool is being used, I'm a bit shocked at how big the numbers are getting:

![](https://www.troyhunt.com/content/images/2023/02/2023-02-09_17-33-03.png)

That's well more than double the number of monthly requests from when [I wrote the blog post about the FBI and NCA only just over a year ago](https://www.troyhunt.com/open-source-pwned-passwords-with-fbi-feed-and-225m-new-nca-passwords-is-now-live/), and I imagine that will only continue to increase, especially with today's announcement about NTLM hashes. Thank you to everyone that has taken this data and done great things with it, we're grateful that it's been put to good use and has undoubtedly helped an untold number of people to make better password choices 😊

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)
[Pwned Passwords](/tag/pwned-passwords/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Pwned%20Passwords%20Adds%20NTLM%20Support%20to%20the%20Firehose&url=https://www.troyhunt.com/pwned-passwords-adds-ntlm-support-to-the-firehose/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/pwned-passwords-adds-ntlm-support-to-the-firehose/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/pwned-passwords-adds-ntlm-support-to-the-firehose/)
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

[#### Weekly Update 334](/weekly-update-334/)
[#### Weekly Update 333](/weekly-update-333/)

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