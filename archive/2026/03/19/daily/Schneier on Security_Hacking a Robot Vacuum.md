---
title: Hacking a Robot Vacuum
url: https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html
source: Schneier on Security
date: 2026-03-19
fetch_date: 2026-03-20T04:09:24.639640
---

# Hacking a Robot Vacuum

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

## Hacking a Robot Vacuum

Someone tries to remote control his own DJI Romo vacuum, and ends up controlling [7,000 of them](https://www.theverge.com/tech/879088/dji-romo-hack-vulnerability-remote-control-camera-access-mqtt) from all around the world.

The IoT is horribly insecure, but we [already knew that](https://www.schneier.com/books/click-here/).

Tags: [Internet of Things](https://www.schneier.com/tag/internet-of-things/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on March 19, 2026 at 5:47 AM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html#comments)

### Comments

Wow •
[March 19, 2026 6:01 AM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/#comment-452987)

Pretty impressive screwup for a company like DJI. Interesting read! Somehow I’m first

Clive Robinson •
[March 19, 2026 10:10 AM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/#comment-452992)

@ Bruce, ALL,

With regards,

> “The IoT is horribly insecure, but we already knew that.”

It’s not what “we already knew” it’s about what the many others don’t know that really matters.

The reality is that “vibe coding” is heading toward IoT devices near you any time soon… And with them spread far and wide, security will be even worse for everyone…

I guess the real question will be,

“How long before the Internet is unusable, due to the proliferation of junk code on junk hardware?”

Rontea •
[March 19, 2026 10:59 AM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/#comment-452993)

This isn’t some edge case—it’s the predictable result of shipping connected products with minimal authentication, insecure communication protocols, and no meaningful patching strategy.

The industry keeps racing to connect everything to the Internet, from vacuums to refrigerators, and the result is a global network of vulnerable devices waiting to be abused. We’ve known this for years, and yet the market rewards speed and low cost over security. Until manufacturers are held accountable—and until regulation enforces baseline security standards—these kinds of hacks will only get worse.

Bernie •
[March 19, 2026 11:17 AM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/#comment-452994)

Some correct me if I’m wrong.

The article’s sub-headline-thing reads, “The immediate threat may be fixed, but this raises serious questions.” What serious questions does it raise (that haven’t already been raised long enough ago)? Or am I reading too much into that sentence? Is it more clickbait than anything?

lurker •
[March 19, 2026 1:36 PM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/#comment-452996)

@Bernie, Clive Robinson

You must be as old as me. @Clive said it above:

“it’s about what the many others don’t know that really matters.”

We know that putting a vacuum cleaner on the internet is a daft idea fraught with peril. But the Verge article observes:

“… it’s not surprising that a robot vacuum cleaner with a smartphone app would phone home to the cloud. For better or for worse, **users currently expect** those apps to work outside of their own homes. Unless you’ve built a tunnel into your own home network, that means relaying the data through cloud servers first.” [emphasis added]

I expect Azdoufal and many readers of this blog could build their own VPN to control their cleaner from outside their home. But for the average user … So one of the serious questions raised is,

Should IoT makers give users what they want, or what they need? Note that what they need (security, privacy) will cost more than just what they want.

John •
[March 19, 2026 2:30 PM](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/#comment-453000)

IoT devices with internet access are utter nonsense.

The IoT makers could provide an app that runs locally and talks to the IoT devices, inside the firewall. They can poll for instructions from the cloud.

Then we would be discussing security bugs in the app. Security bugs in an app aren’t new, of course, but they are far easier to patch.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/03/hacking-a-robot-vacuum.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/03/hacking-a-robot-vacuum.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F03%2Fhacking-a-robot-vacuum.html "Login")

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

[← Meta’s AI Glasses and Privacy](https://www.schneier.com/blog/archives/2026/03/metas-ai-glasses-and-privacy.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [AI Found Twelve New Vulnerabilities in OpenSSL](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html)
* [AIs Are Getting Better at Finding and Exploiting Security Vulnerabilities](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html)
* [AIs are Getting Better at Finding and Exploiting Internet Vulnerabilities](https://www.schneier.com/b...