---
title: Have I Been Pwned 2.0 is Now Live!
url: https://www.troyhunt.com/have-i-been-pwned-2-0-is-now-live/
source: Troy Hunt's Blog
date: 2025-05-20
fetch_date: 2025-10-06T22:28:40.692024
---

# Have I Been Pwned 2.0 is Now Live!

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Have I Been Pwned 2.0 is Now Live!

20 May 2025

This has been a *very* long time coming, but finally, after a marathon effort, [the brand new Have I Been Pwned website is now live](https://haveibeenpwned.com/?ref=troyhunt.com)!

![](https://www.troyhunt.com/content/images/2025/05/2025-05-15_08-25-12.jpg)

[Feb last year is when I made the first commit](https://github.com/HaveIBeenPwned/ux-rebuild/commit/38853b79597d3d22afad4ff6822ceaa94b6c49f9?ref=troyhunt.com) to the public repo for the rebranded service, and [we soft-launched the new brand in March of this year](https://www.troyhunt.com/soft-launching-and-open-sourcing-the-have-i-been-pwned-rebrand/). Over the course of this time, we've completely rebuilt the website, changed the functionality of pretty much every web page, added a heap of new features, and today, we're even launching a merch store 😎

Let me talk you through just some of the highlights, strap yourself in!

## The Search

The signature feature of HIBP is that big search box on the front page, and now, it's even better - it has confetti!

![](https://www.troyhunt.com/content/images/2025/05/image-16.png)

Well, not for everyone, only about half the people who use it will see a celebratory response. There's a reason why this response is intentionally jovial, let me explain:

As Charlotte and I have travelled and spent time with so many different users of the service around the world, a theme has emerged over and over again: HIBP is a bit playful. It's not a scary place emblazoned with hoodies, padlock icons, and fearmongering about "the dark web". Instead, we aim to be more consumable to the masses and provide factual, actionable information without the hyperbole. Confetti guns (yes, there are several, and they're animated) lighten the mood a bit. The alternative is that you get the red response:

![](https://www.troyhunt.com/content/images/2025/05/image-21.png)

There was a very brief moment where we considered a more light-hearted treatment on this page as well, but somehow a bit of sad trombone really didn't seem appropriate, so we deferred to a more demure response. But now it's on a timeline you can scroll through in reverse chronological order, with each breach summarising what happened. And if you want more info, we have an all-new page I'll talk about in a moment.

Just one little thing first - we've dropped username and phone number search support from the website. Username searches were introduced in 2014 for [the Snapchat incident](https://haveibeenpwned.com/Breach/Snapchat?ref=troyhunt.com), and phone number searches in 2021 for [the Facebook incident](https://haveibeenpwned.com/Breach/Facebook?ref=troyhunt.com). And that was it. That's the only time we ever loaded those classes of data, and there are several good reasons why. Firstly, they're both painful to parse out of a breach compared to email addresses, which we simply use a regex to extract ([we've open sourced the code that does this](https://github.com/HaveIBeenPwned/EmailAddressExtractor?ref=troyhunt.com)). Usernames are a string. Phone numbers are, well, it depends. They're not just numbers because if you properly internationalise them (like they were in the Facebook incident), they've also got a plus at the front, but they're frequently all over the place in terms of format. And we can't send notifications because nobody "owns" a username, and phone numbers are *very* expensive to send SMSs to compared to sending emails. Plus, every other incident in HIBP other than those two has had email addresses, so if we're asking "have I been pwned?" we can always answer that question without loading those two hard-to-parse fields, which usually aren't present in most breaches anyway. When the old site offered to accept them in the search box, it created confusion and support overhead: "why wasn't my number in the [whatever] breach?!". That's why it's gone *from the website*, but we've kept it supported on the API to ensure we don't break anything... just don't expect to see more data there.

## The Breach Page

There are many reasons we created this new page, not least of which is that the search results on the front page were getting too busy, and we wanted to palm off the details elsewhere. So, now we have a dedicated page for each breach, [for example](https://haveibeenpwned.com/Breach/AshleyMadison?ref=troyhunt.com):

![](https://www.troyhunt.com/content/images/2025/05/image-19.png)

That's largely information we had already (albeit displayed in a much more user-friendly fashion), but what's unique about the new page is much more targeted advice about what to do *after* the breach:

![](https://www.troyhunt.com/content/images/2025/05/image-20.png)

[I recently wrote about this section](https://www.troyhunt.com/after-the-breach-finding-new-partners-with-solutions-for-have-i-been-pwned-users/) and how we plan to identify other partners who are able to provide appropriate services to people who find themselves in a breach. Identity protection providers, for example, make a lot of sense for many data breaches.

Now that we're live, we'll also work on fleshing this page out with more breach and user-specific data. For example, if the service supports 2FA, then we'll call that out specifically rather than rely on the generic advice above. Same with passkeys, and we'll add a section for that. A recent discussion with the NCSC while we were in the UK was around adding localised data breach guidance, for example, showing folks from the UK the NCSC logo and a link to [their resource on the topic](https://www.troyhunt.com/after-the-breach-finding-new-partners-with-solutions-for-have-i-been-pwned-users/) (which recommends checking HIBP 🙂).

I'm sure there's much more we can do here, so if you've got any great ideas, drop me a comment below.

## The Dashboard

Over the course of many years, we introduced more and more features that required us to know who you were (or at least that you had access to the email address you were using). It began with [introducing the concept of a sensitive breach](https://www.troyhunt.com/heres-how-im-going-to-handle-ashley/) during the Ashley Madison saga of 2015, which meant the only way to see your involvement in that incident was to receive an email to the address before searching. (Sidenote: [There are many good reasons why we don't do that on every breach](https://www.troyhunt.com/the-ethics-of-running-a-data-breach-search-service/).) In 2019, when [I put an auth layer around the API to tackle abuse](https://www.troyhunt.com/authentication-and-the-have-i-been-pwned-api/) (which it did *beautifully!*) I required email verification first before purchasing a key. And more things followed: a dedicated domain search dashboard, managing your paid subscription and earlier this year, viewing stealer logs for your email address.

We've now unified all these different places into one central dashboard:

![](https://www.troyhunt.com/content/images/2025/05/image-15.png)

From a glance at the nav on the left, you can see a lot of familiar features that are pretty self-explanatory. These combine relevant things for the masses and those that are more business-oriented. They're now all behind the one "Sign In" that verifies access to the email address before being shown. In the future, we'll also add passkey support to avoid needing to send an email first.

The dashboard approach isn't just about moving existing features under one banner; it will also give us a platform on which to build new features in the future that require email address verification first. For example, we've often been asked to provide people with the...