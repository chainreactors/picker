---
title: How We (Almost) Found Chromium's Bug via Crash Reports to Report URI
url: https://www.troyhunt.com/how-we-almost-found-chromiums-bug-via-crash-reports-to-report-uri/
source: Troy Hunt's Blog
date: 2025-10-27
fetch_date: 2025-10-28T03:08:56.615837
---

# How We (Almost) Found Chromium's Bug via Crash Reports to Report URI

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# How We (Almost) Found Chromium's Bug via Crash Reports to Report URI

27 October 2025

Tracking down bugs in software is a pain that all of us who write code must bear. When we're talking about outright errors in a web page, you typically have *something* to get you started (such as output in the console), but that wasn't the case here:

> Sure! Reboots don't help :) Here are the two error screens which show up. [pic.twitter.com/w2dmZcVyHk](https://t.co/w2dmZcVyHk?ref=troyhunt.com)
>
> — Peter Vogel (@PeterVogel) [July 11, 2025](https://twitter.com/PeterVogel/status/1943804862740967584?ref_src=twsrc%5Etfw&ref=troyhunt.com)

That's on a Chromebook, and it's the first user report we had about the issue back in early July. The initial problem this presented is that there are not a lot of people running around with devices we could test on. But there *are* enough people using them that we had multiple similar reports, so we were well beyond just giving people like Peter a bit of "works on my machine", and moving on. But the "SIGILL" error means that something pretty low-level has happened and, as you can see from the screen grab, you can't exactly just pop open the dev tools and peak at what's broken in the site when it can't even load in the first place.

However, after months of making no progress whilst the occasional Chromium user popped their head up and reported exactly the same problem, the answer finally emerged:

> Reading MDN docs I don't find a directive 'report-sha256', so tried only removing that, and no crash.
>
> — Mark : 1x Software Artisan (@virullius) [October 24, 2025](https://twitter.com/virullius/status/1981597950758305836?ref_src=twsrc%5Etfw&ref=troyhunt.com)

Uh... shouldn't a browser just ignore a directive it doesn't recognise? (And incidentally, [report-sha256 is documented in CSP level 3](https://www.w3.org/TR/CSP3/?fbclid=IwY2xjawNsBPVleHRuA2FlbQIxMQABHnebf3gNkC62y9V4xZ1zO8Nhvbw0Q9s-8PQylmnSyIefVK65ssZhcud_z3Hi_aem_lvyQud5NbXgnsU6t9Cva1A&ref=troyhunt.com#reporting).) But the timing was awful coincidental with when we added that exact directive, only just before people started reporting problems:

> Wow, good sleuthing! The timing of when this first began aligns with this commit from [@stebets](https://twitter.com/stebets?ref_src=twsrc%5Etfw&ref=troyhunt.com). I've just dropped it, does it look ok now? Also CC'ing [@Scott\_Helme](https://twitter.com/Scott_Helme?ref_src=twsrc%5Etfw&ref=troyhunt.com) - you seen this before mate? Bug was logged here: [https://t.co/wiKpdmSxhU](https://t.co/wiKpdmSxhU?ref=troyhunt.com) [pic.twitter.com/m2nsDtAMjB](https://t.co/m2nsDtAMjB?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [October 24, 2025](https://twitter.com/troyhunt/status/1981856765135450276?ref_src=twsrc%5Etfw&ref=troyhunt.com)

Getting to the title of this post, we *almost* worked this out ourselves, we just didn't look at data that was right in front of our eyes. Here it is:

![](https://www.troyhunt.com/content/images/2025/10/2025-10-27_18-30-56-1.png)

This is [Report URI's](https://report-uri.com/?ref=troyhunt.com) crash report graph, and until June, we'd had a good run! Crash reports are super cool because your customers' browsers automatically generate them, and with just a little tweaking of your response headers, [you can easily turn your customers into automatic crash reporting bots](https://scotthelme.co.uk/introducing-the-reporting-api-nel-other-major-changes-to-report-uri/?ref=troyhunt.com)! Report URI's value proposition (disclosure: [I have a working relationship with them](https://report-uri.com/about/meet_the_team?ref=troyhunt.com)) is that it can receive those reports and create graphs like you see above. We just weren't watching the reports closely enough, hence the "almost" in the title.

I wanted to write this short post because sometimes, the answer is right in front of your eyes, and if we'd looked at what in hindsight is a really obvious place to check, we would have nailed this months ago. So, turn on crash reporting, *and pay attention to it!*

[Report URI](/tag/report-uri/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20How%20We%20(Almost)%20Found%20Chromium's%20Bug%20via%20Crash%20Reports%20to%20Report%20URI&url=https://www.troyhunt.com/how-we-almost-found-chromiums-bug-via-crash-reports-to-report-uri/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/how-we-almost-found-chromiums-bug-via-crash-reports-to-report-uri/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/how-we-almost-found-chromiums-bug-via-crash-reports-to-report-uri/)
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
8. [Ethical Hacking: SQL Injection](https://pluralsight.pxf.io/c/1196446/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fet...