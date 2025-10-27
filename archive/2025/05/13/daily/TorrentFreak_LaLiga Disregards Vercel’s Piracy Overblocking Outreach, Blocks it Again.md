---
title: LaLiga Disregards Vercel’s Piracy Overblocking Outreach, Blocks it Again
url: https://torrentfreak.com/laliga-disregards-vercels-piracy-overblocking-outreach-blocks-it-yet-again-250512/
source: TorrentFreak
date: 2025-05-13
fetch_date: 2025-10-06T22:30:55.568678
---

# LaLiga Disregards Vercel’s Piracy Overblocking Outreach, Blocks it Again

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# LaLiga Disregards Vercel’s Piracy Overblocking Outreach, Blocks it Again

May 12, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

When anti-piracy enforcement talks went nowhere, LaLiga began blocking Cloudflare IP addresses, regardless of the innocent websites it also rendered inaccessible. Since early February, widespread outages have spread across Spain as IP addresses belonging to other cloud services suffered the same fate. To prevent overblocking, Vercel set up a priority reporting mechanism just for LaLiga. It remains unused and on Sunday, Vercel was blocked once again.

![laliga-emergency](https://torrentfreak.com/images/laliga-emergency.png)
For those who had fun playing #laligagate ‘collateral damage bingo’ over the weekend, a full house meant identifying the top internet intermediaries and services, blocked by LaLiga on Friday, Saturday, and Sunday.

Most services utilize shared IP addresses, so typically the number of non-pirate sites blocked at the same time can run to hundreds of sites, potentially more. According to hayahora.futbol data, the following were targeted more than most:

*24x Cloudflare IP addresses, 3x Meteverse IP addresses, 3x Twitch, 2x QUICCloud, 2x Netify, and 1x InfinityFree.*

GitHub Pages, Cloudflare, and Vercel are among those targeted previously but for whom blocking at one or more ISPs inexplicably remains in place. For those tracking recent events, seeing Vercel on the list again was an unwelcome surprise.

## Vercel Blocked Again

Back in April, Vercel CEO Guillermo Rauch described LaLiga’s blocking as “[indiscriminate](https://torrentfreak.com/vercel-slams-laliga-piracy-blocks-as-unaccountable-internet-censorship-250422/)” and tantamount to an “unaccountable form of internet censorship.”

Yet, while Vercel didn’t hold back its critique, the company also pledged to contact LaLiga to see if surprise no-notice IP address blocking could be replaced by something a little more organized and substantially less blunt. Specifically, a blocking method that wouldn’t result in innocent sites being blocked at the same time.

In a post published Sunday on X, Rauch had some good news, and some bad news.

“We’ve been working with [the team at LaLiga] to ensure uninterrupted access in Spain to the @vercel global CDN,” Rauch revealed.

To help LaLiga mitigate the risk of overblocking, Gauch says the company set up an inbox which gave LaLiga direct access to its Site Reliability Engineering incident management system. This effectively meant that high priority requests could be processed swiftly, in line with LaLiga’s demands while avoiding collateral damage.

## And the Bad News

“Vercel has set up a dedicated inbox for LaLiga to file reports. Sadly, they just blocked another Vercel CDN IP without using this mechanism,” Gauch [wrote](https://x.com/rauchg/status/1921603136705458339) on Sunday.

Why LaLiga apparently chose to disregard Vercel’s overtures isn’t clear. Having the ability to avoid collateral damage and then going in the opposite direction makes little sense.

![vercel-x-laliga](https://torrentfreak.com/images/vercel-x-laliga.png)

“A soccer organization should \*not\* have the ability to broadly block internet infrastructure access to millions of Spanish customers across major internet service providers,” Gauch continued.

“CDN providers like Vercel front millions of mission-critical websites and applications behind the IPs being blocked. Even in the situation a block is required, it can be done on a hostname basis via TLS SNI, rather than IP.

“We’re closely monitoring the situation and continue to offer our assistance to LaLiga to minimize the blast radius of these blocks and help preserve free access to the internet in Spain.”

## Targeting X and Vimeo

Documenting every site affected by LaLiga blocking would be a monumental task but a few stood out over the weekend as potentially significant. Given his stance on free speech, there’s a non-zero risk of Elon Musk taking issue with X IP addresses being blocked to prevent piracy.

![x-block](https://torrentfreak.com/images/x-block.png)

That being said, at least one demand from the Indian government to [suspend 8,000 X accounts](https://x.com/GlobalAffairs/status/1920522981744238814) may have demanded Musk’s undivided attention. Threats to arrest local staff aren’t to be taken lightly.

![india-x](https://torrentfreak.com/images/india-x.png)

Unfortunately, the X account that revealed the existence of the threats was itself [blocked in India on Friday](https://x.com/IndianIdle/status/1920717721186037775).

## Pressure builds on ISPs

When pirate site blocking begins in most countries, it falls to local ISPs to carry out the blocks. Since ISPs are the *de facto* point of complaint when customers’ internet connections develop a sudden ‘fault’, they tend to shoulder a bigger reputational risk than rightsholders.

The difference in Spain, in respect of the court order behind the mayhem of the last 90 days, has two parts. Most importantly, regardless of the existence of a court order, every time a CDN IP address is added to the list by an ISP, they are well aware of the collateral damage that’s likely to cause.

After initially denying anything was wrong, ISPs’ now mention the court order more quickly, with phrasing that implies that their hands are tied.

![digi-response](https://torrentfreak.com/images/digi-response.png)

As mentioned earlier, when an X user told Movistar that Vimeo was inaccessible due to blocking, Movistar responded by shifting the blame to the court order.

![movistar-vimeo](https://torrentfreak.com/images/movistar-vimeo.png)

Casually reporting the blocking of a NASDAQ-listed company is in itself unusual. Arguably, however,the bigger issue concerns the crucial role played by ISPs when LaLiga and Telefonica filed the original application.

Through deals with exclusive rights holder Telefonica, the ISPs sell LaLiga TV packages so had a vested interest in the order being passed. None of the ISPs challenged the application and the fact that they were all in agreement was one of the factors that led to the judge rubber-stamping the application.

In Movistar’s case, the content is indeed currently blocked on the platform due to a court order, but it’s a court order that it a) agreed to comply with, b) stands to benefit from, and c) was requested by owner Telefonica.

Meanwhile, LaLiga president Javier Tebas appears bullish on the role played by intermediaries in the war on piracy. In a recent interview with Argentinian news outlet Clarins, he put three tech companies on notice.

“Google, Cloudflare and to a lesser extent X (the former Twitter), are necessary participants for the crime to be consumed. LaLiga is not going to stop until they go to jail and I am very stubborn,” he warned.

* [![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-left.svg)Next Post](https://torrentf...