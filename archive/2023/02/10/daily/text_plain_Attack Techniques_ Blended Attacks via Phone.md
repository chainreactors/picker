---
title: Attack Techniques: Blended Attacks via Phone
url: https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/
source: text/plain
date: 2023-02-10
fetch_date: 2025-10-04T06:13:45.558582
---

# Attack Techniques: Blended Attacks via Phone

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Blended Attacks via Telephone

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-02-092024-06-05](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/)

Last month, we looked at [a technique](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/) where a phisher serves his attack from the user’s own computer so that anti-phishing code like SmartScreen and SafeBrowsing do not have a meaningful URL to block.

Another approach for conducting an attack like this is to send a lure which demands that the victim complete the attack out-of-band using a telephone. Because the data theft is not conducted over the web, URL reputation systems don’t have anything to block.

Here’s an example of such a scam, which falsely claims that the user was charged $400 for one of the free programs already on their PC:

[![](https://textslashplain.com/wp-content/uploads/2023/02/image-2.png?w=793)](https://textslashplain.com/wp-content/uploads/2023/02/image-2.png)

The attacker hopes that the user, upon seeing this charge, will call the phone number within the email and get tricked into supplying sensitive information. This particular scam’s phone number is routed to a call center purporting to be “Microsoft Support.” Unfortunately, some legitimate companies like [PayPal will send fake invoices on behalf of the attackers](https://textslashplain.com/2024/06/05/attack-techniques-paypal-invoice-scams/) so that your email program may trust the sender.

Another common form of the phone attack is called a [tech support scam](https://consumer.ftc.gov/articles/how-spot-avoid-and-report-tech-support-scams#Spotting), and involves an ad or website that attempts to convince the user that their computer has a problem:

[![](https://textslashplain.com/wp-content/uploads/2023/04/image.png?w=628)](https://textslashplain.com/wp-content/uploads/2023/04/image.png)

Evidence suggests that some email services have gotten wise to telephone-backed scams: because the phone number needs only be read by a human, attackers may try to evade detection and blocking by encoding their phone numbers using non-digit characters or irregular formatting, as in this lure:

[![](https://textslashplain.com/wp-content/uploads/2023/02/image-3.png?w=883)](https://textslashplain.com/wp-content/uploads/2023/02/image-3.png)

…or by embedding the phone number inside an image, like this lure:

[![](https://textslashplain.com/wp-content/uploads/2023/02/image-4.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/02/image-4.png)

Unfortunately, relatively few phones offer any mechanism for warning the user when they’re calling a known-scam number — Google’s “Scam Likely” warnings only seem to show on the Pixel for *inbound calls*. As with traditional phishing attacks, bad actors can usually switch their infrastructure (rental call centers, [Twilio VoIP](https://twitter.com/mdhardeman/status/1643254912568926210), etc) easily after they are blocked.

Stay safe out there!

-Eric

PS: Sometimes this attack technique is lumped in with [vishing](https://en.wikipedia.org/wiki/Voice_phishing), but I tend to think of vishing as an attack in which the initial lure arrives via a phone call or voicemail.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-02-092024-06-05](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
A New Era: PM -> SWE](https://textslashplain.com/2023/02/06/a-new-era-pm-swe/)

[Next Post Next post:
Q: “Remember this Device, Doesn’t?!?”](https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/)

### Leave a comment [Cancel reply](/2023/02/09/attack-techniques-blended-attacks-via-phone/#respond)

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

* 2,392,799 hits

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

* [Comment](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 264 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2023%252F02%252F09%252Fattack-techniques-blended-attacks-via-phone%252F)
* + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2023%252F02%252F09%252Fattack-techniques-blended-attacks-via-phone%252F)
  + [Copy shortlink](https://wp.me/p60i9o-1R2)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/)
  + [Vi...