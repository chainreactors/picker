---
title: Reverse-Engineering Ticketmaster’s Barcode System
url: https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html
source: Instapaper: Unread
date: 2024-07-12
fetch_date: 2025-10-06T17:56:00.205071
---

# Reverse-Engineering Ticketmaster’s Barcode System

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

## Reverse-Engineering Ticketmaster’s Barcode System

[Interesting](https://www.404media.co/scalpers-are-working-with-hackers-to-liberate-non-transferable-tickets-from-ticketmasters-ecosystem/):

> By reverse-engineering how Ticketmaster and AXS actually make their electronic tickets, scalpers have essentially figured out how to regenerate specific, genuine tickets that they have legally purchased from scratch onto infrastructure that they control. In doing so, they are removing the anti-scalping restrictions put on the tickets by Ticketmaster and AXS.

EDITED TO ADD (7/14): More [information](https://www.404media.co/the-ticketmaster-hack-is-becoming-a-logistical-nightmare-for-fans-and-brokers/).

Tags: [hacking](https://www.schneier.com/tag/hacking/), [reverse engineering](https://www.schneier.com/tag/reverse-engineering/)

[Posted on July 9, 2024 at 12:27 PM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html) •
[7 Comments](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html#comments)

### Comments

Aaron •
[July 9, 2024 1:37 PM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439181)

Ticket prices won’t stop Taylor Swift fans from seeing her concerts…

Clive Robinson •
[July 9, 2024 2:25 PM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439182)

@ Bruce, ALL,

All of these “ticket systems” can be got around because there is a fatal flaw in all of the systems.

It is a very general failure that I’ve mentioned before, as has the the then head of the UK’s MI5 I won’t go into it in depth again people can search the blog.

But simply,

There is no way to reliably tie a physical object like a ticket or human to a piece of information.

And as tickets are seen as an unessecary loss of profit they are either not issued or issued in a form that is easily forgeable.

As Stella Rimington noted nearly two decades ago,

> *“All our other documents are quite easily forgeable and if you have ID cards at great expense and people can go into the back room and forge them then they are going to be absolutely useless”*

<https://www.theguardian.com/uk/2005/nov/17/idcards.immigrationpolicy>

So if you can work out how to forge the information, then you can make as many tickets as you want.

Just turn up early so you present the information first.

Clive Robinson •
[July 9, 2024 2:37 PM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439183)

@ Bruce,

You might also want to add this link,

<https://www.404media.co/the-ticketmaster-hack-is-becoming-a-logistical-nightmare-for-fans-and-brokers/>

As it adds more information towards the bottom.

MrC •
[July 9, 2024 9:36 PM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439188)

Does this intersect at all with the ransomware actors that are releasing stolen ticketmaster barcodes?

blitter •
[July 10, 2024 4:56 AM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439192)

For completeness, a technical writeup:

Jon (a different Jon) •
[July 10, 2024 11:01 AM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439198)

What I find interesting (I didn’t sign up, so couldn’t read the whole article – pardon me if I’m completely out in left field) is that they’re suing over reverse-engineering.

This is exactly what copyright and patent laws are for – reveal it, get protection. Don’t reveal it, keep it as a trade secret, and although you can keep it as a secret, you are always at risk of someone else successfully reverse-engineering it.

But noo, apparently someone violated the DMCA or something? Kinda makes a mockery of the whole thing, that.

J.

Arclight •
[July 10, 2024 12:21 PM](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/#comment-439201)

The purpose of the Ticketmaster system isn’t to prevent scalping. It’s there to prevent scalping by entities other than Ticketmaster.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2024/07/reverse-engineering-ticketmasters-barcode-system.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2024%2F07%2Freverse-engineering-ticketmasters-barcode-system.html "Login")

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

[← On the CSRB’s Non-Investigation of the SolarWinds Attack](https://www.schneier.com/blog/archives/2024/07/on-the-csrbs-non-investigation-of-the-solarwinds-attack.html) [RADIUS Vulnerability →](https://www.schneier.com/blog/archives/2024/07/radius-vulnerability.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [Spying on People Through Airportr Luggage Delivery Service](https://www.schneier.com/blog/archives/2025/08/spying-on-people-through-airportr-luggage-delivery-service.html)
* [Aeroflot Hacked](http...