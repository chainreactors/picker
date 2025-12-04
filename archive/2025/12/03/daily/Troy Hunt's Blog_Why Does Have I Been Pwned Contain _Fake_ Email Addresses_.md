---
title: Why Does Have I Been Pwned Contain "Fake" Email Addresses?
url: https://www.troyhunt.com/why-does-have-i-been-pwned-contain-fake-email-addresses/
source: Troy Hunt's Blog
date: 2025-12-03
fetch_date: 2025-12-04T03:19:37.695087
---

# Why Does Have I Been Pwned Contain "Fake" Email Addresses?

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Why Does Have I Been Pwned Contain "Fake" Email Addresses?

04 December 2025

Normally, when someone sends feedback like this, I ignore it, but it happens often enough that it deserves an explainer, because the answer is really, really simple. So simple, in fact, that it should be evident to the likes of Bruce, who decided his misunderstanding [deserved a 1-star Trustpilot review yesterday](https://www.trustpilot.com/users/5d15ed4f97935fab62d61080?ref=troyhunt.com):

![](https://www.troyhunt.com/content/images/2025/12/image.png)

Now, frankly, [Trustpilot is a pretty questionable source of real-world, quality reviews anyway](https://x.com/troyhunt/status/1981506927168254085?ref=troyhunt.com), but the same feedback has come through other channels enough times that let's just sort this out once and for all. It all begins with one simple question:

## What is an Email Address?

You think you know - and Bruce thinks he knows - but you might both be wrong. To explain the answer to the question, we need to start with how HIBP ingests data, and that really is pretty simple: someone sends us a breach (which is typically just text files of data), and we run [the open source Email Address Extractor](https://github.com/HaveIBeenPwned/EmailAddressExtractor?ref=troyhunt.com) tool over it, which then dumps all the unique addresses into a file. That file is then uploaded into the system, where the addresses are then searchable.

The logic for how we extract addresses is all in that Github repository, but in simple terms, it boils down to this:

1. There must be an @ symbol
2. There can be up to 64 characters before it (the alias)
3. There can be up to 255 characters after it (the domain)
4. The domain must contain a period
5. The domain must also have [a valid TLD](https://data.iana.org/TLD/tlds-alpha-by-domain.txt?ref=troyhunt.com)
6. A few other little criteria that are all documented in the public repo

*That is all!* We can't then tell if there's an actual mailbox behind the address, as that would require *massive* per-address processing, for example, sending an email to each one and seeing if it bounces. Can you imagine doing that *7 billion times?!* That's the number of unique addresses in HIBP, and clearly, it's impossible. So, that means all the following were parsed as being valid and loaded into HIBP (deep links to the search result):

1. [test@example.com](https://haveibeenpwned.com/account/test%40example.com?ref=troyhunt.com)
2. [\_test@google.com](https://haveibeenpwned.com/account/_test%40google.com?ref=troyhunt.com)
3. [fuckingwasteoftime@foo.com](https://haveibeenpwned.com/account/fuckingwasteoftime%40foo.com?ref=troyhunt.com)

I particularly like that last one, as it feels like a sentiment Bruce would express. It's also a great example as it's clearly not "real"; the alias is a bit of a giveaway, as is the domain ("foo" is commonly used as a placeholder, similar to how we might also use "bar", or combine them as "foo bar"). But if you follow the link and see the breach it was exposed in, you'll see a very familiar name:

![](https://www.troyhunt.com/content/images/2025/12/image-1.png)

Which brings us to the next question:

## How Do "Fake" Email Addresses End up in Real Websites?

This is also going to seem profoundly simple when you see it. Here goes:

![](https://www.troyhunt.com/content/images/2025/12/image-2.png)

Any questions, Bruce? This is just as easily explainable as why *we* considered it a valid address and ingested it into HIBP: the email address has a valid structure. That is all. That's how it got into Adobe, and that's how it then flowed through into HIBP.

Ah, but shouldn't Adobe *verify* the address? I mean, shouldn't they send an email to the address along the lines of "Hey, are you sure you want to sign up for this service?" Yes, they should, but here's the kicker: *that doesn't stop the email address from being added to their database in the first place!* The way this normally works (and this is what we do with HIBP when you sign up for [the free notification service](https://haveibeenpwned.com/NotifyMe?ref=troyhunt.com)) is you enter the email address, the system generates a random token, and then the two are saved together in the database. A link with the token is then emailed to the address and used to verify the user if they then follow that link. And if they don't follow that link? We delete the email address if it hasn't been verified within a few days, but evidently, Adobe doesn't. Most services don't, so here we are.

## How Can I Be Really Sure Actual Fake Addresses Aren't in HIBP?

This is *also* going to seem profoundly obvious, but *genuinely* random email addresses(not "thisisfuckinguseless@") won't show up in HIBP. Want to test the theory? [Try 1Password's generator](https://1password.com/password-generator?ref=troyhunt.com) (yes, Bruce, they also sponsor HIBP):

![](https://www.troyhunt.com/content/images/2025/12/image-3.png)

Now, [whack that on the foo.com domain and do a search](https://haveibeenpwned.com/account/tobV7dPADsGMT4NNXYsj%40foo.com?ref=troyhunt.com):

![](https://www.troyhunt.com/content/images/2025/12/image-4.png)

Huh, would you look at that? And you can keep doing that over and over again. You’ll get the same result because they are fabricated addresses that no one else has created or entered into a website that was subsequently breached, ipso facto proving they cannot appear in the dataset.

## Conclusion

[Today is HIBP's 12th birthday](https://www.troyhunt.com/introducing-have-i-been-pwned/), and I've taken particular issue with Bruce's review because it calls into question the integrity with which I run this service. [This is now the 218th blog post I've written about HIBP](https://www.troyhunt.com/tag/have-i-been-pwned-3f/), and over the last dozen years, I've detailed everything from the architecture to the ethical considerations to how I verify breaches. It's hard to imagine being any more transparent about how this service runs, and per the above, it's *very* simple to disprove the Bruces of the world. If you've read this far and have an accurate, fact-based review you'd like to leave, that'd be awesome 😊

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Why%20Does%20Have%20I%20Been%20Pwned%20Contain%20%22Fake%22%20Email%20Addresses%3F&url=https://www.troyhunt.com/why-does-have-i-been-pwned-contain-fake-email-addresses/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/why-does-have-i-been-pwned-contain-fake-email-addresses/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/why-does-have-i-been-pwned-contain-fake-email-addresses/)
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
* [Data from connected CloudPets teddy bears leaked and ranso...