---
title: 2 Billion Email Addresses Were Exposed, and We Indexed Them All in Have I Been Pwned
url: https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/
source: Instapaper: Unread
date: 2025-11-08
fetch_date: 2025-11-09T03:14:51.651379
---

# 2 Billion Email Addresses Were Exposed, and We Indexed Them All in Have I Been Pwned

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# 2 Billion Email Addresses Were Exposed, and We Indexed Them All in Have I Been Pwned

05 November 2025

I hate hyperbolic news headlines about data breaches, but for the "2 Billion Email Addresses" headline to be hyperbolic, it'd need to be exaggerated or overstated - and it isn't. It's rounded up from the more precise number of 1,957,476,021 unique email addresses, but other than that, it's exactly what it sounds like. Oh - and 1.3 billion unique passwords, 625 million of which we'd never seen before either. It's the most extensive corpus of data we've ever processed, by a *significant* margin.

**Edit:** Just to be crystal clear about the origin of the data and the role of Synthient (who you’ll read about in the next paragraph): this data came from numerous locations where cybercriminals had published it. Synthient (run by Ben during his final year of college) indexed that data and provided it to Have I Been Pwned solely for the purpose of notifying victims. He’s the good guy shining a light on the bad guys, so keep that in mind as you read on. (Some of the feedback Ben has received is exactly what I foreshadowed in the final paragraph of this post.)

A couple of weeks ago, [I wrote about the 183M unique email addresses that Synthient had indexed in their threat intelligence platform and then shared with us](https://www.troyhunt.com/inside-the-synthient-threat-data/). I explained that this was only *part* of the corpus of data they'd indexed, and that it didn't include the credential stuffing records. Stealer log data is obtained by malware running on infected machines. In contrast, credential stuffing lists usually originate from other data breaches where email addresses and passwords are exposed. They're then bundled up, sold, redistributed, and ultimately used to log in to victims' accounts. Not just the accounts they were initially breached from, either, because people reuse the same password over and over again, the data from one breach is frequently usable on completely unrelated sites. A breach of a forum to comment on cats often exposes data that can then be used to log in to the victim's shopping, social media and even email accounts. In that regard, credential stuffing data becomes "the keys to the castle".

Let me run through how we verified the data, what you can do about it and for the tech folks, some of the hoops we had to jump through to make processing this volume of data possible.

## Data Verification

The first person whose data I verified was easy - me 😔 An old email address I've had since the 90s has been in credential stuffing lists before, so it wasn't too much of a surprise. Furthermore, I found a password associated with my address, which I'd *definitely* used many eons ago, and it was about as terrible as you'd expect from that era. However, none of the other passwords associated with my address were familiar. They certainly looked like passwords that other people might have feasibly used, but I'm pretty sure they weren't mine. One was even just an IP address from Perth on the other side of the country, which is both infeasible as a password I would have used, yet eerily close to home. I mean, of all the places in the world an IP address could have appeared from, it had to be somewhere in my own country I've been many times before...

Moving on to HIBP subscribers, I reached out to a handful and asked for support verifying the data. I chose a mix of subscribers with many who'd never been involved in any data breach we'd ever seen before; my experience above suggested that there's recycled data in there, and we had previously verified that when investigating those other incidents. However, is the all-new stuff legitimate? The very first response I received was exactly what I was looking for:

> #1 is an old password that I don't use anymore. #2 is a more recent password. Thanks for the heads up, I've gone and changed the password for every critical account that used either one.

Perfectly illustrating most people's behaviour with passwords, #2 referred to above was just #1 with two exclamation marks at the end!! (Incidentally, these were simple six and eight-character passwords, and neither of them was in [Pwned Passwords](https://haveibeenpwned.com/Passwords?ref=troyhunt.com) either.) He had three passwords in total, which also means one of them, like with my data, was not familiar. However, the most important thing here is that this example perfectly illustrates why we put the effort into processing data like this: #2 was a real, live password that this guy was actively using, and it was sitting right next to his email address, being passed around among criminals. However, through this effort, that credential pair has now become useless, which is precisely what we're aiming for with this exercise, just a couple of billion times over.

The second respondent only had one password against their address:

> Yes that was a password I used for many years for what I would call throw away or unimportant accounts between 20 and 10 years ago

That was also only eight characters, but this time, we'd seen it in Pwned Passwords many times before. And the observation about the password's age was consistent with my own records, so there's definitely some pretty old data in there.

The following response was not at all surprising:

> I am familiar with that password... I used it almost 10 years ago... and cannot recall the last time I used it.

That was on a corporate account, too, and the owner of the address duly forwarded my email to the cybersecurity team for further investigation. The single password associated with this lady's email address had a massive *nine characters*, and also hadn't previously appeared in Pwned Passwords.

Next up was a respondent who replied inline to my questions, so I'll list them below with the corresponding answers:

> Is this familiar? Yes

> Have you ever used it in the past? Yes and is still on some accounts I do not use any longer.

> And if so, how long ago? Unfortunately, it is still on some active accounts that I have just made a list of to change or close immediately.

This individual's eight-character password with uppercase, lowercase, numbers and a "special" character also wasn't in Pwned Passwords. Similarly, as with the earlier response, that password was still in active use, posing a real risk to the owner. It would pass most password complexity criteria and slip through any service using Pwned Passwords to block bad ones, so again, this highlights why it was so important for us to process the data.

The next person had three different passwords against rows with their email address, and they came back with a now common response:

> Yes, these are familiar, last used 10 years ago

We'd actually seen all three of them in Pwned Passwords before, many times each. Another respondent with precisely the kind of gamer-like passwords you'd expect a kid to use (one of which we hadn't seen before), also confirmed (I think?) their use:

> maybe when i was a kid lol

Responses that weren't an emphatic "yes, that's my data" were scarce. The two passwords against one person's name were both in Pwned Passwords (albeit only once each), yet it's entirely possible that neither of them had been used by this specific individual before. It's also possible they'd forgotten a password they'd used more than a decade ago, or it may have even been automatically assigned to them by the service that was subsequently breached. Put it down as a statistical anomaly, but I thought it was worth mentioning to highlight that being in this data set isn't a guarantee of a genuine password...