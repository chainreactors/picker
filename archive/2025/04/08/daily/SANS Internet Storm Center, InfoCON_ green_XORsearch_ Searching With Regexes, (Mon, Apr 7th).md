---
title: XORsearch: Searching With Regexes, (Mon, Apr 7th)
url: https://isc.sans.edu/diary/rss/31834
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-08
fetch_date: 2025-10-06T22:08:40.716106
---

# XORsearch: Searching With Regexes, (Mon, Apr 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31830)
* [next](/diary/31838)

# [XORsearch: Searching With Regexes](/forums/diary/XORsearch%2BSearching%2BWith%2BRegexes/31834/)

**Published**: 2025-04-07. **Last Updated**: 2025-04-07 12:34:56 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/XORsearch%2BSearching%2BWith%2BRegexes/31834/#comments)

Xavier asked me a question from one of his FOR610 students: "how can you perform a regex search with XORsearch"?

[XORsearch](https://blog.didierstevens.com/programs/xorsearch/) is a tool like grep but it performs a brute-force attack on the input file, trying out different encodings like XOR.

You can give it a string to search for, but not a regular expression.

There is a work around however: let XORsearch extract all possible strings, and then use a regular expression to grep through the results.

Here is an example with a Cobalt Strike beacon:

![](https://isc.sans.edu/diaryimages/images/20250407-142435.png)

Option -S instructs XORsearch to extract all ASCII strings, and re-search.py is used with its built-in regular expression for IPv4 address.

We obtain one address, that we then use directly with XORsearch:

![](https://isc.sans.edu/diaryimages/images/20250407-142511.png)

This gives us more information: we see a URL path, and we know the encoding is XOR, and the key is 0x0D.

With option -n, we can look for even more info surrounding that IPv4 address:

![](https://isc.sans.edu/diaryimages/images/20250407-142614.png)

There also a method using YARA rules, but for that I need to publish a Python version of xorsearch first. More details in an upcoming diary entry.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/XORsearch%2BSearching%2BWith%2BRegexes/31834/#comments)

* [previous](/diary/31830)
* [next](/diary/31838)

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