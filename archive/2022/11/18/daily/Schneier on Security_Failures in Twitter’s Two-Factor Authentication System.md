---
title: Failures in Twitter’s Two-Factor Authentication System
url: https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html
source: Schneier on Security
date: 2022-11-18
fetch_date: 2025-10-03T23:09:24.001142
---

# Failures in Twitter’s Two-Factor Authentication System

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

## Failures in Twitter’s Two-Factor Authentication System

Twitter is having [intermittent problems](https://www.wired.com/story/twitter-two-factor-sms-problems/) with its two-factor authentication system:

> Not all users are having problems receiving SMS authentication codes, and those who rely on an authenticator app or physical authentication token to secure their Twitter account may not have reason to test the mechanism. But users have been self-reporting issues on Twitter since the weekend, and WIRED confirmed that on at least some accounts, authentication texts are hours delayed or not coming at all. The meltdown comes less than two weeks after Twitter [laid off about half of its workers](https://www.wired.com/story/musk-layoffs-twitter-management/), roughly 3,700 people. Since then, engineers, operations specialists, IT staff, and security teams have been stretched thin attempting to adapt Twitter’s offerings and build new features per new owner Elon Musk’s agenda.

On top of that, it seems that the system has a [new vulnerability](https://www.inforisktoday.com/twitter-two-factor-authentication-has-vulnerability-a-20475):

> A researcher contacted Information Security Media Group on condition of anonymity to reveal that texting “STOP” to the Twitter verification service results in the service turning off SMS two-factor authentication.
>
> “Your phone has been removed and SMS 2FA has been disabled from all accounts,” is the automated response.
>
> The vulnerability, which ISMG verified, allows a hacker to spoof the registered phone number to disable two-factor authentication. That potentially exposes accounts to a password reset attack or account takeover through password stuffing.

This is not a good sign.

Tags: [authentication](https://www.schneier.com/tag/authentication/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [passwords](https://www.schneier.com/tag/passwords/), [SMS](https://www.schneier.com/tag/sms/), [Twitter](https://www.schneier.com/tag/twitter/), [two-factor authentication](https://www.schneier.com/tag/two-factor-authentication/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on November 17, 2022 at 5:53 AM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html) •
[29 Comments](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html#comments)

### Comments

Beatrix Willius •
[November 17, 2022 6:53 AM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412562)

Thanks so much for making my day. Who knew that people working at Twitter actually did something?

Untitled •
[November 17, 2022 7:45 AM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412564)

Twitter’s AI isn’t working either. A British astronomer was locked out of her account for three months for posting a photo of a comet that Twitter said was ‘intimate content’. It took intevention by the BBC to get her account back.

Joe •
[November 17, 2022 8:00 AM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412566)

I wonder if this is a new vulnerability or just newly discovered vulnerability that happened to make the news in a convenient time.

Rob •
[November 17, 2022 8:23 AM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412568)

There’s another vulnerability I’ve read about. They blocked name changes to verified users, but you can potentially get around it by rapidly clicking “Save”

Frank B. •
[November 17, 2022 9:21 AM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412572)

Inside the Chief Twits head there are two pigeons fighting over a french fry. Just wave something shiny in front of his eyes and they’ll get distracted and move on to something new.

Norio •
[November 17, 2022 2:52 PM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412577)

> This is not a good sign.

That is one of the best understatements I’ve seen.

@Untitled–the comet was penetrating the solar system at the time, and that’s pretty intimate content.

Ted •
[November 17, 2022 3:44 PM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412579)

Exactly how “hardcore” are FTC consent decrees? And do they have them on Mars?

Joe Sullivan grabs a tub of popcorn.

<https://www.cnn.com/2022/11/11/tech/musk-twitter-ftc>

SpaceLifeForm •
[November 17, 2022 5:13 PM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412581)

Re: Mastodon

I’ll just note that Mastodon does not do SMS 2FA which is good.

That said, if you are going to roam into the various swamplands to drink the water, I would NOT set up 2FA on Mastodon. Stay on solid ground, and use a long complex password.

‘https://sts10.github.io/2022/11/11/mastodon-two-factor-authentication.html

‘https://sts10.github.io/2022/11/12/mastodon-2fa-security-key.html

Note that in order to go the hardware security key route, you must have already taken the software authentication route to get there.

This is not optimal path.

Some dude did not get the memo.

‘https://apnews.com/article/62c9ed67a1e70fb59da3ccb75c2b5212

Ted •
[November 17, 2022 6:49 PM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412586)

I’m really looking forward to a podcast episode featuring Jerry Bell, the administrator of the infosec.exchange Mastodon instance.

It should be coming out soon on the Redefining Cybersecurity podcast.

[https://infosec.exchange/@seanmartin/109356084690447792](https://infosec.exchange/%40seanmartin/109356084690447792)

Apparently Jerry is an IBM Public Cloud VP and CISO. So says LinkedIn. But you wouldn’t know it based on his infosec.exchange profile and his very down-to-earth interactions on the platform.

[https://infosec.exchange/@jerry/109356542388834164](https://infosec.exchange/%40jerry/109356542388834164)

Clive Robinson •
[November 17, 2022 8:13 PM](https://www.schneier.com/blog/archives/2022/11/failures-in-twitters-two-factor-authentication-system.html/#comment-412592)

@ Frank B., AlanS, ALL,

Re : Inside the Chief Twits head

Remember they are also a speed freak who has left the wheelhouse…

Nobody has a clue about direction or destination only that they will get there way faster than is safe.

Some of the “hold rats” have been offered a deal to “jump ship” so the Chief can get more speed.

Arguably it might be the best offer of their life such as...