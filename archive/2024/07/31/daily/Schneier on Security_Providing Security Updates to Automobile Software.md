---
title: Providing Security Updates to Automobile Software
url: https://www.schneier.com/blog/archives/2024/07/providing-security-updates-to-automobile-software.html
source: Schneier on Security
date: 2024-07-31
fetch_date: 2025-10-06T17:45:05.890496
---

# Providing Security Updates to Automobile Software

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

## Providing Security Updates to Automobile Software

Auto manufacturers are [just starting to realize](https://www.wired.com/story/cars-are-now-rolling-computers-so-how-long-will-they-get-updates-automakers-cant-say/) the problems of supporting the software in older models:

> Today’s phones are able to receive updates six to eight years after their purchase date. Samsung and Google provide Android OS updates and security updates for seven years. Apple [halts servicing](https://support.apple.com/en-us/102772) products seven years after they stop selling them.
>
> That might not cut it in the auto world, where the average age of cars on US roads is only going up. A [recent report](https://www.spglobal.com/mobility/en/research-analysis/average-age-vehicles-united-states-2024.html) found that cars and trucks just reached a new record average age of 12.6 years, up two months from 2023. That means the car software hitting the road today needs to work­—and maybe even improve—­beyond 2036. The average length of smartphone ownership is just [2.8 years](https://www.telegraph.co.uk/business/2023/12/26/surging-bills-prompt-people-keep-mobile-phones-for-longer).

I [wrote about this](https://www.schneier.com/books/click-here/) in 2018, in *Click Here to Kill Everything*, talking about patching as a security mechanism:

> This won’t work with more durable goods. We might buy a new DVR every 5 or 10 years, and a refrigerator every 25 years. We drive a car we buy today for a decade, sell it to someone else who drives it for another decade, and that person sells it to someone who ships it to a Third World country, where it’s resold yet again and driven for yet another decade or two. Go try to boot up a 1978 Commodore PET computer, or try to run that year’s VisiCalc, and see what happens; we simply don’t know how to maintain 40-year-old [consumer] software.
>
> Consider a car company. It might sell a dozen different types of cars with a dozen different software builds each year. Even assuming that the software gets updated only every two years and the company supports the cars for only two decades, the company needs to maintain the capability to update 20 to 30 different software versions. (For a company like Bosch that supplies automotive parts for many different manufacturers, the number would be more like 200.) The expense and warehouse size for the test vehicles and associated equipment would be enormous. Alternatively, imagine if car companies announced that they would no longer support vehicles older than five, or ten, years. There would be serious environmental consequences.

We really don’t have a good solution here. Agile updates is how we maintain security in a world where new vulnerabilities arise all the time, and we don’t have the economic incentive to secure things properly from the start.

Tags: [books](https://www.schneier.com/tag/books/), [cars](https://www.schneier.com/tag/cars/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [software](https://www.schneier.com/tag/software/)

[Posted on July 30, 2024 at 7:07 AM](https://www.schneier.com/blog/archives/2024/07/providing-security-updates-to-automobile-software.html) •
[33 Comments](https://www.schneier.com/blog/archives/2024/07/providing-security-updates-to-automobile-software.html#comments)

### Comments

wiredog •
[July 30, 2024 8:00 AM](https://www.schneier.com/blog/archives/2024/07/providing-security-updates-to-automobile-software.html/#comment-439693)

As far as security goes, if data connections are disabled that problem is solved. At least for remote access exploits. As always, if the Bad Guys have physical access they can do what they want. The data connection (an LTE connection on my car, and what happens when LTE goes away?) is used for navigation (I use my cell phone), the OnStar type services (ditto), and OTA software upgrades. The car runs fine if you pull the fuse for the LTE radio, though you do get error messages on some screens.

The easy thing for car manufacturers to do is get rid of the data connection and rely on the owner’s cell phone for any remote connectivity needed. The control bus (CANBUS, IIRC?) should be completely separated from the infotainment system, of course the two systems are getting more tightly integrated all the time.

I have a nasty feeling that this will all fly below the radar until either an update error, or cyberattack, bricks a bunch of cars. Bonus havoc if some of them are driving at freeway speeds when it happens with extra bonus wrongful death lawsuits.

Clive Robinson •
[July 30, 2024 8:15 AM](https://www.schneier.com/blog/archives/2024/07/providing-security-updates-to-automobile-software.html/#comment-439694)

@ Bruce, ALL,

Re : More than meets the eye.

> “We really don’t have a good solution here. Agile updates is how we maintain security in a world where new vulnerabilities arise all the time, and we don’t have the economic incentive to secure things properly from the start.”

I think it’s fair to say that people now realise that “Code Signing” really is the “busted flush” identified on this blog way way more than a decade ago.

Also the latest bit of fun with CrowdStrike and Secure Boot in the past few days emphasize just how cracked and broken such “over the network updating is.

What has not been made clear but really should be is,

“What if the update completely borks the update process as part of the update problems?”

Yup 1ton bricks as far as the eye can see potentially blocking the roads and highways…

So the current way we do “agile updates” is really a bad idea, which we already know. Because high risk systems are not updated this way and in some cases is forbidden.

Imagine the flight system in your aircraft getting borked or worse bricked mid flight…

Why should any other vehicle be treated any less than “best practice” for vehicles.

But there is another issue which hides behind “we don’t have the economic incentive to secure things properly from the start”

Actually the opposite is the true state of things. The economic incentive is to get people to not own what they buy.

Hands up who remembers what Apple did to battery systems to get you to update faster?

How about HP Printers and the cartridges and the repeated unlawful scams they have pulled?

Then how about John Deere tractors?

And the now common in the car industry of making you rent what you have purchased like AirCon being built in but disabled unless you pay lots of money each month?

The best incentive is to make you pay over and over… But the lowest manufacturing cost is “pile it all in”. So all sorts of “security tricks” are being added to bleed you over and over…

Imagine the fun of you not wanting air-con any longer, so some low wage droid trying to make quoter accidently causes something else to be disabled like anti-lock breaks after all “one bit is the same as the next bit”.

Oh and the ca...