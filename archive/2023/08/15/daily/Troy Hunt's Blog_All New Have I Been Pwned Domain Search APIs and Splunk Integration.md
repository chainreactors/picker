---
title: All New Have I Been Pwned Domain Search APIs and Splunk Integration
url: https://www.troyhunt.com/all-new-have-i-been-pwned-domain-search-apis-and-splunk-integration/
source: Troy Hunt's Blog
date: 2023-08-15
fetch_date: 2025-10-04T12:04:19.126613
---

# All New Have I Been Pwned Domain Search APIs and Splunk Integration

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# All New Have I Been Pwned Domain Search APIs and Splunk Integration

15 August 2023

I've been teaching my 13-year old son Ari how to code since I first got him started on Scratch many years ago, and gradually progressed through to the current day where he's getting into Python in Visual Studio Code. As I was writing [the new domain search API for Have I Been Pwned](https://www.troyhunt.com/welcome-to-the-new-have-i-been-pwned-domain-search-subscription-service/) (HIBP) over the course of this year, I was trying to explain to him how powerful APIs are:

> Think of HIBP as one website that does pretty much one thing; you load it in your browser and search through data breaches which then display on the screen. But when you have an API, it's no longer just locked into your browser, it's in all sorts of other systems. Mobile apps, other websites, dashboards and if you really want, you can even integrate the lights in your room with HIBP! Why? How? Well, there's [a Home Assistant integration for HIBP](https://www.home-assistant.io/integrations/haveibeenpwned/?ref=troyhunt.com) and being pwned in a new breach could raise an event there you can then use YAML to perform an action with, for example flashing a light red. That might be weird and unnecessary, but when you have an API, suddenly all these things you never thought of are possible.

It took [Brett Adams](https://bre77.au/?ref=troyhunt.com) less than a day after we released the new domain search API last Monday for him to reach out to me with one of those ideas. He wanted to build a Splunk app (Brett is a Splunk MVP so this was right up his alley) to surface breached data about an organisation's domains right into the place where so many security engineers spend their days. He just wanted 2 new APIs to make the user experience the best it could be:

1. One that can show you the subscription level for someone's key
2. One that can show you all the domains they're monitoring

That seems so ridiculously obvious, why didn't I think of that originally?! But hey, easy fix, so the next day Brett had his APIs. And today, you also have the APIs because [they're now all publicly documented](https://haveibeenpwned.com/API/v3?ref=troyhunt.com) and ready for you to consume. You also have Brett's Splunk app and because he's published it to Splunkbase, [you can go and pull it into your own Splunk instance](https://splunkbase.splunk.com/app/6996?ref=troyhunt.com), plug in your HIBP API key and it's job done!

I'll leave you with a bunch of screen caps from Brett's work, starting with a zoomed in grab of what I suspect folks will find the most valuable - the addresses on their domains and their appearances across breaches:

![](https://www.troyhunt.com/content/images/2023/08/summary-2.png)

That's a fragment of the broader dashboard that also breaks down the incidents over time:

![](https://www.troyhunt.com/content/images/2023/08/summary-1.png)

The starting point for this is simply plugging your API key into the interface:

![](https://www.troyhunt.com/content/images/2023/08/setup.png)

I like these headline figures and I picture particularly large organisations that have gone through various acquisitions of different brands with various domains finding this really useful:

![](https://www.troyhunt.com/content/images/2023/08/by_breach.png)![](https://www.troyhunt.com/content/images/2023/08/by_domain.png)![](https://www.troyhunt.com/content/images/2023/08/by_email.png)

And speaking of breaches, there's a lot of them which Brett has visualised across the course of time:

![](https://www.troyhunt.com/content/images/2023/08/all_breaches.png)

So that's it, you can see [all the APIs documented on the HIBP website](https://haveibeenpwned.com/API/v3?ref=troyhunt.com) and you can [grab Brett's app right now from Splunkbase](https://splunkbase.splunk.com/app/6996?ref=troyhunt.com). You can also [find all the code for this in Brett's GitHub repo](https://github.com/Bre77/hibp/?ref=troyhunt.com) should you wish to have a read through it.

The HIBP APIs are there for other people to build awesome things. If you're one of those people, please [get in touch with me](https://www.troyhunt.com/contact/) and show me what you've created, I can't wait to see more integrations like Brett's 😊

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20All%20New%20Have%20I%20Been%20Pwned%20Domain%20Search%20APIs%20and%20Splunk%20Integration&url=https://www.troyhunt.com/all-new-have-i-been-pwned-domain-search-apis-and-splunk-integration/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/all-new-have-i-been-pwned-domain-search-apis-and-splunk-integration/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/all-new-have-i-been-pwned-domain-search-apis-and-splunk-integration/)
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
7. [Introduction to Browser Security Headers](https://p...