---
title: User Agent Strings Curiosities, (Sun, Oct 4th)
url: https://isc.sans.edu/diary/rss/33394
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-04
fetch_date: 2026-10-05T07:57:33.704868
---

# User Agent Strings Curiosities, (Sun, Oct 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33392)
* [next](/diary/33396)

Click HERE to learn more about classes Didier is teaching for SANS

# [User Agent Strings Curiosities](/forums/diary/User%2BAgent%2BStrings%2BCuriosities/33394/)

**Published**: 2026-10-04. **Last Updated**: 2026-10-04 07:58:51 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/User%2BAgent%2BStrings%2BCuriosities/33394/#comments)

Sometimes I have to smile, or my interest is triggered, when I review new User Agent Strings in the honeypot logs.

Like when I see an "authorized" scan:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-45-29.png)

Or when I'm owned for the umpteenth time:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-43-50.png)

I regularly see URLs or email addresses for when you want to know more, or get in touch, with the persons behind a scanner:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-50-13.png)

(around the end of this list, you'll see the Belarus email address we [wrote about recently](https://isc.sans.edu/diary/HELPMEESCAPEFROMBELARUSPLEASE%2BGuest%2BDiary/33130))

Many variants of masscan:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-54-10.png)

Even a KGB variant.

As you can guess, "scan" is a popular word to include in your UAS:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-57-47.png)

And some wordplays are thrown in:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-03-28.png)

And they do not shy away from discrediting:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-01-45.png)

Sometime complete lists of User Agent Strings are used: the scanner will select a new UAS for each request. They don't always sanitize these list, as you can see with these weird "User Agent Strings":

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-07-45.png)

These lines actually appear in [this repository of User Agent Strings](https://gist.github.com/alexanderldavis/93e5c8dc779dfb27b835ec98bebca0cd), to separate them in groups:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-12-18.png)
And because of a lack of quality control, these separator lines also get used as UAS in a request.

Of course, there are also attempts to exploit the parsing of a User Agent String. Shellshock may be more than 10 years old, I still see it in User Agent Strings:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-15-14.png)

And sometimes I think: "Huh, are they scanning for this too?". Like the last one:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-21-26.png)

Scanning for servers that stream GPS correction data via the [NTRIP protocol](https://en.wikipedia.org/wiki/Networked_Transport_of_RTCM_via_Internet_Protocol) (a NTRIP header was also included in this request).

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/User%2BAgent%2BStrings%2BCuriosities/33394/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33392)
* [next](/diary/33396)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)