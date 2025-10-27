---
title: SPF and DMARC use on 100k most popular domains, (Thu, Jan 19th)
url: https://isc.sans.edu/diary/rss/29452
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-20
fetch_date: 2025-10-04T04:24:41.957798
---

# SPF and DMARC use on 100k most popular domains, (Thu, Jan 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29448)
* [next](/diary/29456)

# [SPF and DMARC use on 100k most popular domains](/forums/diary/SPF%2Band%2BDMARC%2Buse%2Bon%2B100k%2Bmost%2Bpopular%2Bdomains/29452/)

**Published**: 2023-01-19. **Last Updated**: 2023-01-19 11:16:28 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[3 comment(s)](/diary/SPF%2Band%2BDMARC%2Buse%2Bon%2B100k%2Bmost%2Bpopular%2Bdomains/29452/#comments)

Not too long ago, I wrote a diary discussing SPF and DMARC use on GOV subdomains in different ccTLDs around the world[[1](https://isc.sans.edu/diary/29384)]. The results weren’t too optimistic – it turned out that only about 42% of gov.cctld domains had a valid SPF record published and only about 19% of such domains had a valid DMARC record published.

Since I created a quick script for gathering SPF and DMARC records for an arbitrary list of domains for that diary, I thought it might be interesting to use it again this week, hopefully to get some more optimistic data. Specifically, I used it to take a look at SPF and DMARC adoption on world’s most popular domains – the top 100 thousand (as well as th top 10 thousand and the top 1 thousand) most visited domains according to the Tranco list[[2](https://tranco-list.eu/)].

Of course, not all domains that lead to most popular websites are necessarily also used for sending and receiving e-mail (only approximately 77.65% of the top 100k domains had a DNS MX record set), however, in such instances, it would be advisable for the domain owners to set up a “blocking” record for SPF (v=spf1 -all) and DMARC (v=DMARC1; p=reject;). Nevertheless, of the top 100k Tranco domains, only about 2.13% had an SPF “blocker” record set and only 1.41% had both an SPF and DMARC “blocker” records published. The situation was somewhat better when one looked only at the top 10k domains (where 4.29% domains had an SPF blocker and 3.12% had both SPF and DMARC blockers), and even better if one only considered the top 1k domains (where the numbers came to 6.6% and 5.2%, respectively).

In any case, the overall situation for the world’s most popular domains was, as I have hoped, significantly more optimistic than for the governmental domains we discussed in the aforementioned diary. Of the 100k most popular domains, almost 64.7% had valid and “reasonable” SPF records, which is not bad. On the other hand, 40 of these domains had a “+all” directive included in their SPF records, which basically means that their owners explicitly stated that any server is allowed to send e-mail on behalf of their domains… Which is somewhat unfortunate.

As with the number of “blocking” records, the situation was better when one only looked at the top 10k domains (67.8% had valid SPF records) and the top 1k (SPF records were set for 71.9% of these domains). This makes sense, since one would expect that the more popular a domain is, the more their owners would care about security… At least, on average.

[![](https://isc.sans.edu/diaryimages/images/23-01-19-tranco-spf.png)](https://isc.sans.edu/diaryimages/images/23-01-19-tranco-spf.png)

The differences between 100k, 10k and 1k top domains were similar when it came to DMARC records.

Of the top 100k Tranco domains, only 37.8% had a valid DMARC record set, while for the 10k domains, it was 51.9%, and for the top 1k domains, it was 63.4%.

[![](https://isc.sans.edu/diaryimages/images/23-01-19-tranco-dmarc.png)](https://isc.sans.edu/diaryimages/images/23-01-19-tranco-dmarc.png)

Although the numbers are much better than for the governmental domains, they are still far from ideal. After all, if almost 72% of the world’s top 1000 most popular domains have a valid SPF record set, it still means that about 28% of these domains either have an invalid record set or completely lack any such record (not to mention a DMARC record)… And it is a little disheartening when one considers that this basically translates to “anyone can send e-mail on behalf of these domains”.

[1] <https://isc.sans.edu/diary/29384>
[2] <https://tranco-list.eu/>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [SPF](/tag.html?tag=SPF) [Spam](/tag.html?tag=Spam) [DMARC](/tag.html?tag=DMARC)

[3 comment(s)](/diary/SPF%2Band%2BDMARC%2Buse%2Bon%2B100k%2Bmost%2Bpopular%2Bdomains/29452/#comments)

* [previous](/diary/29448)
* [next](/diary/29456)

### Comments

Thanks Jan for the interesting survey.

Can you be a bit more explicit on what exactly you mean by “valid” SPF records, for example the “?all” is valid or not?

Also another forgotten RFC, ideal for dormant domains is the NULL MX RFC7505.

#### Mike B

#### Jan 20th 2023 2 years ago

For SPF, records with incorrect syntax or format, or those containing the "+all" directive or missing any "all" directive were considered "invalid/useless". For DMARC, records with incorrect syntax or format, or those missing any policy definition were considered as such.

#### Jan

#### Jan 20th 2023 2 years ago

This is very interesting but what is the Risk score for something like this? Since when you buy a domain no one disables email via spf by default, so what data would convince a company to invest the time to even worry about such an attack vector? I am very interested in the answer!

#### Papalorian

#### Jan 20th 2023 2 years ago

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