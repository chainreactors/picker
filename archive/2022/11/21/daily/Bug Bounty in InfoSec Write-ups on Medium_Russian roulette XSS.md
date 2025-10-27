---
title: Russian roulette XSS
url: https://infosecwriteups.com/russian-roulette-xss-bbba6afd2570?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-21
fetch_date: 2025-10-03T23:19:07.238761
---

# Russian roulette XSS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fbbba6afd2570&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frussian-roulette-xss-bbba6afd2570&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frussian-roulette-xss-bbba6afd2570&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bbba6afd2570---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bbba6afd2570---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Russian roulette XSS

[![Splintersec](https://miro.medium.com/v2/resize:fill:64:64/1*GfW4isI5e-cPs_8-b2gENw@2x.jpeg)](https://splint3rsec.medium.com/?source=post_page---byline--bbba6afd2570---------------------------------------)

[Splintersec](https://splint3rsec.medium.com/?source=post_page---byline--bbba6afd2570---------------------------------------)

5 min read

·

Nov 19, 2022

--

Listen

Share

## Story

Press enter or click to view image in full size

![]()

It all happened during an exhaustive week of studying, the night before having a tough exam in Datascience, where I have to remember all kind of complex math formulas. 10 pm, tired of studying and don’t feel sleepy yet, I decided to hunt on Synack for 1 hour before going to bed. And this was the best decision I made that night!

The motivation behind choosing Synack over other platforms is that my friend Conda got into the SRT and I remembered that tweet!

I launched my [LP+](https://www.synack.com/blog/introducing-launchpoint-plus-for-trusted-testing/) then I started looking for new targets. I noticed one with a Blitz running so I decided to give it a try. — Blitz is a kind of promotion that runs for a small period of time, where you get extra cash as a bonus depending on the severity of your report. -

## The hunt

I opened my Burpsuite and logged into the website, To my surprise it was in a foreign language that I couldn’t speak **(Tip: foreign language websites are less tested by other hunters because most of them are lazy to translate the content)** So I had a translation extension that allowed me to understand what every section was about. And as every hunter should do, I started clicking around all the possible buttons I see in front of my eyes. Tested different functionalities and became quite familiar with the platform.

Back to Burpsuite, I had the log of all HTTP requests that went through that period of time, API ones were interesting. So because of the time restriction (exam at 8 am), I decided to start with business logic bugs as this website deals with money transactions, tried all different combinations of paying negative amounts, withdrawing money with a different amount, changing POST requests to GET and so on… But none were successful. I tried to look for IDOR since the requests had numerical IDs, but unfortunately there was a hash value calculated in the cookies that didn’t allow me to do that.

## The hidden File Upload

In a hidden section of the website, where you had to dig through the settings in order to find it, I noticed an upload button, like this one:

![]()

This button was about sending your documents to the website’s administrators, so that they can verify them. And another helpful thing was that this button didn’t disappear after sending my docs, which means I can try resending them as much as I can, but only until the admins approve my documents. Good attack point!

So I behaved like a normal user and I uploaded a dummy file, then clicked on upload. Went to Burpsuite and saw what happens behind the scenes, the file is sent to the website in a JSON POST request, that contains two keys; **filename** and **data**, obviously the first one is about the name of our document and the second one contains the base64 value of our doc.

## The final shot, Russian Roulette

Here I decided to finish my hunting session and append my Blind XSS payload to the filename, because… Why not, right? Even if it doesn’t work I would still be familiar with the website and test other stuff in the next day.

Press enter or click to view image in full size

![]()

That XSS hunter URL is not mine

## Disclaimer for SRT members

This target allowed to include third party websites such as XSS Hunter to perform the testing, **read the scope!!** and if it’s mentioned that you’re not allowed to include third parties, you should not use similar websites.

## Next day

So that night I went to sleep after sending the payload, and woke up at 6 to revise for the exam, went to the university and I did well! So until now I am on the safe side of not studying again for the retake XD, which means more hunting time in the future!

My day was normal, nothing in my inbox yet, came back home, had a 1 hour break from school and started studying again for the next exam. Usually I turn off wifi on my phone while studying to not get easily distracted, so when I finished, I turned off my laptop and went to brush my teeth. On my way I decided to turn on the wifi on my phone and check my notifications… And yes, you guessed it right, to my surprise I received 5 consecutive gmail notifications that my payload was fired somewhere in the internet :D

Without thinking I changed my mind to brush my teeth and started running to my laptop, turned it on and while doing that I was rechecking the phone if it was a false positive, it doesn’t appear to be so! Now I have to be very quick in reporting to avoid falling in the duplicate zone.

## Reporting

It was 11 pm when I sent a very fast report, included the PoC screenshots, cookies and steps, then submitted it. 2 days after, the VO sent a message on the report that I need to elaborate more steps in my submission, like what an attacker can do with the cookies, include XSS Hunter screenshots and so on… I did that knowing that this is definitely not a duplicate report, so I took more than enough time to write the report this time, and be as specific as possible, so that when the client reads it he will understand every small detail.

The same day in the evening, I received an email stating that my vulnerability was accepted!

Press enter or click to view image in full size

![]()

And if this means something, it means that Synack is a very professional and fast platform, where you get paid on triage, and get professional replies on your reports. And we closed the submission with such a nice reply from the VO

![]()

## Final thoughts

Indeed, my friend Conda motivated me to hunt and discover the platform more and more, it is h...