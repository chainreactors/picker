---
title: Attack Techniques: Phishing via Mailto
url: https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/
source: text/plain
date: 2023-01-12
fetch_date: 2025-10-04T03:39:34.415065
---

# Attack Techniques: Phishing via Mailto

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Phishing via Mailto

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-11](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/), [security](https://textslashplain.com/tag/security/)

Earlier today, we looked at a technique where a phisher serves his [attack from the user’s own computer](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/) so that anti-phishing code like SmartScreen and SafeBrowsing do not have a meaningful URL to block.

A similar technique is to encode the attack within a `mailto` URL, because anti-phishing scanners and email clients rarely apply reputation intelligence to the addressee of outbound email.

In this attack, the phisher’s lure email contains a link which points at a URL that uses the `mailto:` scheme to construct a reply email:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-22.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-22.png)

A victim who falls for this attack and clicks the link will find that their email client opens with a new message with a subject of the attacker’s choice, addressed to the attacker, possibly containing pre-populated body text that requests personal information. Alternatively, the user might just respond by sending a message saying “*Hey, please protect me*” or the like, and the attacker, upon receipt of the reply email, can then socially-engineer personal information out of the victim in subsequent replies.

The even lazier variant of this attack is to simply email the victim directly and request that they provide all of their personal information in a reply:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-23.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-23.png)

While this version of the attack feels even less believable, victims *[still](https://www.cnbc.com/2019/04/18/nigerian-prince-scams-still-rake-in-over-700000-dollars-a-year.html)* fall for the scam, and there are even [logical reasons](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/WhyFromNigeria.pdf) for scammers to target only the most credulous victims.

Notably, while mail-based attacks *might* solicit the user’s credentials information, they might not even bother, instead directly asking for other monetizable information like credit card or banking numbers.

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-11](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/), [security](https://textslashplain.com/tag/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Attack Techniques: Phishing via Local Files](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/)

[Next Post Next post:
Attack Techniques: Priming Attacks on Legitimate Sites](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/)

### Leave a comment [Cancel reply](/2023/01/11/attack-techniques-phishing-via-mailto/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscribe to Posts") [RSS - Posts](https://textslashplain.com/feed/ "Subscribe to Posts")

## Blog Stats

* 2,396,348 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browsers  (183)
design  (21)
dev  (84)
fiddler  (25)
life  (52)
perf  (20)
politics  (2)
privacy  (26)
reviews  (2)
running  (18)
security  (158)
storytelling  (47)
tech  (34)
travel  (9)
Uncategorized  (16)
web  (151)
windmills  (12)

![ericlaw](https://2.gravatar.com/avatar/89c27d27b73dd3690b3dad59f3a539d1?s=320)

#### [ericlaw](https://gravatar.com/ericlaw1979)

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity.

[View Full Profile →](https://gravatar.com/ericlaw1979)

[text/plain](https://textslashplain.com/),
[A WordPress.com Website](https://wordpress.com/?ref=footer_custom_acom).

* [Comment](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 264 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2023%252F01%252F11%252Fattack-techniques-phishing-via-mailto%252F)
* + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2023%252F01%252F11%252Fattack-techniques-phishing-via-mailto%252F)
  + [Copy shortlink](https://wp.me/p60i9o-1MX)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/)
  + [View post in Reader](https://wordpress.com/reader/blogs/88727790/posts/6879)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

##

##

Loading Comments...

Write a Comment...

Email (Required)

Name (Required)

Website

###

%d

![](https://pixel.wp.com/b.gif?v=noscript)