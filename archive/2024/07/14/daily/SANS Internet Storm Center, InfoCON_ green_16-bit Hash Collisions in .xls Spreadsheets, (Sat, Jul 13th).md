---
title: 16-bit Hash Collisions in .xls Spreadsheets, (Sat, Jul 13th)
url: https://isc.sans.edu/diary/rss/31066
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-14
fetch_date: 2025-10-06T17:41:32.078505
---

# 16-bit Hash Collisions in .xls Spreadsheets, (Sat, Jul 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31064)
* [next](/diary/31068)

# [16-bit Hash Collisions in .xls Spreadsheets](/forums/diary/16bit%2BHash%2BCollisions%2Bin%2Bxls%2BSpreadsheets/31066/)

**Published**: 2024-07-13. **Last Updated**: 2024-07-13 06:19:07 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/16bit%2BHash%2BCollisions%2Bin%2Bxls%2BSpreadsheets/31066/#comments)

A couple years ago, in diary entry "[Unprotecting Malicious Documents For Inspection](https://isc.sans.edu/diary/Unprotecting%2BMalicious%2BDocuments%2BFor%2BInspection/27126)" I explain how .xls spreadsheets are password protected (but not encrypted). And in follow-up diary entry "[Maldocs: Protection Passwords](https://isc.sans.edu/diary/Maldocs%2BProtection%2BPasswords/27146)", I talk about an update to my oledump plugin [plugin\_biff.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/plugin_biff.py) to crack these passwords using password lists (by default, an embedded password list is used that is taken from the [2011 public-domain default password list used by John The Ripper](https://github.com/openwall/john/blob/c1ce5775c3022217b1a414bba764ae405e82a443/run/password.lst)).

Since the hashing algorithm used for the protection of .xls files produces a 16-bit integer with its highest bit set, there are 32768 (0x8000) possible hash values (called verifier), and thus ample chance to generate hash collisions.

I generated such a list, and included it in an update of my oledump plugin plugin\_biff.py:

![](https://isc.sans.edu/diaryimages/images/20240711-220327.png)

I took care to generate passwords prioritizing letters and digits over special characters.

Here is an example of a .xls workbook with a protected sheet. The protection password I used for this sheet is azeqsdwxc, a weak password that is not in the embedded list. Thus this password is not found in the password list when plugin plugin\_biff.py attempts to crack it:

![](https://isc.sans.edu/diaryimages/images/20240711-215850.png)

With previous versions of plugin plugin\_biff.py, the report would state that the password was not cracked. But in this new version, when a password can not be cracked with the embedded or provided password list, the password is taken from the embedded verifier table. In this case, that password is bbbbhz (the verifier is 0xd9b1).

This means that both password azeqsdwxc and bbbbhz hash to the same value: verifier 0xd9b1.

And thus that the sheet can also be unprotected with password bbbbhz too:

![](https://isc.sans.edu/diaryimages/images/20240711-215255.png)

So with this new version of oledump plugin plugin\_biff.py, a password will always be provided for protected .xls files, whatever the value of the verifier.

Of course, this is only useful if you don't want or can't alter the sheet to remove the protection. Since these passwords just offer protection, and are not actually used to encrypt, it's possible to remove the protection without knowing the password, as I explained in my blog post "[Quickpost: oledump.py plugin\_biff.py: Remove Sheet Protection From Spreadsheets](https://blog.didierstevens.com/2021/02/12/quickpost-oledump-py-plugin_biff-py-remove-sheet-protection-from-spreadsheets/)".

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [cracking](/tag.html?tag=cracking) [password](/tag.html?tag=password) [excel](/tag.html?tag=excel)

[0 comment(s)](/diary/16bit%2BHash%2BCollisions%2Bin%2Bxls%2BSpreadsheets/31066/#comments)

* [previous](/diary/31064)
* [next](/diary/31068)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)