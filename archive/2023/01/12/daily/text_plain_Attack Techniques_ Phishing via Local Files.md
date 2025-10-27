---
title: Attack Techniques: Phishing via Local Files
url: https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/
source: text/plain
date: 2023-01-12
fetch_date: 2025-10-04T03:39:35.449019
---

# Attack Techniques: Phishing via Local Files

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Phishing via Local Files

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-112025-04-30](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[authentication](https://textslashplain.com/tag/authentication/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [Passkeys](https://textslashplain.com/tag/passkeys/), [passwords](https://textslashplain.com/tag/passwords/), [phishing](https://textslashplain.com/tag/phishing/)

One attack technique I’ve seen in use recently involves enticing the victim to enter their password into a locally-downloaded HTML file.

The attack begins by the victim receiving an email **lure** with a HTML file attachment (for me, often with the `.shtml` file extension):

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-17.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-17.png)

When the user opens the file, a HTML-based **credential prompt** is displayed, with the attacker hoping that the user won’t notice that the prompt isn’t coming from the legitimate logon provider’s website:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-18.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-18.png)

Fake Excel file

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-52.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-52.png)

Fake Word Document

Notably, because the HTML file is opened locally, the URL refers to a file path on the local computer, and as a consequence the local `file://` URL will not have any reputation in anti-phishing services like Windows SmartScreen or Google Safe Browsing.

A HTML form within the **lure** file targets a credential **recording endpoint** on infrastructure which the attacker has either rented or compromised on a legitimate site:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-21.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-21.png)

If the victim is successfully tricked into supplying their password, the data is sent in a HTTP `POST` request to the recording endpoint:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-20.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-20.png)

Sometimes the recording endpoint is a webserver rented by the attacker. Sometimes, it’s a webserver that’s been compromised by a hack. Sometimes, it’s an endpoint run by a legitimate “Software as a Service” [like FormSpree](https://twitter.com/ericlaw/status/1637956850636161025) that has a scammer as a customer. And, sometimes, the endpoint is a legitimate web API [like Telegram](https://twitter.com/ericlaw/status/1631334761082888199), where the attacker is on the other end of the connection:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-53.png?w=928)](https://textslashplain.com/wp-content/uploads/2023/01/image-53.png)

To help prevent the user from recognizing that they’ve just been phished, the attacker then redirects the victim’s browser to an unrelated error page on the legitimate login provider:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-19.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-19.png)

The attacker can later collect the database of submitted credentials from the collection endpoint at their leisure.

Passwords are a terrible legacy technology, and now that [viable alternatives now exist](https://textslashplain.com/2022/08/05/passkeys/), sites and services should strive to eliminate passwords as soon as possible.

-Eric

PS: The Local HTML File attack vector can also be used to [smuggle malicious downloads](https://www.microsoft.com/en-us/security/blog/2021/11/11/html-smuggling-surges-highly-evasive-loader-technique-increasingly-used-in-banking-malware-targeted-attacks/) past an organization’s firewall/proxy. JavaScript in the HTML page can [generate a file](https://textslashplain.com/2018/08/06/script-generated-download-files/) and hand it to the download manager to write to disk.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-112025-04-30](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[authentication](https://textslashplain.com/tag/authentication/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [Passkeys](https://textslashplain.com/tag/passkeys/), [passwords](https://textslashplain.com/tag/passwords/), [phishing](https://textslashplain.com/tag/phishing/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
ProjectK.commit()](https://textslashplain.com/2022/12/17/projectk-commit/)

[Next Post Next post:
Attack Techniques: Phishing via Mailto](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-mailto/)

### Leave a comment [Cancel reply](/2023/01/11/attack-techniques-phishing-via-local-files/#respond)

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

* [Comment](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 264 other subscribers

  Sign me up

  +...