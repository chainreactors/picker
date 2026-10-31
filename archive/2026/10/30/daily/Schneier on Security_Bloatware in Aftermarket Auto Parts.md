---
title: Bloatware in Aftermarket Auto Parts
url: https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html
source: Schneier on Security
date: 2026-10-30
fetch_date: 2026-10-31T07:48:45.544816
---

# Bloatware in Aftermarket Auto Parts

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

## Bloatware in Aftermarket Auto Parts

This [story](https://www.thedrive.com/news/cheap-aftermarket-head-units-are-loaded-with-spyware-by-the-way) is interesting:

> One Civic owner purchased a cheap aftermarket head unit off Amazon, and decided to have Claude work its magic on it, like it would a smart TV. What was reportedly discovered isn’t surprising, but is worth knowing about.
>
> Among the pre-installed bloatware—­or spyware, if you’re being less charitable­—was a voice assistant equipped with WebView, an Android system component that lets apps display content off the web. This apparently always used about a third of processing power, even while idle, which isn’t great. There were also Baidu location services, a call recorder (!), a DAB radio client that is pretty much useless in the U.S., and Adobe Acrobat, presumably so your passenger can entertain themselves with PDFs on the go.

It’s interesting because it exposes all the insecurities in this piece of IoT software. But I think the real story is that a random person was able to do this reverse-engineering with the help of AI. Expect a lot more stories like this in the future.

Tags: [AI](https://www.schneier.com/tag/ai/), [cars](https://www.schneier.com/tag/cars/), [Internet of Things](https://www.schneier.com/tag/internet-of-things/), [spyware](https://www.schneier.com/tag/spyware/)

[Posted on October 30, 2026 at 11:20 AM](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html#comments)

### Comments

Rontea •
[October 30, 2026 1:06 PM](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html/#comment-459359)

Cheap aftermarket devices—especially ones running Android variants—are the definition of untrusted hardware. They’re loaded with services and apps you didn’t ask for, phone home to places you don’t control, and often keep running even when you think they’re idle.

Stick to reputable vendors, keep them segmented, and if you must tinker, know exactly what firmware you’re flashing and where it came from. Trust is earned, not assumed.

lurker •
[October 30, 2026 1:14 PM](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html/#comment-459360)

What’s wrong with a call recorder? Perhaps (the article didn’t say) it’s always on, with no off switch. But either party to a call should be able to record the call at will, and the other party **must** be automatically advised of that fact.

As the article concluded this stuff was made for a very different marketplace. *Caveat emptor.*

freedom •
[October 30, 2026 1:20 PM](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html/#comment-459361)

> a random person was able to do this reverse-engineering

The “random person” did not do any “reverse engineering” at all.

The “random person” knows exactly nothing about computer security, thus he can’t do any “reverse engineering” at all. The “random person” asked a CIA-NSA-chatbot a meaningless question and the CIA chatbot produced a bunch of propaganda.

Maybe this “random person” should use the “claude” CIA chatbot to “reverse engineering” the “claude” CIA chatbot itself? That should me marginally more entertaining.

DBA •
[October 30, 2026 1:43 PM](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html/#comment-459362)

Very interesting. His entire process took him about two hours to debloat the head after connecting his laptop to the head unit via WiFi, and he disabled remote updates and connections, except through his laptop via the USB port. And to maintain access, he configured a USB key that could access the USB port in the event the laptop failed.

Pretty neat.

The article links to a Reddit post here:
<https://www.reddit.com/r/ClaudeCode/comments/1xf2lur/i_pointed_claude_code_at_the_cheap_chinese_head/>

I replaced my Subaru’s stereo a few years ago with a JVC/Kenwood to get a better Apple Play system. This makes me wonder what I’d find if I attempted the same thing.

Jeremy Nimmo •
[October 30, 2026 7:51 PM](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html/#comment-459366)

Absolutely idiotic commentary.

An Android device from China came with a combination of:
1) Standard Android AOSP software
2) Superior Chinese alternatives to Google services, which make sure that:
2a) The device doesn’t carry the premium that it would to be ‘endorsed’ by the psychopathic blood drenched freaks at Google
2b) Users have vastly more privacy than they would using Google location services. Ever heard of people in the US being persecuted because they got caught up in a Baidu ‘geofence warrant’? That’s right, you haven’t, because that’s a GOOGLE problem, the Chinese alternatives are far, far better

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/10/bloatware-in-aftermarket-auto-parts.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F10%2Fbloatware-in-aftermarket-auto-parts.html "Login")

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

[← Studying Fraudulent North Korean IT Workers](https://www.schneier.com/blog/archives/2026/10/studying-fraudulent-north-korean-it-workers.html) [Friday Squid Blogging: Bigfin Squid Off California Coast →](https://www.schneier.com/blog/archives/2026/10/friday-squid-blogging-bigfin-squid-off-california-coast.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersecti...