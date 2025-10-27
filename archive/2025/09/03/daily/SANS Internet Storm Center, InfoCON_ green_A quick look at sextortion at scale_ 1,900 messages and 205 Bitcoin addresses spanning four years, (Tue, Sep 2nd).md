---
title: A quick look at sextortion at scale: 1,900 messages and 205 Bitcoin addresses spanning four years, (Tue, Sep 2nd)
url: https://isc.sans.edu/diary/rss/32252
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-03
fetch_date: 2025-10-02T19:34:41.685245
---

# A quick look at sextortion at scale: 1,900 messages and 205 Bitcoin addresses spanning four years, (Tue, Sep 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32248)
* [next](/diary/32256)

# [A quick look at sextortion at scale: 1,900 messages and 205 Bitcoin addresses spanning four years](/forums/diary/A%2Bquick%2Blook%2Bat%2Bsextortion%2Bat%2Bscale%2B1900%2Bmessages%2Band%2B205%2BBitcoin%2Baddresses%2Bspanning%2Bfour%2Byears/32252/)

**Published**: 2025-09-02. **Last Updated**: 2025-09-02 06:05:33 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/A%2Bquick%2Blook%2Bat%2Bsextortion%2Bat%2Bscale%2B1900%2Bmessages%2Band%2B205%2BBitcoin%2Baddresses%2Bspanning%2Bfour%2Byears/32252/#comments)

What can almost 2,000 sextortion messages tell us about how threat actors operate and whether they are successful? Let’s find out.

Although it is true that I covered sextortion in my last diary[[1](https://isc.sans.edu/diary/Do%2Bsextortion%2Bscams%2Bstill%2Bwork%2Bin%2B2025/32178)], I thought the topic deserved further discussion today.

This is not because we didn’t cover sextortion in enough depth here at the Internet Storm Center over the previous years – we did – for example, see the pre-2020 series of articles from Rick in which he discussed tracking of sextortion payments[[2](https://isc.sans.edu/diary/Sextortion%2BFollow%2Bthe%2BMoney%2BThe%2BFinal%2BChapter/25204)]. The reason is that in my latest diary, we only had a fairly small sample to base our observations on… And this has recently changed.

After the last diary was published, our friend and colleague “l0c4l“ from France got in touch with me and offered to share his dataset containing  approximately 1,900 sextortion messages for further analysis. And as Marlon Brando put it – it was an offer I couldn’t refuse.

After some initial cleanup of the received data, I was left with 1,888 individual sextortion messages that – according to their headers – were sent between June 2021 and August 2025. In these e-mails, there were 193 unique Bitcoin addresses to which recipients were supposed to send payments.

Although in some messages threat actors offered Ethereum (ETH) as an alternative to Bitcoin and provided a corresponding second wallet/address as a result, I only used the BTC addresses for further analysis.

Before moving on, I added the data from my own dataset (which was discussed last time) to the new dataset. After that, I ended up with 1,909 messages in which 205 unique addresses (203 BTC, 2 LTC) were used. This – although not overwhelmingly large – was a reasonable sample size for further analysis.

So, what can we learn from it?

* The use of specific cryptocurrency addresses in sextortion messages seems to be fairly short-lived. Approximately 46% of the addresses in the dataset were only used for a single day, another 21% for two days, and additional 16% for three days. Use over a time span exceeding one week was found for only 10 addresses, six of which were used for longer than a month. The “longest-living” address was used in 13 different messages sent over the course of 104 days. This pushed the average length of use to 3.7 days, with median being 2 days.
  [![](https://isc.sans.edu/diaryimages/images/25-09-05-histogram-days-address-in-use.png)](https://isc.sans.edu/diaryimages/images/25-09-05-histogram-days-address-in-use.png)
* While most addresses were used with only one message template – and correspondingly with only a single requested payment amount – this wasn’t always the case. Requests related to nine Bitcoin addresses (4.4%) varied across messages. The minimum non-zero difference identified for one address was 40 USD (threat actors asked for 250 USD in some messages and 290 USD in others), while the maximum difference was 4,500 USD (some messages asked for 500 USD, while others for 5,000 USD in connection with the same Bitcoin address).
* Considering the highest requested payment for each address, the average requested amount was 1,716 USD, with a median of 1,370 USD.

  [![](https://isc.sans.edu/diaryimages/images/25-09-05-histogram-maximum-requested-per-address.png)](https://isc.sans.edu/diaryimages/images/25-09-05-histogram-maximum-requested-per-address.png)
* The difference between the highest and lowest amounts that threat actors tried to extort was surprisingly large. In our sample, the minimum requested amount in any sextortion message was 250 USD, while the largest was 36,500 EUR (about 43,000 USD). Such large amounts were exceptional, however, as only two Bitcoin addresses were connected with requests exceeding 5,000 USD (the aforementioned one, and another one related to a request for 32,300 EUR, roughly 38,000 USD).
* Of the 205 cryptocurrency addresses in our dataset, only 57 (~28%) didn’t receive any payment at all, while the remaining addresses did. Overall, the average amount received by a single address was 0.083873483 BTC (approximately 9,150 USD at the time of writing), with median at 0.03954898 BTC (~ 4,315 USD). The largest total amount received by any single address in the dataset was 0.69163943 BTC (~ 75,459 USD).

When writing the last diary – covering cryptocurrency addresses that were used in sextortion campaigns between September 2024 and August 2025 – I was under the impression that the fact that “only” 40% of addresses in that dataset received no payments was a fairly bad result. It turns out that it was significantly better than the proportion observed in our larger dataset, which covers a much longer timespan. Hopefully this indicates a decrease in the effectiveness of sextortion over time, and decreasing willingness of recipients to pay… If so, let’s hope that this trend continues.

[1] [https://isc.sans.edu/diary/Do+sextortion+scams+still+work+in+2025/32178](https://isc.sans.edu/diary/Do%2Bsextortion%2Bscams%2Bstill%2Bwork%2Bin%2B2025/32178)
[2] [https://isc.sans.edu/diary/Sextortion+Follow+the+Money+The+Final+Chapter/25204](https://isc.sans.edu/diary/Sextortion%2BFollow%2Bthe%2BMoney%2BThe%2BFinal%2BChapter/25204)

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [Bitcoin](/tag.html?tag=Bitcoin) [Phishing](/tag.html?tag=Phishing) [Sextortion](/tag.html?tag=Sextortion)

[0 comment(s)](/diary/A%2Bquick%2Blook%2Bat%2Bsextortion%2Bat%2Bscale%2B1900%2Bmessages%2Band%2B205%2BBitcoin%2Baddresses%2Bspanning%2Bfour%2Byears/32252/#comments)

* [previous](/diary/32248)
* [next](/diary/32256)

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
Developers: We have an [API](/api/) for yo...