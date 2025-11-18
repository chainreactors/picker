---
title: Decoding Binary Numeric Expressions, (Mon, Nov 17th)
url: https://isc.sans.edu/diary/rss/32490
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-17
fetch_date: 2025-11-18T03:15:17.300783
---

# Decoding Binary Numeric Expressions, (Mon, Nov 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32488)
* [next](/diary/32492)

# [Decoding Binary Numeric Expressions](/forums/diary/Decoding%2BBinary%2BNumeric%2BExpressions/32490/)

**Published**: 2025-11-17. **Last Updated**: 2025-11-17 07:18:53 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Decoding%2BBinary%2BNumeric%2BExpressions/32490/#comments)

In diary entry "[Formbook Delivered Through Multiple Scripts](https://isc.sans.edu/diary/Formbook%20Delivered%20Through%20Multiple%20Scripts/32480)", Xavier mentions that the following line:

```

Nestlers= array(79+1,79,80+7,60+9,82,83,72,69,76,76)
```

decodes to the string POWERSHELL.

My tool [numbers-to-hex.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/numbers-to-hex.py) is a tool that extracts numbers from text files, and converts them to hexadecimal.

Like this:

![](data:image/png;base64...)

I can then use another tool, [hex-to-bin.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/hex-to-bin.py) to convert the hexadecimal numbers to binary, and then we see this string:

![](data:image/png;base64...)

This string is not exactly the string POWERSHELL, but we can see parts of it.

The reason the decoding fails, is because of binary numeric expressions like this one: 79+1

My tool numbers-to-hex.py does not recognize binary numeric expressions like 79+1, it just recognizes two numbers: 79 and 1.

79 converted to hexadecimal is 4f, and 1 converted to hexadecimal is 01.

Those hex numbers converted to ASCII give O (4f) and a smiley (01).

So Xavier's example inspired me to update my tool, so that it can also handle binary numeric expressions (binary here means that the operator, + in our example, takes 2 operands).

You enable this mode with option -e:

![](data:image/png;base64...)

So this time, 79+1 is converted to 50 hexadecimal.

And this properly decodes this obfuscated string:

![](data:image/png;base64...)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Decoding%2BBinary%2BNumeric%2BExpressions/32490/#comments)

* [previous](/diary/32488)
* [next](/diary/32492)

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