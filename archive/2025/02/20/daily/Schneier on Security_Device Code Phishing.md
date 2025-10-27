---
title: Device Code Phishing
url: https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html
source: Schneier on Security
date: 2025-02-20
fetch_date: 2025-10-06T20:39:42.678960
---

# Device Code Phishing

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

## Device Code Phishing

This isn’t new, but it’s [increasingly popular](https://arstechnica.com/information-technology/2025/02/russian-spies-use-device-code-phishing-to-hijack-microsoft-accounts/):

> The technique is known as device code phishing. It exploits “device code flow,” a form of authentication formalized in the industry-wide [OAuth standard](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-device-flow-07#section-3.4). Authentication through device code flow is designed for logging printers, smart TVs, and similar devices into accounts. These devices typically don’t support browsers, making it difficult to sign in using more standard forms of authentication, such as entering user names, passwords, and two-factor mechanisms.
>
> Rather than authenticating the user directly, the input-constrained device displays an alphabetic or alphanumeric device code along with a link associated with the user account. The user opens the link on a computer or other device that’s easier to sign in with and enters the code. The remote server then sends a token to the input-constrained device that logs it into the account.
>
> Device authorization relies on two paths: one from an app or code running on the input-constrained device seeking permission to log in and the other from the browser of the device the user normally uses for signing in.

Tags: [authentication](https://www.schneier.com/tag/authentication/), [authorization](https://www.schneier.com/tag/authorization/), [phishing](https://www.schneier.com/tag/phishing/), [Russia](https://www.schneier.com/tag/russia/)

[Posted on February 19, 2025 at 10:07 AM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html) •
[6 Comments](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html#comments)

### Comments

Clive Robinson •
[February 19, 2025 5:19 PM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/#comment-443211)

From the article we see,

> *‘“While Device Code Authentication attacks are not new, they appear to have been rarely leveraged by nation-state threat actors,” Volexity CEO Steven Adair wrote’*

May cause people to think,

“Why, are they poor attacks?”

The attacks work and as noted elsewhere in the article they are very effective…

So why have other “Nation-State Actors” not used them?

It’s because in less hostile times the NatState agencies much prefer to not be seen or heard by the persons/entities of interest they are targeting. It’s part of the “Advanced Persistent Threat”(APT) thinking where “discretion” and not “tipping off” are key to longterm success.

However in hostile times they will in effect be playing “Capture the flag” or to obtain an objective as quickly as expedient.

So in non hostile times you in effect want to,

1, “Watch from cover” (being discreet).

For APT you would ideally not want to go inside a person/entity of interests systems or network. Because if they go looking or have hidden instrumentation then you will be seen and action against you taken.

Also the thing about the Internet is it’s mostly not anonymous that is you can not setup some kind of interaction with an entity without,

1, Leaving a trail that can be followed.
2, Alerting the entity that you are interested in them in some way.

Thus if the entity of interest gets “curious” and back tracks your communications they will fairly quickly find there is something odd or does not add up. At which point things unravel and not only is the entity “tipped off” there is a real probability they will be able to identify you.

Thus in less hostile times, you would get access to an “up-stream router” beyond the entity of interests “scope” and “tee-off” any and all traffic knowing that the entity of interest can not see you doing this.

Then you would use “traffic analysis” to build up a “Communications & Connectivity Profile” to establish “base lines” to work “Deltas” against.

If you need to go after “plaintext” then you would find some way for getting KeyMat to be leaked via some form of side channel (all early AES implementations had horrendous “time based” side channels that spewed the KeyMat far and wide). Another way is to abuse CA PubKey systems by tampering with the supply chain of updates in browsers and the like, just dropping in a fake CA Cert has been and still is used as a “magic key” backdoor in many places in the world.

Andy •
[February 19, 2025 11:58 PM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/#comment-443218)

Surprisingly I didn’t see a screenshot of Microsoft’s screen explaining to the user what s/he was about to grant access to by providing that code. While the user is the final link, the weak one could be the UI

ResearcherZero •
[February 21, 2025 1:32 AM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/#comment-443243)

@Clive

I assume by “rarely” he means only when they want to access a device or someone’s phone.
Some might use the term “regularly” in it’s place, or another adjective “methodically”.

jmzc •
[February 21, 2025 7:40 AM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/#comment-443248)

OAuth is not for authentication

ResearcherZero •
[February 25, 2025 5:58 AM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/#comment-443323)

@Clive Robinson

Microsoft found a way to reduce both the attack surface and phishing. 😉

‘https://www.abc.net.au/news/2025-02-25/microsoft-365-subscription-price-hike-consumer-complaints-accc/104965682

[Rustwer](http://crypticrisk.com) •
[March 17, 2025 11:13 AM](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/#comment-443732)

Doesn’t seem like a vulnerability at all. Just your normal old social engineering silliness, but 3-letters and intel like to go berzerk whenever anything “new” happens.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/02/device-code-phishing.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/02/device-code-phishing.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F02%2Fdevice-code-phishing.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

Δ

[← Story About Medical Devi...