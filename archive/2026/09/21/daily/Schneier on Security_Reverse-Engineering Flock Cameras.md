---
title: Reverse-Engineering Flock Cameras
url: https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html
source: Schneier on Security
date: 2026-09-21
fetch_date: 2026-09-22T07:05:09.085597
---

# Reverse-Engineering Flock Cameras

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

## Reverse-Engineering Flock Cameras

Hackers captured a Flock camera and got a [look](https://www.404media.co/hackers-stole-flocks-camera-software-revealing-how-the-company-tracks-cars-and-people-2/) (alternate [link](https://archive.ph/gQoMs)) at the software:

> While much of the automatic license plate reader’s (ALPR) most sensitive storage remained encrypted and inaccessible, the joint analysis of the recovered data shows that software running on the device explicitly detects people as well as vehicles, license plates, and bicycles. The camera can produce dozens of images of a single passing vehicle and, according to several weeks of recovered logs, generated more than a million images. Its computer-vision software also sometimes isolated bumper stickers and other graphics, including, in one case, an American flag patch on a motorcyclist’s saddlebag.

If you’re wondering how the hackers got by disk encryption, one of the unencrypted partitions contained the key for an encrypted partition. That’s pretty bad security engineering.

Tags: [AI](https://www.schneier.com/tag/ai/), [cameras](https://www.schneier.com/tag/cameras/), [cars](https://www.schneier.com/tag/cars/), [reverse engineering](https://www.schneier.com/tag/reverse-engineering/)

[Posted on September 21, 2026 at 10:37 AM](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html#comments)

### Comments

Anonymous •
[September 21, 2026 10:46 AM](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html/#comment-458249)

Screw the Mudd-Slimeys. God bless Israel – the holy land.

Clive Robinson •
[September 21, 2026 1:51 PM](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html/#comment-458259)

@ Bruce, ALL,

With regards,

> “… one of the unencrypted partitions contained the key for an encrypted partition. That’s pretty bad security engineering.”

But is it really surprising?

I looked at a video of a Flock camera getting physically stripped down to see what hardware it used.

I was not impressed, to be blunt much of it was low cost “not made in the USA” type stuff.

The issue that the designers would have had as they are battery operated from a small solar cell is

How to do key negotiation when powering up from a flat battery…

I have a sneaky suspicion / feeling that encryption from any camera unit back to Flock HQ will use the same Key-Mat at some point. So when you know what it is for one you know what it is for others…

I guess we will have to wait for a full breakdown on that.

Clive Robinson •
[September 21, 2026 2:34 PM](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html/#comment-458271)

@ Bruce, ALL,

**Is the boot on the other foot?**

Apparently the Washington D.C. Police force is challenging the use of Flock Cameras by the Internal Affairs [1].

But such news I hope is going to probably finally hit even the dimmest of those “Folks on The Hill” that every single road user that turns up to their homes no matter what the time of day will be recorded and available to who ever can get / be given access the pictures.

Worse any one with Flock access will be able to track backwards to where the road users originated and who they are.

And the “blackmail potential” of Flock and others who can “get access to the images” will be enormously persuasive…

[1] There are a lot of articles so I won’t bother with a link. Just say a search with the string

“D.C. Police union challenge Flock usage by internal affairs”

Will get you a whole selection only some of which will be Paywalled.

[Anonymous](https://gainsec.com) •
[September 21, 2026 8:10 PM](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html/#comment-458277)

You don’t have to wait, all of this was already done a year ago… and they didn’t fix any of the issues… <https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Jon%20Gaines%20-%20Bird%20Hunting%20Season%20The%20Final%20Flight%20-%20PDF%20v1.pdf>

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/09/reverse-engineering-flock-cameras.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F09%2Freverse-engineering-flock-cameras.html "Login")

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

[ ]  Notify me of new posts by email.

Δ

[← Friday Squid Blogging: On Squid Egg Sacs](https://www.schneier.com/blog/archives/2026/09/friday-squid-blogging-on-squid-egg-sacs.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier) and the [Munk School](https://munkschool.utoronto.ca/) at the University of Toronto, a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

[Contact Info](https://www.schneier.com/blog/about/contact/)

### Related Entries

* [Are AIs Still Struggling with CAPTCHAs?](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html)
* [How Candidates Could Use AI for Good](https://www.schneier.com/blog/archives/2026/09/how-candidates-could-use-ai-for-good.html)
* [Using AI for...