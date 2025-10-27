---
title: Attack Techniques: Encrypted Archives
url: https://textslashplain.com/2024/10/02/attack-techniques-encrypted-archives/
source: text/plain
date: 2024-10-03
fetch_date: 2025-10-06T18:52:44.251725
---

# Attack Techniques: Encrypted Archives

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Encrypted Archives

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-10-022024-10-02](https://textslashplain.com/2024/10/02/attack-techniques-encrypted-archives/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [malware](https://textslashplain.com/tag/malware/), [SmartScreen](https://textslashplain.com/tag/smartscreen/), [zip](https://textslashplain.com/tag/zip/)

Tricking a user into downloading and opening malware is a common attack technique, and defenders have introduced security scanners to many layers of the ecosystem in an attempt to combat the technique:

* Web hosting providers may scan files served from their infrastructure.
* Network gateways and proxies may scan files in transit from server to client.
* Email web apps may scan files when received as attachments.
* Client download managers scan files as they’re downloaded from the internet.
* Client AV and OS security features scan downloaded files as they’re stored on disk or opened.

With all this scanning in place, attackers have great incentives to try to prevent their malicious code from detection up until the moment that a user is infected.

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-4.png?w=437)](https://textslashplain.com/wp-content/uploads/2024/10/image-4.png)

One technique attackers use to avoid getting blocked is delivering the malware inside an archive: for example, using a `.zip`, `.rar`, or `.7z` file. Unfortunately for attackers, defenders long ago caught on to this technique and enhanced scanners to peek inside archives. For example, if you download a `.zip` file in Chrome or Edge, the browser will decompress the archive file and scan the files within it using SafeBrowsing or SmartScreen. Client AV software will scan inside archives on disk, etc.

Attackers were forced to take another step — encrypting the archive using a password that they share with the user.

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-3.png?w=561)](https://textslashplain.com/wp-content/uploads/2024/10/image-3.png)

Requiring that the end-user type a password to get at the malicious content adds some friction– users might not understand how to do so, or might get suspicious if this isn’t something they’re used to doing. However, the tradeoff is that many of the security scanners (at the web host, gateway, and download manager) will not be able to peek inside the archive1 to hunt out malicious content. Only security scanners run after the archive’s content is extracted will have the opportunity to block the malware.

This attack works best when the attacker has established some pretext for the file being encrypted; e.g. claiming that it contains private content like financial records, [a “free trial” of a paid app](https://x.com/josephfcox/status/1841464839123730446/photo/2), or other types of illegal programs like [keygen/cracking software](https://x.com/ericlaw/status/1841148596491862114).

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-2.png?w=575)](https://textslashplain.com/wp-content/uploads/2024/10/image-2.png)

<https://www.404media.co/a-network-of-ai-nudify-sites-are-a-front-for-notorious-russian-hackers-2/>

This same encryption technique is sometimes used to [hide URLs](https://textslashplain.com/2023/08/18/attack-techniques-qr-codes/#:~:text=attackers%20try%20to-,hide%20URLs,-%2C%20using%20techniques%20like) used in phishing attacks: The attacker sends the user a phishing link inside an encrypted PDF or ZIP file, and thereby scanners that would ordinarily block the phishing link are blinded.

What can a security administrator do to combat this threat vector?

First, help your users understand that encrypted archives are inherently more risky than average. Consider blocking or quarantining encrypted archives, or enable prompting the user for the password if your security software supports the [option](https://chromeenterprise.google/policies/#SafeBrowsingDeepScanningEnabled). Ensure that your users exclusively use archive extraction software that [correctly propagates the Mark-of-the-Web](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/#:~:text=Origin%2DLaundering%20via%20Archives), so that client security software is able to detect files extracted from archives that originated from untrusted sources.

Stay safe out there!

-Eric

1 In rare cases, a security program *might* be able to decrypt the archive (if it uses an extremely common password, or if it’s configured to detect the password in an email message or download page) but this is, to the best of my knowledge, *extremely* uncommon.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2024/10/02/attack-techniques-encrypted-archives/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2024/10/02/attack-techniques-encrypted-archives/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-10-022024-10-02](https://textslashplain.com/2024/10/02/attack-techniques-encrypted-archives/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [malware](https://textslashplain.com/tag/malware/), [SmartScreen](https://textslashplain.com/tag/smartscreen/), [zip](https://textslashplain.com/tag/zip/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Welcome to Fall, I guess?](https://textslashplain.com/2024/09/16/welcome-to-fall-i-guess/)

[Next Post Next post:
Content-Blocking in Manifest v3](https://textslashplain.com/2024/10/13/content-blocking-in-manifest-v3/)

### Leave a comment [Cancel reply](/2024/10/02/attack-techniques-encrypted-archives/#respond)

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

* 2,396,650 hits

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
[A WordPress.com Website](https://wordpres...