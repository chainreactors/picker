---
title: Mass Ransomware Attack
url: https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html
source: Schneier on Security
date: 2023-03-24
fetch_date: 2025-10-04T10:34:00.787249
---

# Mass Ransomware Attack

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

## Mass Ransomware Attack

A vulnerability in a popular data transfer tool has resulted in a [mass ransomware attack](https://techcrunch.com/2023/03/22/fortra-goanywhere-ransomware-attack/):

> TechCrunch has learned of dozens of organizations that used the affected GoAnywhere file transfer software at the time of the ransomware attack, suggesting more victims are likely to come forward.
>
> However, while the number of victims of the mass-hack is widening, the known impact is murky at best.
>
> Since the attack in late January or early February—the exact date is not known—Clop has disclosed less than half of the 130 organizations it claimed to have compromised via GoAnywhere, a system that can be hosted in the cloud or on an organization’s network that allows companies to securely transfer huge sets of data and other large files.

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [hacking](https://www.schneier.com/tag/hacking/), [ransomware](https://www.schneier.com/tag/ransomware/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on March 23, 2023 at 7:05 AM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html) •
[6 Comments](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html#comments)

### Comments

[Lawrence](http://tech.dolhub.com) •
[March 23, 2023 12:17 PM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/#comment-419732)

“GoAnywhere, a system that can be hosted in the cloud or on an organization’s network that allows companies to securely transfer huge sets of data and other large files”

Apparently not so “securely”. 😉

1&1~=Umm •
[March 23, 2023 1:18 PM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/#comment-419733)

One known target is Hitachi,

<https://www.techradar.com/news/hitachi-energy-confirms-data-breach-after-being-hit-by-clop-ransomware>

Both their Bank and energy sub corporates.

RealFakeNews •
[March 23, 2023 7:21 PM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/#comment-419738)

Wait…so self-hosted instances that should be operating behind firewalls/authentication systems, were just “compromised” en-mass?

Self-hosted instances “phoning home”/backdoored?

The question I’d ask is: was it written for this purpose?

HoKnowz •
[March 24, 2023 9:28 AM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/#comment-419756)

@RealFakeNews

> The question I’d ask is: was it written for this purpose?

Or an inside job at that company, anyway. From the looks of it.

Andrew •
[March 24, 2023 2:09 PM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/#comment-419767)

This application is routinely located in the DMZ. A zero day flaw reportedly was exploited to enable unauthorized access. Like with user VPN concentrators and web apps and APIs in general, software on the public internet that act as a gateway to data or the network will be targeted. My understanding is that both client deployed and the vendor hosted services were (are, if still not patched) vulnerable.

Ideally access to these services from the public internet will be as narrow as possible, with access limited to only whitelisted known business partners that you have contractual partnership to share data with allowed, as a minimum control. But like with user VPN the business may not know or be able to control the sources. Or equally likely they don’t justify/value or appreciate the importance here of least privilege.

No “back door” necessary when there is an exploitable flaw and access from the entire internet.

Minding biz •
[March 24, 2023 8:13 PM](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/#comment-419785)

It’s the same company that owns Cobalt Strike. Formerly Help Systems. They changed their name after Cobalt Strike repeatedly involved in ransomware attacks.

They call themselves a cybersecurity company.

They purchased 3 dozen companies in the last few years. Likely they have customers everywhere as a result. But most interesting is they recently purchased another red team tool company.

<https://www.itjungle.com/2022/10/05/helpsystems-goes-on-the-security-offensive-again/>

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2023/03/mass-ransomware-attack.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2023/03/mass-ransomware-attack.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2023%2F03%2Fmass-ransomware-attack.html "Login")

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

[← ChatGPT Privacy Flaw](https://www.schneier.com/blog/archives/2023/03/chatgpt-privacy-flaw.html) [Exploding USB Sticks →](https://www.schneier.com/blog/archives/2023/03/exploding-usb-sticks.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [Daniel Miessler on the AI Attack/Defense Balance](https://www.schneier.com/blog/archives/2025/10/daniel-miessler-on-the-ai-attack-defense-balance.html)
* [US Disrupts Massive Cell Phone Array in New York](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html)
* [Apple's New Memory Integrity Enforcement](https:/...