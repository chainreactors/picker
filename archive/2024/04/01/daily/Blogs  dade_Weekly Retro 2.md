---
title: Weekly Retro 2
url: https://0xda.de/blog/2024/03/weekly-retro-2/
source: Blogs  dade
date: 2024-04-01
fetch_date: 2025-10-04T12:15:01.928391
---

# Weekly Retro 2

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/03/weekly-retro-2/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

10 minutes

# [Weekly Retro 2](https://0xda.de/blog/2024/03/weekly-retro-2/)

---

* [XZ Backdoor](#xz-backdoor)
* [People Data Labs](#people-data-labs)
* [AT&T Admits It’s Their Data](#att-admits-its-their-data)
* [Signal 0-Click? Not Likely](#signal-0-click-not-likely)
* [Site Updates](#site-updates)
  + [Feeds](#feeds)
  + [Site Search](#site-search)
  + [Book Shortcodes](#book-shortcodes)
* [What I’m Reading](#what-im-reading)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

I hope you’ve got your popcorn ready, this week was a doozy. I spent most of my week doing company events in San Francisco, but that didn’t stop me from keeping up with some absolutely ridiculous events around the internet, including the xz backdoor, another sleazy data broker, an update to the AT&T breach, and some unsubstantiated noise clouding Signal.

I even managed to find time to work on my site some more, addressing a couple points of feedback, and adding a completely overkill feature that is just cool.

## XZ Backdoor

I feel like we just have to start with the xz backdoor – even though it only came to light on Friday, it immediately captured my whole attention and I hardly remember anything that happened before Friday.

For those who haven’t been following the saga, the gist of it is that a maintainer of the popular `xz` package, which is used for compression/decompression by a variety of upstream programs, attempted to ship an update to the package that would inject a NOBUS backdoor authorization mechanism when used in the context of sshd.

To catch up on what is going on, I highly recommend Evan Boehs’ “[Everything I Know About the Xz Backdoor](https://boehs.org/node/everything-i-know-about-the-xz-backdoor).” In it, he covers the timeline of the user, Jia Tan, including some other suspicious behavior going back to 2021.

We know that [Kali](https://twitter.com/kalilinux/status/1773786266074513523) and [Homebrew](https://twitter.com/bcrypt/status/1773792762908786770) were both impacted, as well as have [ideas of other impacted distros](https://xeiaso.net/notes/2024/xz-vuln/). Some other interesting theories that I’ve seen involve [very abnormal commit times](https://twitter.com/birchb0y/status/1773871381890924872) and potential [co-conspirators](https://twitter.com/f0wlsec/status/1773824841331740708). I think it remains to be seen if the developer was [complicit, compelled, or compromised](https://twitter.com/_MG_/status/1774144209232298378), though many minds smarter than I are definitely leaning towards “complicit.” I suppose only time will tell.

[Technical](https://gist.github.com/smx-smx/a6112d54777845d389bd7126d6e9f504) [analysis](https://bsky.app/profile/filippo.abyssdomain.expert/post/3kowjkx2njy2b) is still [ongoing](https://gynvael.coldwind.pl/?id=782), but what we’ve seen so far is quite interesting. One of the findings that especially surprised me is [this stray dot](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=f9cf4c05edd14dedfe63833f8ccbe41b55823b00) that somehow led to a sandbox not being used. I don’t pretend to understand enough about it, but that’s such a simple diff that I would have never thought to attempt.

## People Data Labs

I saw an [interesting twitter thread](https://twitter.com/parth220_/status/1771589789143478471) while I was totally absolutely paying complete attention in a work session about a sophisticated phishing attack that relied on a lot of existing information and Caller ID spoofing. What stood out to me about this thread wasn’t the phishing attack details, but rather the reference to People Data Labs.

I’ve spent a pretty good amount of time trying to hunt my personal information off the internet from various data brokers. I remember using an old version of Delete Me’s [Opt Out Guides](https://joindeleteme.com/blog/opt-out-guides/) probably close to 10 years ago now. But I had never heard of this People Data Labs, so I was curious.

They purport to be a business to business “people enrichment” service, providing additional context about people. From what I can tell, “business to business” in this sense means due diligence going so far as “Owns a domain name,” and no farther. Within a few minutes I had my free account and was able to look up myself and some friends who gave me consent to look them up.

While pulling the data, I noticed this [remarkable API design](https://twitter.com/0xdade/status/1772865233352110266), where they just have you run a sql query against a data set and then return the results to you. The `/v5/` in the URL is what makes it super funny to me, though. Five iterations of the API to land on “Just send us SQL, we’ll figure it out.”

As far as the data this broker has, it seems like it may have been primarily scraped or collected from other data brokers as a sort of aggregation. They had very little information on me – one old email address, a phone number that belonged to my dead grandparents, and an address that belonged to my other grandparents a little over a decade ago. That’s about all they had on me. But they had much more on my friend, which appeared to heavily rely on Facebook and Linkedin scraping, combined with company enrichment data from a site like ZoomInfo.

Overall, these companies are parasites and deserve to have their business destroyed. But short of being able to single handedly destroy their business, I’d recommend [requesting them to delete your data](https://privacy.peopledatalabs.com/policies?modal=take-control). I’ve also gone ahead and submitted them to [Yael Grauer’s BADBOOL list](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List/pull/39).

If manually submitting opt out requests sounds exhausting, there are multiple services that will do it for you on an ongoing basis for an annual fee. I don’t personally use them, since I’m the type of nerd that enjoys opting out myself. But I have made many recommendations for [Delete Me](https://joindeleteme.com/) and it has worked well for the folks who use it and don’t want to think about it.

## AT&T Admits It’s Their Data

Following up on the data breach I touched on in last week’s retro, [AT&T has admitted](https://about.att.com/story/2024/addressing-data-set-released-on-dark-web.html) that their data was leaked, though they still can’t say if they were breached or if it originated from a partner.

[TechCrunch](https://techcrunch.com/2024/03/30/att-reset-account-passcodes-customer-data/) also reported that bulk account passcode resets were sent out, since the passcodes were also included in the leaked data. I can’t say I’m surprised to see [Chick3nman](https://twitter.com/Chick3nman512) quoted as the researcher, and it’s pretty funny that they normalized the encryption of all passcodes, such that there were only 10,000 unique encrypted values. It makes sense if you want to save database size by normalizing the encrypted passcodes into their own table. But if they were stored inline on the table, then there was no reason to not uniquely encrypt each passcode such that there were never duplicates.

As always, [Have I Been Pwned](https://haveibeenpwned.com/) can let you know if your data was breached, but only if you know which email address you used for AT&T or AT&T affiliated services.

## Signal 0-Click? Not Likely

I was really on the fence about even including this, but I think it deserves add...