---
title: SSL 2.0 turns 30 this Sunday... Perhaps the time has come to let it die&#x3f;, (Fri, Feb 7th)
url: https://isc.sans.edu/diary/rss/31664
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-08
fetch_date: 2025-10-06T20:47:29.134528
---

# SSL 2.0 turns 30 this Sunday... Perhaps the time has come to let it die&#x3f;, (Fri, Feb 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31660)
* [next](/diary/31666)

# [SSL 2.0 turns 30 this Sunday... Perhaps the time has come to let it die?](/forums/diary/SSL%2B20%2Bturns%2B30%2Bthis%2BSunday%2BPerhaps%2Bthe%2Btime%2Bhas%2Bcome%2Bto%2Blet%2Bit%2Bdie/31664/)

**Published**: 2025-02-07. **Last Updated**: 2025-02-07 10:41:59 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[1 comment(s)](/diary/SSL%2B20%2Bturns%2B30%2Bthis%2BSunday%2BPerhaps%2Bthe%2Btime%2Bhas%2Bcome%2Bto%2Blet%2Bit%2Bdie/31664/#comments)

The SSL 2.0 protocol was originally published back in February of 1995[[1](https://datatracker.ietf.org/doc/html/rfc6176#ref-SSL2)], and although it was quickly found to have significant security weaknesses, and a more secure alternative was released only a year later[[2](https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0)], it still received a fairly wide adoption.

![](https://isc.sans.edu/diaryimages/images/25-02-07-trends.png)

Nevertheless, since it was officially deprecated nearly 14 years ago, in March of 2011[[3](https://en.wikipedia.org/wiki/Transport_Layer_Security#History_and_development)], and all newer IT systems subsequently lack support for it, one might reasonably expect that this outdated and insecure protocol would now be the stuff of legends more than something one might see in one’s daily life. Or – rather – while there are undoubtedly numerous legacy systems in existence that still support SSL 2.0, and even use it in the context of local networks, one would probably not expect to see large numbers of servers that still support this protocol exposed to the internet… Though, as we have discussed previously [[4](https://isc.sans.edu/diary/29908),[5](https://isc.sans.edu/diary/31550)], one would be wrong.

Still, since the aforementioned protocol will celebrate its 30th birthday this Sunday, I thought it might be worthwhile to take a closer look at how common it is at this point, and what systems still support it.

Going by the numbers from Shodan, at the time of writing, there still appear to be nearly 423 thousand public IP addresses, on which servers supporting SSL 2.0 are accessible on some port[[6](https://www.shodan.io/search?query=ssl.version%3Asslv2)].

Looking at the most common ports, we can see that the overwhelming majority of systems that still support the outdated protocol are almost certainly web servers, and that most of what remains seems to consist primarily of e-mail servers…

[![](https://isc.sans.edu/diaryimages/images/25-02-07-ports.png)](https://isc.sans.edu/diaryimages/images/25-02-07-ports.png)

If we look at the countries, where at least 1000 SSL 2.0-enabled servers appear to be located, we can see that only three countries together – the United States, Kazakhstan and Tunisia – host more than half of what is out there…

[![](https://isc.sans.edu/diaryimages/images/25-02-07-countries.png)](https://isc.sans.edu/diaryimages/images/25-02-07-countries.png)

We have discussed the situation at the top of the list – especially in Kazakhstan – previously[[7](https://isc.sans.edu/diary/29988)], and although the overall numbers are still certainly high, it seems worth mentioning that even in these countries, the numbers of SSL 2.0 enabled systems (at least web servers, as you can see in the following chart) has decreased significantly over the past two years…

[![](https://isc.sans.edu/diaryimages/images/25-02-07-kz-tn-us.png)](https://isc.sans.edu/diaryimages/images/25-02-07-kz-tn-us.png)

Since we are on the topic of changes in the number of servers that still support SSL 2.0, we should also look at how the overall global situation has evolved over time…

[![](https://isc.sans.edu/diaryimages/images/25-02-07-trends.png)](https://isc.sans.edu/diaryimages/images/25-02-07-trends.png)

As we can see, the rate of removal of SSL 2.0 enabled systems from the internet has significantly increased in approximately the last 3 months, which is quite fortunate. Not because the protocol itself is weak, but because any device that still supports it is – given its long-ago deprecation – significantly outdated, and therefore most likely contains old and significant vulnerabilities.

The road still before us certainly isn’t short – over 422 thousand servers that support the outdated protocol remain on the internet – nevertheless, the situation seems to be getting better. We can only hope that with its 30th birthday quickly approaching, the time is finally comming to let SSL 2.0 – and most of the systems that support it – go, at least on the global internet…

[1] <https://datatracker.ietf.org/doc/html/rfc6176#ref-SSL2>
[2] <https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0>
[3] <https://en.wikipedia.org/wiki/Transport_Layer_Security#History_and_development>
[4] <https://isc.sans.edu/diary/29908>
[5] <https://isc.sans.edu/diary/31550>
[6] <https://www.shodan.io/search?query=ssl.version%3Asslv2>
[7] <https://isc.sans.edu/diary/29988>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [TLS](/tag.html?tag=TLS) [SSL](/tag.html?tag=SSL) [HTTPS](/tag.html?tag=HTTPS)

[1 comment(s)](/diary/SSL%2B20%2Bturns%2B30%2Bthis%2BSunday%2BPerhaps%2Bthe%2Btime%2Bhas%2Bcome%2Bto%2Blet%2Bit%2Bdie/31664/#comments)

* [previous](/diary/31660)
* [next](/diary/31666)

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