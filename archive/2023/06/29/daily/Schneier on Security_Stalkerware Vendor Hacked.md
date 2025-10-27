---
title: Stalkerware Vendor Hacked
url: https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html
source: Schneier on Security
date: 2023-06-29
fetch_date: 2025-10-04T11:49:08.055575
---

# Stalkerware Vendor Hacked

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Stalkerware Vendor Hacked

The stalkerware company LetMeSpy has been [hacked](https://techcrunch.com/2023/06/27/letmespy-hacked-spyware-thousands/):

> TechCrunch reviewed the leaked data, which included years of victims’ call logs and text messages dating back to 2013.
>
> The database we reviewed contained current records on at least 13,000 compromised devices, though some of the devices shared little to no data with LetMeSpy. (LetMeSpy claims to delete data after two months of account inactivity.)
>
> […]
>
> The database also contained over 13,400 location data points for several thousand victims. Most of the location data points are centered over population hotspots, suggesting the majority of victims are located in the United States, India and Western Africa.
>
> The data also contained the spyware’s master database, including information about 26,000 customers who used the spyware for free and the email addresses of customers who bought paying subscriptions.

The leaked data contains no identifying information, which means people whose data was leaked can’t be notified. (This is actually much more complicated than it might seem, because alerting the victims often means alerting the stalker—which can put the victims into unsafe situations.)

Tags: [data breaches](https://www.schneier.com/tag/data-breaches/), [hacking](https://www.schneier.com/tag/hacking/), [stalking](https://www.schneier.com/tag/stalking/)

[Posted on June 28, 2023 at 7:17 AM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html) •
[7 Comments](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html#comments)

### Comments

Ted •
[June 28, 2023 11:09 AM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423527)

@Winter

> what’s going to be interesting in this specific case is where the *gdpr liability* lies, is it on LMS or on the operators to inform victims, if we’re lucky this could already be enough to bring them down. [my emphasis]

At this time, I don’t know if LMS is already down. The TC article says the “[t]he hacker intimated that they deleted LetMeSpy’s databases stored on the server.”

Does the name of the file sent to maia (jaki\_kraj\_taki\_finfisher. tar) mean anything to you?

Ted •
[June 28, 2023 11:11 AM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423528)

@Winter
What are your thoughts on this from maia arson crimew:

> what’s going to be interesting in this specific case is where the *gdpr liability* lies, is it on LMS or on the operators to inform victims, if we’re lucky this could already be enough to bring them down. [my emphasis]

At this time, I don’t know if LMS is already down. The TC article says the “[t]he hacker intimated that they deleted LetMeSpy’s databases stored on the server.”

Does the name of the file sent to maia (jaki\_kraj\_taki\_finfisher. tar) mean anything to you?

Winter •
[June 28, 2023 11:38 AM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423529)

@Ted

> What are your thoughts on this from maia arson crimew:

That is a question for the legal experts.

If the data is not Personal Identifiable Data (PID) and cannot be traced to natural persons, it does not fall under the GDPR. Also, the GDPR only covers Europe and Europeans. So what follows only holds for any data from Europe.

BUT, time-location data is PID, as are call logs. Storing these requires a legal “reason”, eg, informed consent from the person identified. LetMeSpy is only a data processor, so must rely on the legal status of their clients who are the Data Controllers.

From the context, any PID from Europe would require the clients of LetMeSpy proving legally valid reasons to collect and store the data, which most certainly will be considered PID, which I seriously doubt they could. LetMeSpy is not of the hook in this case as they obviously would know that their clients did collect the data illegally.

Being definitely in the wrong, LetMeSpy would be the target of police and judicial system.

But all hinges on whether there is data from Europe and whether anyone will find it urgent enough to prosecute.

For instance, several EU countries have shown extremely cavelier attitudes towards procecuting crimes against women. I would not be very surprised if stalkers would not be effectively prosecuted in these countries.

Ted •
[June 28, 2023 6:05 PM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423538)

Thanks @Winter.

> BUT, time-location data is PID, as are call logs.

It [looks like](https://www.theregister.com/2023/06/27/letmespy_stalkerware_app_hacked/) the data did include call logs, geolocations, IP addresses, payment logs, email addresses, etc.

In their breach notice LMS said they had notified law enforcement and the Polish data protection authority, UODO. (LMS was apparently a Polish developer.)

Here is a [toot](https://crimew.gay/objects/cc9c55ba-6feb-47e0-a06b-42029d434b72) linking to maia’s blog post. I think the filter may have blocked a direct link to the post due to language in the URL.

lurker •
[June 29, 2023 3:55 PM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423556)

@Ted
foo.finfisher.tar

An old one, must still be a good one. I thought I had seen finfisher snooping at my MacOS server earlier than 2008, but that’s when Wikip says it first appeared exploiting a flaw in iTunes.

Ted •
[June 29, 2023 6:43 PM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423563)

@lurker
A security research blog who first reported the breach had emailed the company, and the hacker actually responded. They even described the initial attack vector:

“SQL injection in API login. SMS content and phone numbers in the database were encrypted, but I changed the user\_id to my own and plaintext of all messages and numbers was visible in the browser.”

<https://niebezpiecznik.pl/post/letmespy-android-wyciek-hacked/>

lurker •
[June 30, 2023 1:20 AM](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/#comment-423572)

@Ted

SQL injection on API login?
That’s an oldie and a goodie too.
As @Clive might say,
They just never learn …

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2023/06/stalkerware-vendor-hacked.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2023/06/stalkerware-vendor-hacked.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2023%2F06%2Fstalkerware-vendor-hacked.html "Login")

Name

E...