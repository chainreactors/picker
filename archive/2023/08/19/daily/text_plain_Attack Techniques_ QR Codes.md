---
title: Attack Techniques: QR Codes
url: https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/
source: text/plain
date: 2023-08-19
fetch_date: 2025-10-04T12:00:17.944091
---

# Attack Techniques: QR Codes

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: QR Codes

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-08-182023-12-15](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/)

As outlined in [earlier posts in this series](https://textslashplain.com/tag/infosecttp/), attackers know that security software can detect their phishing lures and block users from even *seeing* the lure if it contains a known-phishing URL. For example, both Windows Live and Gmail block email that is believed to contain phishing links. If your enterprise uses Microsoft Defender for Office, or you subscribe to Microsoft 365 Family, all inbound hyperlinks through Microsoft email services are rewritten to navigate through the “SafeLinks” service that performs another real-time check for malicious URLs whenever a user clicks on them.

To avoid security software, attackers try to **hide URLs**, using techniques like asking the user to retype URLs from an image, or sticking the link inside a password-protected PDF document, or **avoid URLs** by asking the user to [call a phone number](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/) or [send a reply email](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/) containing sensitive information.

Another technique is to send the user a QR Code. A QR Code is simply a picture that can be converted into the URL using the camera app on our now-ubiquitous mobile phones.

[![](https://textslashplain.com/wp-content/uploads/2023/08/image-18.png?w=194)](https://textslashplain.com/wp-content/uploads/2023/08/image-18.png)

This QR Code points to a blog post

Users are increasingly accustomed to using QR Codes for legitimate purposes, so their use in attack scenarios won’t stand out as much as it once would have.

How does this URL-obfuscation technique benefit an attacker over a plain hyperlink?

* Mail software can’t rewrite QR codes, so features like Microsoft SafeLinks won’t apply.
* The use of a QR Code allows an attacker to **cause the attack flow to move** from a well-protected desktop to a less-protected mobile device.

  For example, users might be using a mobile web browser with weaker real-time anti-phishing reputation services than the browser on their desktop.

  That mobile browser may not be configured to proxy traffic through a secure proxy.

  Similarly, a user’s personal device might not include a password manager, making the attacker’s request for manually-typed credentials more plausible.

Someone recently tried to [phish a Microsoft CTO](https://twitter.com/markrussinovich/status/1708913408912118228) via this approach:

[![](https://textslashplain.com/wp-content/uploads/2023/10/image.png?w=813)](https://textslashplain.com/wp-content/uploads/2023/10/image.png)

Here’s a news article about a [recent attack using the QR Code vector](https://www.bleepingcomputer.com/news/security/major-us-energy-org-targeted-in-qr-code-phishing-attack/).

**Update:** In December 2023, the Microsoft Defender for Office 365 team outlined some of their [protections against QR code phishing](https://techcommunity.microsoft.com/t5/microsoft-defender-for-office/protect-your-organizations-against-qr-code-phishing-with/ba-p/4007041).

Stay safe out there — treat any QR codes received via SMS or email with extra caution. Carefully examine the url in any preview your camera app offers **and** check the browser’s address bar to see the **final URL**, because [open redirectors](https://textslashplain.com/2023/03/16/attack-techniques-open-redirectors-captchas-site-proxies-and-ipfs-oh-my/) are common, so the preview URL may be misleading.

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-08-182023-12-15](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:](https://textslashplain.com/2023/08/14/enforcing-smartscreen-with-policy/)

[Next Post Next post:](https://textslashplain.com/2023/08/23/kilimanjaro-coffee-tour/)

## 2 thoughts on “Attack Techniques: QR Codes”

1. ![Tim's avatar](https://0.gravatar.com/avatar/30666246b8eefee56403d70c19f8c6529298223a882171610d84dd2de92d0a96?s=32&d=identicon&r=G) **Tim** says:

   [2023-08-18 at 11:27](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/#comment-36466)

   I can’t believe that the iPhone has no url preview for scanned QR codes – it just opens them. You would really hope the big companies were more on top of these attack vectors.

   [Reply](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/?replytocom=36466#respond)

   1. ![ericlaw's avatar](https://1.gravatar.com/avatar/48ccad455b21f90ad0bcfbbf3826c12a0d744a22409a4005756c19f4efdaa057?s=32&d=identicon&r=G) **[ericlaw](https://textplain.wordpress.com)** says:

      [2023-08-18 at 14:13](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/#comment-36474)

      In fairness to Apple, the original URL could easily be misleading (Google, Bing, LinkedIn, etc, all run effectively open-redirectors), so the “preview” itself could be misleading.

      [Reply](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/?replytocom=36474#respond)

### Leave a comment [Cancel reply](/2023/08/18/attack-techniques-qr-codes/#respond)

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

* 2,392,548 hits

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
[A WordPress.com Website](https://wordpress.com/?ref=f...