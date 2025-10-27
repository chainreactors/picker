---
title: The Have I Been Pwned API Now Has Different Rate Limits and Annual Billing
url: https://www.troyhunt.com/the-have-i-been-pwned-api-now-has-different-rate-limits-and-annual-billing/
source: Troy Hunt's Blog
date: 2022-11-07
fetch_date: 2025-10-03T21:52:57.991545
---

# The Have I Been Pwned API Now Has Different Rate Limits and Annual Billing

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# The Have I Been Pwned API Now Has Different Rate Limits and Annual Billing

07 November 2022

A couple of weeks ago [I wrote about some big changes afoot for Have I Been Pwned](https://www.troyhunt.com/expanding-and-enhancing-the-have-i-been-pwned-api/) (HIBP), namely the introduction of annual billing and new rate limits. Today, it's finally here! These are two of the most eagerly awaited, most requested features on [HIBP's UserVoice](https://haveibeenpwned.uservoice.com/?ref=troyhunt.com) so it's great to see them finally knocked off after years of waiting. In implementing all this, there are changes to the existing "one size fits all" model so if you're using the HIBP API, please make sure you read this carefully and understand the impact (if any) on you. Here goes:

### The Rate Limits and (Some) Pricing is Different

The launch blog post for the authenticated API explained the original rationale behind the $3.50 per month price and most importantly, how I wanted to ensure it didn't pose a barrier:

> In choosing the $3.50 figure, I wanted to ensure it was a number that was inconsequential to a **legitimate** user of the service

As I said in the previous blog post, what I didn't understand at the time was that paradoxically, the low amount *was* a barrier to many organisations! But equally, it's made the API super accessible to the masses so that price stays. The rate limit, however, needed revisiting and to understand why, let's go back to the beginning:

The "1 request per 1,500ms" rate dated all the way back to 2016 [where I'd initially attempted to combat abuse by applying the limit per IP](https://www.troyhunt.com/the-have-i-been-pwned-api-rate-limiting-and-commercial-use/). This was an entirely non-empirical, gut feel, "let's just try and fix the problem right now" decision and it was only very recently I actually started trawling through the data and looking at how the API was being consumed. 1 request every 1,500ms is a maximum of 57,600 requests in a day; here's the number of requests by the top 20 consumers of the service in a recent 24 hour mid-week period:

![](https://www.troyhunt.com/content/images/2022/07/API-requests.png)

Keeping in mind that you're never going to achieve the full 57,600 requests in a day as you'd have to time every single one of them *perfectly* so as not to hit the rate limit, only 1 subscriber even achieved half that potential. In fact, only 9 subscribers achieved even a *quarter* of the potential with everyone else very quickly falling back to a small fraction of even that. To be fair, I'm conscious that I'm taking a full day of data and talking about requests as if they were evenly distributed across the entire period when there are inevitably use cases where it's more a short burst rather than a prolonged, even distribution. Regardless, what the data is saying is that the default "one size fits all" rate limit is *way* above and beyond what almost every single subscriber is actually consuming, and by a significant order of magnitude too. In a way, what we ended up with is the little guys subsidising the big guys.

The bottom line is that we're simultaneously adding a bunch of higher rate limits whilst reducing the entry level rate limit. It's easier if you see it all in context so let's just jump straight into the pricing (all in USD):

![](https://www.troyhunt.com/content/images/2022/11/image-6.png)

This is from Stripe's embeddable pricing table I mentioned in the previous post and it's what you see when you first sign up for a key. With new limits, it's easier to talk about "requests per minute" or RPM so that's the nomenclature we're sticking with now. That entry level 10RPM model will work for well in excess of 90% of current subscribers and it's only a very small percentage of the existing subscriber base exceeding it. (And yes, again, I know these requests are sometimes made in bursts but even still, 10RPM is *far* in excess of the vast majority of use cases.)

There are economies of scale that have been factored in here. Going from 10RPM to 100RPM isn't a 10x increase, it's about a 7x increase. Going to 5 times more requests is only 4 times the price, and so on and so forth. The hope is that this makes it easier for the folks who were previously buying multiple keys to justify scratching all the kludge previously used to do that and replacing it with a single key at a higher RPM.

To get to this outcome, we trawled back through heaps of data ranging from the high-level aggregated stats in the earlier chart to the nature of the organisations buying multiple keys (which we can obviously determine based on the email address used). I also chatted with a bunch of API users both during this process and over the preceding years and have a pretty good sense of the use cases. A few trends became immediately clear:

Firstly, use cases that are *genuinely* personal have a very low rate limit requirement. Checking your own address(es) or those of your family by a custom app, for example. Or one of my favourite uses (and one I *definitely* use), [the Home Assistant integration](https://www.home-assistant.io/integrations/haveibeenpwned/?ref=troyhunt.com):

![](https://www.troyhunt.com/content/images/2022/11/image.png)

On an ongoing basis, HA makes 1 request every 15 minutes. That's all. Each time we looked at genuine personal use cases, 10RPM was plenty.

Next, we found a bunch of use cases used within internal corporate environments, for example to monitor staff exposure in breaches. Now we're talking larger numbers of requests, but it's also something that's way more efficiently done via [the existing domain search feature on the website](https://haveibeenpwned.com/DomainSearch?ref=troyhunt.com). It's an on-demand, self-service and totally free feature that's been there for years. I know it's not API-based and [there are good reasons for that](https://haveibeenpwned.uservoice.com/forums/275398-general/suggestions/19170856-add-domain-search-capability-to-the-api-functions?ref=troyhunt.com) (see the comment from me on that idea), but there's also the Enterprise route if API access is *really* that important (more on that later). Other examples included things like scanning customer emails to assess exposure at points where, for example, account takeover was a risk. In each of these cases, we're primarily talking about *business entities* using the service and I'm comfortable with commercial ventures wearing a greater cost.

And finally, there were the "heavy hitters", the ones with large volumes of keys. One such example using the API en masse provides security services to the big end of town and was funded to the tune of a figure that looks like a phone number. And again, I'm perfectly comfortable with them wearing a cost that's more commensurate to the value as opposed to a figure that was originally arrived at just to keep the bad guys out.

### Existing Subscribers are Grandfathered in for 60 Days

Before I talk about the annual pricing, I want to make sure this headline is clear. *Nothing changes for existing subscribers until the 6th of Jan next year, which is 60 days from today.* On that date, the legacy rate limit of 1 request every 1,500ms will roll to the new 10RPM limit *at exactly the same price.* For that handful of big users for whom the 10RPM limit will be insufficient, you've got a couple of months to work out the best path forward. I'll be emailing every single active subscriber today to ensure everyone is notified well in advance (there's also an updated Terms of Use which requires a notification email to be sent).

What does this mean in practical terms? ...