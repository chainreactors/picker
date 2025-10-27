---
title: Data Breach Misattribution, Acxiom & Live Ramp
url: https://www.troyhunt.com/data-breach-misattribution-acxiom-live-ramp/
source: Troy Hunt's Blog
date: 2022-11-23
fetch_date: 2025-10-03T23:35:01.049473
---

# Data Breach Misattribution, Acxiom & Live Ramp

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Data Breach Misattribution, Acxiom & Live Ramp

23 November 2022

If you find your name and home address posted online, how do you know where it came from? Let's assume there's no further context given, it's just your legitimate personal data and it also includes your phone number, email address... and over 400 other fields of data. *Where on earth did it come from?* Now, imagine it's not just your record, but it's 246 *million* records. Welcome to my world.

This is a story about a massive corpus of data circulating widely within the hacking community and misattributed to a legitimate organisation. That organisation is [Acxiom](https://www.acxiom.com/?ref=troyhunt.com), and their business hinges on providing their customers with data on *their* customers. By the very nature of their business, they process large volumes of data that includes a broad set of personal attributes. By pure coincidence, there is nominal commonality between Acxiom’srecords and the ones in the 246M corpus I mentioned earlier. But I'm jumping ahead to the conclusion, let's go back to the beginning:

### Disclosure and Attribution Debunking

In June last year, I received an email from someone I trust who had sent me data for Have I Been Pwned (HIBP) in the past:

> Have you seen Axciom [sic] data? It was just sent to us. Seems to being traded/sold on some forums. Have you received it yet? If not i can upload it for you. It's quite large tho, ~250M Records.

A corpus of data that size is particularly interesting as it impacts such a huge number of people. So, I reviewed the data and concluded... pretty much nothing. Looks legit, smells legit but there was absolutely nothing beyond the word of one person to tie it to Acxiom (and who knows who they got that word from). Burdened by other more immediately actionable data breaches, I filed it away until recently when that name popped up again, this time on a popular hacking forum:

![](https://www.troyhunt.com/content/images/2022/11/BreachPost.png)

It was referred to as "LiveRamp (Formerly Acxiom)" and before I go any further, let's just clarify the problem with that while you're looking at the image above: LiveRamp was previously a subsidiary of Acxiom, but that hasn't been the case since they separated businesses in 2018 so whoever put this together is referring back to a very old state of play. Regardless, those downloading it from the forum were clearly very excited about it. Seeing this for the second time and spreading far more broadly, I decided to reach out to the (alleged) source and ask Acxiom what was going on.

I dread this process - contacting an organisation about a breach - because I usually get either no response whatsoever or a standoffish one. Rarely do I find a receptive organisation willing to fully investigate an alleged incident, but that's exactly what I found on this occasion. Much of the reason why I wanted to write this post is because whilst I hate breached organisations not properly investigating an incident, I also hate seeing *misattribution* of a breach to an innocent party. That's a particularly sore point for me right now because of this incident just last week:

> This is the dumbest infosec story I’ve read in… forever? It is so profoundly incorrect, poorly researched, never verified, rambling and indistinguishable from parody that I literally went looking for the parody reference. I think he’s actually serious! [https://t.co/oLyIHxb8D3](https://t.co/oLyIHxb8D3?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [November 15, 2022](https://twitter.com/troyhunt/status/1592606998469971970?ref_src=twsrc%5Etfw&ref=troyhunt.com)

I've had various public users of HIBP, commercial users and even governments reach out to ask what's going on because they were concerned about their data. Whilst this incident won't do HIBP any actual harm (and frankly, I'm stunned *anyone* took that story seriously), I can very easily see how misattribution can be damaging to an organisation, indeed that's a key reason why I invest so much effort into properly investigating these claims before putting anything into HIBP. But that ridiculous example is nothing compared to the amount of traction some misattributions get. Remember how just recently a couple of billion TikTok accounts had been "breached"? This made *massive* news headlines until...

> The thread on the hacking forum with the samples of alleged TikTok data has been deleted and the user banned for “lying about data breaches” [https://t.co/9ZKkKvu8JT](https://t.co/9ZKkKvu8JT?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [September 5, 2022](https://twitter.com/troyhunt/status/1566885196250501120?ref_src=twsrc%5Etfw&ref=troyhunt.com)

"Lying about data breaches". Ugh, criminals are so untrustworthy! This happens all the time and when I'm not sure of the origin of a substantial breach, I often write a blog post like this and on many occasions, the masses help establish the origin. So, here goes:

### The Data

Let's jump into the data, starting with 2 of the most obvious things I look for in any new data breach:

1. The total number of unique email addresses is 51,730,831 (many records don't have this field populated)
2. The most recent data I can find is from mid-2020 (which also speaks to the inaccuracy of the LiveRamp association)

As to the aforementioned attributes, they total 410 different columns:

To my eye, this data is *very* generic and looks like a superset of information that may be collected across a large number of people. For example, the sort of data requested when filling out dodgy online competitions. However, unlike many large corpuses of aggregated data I've seen in the past, this one is... neat. For example, here's a little sample of the first 5 columns (redaction of some chars with a dash), note how the names are all uniformly presented:

```
120321486,4,BE-----,B,TAYLOR
120321487,2,JOY,M,----EY
120321466,1,DOYLE,E,------HAM
120321486,3,L----,,TAYLOR
120321486,2,R---,M,TAYLOR
```

Sure, this is just uppercasing characters but over and over again, I found data that was just too neat. The addresses. The phone numbers. Everything about it was far to curated to simply be text entered by humans. My suspicion is that it's likely a result of either a very refined collection process or in the case of addresses, matched using a service to resolve the human-entered address to a normalised form stored centrally.

Perhaps what I was most interested in though was the URL column as that seems to give *some* indication of where the data might have come from. I queried out the top 100 most common ones and took a look:

Eyeballing them, I couldn't help feel that my earlier hunch was on the money - "dodgy online competitions". Not just competitions but a general theme of getting stuff for cheap or more specifically, services that look like they've been built to entice people to part with their personal data.

Take the first one, for example, DIRECTEDUCATIONCENTER.COM. That's a dead domain as of now but [check out what it looked line in March last year](https://web.archive.org/web/20210301163007/http%3A//directeducationcenter.com/):

![](https://www.troyhunt.com/content/images/2022/11/image-11.png)

"I may be contacted by trusted partners and others". What's "others"? Untrusted partners? 🤷‍♂️

Let's try the next one being originalcruisegiveaway.com and again, the site is now gone so it's back over to archive.org:

![](https://www.troyhunt.com/content/images/2022/11/image-13.png)

It's different, but somehow the same. Clicking through to the claim form, it seems the only way you can enter is if you agree to receive comms from all sort...